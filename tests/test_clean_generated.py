import importlib.util
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[1] / "scripts" / "clean_generated.py"
SPEC = importlib.util.spec_from_file_location("clean_generated", SCRIPT)
assert SPEC and SPEC.loader
clean_generated = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean_generated)


def _repository(path: Path) -> Path:
    path.mkdir()
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    (path / ".gitignore").write_text(
        "\n".join(
            [f"/{target}/" for target in clean_generated.GENERATED_DIRECTORIES]
            + [f"/{target}" for target in clean_generated.GENERATED_FILES]
        )
        + "\n"
    )
    return path


def test_clean_removes_only_ignored_generated_paths(tmp_path: Path) -> None:
    root = _repository(tmp_path / "repo")
    generated = root / "pages" / "normalized" / "one.html"
    generated.parent.mkdir(parents=True)
    generated.write_text("generated")
    source = root / "pages" / "media_growth_review.html"
    source.write_text("tracked source")

    clean_generated.clean(root)

    assert not generated.exists()
    assert source.read_text() == "tracked source"


def test_clean_refuses_to_delete_a_tracked_target(tmp_path: Path) -> None:
    root = _repository(tmp_path / "repo")
    generated = root / "app" / "data.js"
    generated.parent.mkdir(parents=True)
    generated.write_text("tracked")
    subprocess.run(["git", "add", "-f", "app/data.js"], cwd=root, check=True)

    with pytest.raises(RuntimeError, match="tracked path: app/data.js"):
        clean_generated.clean(root)

    assert generated.read_text() == "tracked"
