"""Packaging safety boundaries for #769–771 with synthetic local Git inputs."""

import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "package_variant_inventory_handoff_683",
    Path(__file__).resolve().parents[1] / "scripts/adhoc/package_variant_inventory_handoff_683.py",
)
packager = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(packager)


def fingerprint(path):
    raw = path.read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


@pytest.fixture
def package_case(tmp_path, monkeypatch, request):
    """Real source archive; native bundle verification is a separate tested boundary."""
    root = tmp_path / "producer"
    root.mkdir()
    relative = "bacterial/source.yaml"
    recipe = root / "data/normalized_yaml" / relative
    recipe.parent.mkdir(parents=True)
    recipe.write_text("id: CultureMech:000001\nname: Synthetic source\n")
    dependency = root / "src/culturemech/fixture.py"
    dependency.parent.mkdir(parents=True)
    dependency.write_text('"""Synthetic archived implementation."""\n')
    if getattr(request, "param", False):
        (root / ".gitattributes").write_text(
            "data/normalized_yaml/bacterial/source.yaml export-ignore\n"
        )
    for command in (
        ["git", "init", "-q"],
        ["git", "add", "."],
        [
            "git",
            "-c",
            "user.name=Synthetic Fixture",
            "-c",
            "user.email=fixture@example.org",
            "commit",
            "-qm",
            "Synthetic source",
        ],
    ):
        subprocess.run(command, cwd=root, check=True, capture_output=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    monkeypatch.setattr(packager, "ROOT", root)
    bundle = tmp_path / "bundle"
    bundle.mkdir()
    for name in packager.PRODUCTS:
        (bundle / name).write_text("synthetic product\n")
    (bundle / "incidental.txt").write_text("Not a handoff product.\n")
    manifest = {
        "contract": "culturemech-direct-ingredients-v3",
        "status": "CANDIDATE",
        "git": {"dirty": False, "commit": commit},
        "scope": "full_catalog_direct_ingredients",
        "input_dir": "data/normalized_yaml",
        "inputs": {relative: fingerprint(recipe)},
        "dependencies": {"src/culturemech/fixture.py": fingerprint(dependency)},
        "counts": {"variant_change_events": 1, "variant_held_mentions": 0},
        "products": {name: fingerprint(bundle / name) for name in packager.PRODUCTS},
    }
    manifest_path = bundle / "manifest.json"
    manifest_path.write_text(json.dumps(manifest))
    pin = packager.sha(manifest_path)
    queue = tmp_path / "queue.tsv"
    queue.write_text("source_path\tsource_sha256\n" + relative + "\t" + "a" * 64 + "\n")
    coverage = tmp_path / "coverage"
    coverage.mkdir()
    (coverage / "coverage.tsv").write_text("queue_row_number\tstatus\n1\tSTRUCTURED\n")
    summary = {
        "result": "PASS",
        "mode": "postapply",
        "queue_rows": 1,
        "queue_recipes": 1,
        "queue_sha256": packager.sha(queue),
        "coverage_sha256": packager.sha(coverage / "coverage.tsv"),
        "applied_assertions": 1,
        "held_mentions": 0,
        "dispositions": {"STRUCTURED": 1},
        "record_snapshots": [
            {
                "path": "data/normalized_yaml/" + relative,
                "base_sha256": "a" * 64,
                "current_sha256": fingerprint(recipe)["sha256"],
            }
        ],
    }
    (coverage / "summary.json").write_text(json.dumps(summary))
    verification_calls = []

    def verify(path, expected):
        assert packager.sha(path / "manifest.json") == expected
        verification_calls.append(path)
        return {"status": "VERIFIED_CANDIDATE", "manifest_sha256": expected}

    monkeypatch.setattr(packager, "verify_bundle", verify)
    return bundle, pin, coverage, queue, tmp_path / "handoff", verification_calls


def run(case):
    return packager.package(*case[:5])


def test_verified_copies_archive_and_dynamic_dispositions_are_published(package_case):
    bundle, pin, coverage, queue, destination, calls = package_case
    receipt = run(package_case)
    assert calls == [bundle, destination / "bundle"]
    assert receipt == json.loads((destination / "handoff.json").read_text())
    assert packager.sha(destination / "bundle/manifest.json") == pin
    assert packager.sha(destination / "original-review-queue.tsv") == packager.sha(queue)
    assert {path.name for path in (destination / "bundle").iterdir()} == packager.PRODUCTS | {
        "manifest.json"
    }
    assert "1 STRUCTURED" in (destination / "HANDOFF.md").read_text()
    assert "partial holds" in (destination / "HANDOFF.md").read_text()
    assert not (destination / ".handoff.incomplete.json").exists()
    before = (destination / "handoff.json").read_bytes()
    with pytest.raises(ValueError, match="already exists"):
        run(package_case)
    assert (destination / "handoff.json").read_bytes() == before


@pytest.mark.parametrize("source_index", [0, 2, "corpus"])
def test_nested_output_refused_before_any_mutation(package_case, source_index):
    case = list(package_case)
    source = (
        packager.ROOT / "data/normalized_yaml" if source_index == "corpus" else case[source_index]
    )
    before = sorted(path.relative_to(source).as_posix() for path in source.rglob("*"))
    case[4] = source / "nested-handoff"
    with pytest.raises(ValueError, match="overlaps"):
        run(case)
    assert not case[4].exists()
    assert sorted(path.relative_to(source).as_posix() for path in source.rglob("*")) == before
    assert not case[5]


@pytest.mark.parametrize("fault", ["hash", "missing", "duplicate"])
def test_same_count_stale_coverage_cannot_be_admitted(package_case, fault):
    summary_path = package_case[2] / "summary.json"
    summary = json.loads(summary_path.read_text())
    if fault == "hash":
        summary["record_snapshots"][0]["current_sha256"] = "b" * 64
    elif fault == "missing":
        summary["record_snapshots"] = []
    else:
        summary["record_snapshots"] *= 2
    summary_path.write_text(json.dumps(summary))
    assert summary["applied_assertions"] == 1
    with pytest.raises(ValueError, match="coverage recipe"):
        run(package_case)
    assert not package_case[4].exists()


def test_copy_corruption_cannot_publish_acceptance(package_case, monkeypatch):
    copyfile = packager.shutil.copyfile

    def corrupt(source, destination):
        result = copyfile(source, destination)
        if destination.name == "ingredients_list.tsv":
            destination.write_text("Corrupted delivered product.\n")
        return result

    monkeypatch.setattr(packager.shutil, "copyfile", corrupt)
    with pytest.raises(ValueError, match="delivered copy"):
        run(package_case)
    assert not (package_case[4] / "handoff.json").exists()
    assert (package_case[0] / "ingredients_list.tsv").read_text() == "synthetic product\n"


@pytest.mark.parametrize("package_case", [True], indirect=True)
def test_git_archive_exclusion_cannot_hide_required_input(package_case):
    with pytest.raises(ValueError, match="archived corpus membership"):
        run(package_case)
    assert (package_case[4] / "producer-source.tar.gz").stat().st_size > 0
    assert not (package_case[4] / "handoff.json").exists()


def test_final_instruction_write_failure_has_no_accepted_receipt(package_case, monkeypatch):
    write_text = Path.write_text

    def fail(path, *args, **kwargs):
        if path.name == "HANDOFF.md":
            raise OSError("synthetic instruction write failure")
        return write_text(path, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", fail)
    with pytest.raises(OSError, match="instruction write failure"):
        run(package_case)
    assert not (package_case[4] / "handoff.json").exists()


def test_receipt_flush_failure_never_publishes_acceptance(package_case, monkeypatch):
    def fail(_fd):
        raise OSError("synthetic receipt durability failure")

    monkeypatch.setattr(packager.os, "fsync", fail)
    with pytest.raises(OSError, match="receipt durability"):
        run(package_case)
    assert not (package_case[4] / "handoff.json").exists()
