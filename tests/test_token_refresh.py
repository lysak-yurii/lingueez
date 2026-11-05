# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Renewing an expired sign-in token before a database request, and asking the
user to sign in again when the server no longer accepts the session.

Run:  python -m unittest tests.test_token_refresh
"""

import base64
import json
import os
import sys
import threading
import time
import unittest
from unittest import mock

import httpx

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import auth_manager  # noqa: E402
from app.core.supabase_client import SupabaseClient, _jwt_expiry  # noqa: E402


def _jwt(exp, sub="user"):
    def part(data):
        return base64.urlsafe_b64encode(json.dumps(data).encode()).decode().rstrip("=")

    return f"{part({'alg': 'HS256'})}.{part({'exp': exp, 'sub': sub})}.sig"


class _Server:
    """Stands in for Supabase: records the Authorization header of every request."""

    def __init__(self):
        self.seen = []

    def __call__(self, request):
        self.seen.append((request.url.path, request.headers.get("Authorization")))
        return httpx.Response(200, json=[])


class BeforeRequestTests(unittest.TestCase):
    def setUp(self):
        self.server = _Server()
        self.sb = SupabaseClient.__new__(SupabaseClient)
        self.sb._refresh_lock = threading.Lock()
        self.http = httpx.Client(
            transport=httpx.MockTransport(self.server),
            event_hooks={"request": [self.sb._before_request]},
        )
        self.renewals = 0
        self.fresh = _jwt(time.time() + 3600, "fresh")

        def refresher():
            self.renewals += 1
            # The real renewal goes through the same client, to the auth API.
            self.http.post("https://x.supabase.co/auth/v1/token")
            self.sb._auth_token = self.fresh

        self.sb.token_refresher = refresher

    def _get(self, token):
        self.sb._auth_token = token
        self.http.get(
            "https://x.supabase.co/rest/v1/words", headers={"Authorization": f"Bearer {token}"}
        )
        return self.server.seen[-1]

    def test_an_expired_token_is_renewed_before_the_request(self):
        path, header = self._get(_jwt(time.time() - 10))
        self.assertEqual(self.renewals, 1)
        self.assertEqual((path, header), ("/rest/v1/words", f"Bearer {self.fresh}"))
        self.assertEqual(self.server.seen[0][0], "/auth/v1/token")

    def test_a_token_about_to_expire_is_renewed_too(self):
        self._get(_jwt(time.time() + 20))
        self.assertEqual(self.renewals, 1)

    def test_a_valid_token_goes_out_unchanged(self):
        token = _jwt(time.time() + 3000)
        self.assertEqual(self._get(token)[1], f"Bearer {token}")
        self.assertEqual(self.renewals, 0)

    def test_signed_out_requests_are_left_alone(self):
        self.sb._auth_token = None
        self.http.get("https://x.supabase.co/rest/v1/words")
        self.assertEqual(self.renewals, 0)

    def test_a_failed_renewal_still_sends_the_request(self):
        self.sb.token_refresher = lambda: None
        token = _jwt(time.time() - 10)
        self.assertEqual(self._get(token)[1], f"Bearer {token}")

    def test_reads_the_expiry_claim(self):
        self.assertEqual(_jwt_expiry(_jwt(1234)), 1234)
        self.assertIsNone(_jwt_expiry("not-a-jwt"))
        self.assertIsNone(_jwt_expiry(None))


class SessionLostTests(unittest.TestCase):
    def setUp(self):
        self.auth = auth_manager.AuthManager.__new__(auth_manager.AuthManager)
        self.gotrue = mock.Mock()
        self.auth.sb = mock.Mock(get_auth=mock.Mock(return_value=self.gotrue))
        self.auth.registry = mock.Mock()
        self.auth._session = mock.Mock()
        self.auth._user = mock.Mock(id="uid-1")
        self.auth._session_lost = False
        self.auth.on_session_lost = mock.Mock()

    def test_a_refused_renewal_asks_for_sign_in_once(self):
        from supabase_auth.errors import AuthApiError

        self.gotrue.refresh_session.side_effect = AuthApiError(
            "Invalid Refresh Token: Refresh Token Not Found", 400, "refresh_token_not_found"
        )
        self.auth.refresh_if_needed()
        self.auth.refresh_if_needed()

        self.assertEqual(self.gotrue.refresh_session.call_count, 1)
        self.auth.registry.mark_needs_reauth.assert_called_once_with("uid-1", True)
        self.auth.on_session_lost.assert_called_once_with()

    def test_a_network_failure_keeps_trying(self):
        from supabase_auth.errors import AuthRetryableError

        self.gotrue.refresh_session.side_effect = AuthRetryableError("timed out", 0)
        self.auth.refresh_if_needed()
        self.auth.refresh_if_needed()

        self.assertEqual(self.gotrue.refresh_session.call_count, 2)
        self.auth.on_session_lost.assert_not_called()
        self.assertFalse(self.auth._session_lost)

    def test_a_server_error_is_not_taken_for_a_lost_session(self):
        from supabase_auth.errors import AuthApiError

        self.gotrue.refresh_session.side_effect = AuthApiError("boom", 500, None)
        self.auth.refresh_if_needed()
        self.auth.on_session_lost.assert_not_called()


if __name__ == "__main__":
    unittest.main()
