# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for log PII/secret redaction.

Run:  python -m unittest tests.test_log_redaction
"""

import logging
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.log_redaction import RedactionFilter, redact  # noqa: E402


class RedactTests(unittest.TestCase):
    def test_masks_email(self):
        out = redact("login failed for lisak199924@gmail.com today")
        self.assertNotIn("lisak199924@gmail.com", out)
        self.assertIn("<email>", out)

    def test_masks_jwt(self):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.abcDEF123_-x"
        out = redact(f"authorization header was {token}")
        self.assertNotIn(token, out)
        self.assertIn("<jwt>", out)

    def test_masks_key_value_secrets(self):
        for line in (
            'access_token="hunter2supersecret"',
            "refresh-token: abc123def456",
            "api_key=sk-live-0987654321",
            "password = p@ssw0rd!",
            "Bearer eyJxxx.yyy.zzz_value",
        ):
            out = redact(line)
            self.assertIn("<redacted>", out, msg=line)

    def test_preserves_the_secret_label_and_separator(self):
        # Only the value is masked; the key name + separator stay so logs remain
        # diagnostically useful.
        out = redact("api_key=SECRETVALUE")
        self.assertTrue(out.startswith("api_key="), out)
        self.assertNotIn("SECRETVALUE", out)

    def test_leaves_ordinary_lines_untouched(self):
        for line in (
            "Synced 33 words to cloud",
            "User pressed Add Word hotkey",
            "Playback finished for word id 1234",
            "Loaded locale uk with 812 strings",
        ):
            self.assertEqual(redact(line), line)


class RedactionFilterTests(unittest.TestCase):
    def _record(self, msg, *args):
        return logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg=msg,
            args=args,
            exc_info=None,
        )

    def test_filter_masks_in_place_and_returns_true(self):
        f = RedactionFilter()
        rec = self._record("contact me at lisak199924@gmail.com")
        self.assertTrue(f.filter(rec))
        self.assertIn("<email>", rec.getMessage())
        self.assertNotIn("lisak199924@gmail.com", rec.getMessage())

    def test_filter_resolves_args_before_redacting(self):
        f = RedactionFilter()
        rec = self._record("access_token=%s", "hunter2supersecret")
        self.assertTrue(f.filter(rec))
        # args are consumed so getMessage() no longer re-formats.
        self.assertEqual(rec.args, ())
        self.assertIn("<redacted>", rec.getMessage())
        self.assertNotIn("hunter2supersecret", rec.getMessage())


if __name__ == "__main__":
    unittest.main()
