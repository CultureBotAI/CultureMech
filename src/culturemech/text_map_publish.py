"""Stage a validated map and update the static site's navigation status."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

from culturemech.text_map_site import prepare_text_map


def publish(root: Path) -> dict:
    """Validate before site writes; expose the link only after successful staging."""
    with prepare_text_map(root) as ready:
        site = root / "pages"
        if ready is not None:
            ready.stage(site)
        status = {"enabled": ready is not None}
        destination = root / "app" / "text_map_status.json"
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=destination.parent,
                prefix=".text-map-status-",
                delete=False,
            ) as stream:
                temporary = Path(stream.name)
                json.dump(status, stream, sort_keys=True)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return status


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args(argv)
    print(json.dumps(publish(args.root.resolve()), sort_keys=True))
    return 0
