"""Static contract tests for the public hub's vendored-sync checker."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "check_vendored_sync.sh"


def test_checker_governs_itself_and_shared_edison_capture():
    text = SCRIPT.read_text()
    files_block = text.split("FILES=(", 1)[1].split(")", 1)[0]
    assert "scripts/check_vendored_sync.sh" in files_block
    assert "scripts/_edison_capture.py" in text
    assert "existence-based" in text


def test_checker_covers_both_shared_schemas():
    text = SCRIPT.read_text()
    assert "src/*/schema/mech_shared.yaml|src/culturemech/schema/mech_shared.yaml" in text
    assert "src/*/schema/history.yaml|src/culturemech/schema/history.yaml" in text


def test_every_canonical_fetch_has_a_timeout():
    text = SCRIPT.read_text()
    fetches = [line.strip() for line in text.splitlines() if "curl -fsSL" in line]
    assert len(fetches) == 2
    assert all("--max-time 10" in line for line in fetches)
