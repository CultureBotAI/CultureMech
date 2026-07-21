"""Tests for scripts/extract_roles_from_edison.py — Step 7b role extractor."""

from __future__ import annotations

import importlib.util
import json
import sys
import textwrap
from pathlib import Path

import pytest
import yaml


_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "extract_roles_from_edison.py"

_SPEC = importlib.util.spec_from_file_location("_extract_roles", _SCRIPT_PATH)
_ext = importlib.util.module_from_spec(_SPEC)
sys.modules["_extract_roles"] = _ext
_SPEC.loader.exec_module(_ext)  # type: ignore[union-attr]


_MODEL_YAML_ANSWER = textwrap.dedent("""\
    Some prose from the model here...

    ```yaml
    role_research:
      ingredient: L-cysteine
      ingredient_identifier: CHEBI:17561
      nutritional_roles:
        - role: SULFUR_SOURCE
          confidence: 0.95
          evidence:
            - reference_type: PEER_REVIEWED_PUBLICATION
              doi: 10.1128/jb.00456-20
              reference_text: "Smith et al. 2020, J. Bacteriol."
        - role: AMINO_ACID_SOURCE
          confidence: 0.9
          evidence: []
      physicochemical_roles:
        - role: REDUCING_AGENT
          confidence: 0.85
          metabolic_context: "in anaerobic media"
          evidence:
            - reference_type: PEER_REVIEWED_PUBLICATION
              doi: 10.5555/xyz.2019
      cellular_metabolic_roles:
        - role: SUBSTRATE
          confidence: 0.9
          metabolic_context: "assimilatory sulfate reduction"
          evidence: []
      warnings:
        - "Do not confuse with cystine."
    ```

    (End of report.)
    """)


def _write_bundle(tmp_path: Path, slug: str, body_md: str, meta: dict | None = None,
                  citations_text: str | None = None) -> Path:
    """Write a complete Edison bundle under `tmp_path` and return the .md path."""
    md = tmp_path / f"{slug}-edison-literature.md"
    md.write_text(body_md)
    if meta is not None:
        (tmp_path / f"{slug}-edison-literature-meta.yaml").write_text(yaml.safe_dump(meta))
    if citations_text is not None:
        (tmp_path / f"{slug}-edison-literature-citations.md").write_text(citations_text)
    return md


# ---------------- find_role_yaml_block ----------------


def test_find_role_yaml_block_finds_last_matching_fence():
    """Template's own example is in an early fence; the model's answer must win."""
    text = textwrap.dedent("""\
        Template example:
        ```yaml
        role_research:
          ingredient: EXAMPLE
        ```

        Model's actual answer:
        ```yaml
        role_research:
          ingredient: L-cysteine
          nutritional_roles:
            - role: SULFUR_SOURCE
        ```
        """)
    rr = _ext.find_role_yaml_block(text)
    assert rr["ingredient"] == "L-cysteine"


def test_find_role_yaml_block_returns_none_when_absent():
    text = "no yaml here.\n\nJust prose."
    assert _ext.find_role_yaml_block(text) is None


def test_find_role_yaml_block_skips_non_role_yaml_fences():
    """Other ```yaml``` blocks in the doc don't confuse the finder."""
    text = textwrap.dedent("""\
        Some other yaml:
        ```yaml
        unrelated: data
        ```
        The real answer:
        ```yaml
        role_research:
          ingredient: X
        ```
        """)
    rr = _ext.find_role_yaml_block(text)
    assert rr["ingredient"] == "X"


def test_find_role_yaml_block_tolerates_yml_tag():
    text = "```yml\nrole_research:\n  ingredient: X\n```"
    rr = _ext.find_role_yaml_block(text)
    assert rr["ingredient"] == "X"


def test_find_role_yaml_block_skips_malformed_yaml():
    """A malformed yaml fence shouldn't block a later valid one."""
    text = textwrap.dedent("""\
        ```yaml
        role_research:
          ingredient: LATER
        ```
        ```yaml
        role_research: [malformed:: yaml
        ```
        """)
    # Note: reversed iteration means malformed is tried first, then falls back to good one.
    rr = _ext.find_role_yaml_block(text)
    assert rr["ingredient"] == "LATER"


# ---------------- _parse_citations_sidecar ----------------


def test_parse_citations_sidecar_indexes_by_doi(tmp_path):
    sidecar = tmp_path / "cite.md"
    sidecar.write_text(textwrap.dedent("""\
        # Citations

        - **1.** (smith2020) Smith et al. 2020, J. Bacteriol. doi:10.1128/jb.00456-20
        - **2.** (jones2019) Jones et al. 2019, Nature. doi:10.5555/xyz.2019
        """))
    lookup = _ext._parse_citations_sidecar(sidecar)
    assert "10.1128/jb.00456-20" in lookup
    assert "10.5555/xyz.2019" in lookup
    assert "Smith et al" in lookup["10.1128/jb.00456-20"]


def test_parse_citations_sidecar_indexes_pmid(tmp_path):
    sidecar = tmp_path / "cite.md"
    sidecar.write_text("- **1.** (foo) PMID: 12345678. Old paper.")
    lookup = _ext._parse_citations_sidecar(sidecar)
    assert "PMID:12345678" in lookup


def test_parse_citations_sidecar_missing_file_returns_empty(tmp_path):
    assert _ext._parse_citations_sidecar(tmp_path / "nonexistent.md") == {}


# ---------------- _upgrade_evidence ----------------


def test_upgrade_evidence_fills_reference_text_by_doi():
    lookup = {"10.1128/jb.00456-20": "Smith et al. 2020, J. Bacteriol. doi:10.1128/jb.00456-20"}
    evidence = [{"doi": "10.1128/jb.00456-20", "reference_type": "PEER_REVIEWED_PUBLICATION"}]
    up = _ext._upgrade_evidence(evidence, lookup)
    assert "Smith et al" in up[0]["reference_text"]


def test_upgrade_evidence_preserves_existing_reference_text():
    lookup = {"10.1128/jb.00456-20": "Sidecar version"}
    evidence = [{"doi": "10.1128/jb.00456-20", "reference_text": "Curator's version"}]
    up = _ext._upgrade_evidence(evidence, lookup)
    assert up[0]["reference_text"] == "Curator's version"  # never overwrite


def test_upgrade_evidence_leaves_untouched_when_no_match():
    evidence = [{"doi": "10.9999/unknown", "reference_type": "X"}]
    up = _ext._upgrade_evidence(evidence, {})
    assert up[0].get("reference_text") is None


# ---------------- extract_one end-to-end ----------------


def test_extract_one_full_bundle(tmp_path):
    md = _write_bundle(
        tmp_path, "L-cysteine", _MODEL_YAML_ANSWER,
        meta={"slug": "L-cysteine", "ingredient_path": "data/ingredients/mapped/L-cysteine.yaml",
              "ingredient_id": "CHEBI:17561"},
        citations_text=textwrap.dedent("""\
            - **1.** (smith2020) Smith et al. 2020, J. Bacteriol. doi:10.1128/jb.00456-20
            - **2.** (jones2019) Jones et al. 2019, Nature. doi:10.5555/xyz.2019
            """),
    )
    proposal = _ext.extract_one(md)
    assert proposal is not None
    assert proposal["ingredient_slug"] == "L-cysteine"
    assert proposal["ingredient_identifier"] == "CHEBI:17561"
    assert proposal["ingredient_path"] == "data/ingredients/mapped/L-cysteine.yaml"
    assert proposal["source_run"] == "L-cysteine-edison-literature"

    ra = proposal["role_assignments"]
    # Nutritional: 2 roles.
    nut_tokens = [r["role"] for r in ra["nutritional_roles"]]
    assert set(nut_tokens) == {"SULFUR_SOURCE", "AMINO_ACID_SOURCE"}
    # Sulfur got its reference_text filled in from citations sidecar.
    sulfur = next(r for r in ra["nutritional_roles"] if r["role"] == "SULFUR_SOURCE")
    assert "Smith et al" in sulfur["evidence"][0]["reference_text"]

    # Physicochem: 1 role, metabolic_context DROPPED (schema-illegal on non-cellular facet).
    phys = ra["physicochemical_roles"]
    assert len(phys) == 1
    assert phys[0]["role"] == "REDUCING_AGENT"
    assert "metabolic_context" not in phys[0]

    # Cellular metabolic: 1 role, metabolic_context PRESERVED.
    cm = ra["cellular_metabolic_roles"]
    assert cm[0]["role"] == "SUBSTRATE"
    assert cm[0]["metabolic_context"] == "assimilatory sulfate reduction"

    assert proposal["warnings"] == ["Do not confuse with cystine."]


def test_extract_one_returns_none_when_no_yaml_block(tmp_path):
    md = _write_bundle(tmp_path, "unmapped_slug", "Model said no useful roles.")
    assert _ext.extract_one(md) is None


def test_extract_one_returns_none_when_all_facets_empty(tmp_path):
    body = textwrap.dedent("""\
        ```yaml
        role_research:
          ingredient: X
          nutritional_roles: []
          physicochemical_roles: []
          cellular_metabolic_roles: []
        ```
        """)
    md = _write_bundle(tmp_path, "X", body)
    assert _ext.extract_one(md) is None


def test_extract_one_falls_back_to_meta_slug(tmp_path):
    """If the YAML block omits `ingredient:` fall back to meta.slug."""
    body = textwrap.dedent("""\
        ```yaml
        role_research:
          nutritional_roles:
            - role: CARBON_SOURCE
        ```
        """)
    md = _write_bundle(tmp_path, "some_slug", body,
                       meta={"slug": "some_slug", "ingredient_id": "CHEBI:99999"})
    proposal = _ext.extract_one(md)
    assert proposal["ingredient_slug"] == "some_slug"
    assert proposal["ingredient_identifier"] == "CHEBI:99999"


def test_extract_one_coerces_string_shorthand(tmp_path):
    """Model can emit shorthand `- SULFUR_SOURCE` — extractor upgrades to dict form."""
    body = textwrap.dedent("""\
        ```yaml
        role_research:
          ingredient: X
          nutritional_roles:
            - CARBON_SOURCE
            - {role: NITROGEN_SOURCE, confidence: 0.9}
        ```
        """)
    md = _write_bundle(tmp_path, "X", body)
    proposal = _ext.extract_one(md)
    nut = proposal["role_assignments"]["nutritional_roles"]
    assert [r["role"] for r in nut] == ["CARBON_SOURCE", "NITROGEN_SOURCE"]
    # Shorthand entry got default confidence 0.7.
    assert nut[0]["confidence"] == 0.7
    assert nut[1]["confidence"] == 0.9


def test_extract_one_drops_entries_without_role(tmp_path):
    body = textwrap.dedent("""\
        ```yaml
        role_research:
          ingredient: X
          nutritional_roles:
            - confidence: 0.9   # no role key — drop
            - role: CARBON_SOURCE
        ```
        """)
    md = _write_bundle(tmp_path, "X", body)
    proposal = _ext.extract_one(md)
    nut = proposal["role_assignments"]["nutritional_roles"]
    assert [r["role"] for r in nut] == ["CARBON_SOURCE"]


# ---------------- _to_cm_shape ----------------


def test_to_cm_shape_flattens_to_scalar_tokens():
    mim = {
        "ingredient_slug": "X",
        "ingredient_identifier": "CHEBI:1",
        "source_run": "X-edison-literature",
        "role_assignments": {
            "nutritional_roles": [
                {"role": "SULFUR_SOURCE", "confidence": 0.95, "evidence": [{"doi": "..."}]},
                {"role": "AMINO_ACID_SOURCE", "confidence": 0.9, "evidence": []},
            ],
            "physicochemical_roles": [{"role": "REDUCING_AGENT", "confidence": 0.85, "evidence": []}],
        },
    }
    cm = _ext._to_cm_shape(mim)
    assert cm["ingredient_slug"] == "X"
    assert cm["ingredient_identifier"] == "CHEBI:1"
    assert cm["roles"] == {
        "nutritional_roles": ["SULFUR_SOURCE", "AMINO_ACID_SOURCE"],
        "physicochemical_roles": ["REDUCING_AGENT"],
    }
    # Evidence intentionally not carried through — CultureMech carries scalars only.
    assert "evidence" not in json.dumps(cm)


def test_to_cm_shape_skips_facets_without_roles():
    mim = {
        "ingredient_slug": "X",
        "role_assignments": {"nutritional_roles": [{"role": "CARBON_SOURCE"}]},
    }
    cm = _ext._to_cm_shape(mim)
    assert cm["roles"] == {"nutritional_roles": ["CARBON_SOURCE"]}


# ---------------- discover_inputs ----------------


def test_discover_inputs_expands_directory(tmp_path):
    (tmp_path / "a-edison-literature.md").write_text("x")
    (tmp_path / "b-edison-literature.md").write_text("y")
    (tmp_path / "c-something-else.md").write_text("z")
    files = _ext.discover_inputs([tmp_path])
    names = sorted(f.name for f in files)
    assert names == ["a-edison-literature.md", "b-edison-literature.md"]


def test_discover_inputs_dedups_repeated_paths(tmp_path):
    p = tmp_path / "x-edison-literature.md"
    p.write_text("")
    files = _ext.discover_inputs([p, p, tmp_path])
    assert len(files) == 1


# ---------------- CLI main ----------------


def test_main_writes_both_batches(tmp_path):
    _write_bundle(tmp_path, "L-cysteine", _MODEL_YAML_ANSWER,
                  meta={"slug": "L-cysteine", "ingredient_id": "CHEBI:17561"})
    out_mim = tmp_path / "mim.json"
    out_cm = tmp_path / "cm.json"
    rc = _ext.main([str(tmp_path), "--out-mim", str(out_mim), "--out-cm", str(out_cm)])
    assert rc == 0
    mim_data = json.loads(out_mim.read_text())
    assert len(mim_data["proposals"]) == 1
    # MIM batch shape matches PR2 applier's _load_batch expectations.
    p = mim_data["proposals"][0]
    assert "ingredient_identifier" in p
    assert "role_assignments" in p
    assert "nutritional_roles" in p["role_assignments"]
    # CM batch has the scalar shape.
    cm_data = json.loads(out_cm.read_text())
    cp = cm_data["proposals"][0]
    assert cp["roles"]["nutritional_roles"] == ["SULFUR_SOURCE", "AMINO_ACID_SOURCE"]


def test_main_returns_2_when_no_inputs(tmp_path, capsys):
    empty = tmp_path / "empty"
    empty.mkdir()
    rc = _ext.main([str(empty)])
    assert rc == 2


def test_main_records_skipped_files(tmp_path):
    _write_bundle(tmp_path, "no-roles", "Model said no useful roles.")
    out_mim = tmp_path / "mim.json"
    out_cm = tmp_path / "cm.json"
    skipped = tmp_path / "skipped.md"
    rc = _ext.main([str(tmp_path), "--out-mim", str(out_mim), "--out-cm", str(out_cm),
                    "--skipped-report", str(skipped)])
    assert rc == 0
    assert "no `role_research:` fenced YAML block" in skipped.read_text()
    assert json.loads(out_mim.read_text())["proposals"] == []
