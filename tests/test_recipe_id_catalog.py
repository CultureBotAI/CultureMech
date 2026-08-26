"""Lifecycle invariants for externally published CultureMech recipe IDs."""

from __future__ import annotations

import csv
import hashlib
import io
import subprocess
import sys
from pathlib import Path

import assign_culturemech_ids as assigner
import build_recipe_id_catalog as catalog
import pytest
import refresh_id_registry as registry_refresher
import yaml


def _recipe(path: Path, culturemech_id: str, display_name: str = "Example") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    token = hashlib.sha256(str(path).encode("utf-8")).hexdigest()
    path.write_text(
        f"id: {culturemech_id}\n"
        f"id_lineage_token: legacy:{token}\n"
        f"name: {display_name}\ningredients: []\n",
        encoding="utf-8",
    )


def _tombstones(path: Path, *rows: str) -> None:
    rendered_rows = []
    for row in rows:
        values = row.split("\t")
        signature = "sha256:" + hashlib.sha256(row.encode("utf-8")).hexdigest()
        values.insert(1, signature)
        rendered_rows.append("\t".join(values))
    path.write_text(
        "\t".join(catalog.TOMBSTONE_HEADER) + "\n" + "\n".join(rendered_rows) + "\n",
        encoding="utf-8",
    )


def test_valid_merge_and_split_lifecycle(tmp_path):
    corpus = tmp_path / "corpus"
    _recipe(corpus / "one.yaml", "CultureMech:000001", "Survivor one")
    _recipe(corpus / "four.yaml", "CultureMech:000004", "Survivor four")
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(
        tombstones,
        "CultureMech:000002\tMerged record\tMERGED\tCultureMech:000001\tcurated merge",
        "CultureMech:000003\tSplit record\tSPLIT\tCultureMech:000001;CultureMech:000004\tcurated split",
    )

    rows, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert errors == []
    assert rows["CultureMech:000002"].lifecycle_status == "MERGED"
    assert rows["CultureMech:000003"].successor_ids == (
        "CultureMech:000001",
        "CultureMech:000004",
    )
    assert rows["CultureMech:000004"].file_path == "corpus/four.yaml"


def test_retired_id_cannot_be_reused(tmp_path):
    corpus = tmp_path / "corpus"
    _recipe(corpus / "reused.yaml", "CultureMech:000001")
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(
        tombstones,
        "CultureMech:000001\tOld recipe\tDELETED\t\tcurated deletion",
    )

    _, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert any("retired id reused" in error for error in errors)


def test_live_id_rebinding_changes_the_lineage_signature(tmp_path):
    corpus = tmp_path / "corpus"
    record = corpus / "record.yaml"
    _recipe(record, "CultureMech:000001")
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(tombstones)
    before, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)
    assert errors == []

    record.write_text(
        "id: CultureMech:000001\n"
        f"id_lineage_token: legacy:{'f' * 64}\n"
        "name: Replacement\ningredients: []\n",
        encoding="utf-8",
    )
    after, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert errors == []
    assert (
        before["CultureMech:000001"].lineage_signature
        != after["CultureMech:000001"].lineage_signature
    )


def test_assignment_event_must_name_the_current_id(tmp_path):
    corpus = tmp_path / "corpus"
    record = corpus / "record.yaml"
    record.parent.mkdir()
    record.write_text(
        "id: CultureMech:000001\n"
        "name: Rebound record\n"
        "ingredients: []\n"
        "curation_history:\n"
        "- timestamp: '2026-01-01T00:00:00Z'\n"
        "  curator: culturemech-id-assigner-v1.0\n"
        "  action: Assigned CultureMech ID\n"
        "  notes: 'Assigned stable identifier: CultureMech:000002'\n",
        encoding="utf-8",
    )
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(tombstones)

    _, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert any("ID may have been reassigned" in error for error in errors)


def test_registry_refresher_accepts_a_quoted_canonical_id(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "record.yaml").write_text(
        "id: 'CultureMech:000001'\nname: Quoted\ningredients: []\n",
        encoding="utf-8",
    )

    found, missing, duplicates = registry_refresher.scan_corpus(corpus)

    assert found == {"CultureMech:000001": corpus / "record.yaml"}
    assert missing == []
    assert duplicates == {}


def test_allocator_starts_above_a_retired_high_water_id(tmp_path, monkeypatch):
    corpus = tmp_path / "corpus"
    _recipe(corpus / "one.yaml", "CultureMech:000001", "First")
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(
        tombstones,
        "CultureMech:000002\tRetired latest recipe\tDELETED\t\tcurated deletion",
    )
    registry = tmp_path / "registry.tsv"
    registry.write_text(
        "culturemech_id\tfile_path\nCultureMech:000001\tcorpus/one.yaml\n",
        encoding="utf-8",
    )
    rows, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)
    assert errors == []
    published = tmp_path / "catalog.tsv"
    published.write_text(catalog.render_catalog(rows), encoding="utf-8")
    missing = corpus / "new.yaml"
    missing.write_text("name: New recipe\ningredients: []\n", encoding="utf-8")
    (tmp_path / "data").mkdir()

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "assign_culturemech_ids.py",
            "--input-dir",
            str(corpus),
            "--registry-output",
            str(registry),
            "--catalog",
            str(published),
            "--tombstones",
            str(tombstones),
        ],
    )

    assert assigner.main() == 0
    assert yaml.safe_load(missing.read_text(encoding="utf-8"))["id"] == "CultureMech:000003"


def test_allocator_refuses_exhaustion_before_writing_any_record(tmp_path, monkeypatch):
    corpus = tmp_path / "corpus"
    _recipe(corpus / "existing.yaml", "CultureMech:999998")
    missing = [corpus / "new-a.yaml", corpus / "new-b.yaml"]
    for path in missing:
        path.write_text("name: New recipe\ningredients: []\n", encoding="utf-8")
    registry = tmp_path / "registry.tsv"
    registry.write_text(
        "culturemech_id\tfile_path\nCultureMech:999998\tcorpus/existing.yaml\n",
        encoding="utf-8",
    )
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(tombstones)
    (tmp_path / "data").mkdir()
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "assign_culturemech_ids.py",
            "--input-dir",
            str(corpus),
            "--registry-output",
            str(registry),
            "--catalog",
            str(tmp_path / "missing-catalog.tsv"),
            "--tombstones",
            str(tombstones),
        ],
    )

    assert assigner.main() == 2
    assert all("id" not in yaml.safe_load(path.read_text(encoding="utf-8")) for path in missing)


def test_active_registry_refuses_an_unrecorded_retirement(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    registry = tmp_path / "registry.tsv"
    registry.write_text(
        "culturemech_id\tfile_path\nCultureMech:000001\tcorpus/deleted.yaml\n",
        encoding="utf-8",
    )
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(tombstones)

    result = registry_refresher.main(
        [
            "--corpus",
            str(corpus),
            "--registry",
            str(registry),
            "--tombstones",
            str(tombstones),
            "--dry-run",
        ]
    )

    assert result == 2


def test_active_registry_accepts_a_recorded_retirement(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    registry = tmp_path / "registry.tsv"
    registry.write_text(
        "culturemech_id\tfile_path\nCultureMech:000001\tcorpus/deleted.yaml\n",
        encoding="utf-8",
    )
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(
        tombstones,
        "CultureMech:000001\tDeleted recipe\tDELETED\t\tcurated deletion",
    )

    result = registry_refresher.main(
        [
            "--corpus",
            str(corpus),
            "--registry",
            str(registry),
            "--tombstones",
            str(tombstones),
            "--dry-run",
        ]
    )

    assert result == 0


def test_unrecorded_gap_is_rejected(tmp_path):
    corpus = tmp_path / "corpus"
    _recipe(corpus / "one.yaml", "CultureMech:000001")
    _recipe(corpus / "three.yaml", "CultureMech:000003")
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(tombstones)

    _, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert any("CultureMech:000002" in error and "absent" in error for error in errors)


@pytest.mark.parametrize(
    ("status", "successors", "message"),
    [
        ("DELETED", "CultureMech:000001", "cannot have successors"),
        ("MERGED", "", "exactly one successor"),
        ("SPLIT", "CultureMech:000001", "at least two successors"),
    ],
)
def test_status_specific_successor_cardinality(tmp_path, status, successors, message):
    corpus = tmp_path / "corpus"
    _recipe(corpus / "one.yaml", "CultureMech:000001")
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(
        tombstones,
        f"CultureMech:000002\tOld recipe\t{status}\t{successors}\tcurated transition",
    )

    _, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert any(message in error for error in errors)


def test_successor_cycles_are_rejected(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(
        tombstones,
        "CultureMech:000001\tFirst\tMERGED\tCultureMech:000002\tcurated merge",
        "CultureMech:000002\tSecond\tMERGED\tCultureMech:000001\tcurated merge",
    )

    _, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert any("successor cycle" in error for error in errors)


def test_split_successors_must_be_distinct(tmp_path):
    corpus = tmp_path / "corpus"
    _recipe(corpus / "one.yaml", "CultureMech:000001")
    tombstones = tmp_path / "tombstones.tsv"
    _tombstones(
        tombstones,
        "CultureMech:000002\tSplit record\tSPLIT\t"
        "CultureMech:000001;CultureMech:000001\tcurated split",
    )

    _, errors = catalog.build_catalog(corpus, tombstones, repo_root=tmp_path)

    assert any("successor_ids must be unique" in error for error in errors)


@pytest.mark.parametrize("value", ["CultureMech:000000", "CultureMech:1000000"])
def test_ids_outside_the_serialized_range_are_rejected(value):
    assert catalog.id_number(value) is None


@pytest.mark.corpus
def test_tracked_catalog_is_complete_current_and_versioned():
    rows, errors = catalog.build_catalog()

    assert errors == []
    assert catalog.DEFAULT_OUT.read_text(encoding="utf-8") == catalog.render_catalog(rows)
    live_files = sum(1 for _ in catalog.DEFAULT_CORPUS.rglob("*.yaml"))
    assert sum(row.lifecycle_status == "ACTIVE" for row in rows.values()) == live_files
    retired = {key for key, row in rows.items() if row.lifecycle_status != "ACTIVE"}
    assert retired == {
        "CultureMech:000190",
        "CultureMech:000306",
        "CultureMech:003009",
        "CultureMech:015406",
    }
    assert {row.lifecycle_status for row in rows.values()} == {"ACTIVE", "DELETED"}
    assert all(
        line.endswith("\t" + catalog.CATALOG_SCHEMA_VERSION)
        for line in catalog.DEFAULT_OUT.read_text(encoding="utf-8").splitlines()[1:]
    )


def test_schema_declares_id_as_the_required_external_identifier():
    schema_path = catalog.REPO / "src" / "culturemech" / "schema" / "culturemech.yaml"
    classes = yaml.safe_load(schema_path.read_text(encoding="utf-8"))["classes"]
    for class_name, former_name_identifier in (
        ("MediaRecipe", "name"),
        ("SolutionRecipe", "preferred_term"),
    ):
        attributes = classes[class_name]["attributes"]
        assert attributes["id"]["required"] is True
        assert attributes["id"]["identifier"] is True
        assert attributes["id"]["pattern"] == r"^CultureMech:(?!000000)\d{6}$"
        assert "identifier" not in attributes[former_name_identifier]


def _rows_in_all_committed_versions(relative_path: str) -> list[dict[str, str]]:
    """Collect complete rows from every version reachable in Git history."""
    history = subprocess.run(
        ["git", "log", "--format=%H", "--", relative_path],
        cwd=catalog.REPO,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    rows: list[dict[str, str]] = []
    for commit in history:
        shown = subprocess.run(
            ["git", "show", f"{commit}:{relative_path}"],
            cwd=catalog.REPO,
            capture_output=True,
            text=True,
        )
        if shown.returncode:
            continue
        rows.extend(csv.DictReader(io.StringIO(shown.stdout), delimiter="\t"))
    return rows


@pytest.mark.corpus
def test_published_catalog_never_forgets_an_issued_id():
    """An ID cannot disappear or be rebound to another record lineage."""
    current, errors = catalog.build_catalog()
    assert errors == []
    historical_rows = _rows_in_all_committed_versions("data/culturemech_recipe_catalog.tsv")
    historical_ids = {(row.get("culturemech_id") or "").strip() for row in historical_rows} - {""}
    assert historical_ids <= set(current), (
        "published CultureMech IDs disappeared from the lifecycle catalog: "
        f"{sorted(historical_ids - set(current))[:10]}"
    )
    rebound = []
    for row in historical_rows:
        culturemech_id = (row.get("culturemech_id") or "").strip()
        historical_signature = (row.get("lineage_signature") or "").strip()
        if (
            culturemech_id in current
            and historical_signature
            and historical_signature != current[culturemech_id].lineage_signature
        ):
            rebound.append(culturemech_id)
    assert not rebound, f"published CultureMech IDs were rebound: {sorted(set(rebound))[:10]}"


@pytest.mark.corpus
def test_tombstone_ledger_is_append_only():
    current, errors = catalog.read_tombstones(catalog.DEFAULT_TOMBSTONES)
    assert errors == []
    current_rows = {
        row["culturemech_id"]: row
        for row in csv.DictReader(
            io.StringIO(catalog.DEFAULT_TOMBSTONES.read_text(encoding="utf-8")),
            delimiter="\t",
        )
    }
    changed = []
    for historical in _rows_in_all_committed_versions("data/culturemech_id_tombstones.tsv"):
        culturemech_id = (historical.get("culturemech_id") or "").strip()
        if culturemech_id not in current_rows or historical != current_rows[culturemech_id]:
            changed.append(culturemech_id)
    assert not changed, (
        "published CultureMech tombstone rows disappeared or changed: "
        f"{sorted(set(changed))[:10]}"
    )
