#!/usr/bin/env python3
"""Stage the configured shared semantic text map before building the static site."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from culturemech.text_map_publish import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
