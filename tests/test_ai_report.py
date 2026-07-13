# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the AI-content report mailto builder (Store policy 11.16).

Run with the project venv:  python -m unittest tests.test_ai_report
"""

import os
import sys
import unittest
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.diagnostics import build_ai_report_mailto, system_info  # noqa: E402
from app.version import REPORT_EMAIL  # noqa: E402


class BuildAiReportMailtoTests(unittest.TestCase):
    def test_addresses_the_report_inbox(self):
        url = build_ai_report_mailto()
        self.assertTrue(url.startswith(f"mailto:{REPORT_EMAIL}?"))

    def test_encodes_subject_and_body(self):
        parsed = urlparse(build_ai_report_mailto())
        params = parse_qs(parsed.query)
        # Both query params are present and url-encoded (parse_qs decodes them).
        self.assertIn("subject", params)
        self.assertIn("body", params)
        subject = params["subject"][0]
        body = params["body"][0]
        self.assertIn("AI-generated", subject)
        # The body carries the reporting template + the environment block, so a
        # reviewer receives enough context to identify the flagged output.
        self.assertIn("Where it appeared", body)
        self.assertIn(system_info(), body)


if __name__ == "__main__":
    unittest.main()
