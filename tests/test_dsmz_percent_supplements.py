"""Offline source/decision guards for the five percent-supplement repairs."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz_percent_supplements as repair  # noqa: E402

BATCH = ROOT / "reports/ingredient_concentration_curation/20261007-percent-supplements"
PLAN = BATCH / "plan.json"
spec = importlib.util.spec_from_file_location(
    "independent_percent_audit", BATCH / "audit_repair.py"
)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def baseline(key):
    item = next(r for r in json.loads(PLAN.read_text())["records"] if r["key"] == key)
    return repair.load_yaml(item["before_text"])


@pytest.fixture
def sources(monkeypatch):
    result = {}
    for mid, source in repair.SOURCES.items():
        labels = (
            source["labels"][:3] + ["Distilled water", "Agar", "Tween 80"]
            if mid == "618"
            else source["labels"] + ["Distilled water", "Methanol", "Methylamine"]
        )
        rows = [{"compound": label} for label in labels]
        water_index = labels.index("Distilled water")
        rows[water_index] = {
            "recipe_order": water_index + 1,
            "compound": "Distilled water",
            "compound_id": 4,
            "amount": 1000,
            "unit": "ml",
            "optional": 0,
        }
        data = {
            "data": {
                "medium": {
                    "id": int(mid),
                    "name": source["title"],
                    "source": "DSMZ",
                    "link": repair.PDF.format(mid),
                },
                "solutions": [
                    {
                        "id": 1326 if mid == "618" else 1973,
                        "name": "Main sol. " + mid,
                        "volume": 1000,
                        "recipe": rows,
                        "steps": [{"step": source["preparation"]}],
                    }
                ],
            }
        }
        raw = json.dumps(data, indent=4)
        pdf = ("synthetic-pdf-fixture-" + mid).encode()
        monkeypatch.setitem(source, "pdf_sha", repair.sha(pdf))
        monkeypatch.setitem(source, "api_sha", repair.sha(raw.encode()))
        result[mid] = {
            "pdf": pdf,
            "pages": 1,
            "text": repair.expected_text(mid),
            "raw": raw,
            "meta": {
                "url": repair.API + mid,
                "response_url": repair.API + mid,
                "http_status": 200,
                "sha256": repair.sha(raw.encode()),
                "accessed_at": "2026-10-07T00:00:00Z",
            },
        }
    rows = []
    for key in ("k618", "k956", "m956"):
        mid = repair.TARGETS[key][2]
        accession = "956_replace_Methanol_with_Methylamine" if key == "m956" else mid
        name = (
            "TWEEN 80A medium"
            if mid == "618"
            else "MEDIUM FOR DSM 14457 AND 14458"
            + ("_replace_Methanol_with_Methylamine" if key == "m956" else "")
        )
        url = repair.PDF.format(mid).replace("https:", "http:")
        rows.append(
            f'<tr><td><a href="/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo={accession}">{accession}</a></td><td>{name}</td><td>7.2</td><td>{"true" if mid == "618" else "false"}</td><td>false</td><td>false</td><td><a href="{url}">{url}</a></td></tr>'
        )
    result["mapping"] = "<table>" + "".join(rows) + "</table>"
    monkeypatch.setattr(repair, "MAPPING_SHA", repair.sha(result["mapping"].encode()))
    return result


def built(key, sources):
    before = baseline(key)
    after, claims, resolutions = repair.build(before, key, sources, "2026-10-07T00:00:00Z")
    mid = repair.TARGETS[key][2]
    item = {
        "key": key,
        "medium_id": mid,
        "claims": claims,
        "claim_resolutions": resolutions,
        "source_sha256": repair.SOURCES[mid]["api_sha"],
        "pdf_sha256": repair.SOURCES[mid]["pdf_sha"],
        "mapping_sha256": repair.MAPPING_SHA if key[0] != "d" else None,
    }
    return before, after, item


@pytest.mark.parametrize("key", repair.TARGETS)
def test_supported_representation_and_independent_inversion(key, sources):
    before, after, item = built(key, sources)
    counts = audit.check(before, after, item)
    assert counts["unsupported_quantity_slots_removed"] == len(before["ingredients"])
    assert counts["new_quantity_slots"] == 1
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["id"] == before["id"] and after["ph_value"] == before["ph_value"] == 7.2
    assert "concentration" not in after["solutions"][0]
    assert all("concentration" not in node for node in after["solutions"][0]["composition"][:-1])
    assert after["solutions"][0]["composition"][-1]["concentration"] == {"value": "1", "unit": "L"}
    if key in {"d956", "k956"}:
        assert after["ingredients"] == []
        assert [v["name"] for v in after["variants"]] == [
            "Methanol alternative",
            "Methylamine alternative",
        ]
    if key == "m956":
        assert [n["preferred_term"] for n in after["ingredients"]] == ["Methylamine"]
        assert after["parent_media"]["id"] == "CultureMech:002134"


@pytest.mark.parametrize(
    "old,new",
    [
        ("956. MEDIUM", "957. MEDIUM"),
        ("KH2PO4 2.000 g", "KH2PO4 3.000 g"),
        ("FeSO4 x 7 H2O", "FeSO4 x 6 H2O"),
        ("1000.000 ml", "1000.000 L"),
        ("0.5%", "0.5% v/v"),
        ("0.3%", "0.03%"),
        (" or methylamine", " and methylamine"),
        ("sterilised medium", "unsterilised medium"),
        ("pH 7.2", "pH 7.0"),
        ("All rights reserved", "All rights reserved extra instruction"),
    ],
)
def test_pdf_full_scope_not_just_snippet(old, new, sources):
    sources["956"]["text"] = sources["956"]["text"].replace(old, new)
    with pytest.raises(ValueError, match="PDF identity"):
        repair.inspect_sources("956", sources["956"])


@pytest.mark.parametrize(
    "field,value", [("compound_id", 99), ("amount", 100), ("unit", "g"), ("optional", 1)]
)
def test_api_water_scope_even_with_recomputed_fixture_hash(field, value, sources, monkeypatch):
    source = sources["618"]
    data = json.loads(source["raw"])
    data["data"]["solutions"][0]["recipe"][3][field] = value
    source["raw"] = json.dumps(data, indent=4)
    source["meta"]["sha256"] = repair.sha(source["raw"].encode())
    monkeypatch.setitem(repair.SOURCES["618"], "api_sha", source["meta"]["sha256"])
    with pytest.raises(ValueError, match="water identity"):
        repair.inspect_sources("618", source)


@pytest.mark.parametrize("field,value", [("pdf", b"changed"), ("pages", 2)])
def test_pdf_bytes_and_page_count(field, value, sources):
    sources["618"][field] = value
    with pytest.raises(ValueError, match="PDF"):
        repair.inspect_sources("618", sources["618"])


@pytest.mark.parametrize(
    "old,new",
    [
        ("DSMZ_Medium956.pdf", "DSMZ_Medium957.pdf"),
        ("956_replace_Methanol_with_Methylamine", "956_replace_Methylamine_with_Methanol"),
        ("<td>7.2</td>", "<td>8.2</td>"),
        ("MEDIUM FOR DSM 14457 AND 14458", "MEDIUM FOR DSM 14457 AND 14458 VARIANT"),
    ],
)
def test_mapping_semantics_even_with_recomputed_fixture_hash(old, new, sources, monkeypatch):
    raw = sources["mapping"].replace(old, new)
    monkeypatch.setattr(repair, "MAPPING_SHA", repair.sha(raw.encode()))
    with pytest.raises(ValueError, match="source ID"):
        repair.mapping_row("m956", raw)


@pytest.mark.parametrize(
    "field,value",
    [
        ("id", "CultureMech:999999"),
        ("ph_value", 8),
        ("physical_state", "SOLID_AGAR"),
        ("notes", "changed"),
        ("variants", [{"name": "unreviewed"}]),
    ],
)
def test_unreviewed_local_context_rejected(field, value, sources):
    doc = baseline("d956")
    doc[field] = value
    with pytest.raises(ValueError, match="local formulation"):
        repair.build(doc, "d956", sources, "2026-10-07T00:00:00Z")


@pytest.mark.parametrize(
    "key,pointer,value",
    [
        ("d618", ["solutions", 0, "composition", 0, "notes"], "5 g/L"),
        ("d618", ["solutions", 0, "composition", 4, "concentration", "value"], "1000"),
        ("d618", ["solutions", 0, "composition", 4, "concentration", "unit"], "G_PER_L"),
        ("d618", ["ingredients", 0, "notes"], "1% w/v"),
        ("d618", ["ingredients", 0, "concentration"], {"value": "10", "unit": "G_PER_L"}),
        ("d618", ["solutions", 0, "concentration"], {"value": "1", "unit": "L"}),
        ("d956", ["variants", 0, "modifications", 1], "Add both alternatives."),
        ("d956", ["variants", 1, "relationship"], "SOURCE_DUPLICATE"),
        ("d956", ["variants", 1, "evidence", 0, "snippet"], "false quote"),
        ("d956", ["variant_children", 1, "id"], "CultureMech:999999"),
        (
            "d956",
            ["solutions", 0, "composition", 0, "evidence", 0, "explanation"],
            "Verified final concentration.",
        ),
        ("d956", ["solutions", 0, "composition", 0, "term", "id"], "CHEBI:99999"),
        ("m956", ["parent_media", "relationship"], "SOURCE_DUPLICATE"),
        ("m956", ["ingredients", 0, "preferred_term"], "Methanol"),
        ("m956", ["preparation_steps", 0, "description"], "Add both supplements."),
        ("m956", ["evidence", 1, "snippet"], "unverified mapping"),
        ("k618", ["references", 0, "reference"], "https://example.invalid"),
        ("k618", ["curation_history", 0, "notes"], "rewritten history"),
        ("k618", ["ph_value"], 8),
    ],
)
def test_independent_audit_rejects_unreviewed_changes(key, pointer, value, sources):
    before, after, item = built(key, sources)
    node = after
    for part in pointer[:-1]:
        node = node[part]
    node[pointer[-1]] = value
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def make_repo(tmp_path, monkeypatch, sources):
    root = tmp_path / "repo"
    root.mkdir()
    records = json.loads(PLAN.read_text())["records"]
    for item in records:
        path = root / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])

    def git(*args):
        return subprocess.check_output(["git", *args], cwd=root)

    git("init", "-q")
    git("add", "data")
    git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "fixture")
    monkeypatch.setattr(repair, "read_sources", lambda _: copy.deepcopy(sources))
    return root, tmp_path / "plan.json", git


def test_preview_apply_readback_noop_and_unrelated_commit(tmp_path, monkeypatch, sources):
    root, plan, git = make_repo(tmp_path, monkeypatch, sources)
    preview, result = repair.process(root, tmp_path, plan, "preview")
    assert result["changed"] == 0
    with pytest.raises(ValueError, match="overwrite"):
        repair.process(root, tmp_path, plan, "preview")
    assert repair.process(root, tmp_path, plan, "apply")[1]["changed"] == 5
    assert repair.process(root, tmp_path, plan, "verify")[1]["already_applied"] == 5
    assert repair.process(root, tmp_path, plan, "apply")[1]["changed"] == 0
    git(
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.invalid",
        "commit",
        "--allow-empty",
        "-qm",
        "unrelated",
    )
    assert repair.process(root, tmp_path, plan, "verify")[0]["commit"] == preview["commit"]
    repair.report(tmp_path / "reports", preview, True)
    markers = [
        line
        for p in (tmp_path / "reports").rglob("*.md")
        for line in p.read_text().splitlines()
        if line.startswith("- Record:")
    ]
    assert len(markers) == len(set(markers)) == 3


@pytest.mark.parametrize("failure", ["last_record", "plan", "symlink", "case"])
def test_apply_preflight_rejects_drift_without_partial_write(
    failure, tmp_path, monkeypatch, sources
):
    root, plan, git = make_repo(tmp_path, monkeypatch, sources)
    frozen, _ = repair.process(root, tmp_path, plan, "preview")
    last = root / frozen["records"][-1]["path"]
    if failure == "last_record":
        last.write_text(last.read_text() + "# concurrent edit\n")
    elif failure == "plan":
        frozen["records"][-1]["claims"][0]["new"] = "tampered"
        plan.write_text(json.dumps(frozen))
    elif failure == "symlink":
        copy_path = tmp_path / "copy.yaml"
        copy_path.write_bytes(last.read_bytes())
        last.unlink()
        last.symlink_to(copy_path)
    else:
        git("rm", "--cached", frozen["records"][-1]["path"])
    with pytest.raises(ValueError):
        repair.process(root, tmp_path, plan, "apply")
    first = frozen["records"][0]
    assert (root / first["path"]).read_text() == first["before_text"]


def test_applied_successors_and_history():
    plan = json.loads(PLAN.read_text())
    total = 0
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert repair.sha(raw) == item["after_sha256"]
        counts = audit.check(repair.load_yaml(item["before_text"]), repair.load_yaml(raw), item)
        total += counts["unsupported_quantity_slots_removed"]
    assert total == 31
