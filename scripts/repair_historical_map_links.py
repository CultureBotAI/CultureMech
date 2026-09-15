#!/usr/bin/env python3
"""Repair retained historical media map routes from the current corpus."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from culturemech.historical_map_links import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
