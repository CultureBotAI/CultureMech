"""Source projection, immutable provenance, and guarded medium323 application."""

import copy
import json
import subprocess

import pytest
import repair_medium323_ingredients as repair

pytestmark = pytest.mark.usefixtures("no_reference_cache_reads")


@pytest.fixture
def plan():
    return json.loads(repair.PLAN_PATH.read_text())


@pytest.fixture(params=["K323", "D323", "S599", "S6552"])
def reviewed(plan, request):
    item = next(r for r in plan["records"] if r["key"] == request.param)
    return (
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
        item,
    )


def rehash(item, doc):
    item["after_text"] = repair.runner.render(item["before_text"], doc).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_independent_source_review(reviewed):
    before, after, item = reviewed
    counts = repair.audit.check(before, after, item)
    assert counts["new_curation_history"] == 1
    assert counts["new_evidence"] > 0
    assert after["curation_history"][:-1] == before["curation_history"]


@pytest.mark.parametrize(
    "change",
    [
        "amount",
        "basis",
        "chemical",
        "snippet",
        "explanation",
        "history",
        "metadata",
        "claims",
        "delta",
        "publication",
    ],
)
def test_rehashed_common_forgery_rejected(reviewed, change):
    before, after, item = reviewed
    node = after.get("composition", after.get("ingredients"))[0]
    if change == "amount":
        node["concentration"]["value"] = "999"
    elif change == "basis":
        node["concentration"]["per_volume"] = "100 ml"
    elif change == "chemical":
        node["term"]["id"] = "CHEBI:15377"
    elif change == "snippet":
        node["evidence"][0]["snippet"] = "Unquoted invented source text"
    elif change == "explanation":
        node["evidence"][0]["explanation"] = "This proves an unrelated medium"
    elif change == "history":
        after["curation_history"][0]["notes"] = "rewritten old history"
    elif change == "metadata":
        after["category"] = "fungal"
    elif change == "claims":
        item["claims"][0]["old"]["value"] = "12345"
    elif change == "delta":
        item["field_changes"].pop()
    else:
        item["publication_identity_resolved"] = True
    rehash(item, after)
    with pytest.raises((AssertionError, KeyError, ValueError)):
        repair.audit.check(before, after, item)


SPECIAL = [
    ("K323", "numeric_null"),
    ("K323", "duplicate"),
    ("K323", "carbonate_id"),
    ("K323", "stereochemistry"),
    ("K323", "equivalence"),
    ("K323", "physical_state"),
    ("D323", "wrong_dose"),
    ("D323", "wrong_stock"),
    ("D323", "stock_identity"),
    ("D323", "water_identity"),
    ("D323", "trim_note"),
    ("D323", "heating"),
    ("D323", "relationship"),
    ("S599", "prior_evidence"),
    ("S599", "sodium_identity"),
    ("S599", "swapped_rows"),
    ("S6552", "placeholder"),
    ("S6552", "bibliography"),
]


@pytest.mark.parametrize("key,change", SPECIAL)
def test_specific_forgery_rejected(plan, key, change):
    item = next(r for r in plan["records"] if r["key"] == key)
    before, after = (repair.runner.load_yaml(item[f]) for f in ("before_text", "after_text"))
    if change == "numeric_null":
        node = next(n for n in after["ingredients"] if n["preferred_term"] == "n-Butyric acid")
        node["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif change == "duplicate":
        after["ingredients"][-1] = copy.deepcopy(after["ingredients"][-2])
    elif change == "carbonate_id":
        node = next(n for n in after["ingredients"] if n["preferred_term"] == "NaHCO3")
        node["term"] = {"id": "CHEBI:29377", "label": "sodium carbonate"}
    elif change == "stereochemistry":
        after["ingredients"][9]["term"] = {
            "id": "CHEBI:15377",
            "label": "water",
        }
    elif change == "equivalence":
        after["parent_media"]["relationship"] = "SOURCE_DUPLICATE"
    elif change == "physical_state":
        after["physical_state"] = "LIQUID"
    elif change == "wrong_dose":
        after["solutions"][0]["concentration"]["value"] = "1.4"
    elif change == "wrong_stock":
        after["solutions"][0]["culturemech_term"]["id"] = "CultureMech:014736"
    elif change == "stock_identity":
        after["solutions"][0]["composition"][2]["term"] = {
            "id": "CHEBI:26710",
            "label": "sodium chloride",
        }
    elif change == "water_identity":
        after["ingredients"][13]["term"] = {"id": "CHEBI:26710", "label": "sodium chloride"}
    elif change == "trim_note":
        after["ingredients"][12]["notes"] = after["ingredients"][12]["notes"].lstrip()
    elif change == "heating":
        after["preparation_steps"][2]["action"] = "HEAT"
    elif change == "relationship":
        after["variant_children"][0]["id"] = "CultureMech:014736"
    elif change == "prior_evidence":
        after["composition"][0]["evidence"][0]["explanation"] += " Different earlier claim."
    elif change == "sodium_identity":
        after["composition"][8]["chebi_term"] = {"id": "CHEBI:8806", "label": "Resazurin"}
    elif change == "swapped_rows":
        a, b = after["composition"][2:4]
        a["evidence"], b["evidence"] = b["evidence"], a["evidence"]
    elif change == "placeholder":
        after["ingredients"] = copy.deepcopy(before["ingredients"])
    else:
        after["references"][0]["title"] = "Invented title"
    rehash(item, after)
    with pytest.raises((AssertionError, KeyError, ValueError)):
        repair.audit.check(before, after, item)


def tree(tmp_path, plan):
    root = tmp_path.resolve()
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    for item in plan["records"]:
        path = root / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "add", "data/normalized_yaml"], cwd=root, check=True)
    return root


def test_apply_readback_repeat_noop(tmp_path, plan):
    root = tree(tmp_path, plan)
    assert repair.apply(plan, root) == {"changed": 4, "already_applied": 0}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 4}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 4}


@pytest.mark.parametrize(
    "change", ["drift", "duplicate", "case", "symlink", "ancestor", "verify", "late_drift"]
)
def test_whole_batch_preflight(tmp_path, plan, change, monkeypatch):
    root = tree(tmp_path, plan)
    first = root / plan["records"][0]["path"]
    original = first.read_bytes()
    last = root / plan["records"][-1]["path"]
    if change == "drift":
        last.write_bytes(last.read_bytes() + b"\n# concurrent edit\n")
    elif change == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif change == "case":
        plan["records"][-1]["path"] = plan["records"][-1]["path"].replace("treponema", "TREPONEMA")
    elif change == "symlink":
        external = root / "outside.yaml"
        last.rename(external)
        last.symlink_to(external)
    elif change == "ancestor":
        external = root / "outside"
        last.parent.rename(external)
        last.parent.symlink_to(external, target_is_directory=True)
    elif change == "late_drift":
        real_check = repair.audit.check

        def changing_check(before, after, item):
            result = real_check(before, after, item)
            if item["key"] == plan["records"][-1]["key"]:
                first.write_bytes(original + b"\n# concurrent edit during preflight\n")
            return result

        monkeypatch.setattr(repair.audit, "check", changing_check)
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=change == "verify")
    assert first.read_bytes() == (
        original + b"\n# concurrent edit during preflight\n" if change == "late_drift" else original
    )


@pytest.mark.parametrize("which", ["DRAFT", "CAPTURE"])
def test_review_input_tampering(tmp_path, monkeypatch, which):
    path = tmp_path / "forged.json"
    path.write_text("{}")
    monkeypatch.setattr(repair.audit, which, path)
    with pytest.raises(AssertionError, match="Reviewed input drift"):
        repair.audit.reviewed() if which == "DRAFT" else repair.audit.sources()


def test_late_parent_symlink_rejected(tmp_path, plan, monkeypatch):
    root = tree(tmp_path, plan)
    first = root / plan["records"][0]["path"]
    original = first.read_bytes()
    real_check = repair.audit.check

    def changing_check(before, after, item):
        result = real_check(before, after, item)
        if item["key"] == plan["records"][-1]["key"]:
            parent = first.parent
            relocated = root / "late-relocated"
            parent.rename(relocated)
            parent.symlink_to(relocated, target_is_directory=True)
        return result

    monkeypatch.setattr(repair.audit, "check", changing_check)
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root)
    assert first.read_bytes() == original


def test_complete_source_preserves_supported_cysteine_identity(plan):
    item = next(r for r in plan["records"] if r["key"] == "K323")
    before, after = (repair.runner.load_yaml(item[f]) for f in ("before_text", "after_text"))
    old, new = before["ingredients"][9], after["ingredients"][9]
    assert old["term"] == new["term"]
    assert old["mediaingredientmech_chebi_term"] == new["mediaingredientmech_chebi_term"]
    assert repair.audit.CYSTEINE_SEED_ROW in new["evidence"][0]["explanation"]
    new.pop("term")
    rehash(item, after)
    with pytest.raises((AssertionError, KeyError)):
        repair.audit.check(before, after, item)


def test_preview_is_read_only(tmp_path, plan):
    root = tree(tmp_path, plan)
    # git rev-parse requires a baseline commit; this stays inside the fixture tree.
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.invalid",
            "commit",
            "-qm",
            "fixture",
        ],
        cwd=root,
        check=True,
    )
    preview = repair.preview(root)
    assert len(preview["records"]) == 4
    for item in preview["records"]:
        assert (root / item["path"]).read_text() == item["before_text"]
