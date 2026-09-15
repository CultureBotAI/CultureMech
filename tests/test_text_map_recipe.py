"""Exercise the actual just recipe without resolving dependencies or running a model."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]


@pytest.mark.skipif(shutil.which("just") is None, reason="the just developer tool is required")
def test_recipe_preserves_quoted_path_arguments(tmp_path):
    tools = tmp_path / "tools"
    tools.mkdir()
    receipt = tmp_path / "argv.json"
    uv = tools / "uv"
    uv.write_text(
        "#!/usr/bin/env python3\n"
        "import json, os, sys\n"
        "with open(os.environ['TEXT_MAP_ARGV_RECEIPT'], 'w') as output:\n"
        "    json.dump(sys.argv[1:], output)\n"
    )
    uv.chmod(0o755)
    args = [
        "--output",
        str(tmp_path / "output folder" / "inputs.jsonl"),
        "--record",
        "data/example/a record.yaml",
        "--limit",
        "3",
    ]
    env = dict(
        os.environ,
        PATH=str(tools) + os.pathsep + os.environ["PATH"],
        TEXT_MAP_ARGV_RECEIPT=str(receipt),
    )
    subprocess.run(
        ["just", "text-map-inputs", *args],
        cwd=REPO,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    assert json.loads(receipt.read_text()) == ["run", "python", "scripts/text_map_inputs.py", *args]


@pytest.mark.skipif(shutil.which("just") is None, reason="the just developer tool is required")
def test_page_recipe_stages_first_and_preserves_quoted_arguments(tmp_path):
    tools = tmp_path / "tools"
    tools.mkdir()
    receipt = tmp_path / "calls.jsonl"
    uv = tools / "uv"
    uv.write_text(
        "#!/usr/bin/env python3\n"
        "import json, os, sys\n"
        "with open(os.environ['TEXT_MAP_ARGV_RECEIPT'], 'a') as output:\n"
        "    output.write(json.dumps(sys.argv[1:]) + '\\n')\n"
    )
    uv.chmod(0o755)
    args = [
        "--out-dir",
        str(tmp_path / "record pages"),
        "--index-dir",
        str(tmp_path / "index pages"),
    ]
    env = dict(
        os.environ,
        PATH=str(tools) + os.pathsep + os.environ["PATH"],
        TEXT_MAP_ARGV_RECEIPT=str(receipt),
    )
    subprocess.run(
        ["just", "gen-media-pages", *args],
        cwd=REPO,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    assert [json.loads(line) for line in receipt.read_text().splitlines()] == [
        ["run", "python", "scripts/stage_text_map.py"],
        ["run", "python", "src/culturemech/render_media_pages.py", *args],
    ]
