"""Primary-source scope and guarded chemical-form corrections for the M63 grid."""

import copy
import json
import subprocess

import pytest
import review_m63_primary_concentrations as repair


@pytest.fixture
def plan():
    return json.loads(repair.PLAN.read_text())


@pytest.fixture(params=sorted(repair.KEYS))
def reviewed(plan, request):
    item = next(r for r in plan["records"] if r["key"] == request.param)
    return tuple(repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")) + (item,)


def rehash(item, doc):
    item["after_text"] = repair.runner.render(item["before_text"], doc).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_full_claim_inventory_and_evidence_scope(reviewed):
    before, after, item = reviewed
    assert "&id" not in item["after_text"] and "*id" not in item["after_text"]
    assert repair.check(before, after, item) == {
        "new_evidence": 7,
        "new_references": 2,
        "new_curation_history": 1,
        "supplied_hydrate_identities_corrected": 2,
        "ingredient_labels_corrected": 1,
    }
    assert len(item["claims"]) == 7
    assert [c["status"] for c in item["claims"]].count("correct") == 3
    assert [c["status"] for c in item["claims"]].count("evidence_only") == 4
    assert [n["concentration"] for n in before["ingredients"]] == [
        n["concentration"] for n in after["ingredients"]
    ]
    for key in ("preparation_steps", "target_organisms", "parent_media", "variant_children"):
        assert before.get(key) == after.get(key)
    for node in after["ingredients"]:
        if not node.get("evidence"):
            continue
        entry = node["evidence"][0]
        assert entry["reference"] in {
            "doi:10.1186/1471-2180-10-256",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC220425/",
        }
        assert (
            "Other base-medium amounts" in entry["explanation"]
            or "reference 48" in entry["explanation"]
        )
    by_name = {n["preferred_term"]: n for n in after["ingredients"]}
    for label, identifier in (
        ("Potassium dihydrogen phosphate", "CHEBI:63036"),
        ("Magnesium sulfate heptahydrate", "CHEBI:31795"),
        ("Ferrous sulfate heptahydrate", "CHEBI:75836"),
    ):
        assert by_name[label]["term"]["id"] == identifier
    assert len(after["references"][0]["authors"].split("; ")) == 7


def test_old_evidence_only_preview_is_not_applicable():
    old = json.loads((repair.HERE / "plan.json").read_text())
    with pytest.raises(AssertionError):
        repair.apply(old)


@pytest.mark.parametrize("index", range(7))
@pytest.mark.parametrize(
    "field,value", [("value", "999"), ("unit", "G_PER_L"), ("per_volume", "100 mL")]
)
def test_every_ingredient_amount_is_immutable(reviewed, index, field, value):
    before, after, item = reviewed
    after["ingredients"][index]["concentration"][field] = value
    rehash(item, after)
    with pytest.raises(AssertionError):
        repair.check(before, after, item)


@pytest.mark.parametrize(
    "kind",
    [
        "identity",
        "quote",
        "scope",
        "wrong_doi",
        "base_evidence",
        "history",
        "reference",
        "reorder",
        "preparation",
        "claim",
    ],
)
def test_rehashed_semantic_forgery_is_rejected(reviewed, kind):
    before, after, item = reviewed
    node = next(n for n in after["ingredients"] if n.get("evidence"))
    if kind == "identity":
        node["term"] = {"id": "CHEBI:15377", "label": "water"}
    elif kind in {"quote", "scope", "wrong_doi"}:
        key = {"quote": "snippet", "scope": "explanation", "wrong_doi": "reference"}[kind]
        node["evidence"][0][key] = "unreviewed"
    elif kind == "base_evidence":
        after["ingredients"][4]["evidence"] = copy.deepcopy(node["evidence"])
    elif kind == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif kind == "reference":
        after["references"][0]["year"] = 1982
    elif kind == "reorder":
        after["ingredients"].reverse()
    elif kind == "preparation":
        after["preparation_steps"][0]["description"] = "unsupported protocol"
    else:
        item["claims"][4]["status"] = "verified"
    rehash(item, after)
    with pytest.raises((AssertionError, KeyError)):
        repair.check(before, after, item)


def make_repo(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in plan["records"]:
        target = tmp_path / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    # Actual schema checks run separately on every before/after recipe.
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return tmp_path


def test_guarded_apply_and_noop(plan, tmp_path, monkeypatch):
    root = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, root) == {"changed": 12, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 12}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 12}


@pytest.mark.parametrize(
    "kind",
    [
        "late_drift",
        "duplicate",
        "outside",
        "symlink",
        "version",
        "source",
        "verify_before_apply",
        "case",
        "counts",
    ],
)
def test_all_targets_preflight_before_any_write(plan, tmp_path, monkeypatch, kind):
    root = make_repo(tmp_path, plan, monkeypatch)
    original = {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}
    last = plan["records"][-1]
    if kind == "late_drift":
        target = root / last["path"]
        target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
        original[last["path"]] = target.read_bytes()
    elif kind == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif kind == "outside":
        last["path"] = "../../outside.yaml"
    elif kind == "symlink":
        target = root / last["path"]
        saved = root / "elsewhere.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    elif kind == "version":
        plan["version"] = 999
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    elif kind == "case":
        last["path"] = last["path"].replace("modified_m63", "Modified_M63")
    elif kind == "counts":
        last["counts"]["new_evidence"] = 999
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=kind == "verify_before_apply")
    assert all((root / p).read_bytes() == raw for p, raw in original.items())
