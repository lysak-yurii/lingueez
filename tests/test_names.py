# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Display-name rules, renaming the account and changing its password.

Run:  python -m unittest tests.test_names
"""

import os
import sys
import unittest
from types import SimpleNamespace
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import auth_manager  # noqa: E402
from app.core.names import normalize_name  # noqa: E402


class NormalizeNameTests(unittest.TestCase):
    def test_accepts_names_from_any_script(self):
        for name in (
            "Yurii Lysak",
            "Анна-Марія",
            "O'Neil",
            "J. R. Tolkien",
            "王伟",
            "José Núñez",
            "Ελένη",
            "van der Berg",
            "McDonald",
        ):
            self.assertEqual(normalize_name(name), name)

    def test_tidies_spacing_and_single_case_input(self):
        self.assertEqual(normalize_name("  yurii   lysak "), "Yurii Lysak")
        self.assertEqual(normalize_name("YURII LYSAK"), "Yurii Lysak")
        self.assertEqual(normalize_name("anna-maria o'neil"), "Anna-Maria O'Neil")

    def test_rejects_what_is_not_a_name(self):
        for bad in (
            "",
            "a",
            "1",
            "ab1",
            "test123",
            "a.",
            "--",
            "-Anna",
            "me@mail.com",
            "😀😀",
            "http://x.io",
            "x" * 51,
        ):
            self.assertIsNone(normalize_name(bad), bad)


class _Auth:
    def __init__(self, sign_in_error=None):
        self.updates = []
        self.sign_in_error = sign_in_error

    def update_user(self, attrs):
        self.updates.append(attrs)
        meta = attrs.get("data")
        return SimpleNamespace(
            user=SimpleNamespace(
                id="u1", email="me@x.io", user_metadata=meta or {}, app_metadata={}
            )
        )

    def sign_in_with_password(self, creds):
        if self.sign_in_error:
            raise Exception(self.sign_in_error)
        return SimpleNamespace(session=None)


class AccountChangesTests(unittest.TestCase):
    def _manager(self, auth):
        sb = SimpleNamespace(get_auth=lambda: auth)
        with (
            mock.patch.object(auth_manager, "SecureStore"),
            mock.patch.object(auth_manager, "get_account_registry"),
        ):
            m = auth_manager.AuthManager(sb)
        m._user = SimpleNamespace(
            id="u1", email="me@x.io", user_metadata={}, app_metadata={"providers": ["email"]}
        )
        return m

    def test_rename_writes_every_name_key_and_the_account_list(self):
        auth = _Auth()
        m = self._manager(auth)
        self.assertEqual(m.change_name("Anna"), (True, None))
        self.assertEqual(
            auth.updates[-1]["data"], {"display_name": "Anna", "full_name": "Anna", "name": "Anna"}
        )
        self.assertEqual(m.current_user_name(), "Anna")
        m.registry.upsert.assert_called_with("u1", "me@x.io", "Anna")

    def test_password_change_checks_the_current_one_first(self):
        auth = _Auth(sign_in_error="Invalid login credentials")
        ok, err = self._manager(auth).change_password("wrong", "newpass1")
        self.assertFalse(ok)
        self.assertEqual(err, "Current password is incorrect.")
        self.assertEqual(auth.updates, [])

        auth = _Auth()
        self.assertEqual(self._manager(auth).change_password("old", "newpass1"), (True, None))
        self.assertEqual(auth.updates, [{"password": "newpass1"}])

    def test_only_password_accounts_can_change_one(self):
        m = self._manager(_Auth())
        self.assertTrue(m.has_password())
        m._user.app_metadata = {"providers": ["google"]}
        self.assertFalse(m.has_password())


if __name__ == "__main__":
    unittest.main()
