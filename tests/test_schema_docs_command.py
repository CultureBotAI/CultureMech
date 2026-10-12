"""The schema-doc recipe must use the maintained generator and propagate failure."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest
from linkml.generators.docgen import DocGenerator

from tests.test_markdown_links import LINK_RE, _resolves_case_sensitively

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("generator_exit,write_output", [(0, True), (23, False), (0, False)])
def test_docs_recipe_propagates_generator_status(tmp_path, generator_exit, write_output):
    just = shutil.which("just")
    if not just:
        pytest.skip("just is not installed")
    for name in ("justfile", "project.justfile"):
        shutil.copyfile(ROOT / name, tmp_path / name)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake_uv = bin_dir / "uv"
    fake_uv.write_text(
        '#!/bin/sh\nprintf "%s\\n" "$@" > "$TEST_ARGS"\n'
        'if [ "$TEST_WRITE_OUTPUT" = yes ]; then\n'
        '  mkdir -p "$5/classes"\n'
        '  printf "# Schema\\n" > "$5/index.md"\n'
        '  printf "# SolutionRecipe\\n" > "$5/classes/SolutionRecipe.md"\n'
        'fi\nexit "$TEST_UV_EXIT"\n'
    )
    fake_uv.chmod(0o755)
    argv = tmp_path / "args.txt"
    old_docs = tmp_path / "docs/schema"
    old_docs.mkdir(parents=True)
    (old_docs / "stale.md").write_text("previous generated documentation\n")
    done = subprocess.run(
        [just, "gen-docs"],
        cwd=tmp_path,
        env={
            **os.environ,
            "PATH": str(bin_dir) + os.pathsep + os.environ.get("PATH", ""),
            "TEST_ARGS": str(argv),
            "TEST_UV_EXIT": str(generator_exit),
            "TEST_WRITE_OUTPUT": "yes" if write_output else "no",
        },
        capture_output=True,
        text=True,
    )
    actual = argv.read_text().splitlines()
    assert actual[:4] == [
        "run",
        "gen-doc",
        "--subfolder-type-separation",
        "--directory",
    ]
    assert len(actual) == 6 and actual[4].startswith("docs/.schema.")
    assert actual[5] == "src/culturemech/schema/culturemech.yaml"
    success = generator_exit == 0 and write_output
    assert (done.returncode == 0) == success
    assert ("Schema docs generated" in done.stdout) == success
    assert not list((tmp_path / "docs").glob(".schema.*"))
    if success:
        assert (old_docs / "classes/SolutionRecipe.md").is_file()
        assert not (old_docs / "stale.md").exists()
    else:
        assert (old_docs / "stale.md").read_text() == "previous generated documentation\n"


def test_type_separated_docs_preserve_class_and_slot_pages(tmp_path):
    generator = DocGenerator(
        str(ROOT / "src/culturemech/schema/culturemech.yaml"),
        subfolder_type_separation=True,
    )
    generator.serialize(directory=str(tmp_path))
    for name in ("Term", "Descriptor"):
        class_page = tmp_path / "classes" / f"{name}.md"
        slot_page = tmp_path / "slots" / f"{name.lower()}.md"
        assert _resolves_case_sensitively(class_page)
        assert _resolves_case_sensitively(slot_page)
        assert class_page.read_text() != slot_page.read_text()
    assert "evidence" in (tmp_path / "classes/SolutionRecipe.md").read_text()
    documents = list(tmp_path.rglob("*.md"))
    assert len(documents) > 100
    for path in documents:
        for match in LINK_RE.finditer(path.read_text()):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#", "<")):
                continue
            target = target.split("#", 1)[0].split(" ", 1)[0]
            if target.endswith(".md"):
                assert _resolves_case_sensitively((path.parent / target).resolve()), (
                    path,
                    target,
                )
