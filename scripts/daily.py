"""
scripts/daily.py

Simplified daily.py
- Fetch data from sources
- Filter based on keywords
- Send results to Slack
"""

from __future__ import annotations

from radar.main import run_daily

if __name__ == "__main__":
    run_daily(publish=False)  # Slack 전송 비활성화