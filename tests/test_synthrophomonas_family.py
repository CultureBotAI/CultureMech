"""Source projection, corruption attacks, and guarded medium212 application."""

import copy
import importlib.util
import json
import subprocess
from dataclasses import replace

import pytest
import repair_synthrophomonas_family as repair

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger

spec = importlib.util.spec_from_file_location("synthrophomonas_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads(repair.PLAN_PATH.read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}
DOCS = {
    k: (repair.runner.load_yaml(r["before_text"]), repair.runner.load_yaml(r["after_text"]))
    for k, r in ITEMS.items()
}


def rewritten(item, after):
    item["after_text"] = repair.runner.render(item["before_text"], after).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())
    return item


@pytest.mark.parametrize("key", ITEMS)
def test_independent_projection_accounts_for_every_source_and_old_quantity(key):
    before, after = copy.deepcopy(DOCS[key])
    result = audit.check(before, after, ITEMS[key])
    assert result["source_nodes"] == len(ITEMS[key]["lineage"])
    assert result["old_quantity_slots"] == len(ITEMS[key]["prior_quantities"])


@pytest.mark.parametrize(
    "key,path", [(k, n["pointer"]) for k, r in ITEMS.items() for n in r["lineage"]]
)
def test_invented_quantity_is_rejected_even_with_valid_serialization_and_hash(key, path):
    before, after = copy.deepcopy(DOCS[key])
    item = copy.deepcopy(ITEMS[key])
    audit.get(after, path)["concentration"] = {"value": "987654", "unit": "G_PER_L"}
    with pytest.raises(AssertionError):
        audit.check(before, after, rewritten(item, after))


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "drop_node",
        "extra_node",
        "identity",
        "grounding",
        "quote",
        "history",
        "claim",
        "lineage",
        "title",
        "year",
    ],
)
def test_provenance_or_structure_damage_fails_independent_readback(key, mutation):
    before, after = copy.deepcopy(DOCS[key])
    item = copy.deepcopy(ITEMS[key])
    pointer = item["lineage"][0]["pointer"]
    node = audit.get(after, pointer)
    if mutation == "drop_node":
        audit.get(after, pointer[:-1]).pop(0)
    elif mutation == "extra_node":
        audit.get(after, pointer[:-1]).append(copy.deepcopy(node))
    elif mutation == "identity":
        after["id"] = "CultureMech:999999"
    elif mutation == "grounding":
        node["term"] = {"id": "CHEBI:123", "label": "invented"}
    elif mutation == "quote":
        container = node if node.get("evidence") else after
        container["evidence"][0]["snippet"] = "not an inspected source quotation"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten old event"
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "title":
        after["references"][0]["title"] = "Wrong source title"
    else:
        after["references"][0]["year"] = 2026
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, rewritten(item, after))


@pytest.mark.parametrize("key", ITEMS)
def test_rebuild_is_deterministic_and_does_not_change_input(key):
    before = copy.deepcopy(DOCS[key][0])
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == DOCS[key][0]
    assert (
        after == DOCS[key][1]
        and claims == ITEMS[key]["claims"]
        and lineage == ITEMS[key]["lineage"]
    )


def test_all_prior_evidence_content_and_supported_quantities_survive():
    count, extended = 0, 0
    for before, after in DOCS.values():
        for pointer, old in audit.walk(before):
            if len(pointer) > 1 and pointer[-2] == "evidence":
                new = audit.get(after, pointer)
                assert {k: v for k, v in new.items() if k != "explanation"} == {
                    k: v for k, v in old.items() if k != "explanation"
                }
                assert new["explanation"].startswith(old["explanation"])
                count += 1
                extended += new != old
                if pointer[0] == "composition":
                    assert (
                        audit.get(before, pointer[:2])["concentration"]
                        == audit.get(after, pointer[:2])["concentration"]
                    )
    assert count == 69 and extended == 14


def test_original_mass_inputs_do_not_become_assumed_final_rates():
    missing = 0
    for key, count in (("D212", 6), ("D212a", 9)):
        after = DOCS[key][1]
        assert after["ingredients"] == [] and len(after["solutions"]) == count
        for path, expected in audit.projection(
            key, audit.snapshot((repair.HERE / "context.json").read_bytes())[1]
        ).items():
            if expected["quantity"] is None:
                assert "concentration" not in audit.get(after, path)
                assert "Exact batch input:" in audit.get(after, path)["notes"]
                missing += 1
    assert missing == 49


def test_five_liquid_input_corrections_do_not_assume_density_or_percent_basis():
    for key, index, value in (
        ("S125", 0, "0.0001"),
        ("S125", 1, "0.02"),
        ("S446", 7, "0.0005"),
        ("S453", 7, "0.0005"),
        ("S595", 0, "0.01"),
    ):
        assert DOCS[key][1]["composition"][index]["concentration"] == {"value": value, "unit": "L"}
    assert "95 %" in DOCS["S125"][1]["composition"][1]["notes"]
    assert "25%" in DOCS["S595"][1]["composition"][0]["notes"]
    assert DOCS["S595"][1]["composition"][-1]["concentration"]["unit"] == "VARIABLE"


def test_provider_formulations_nulls_and_strain_annotations_stay_distinct():
    k = DOCS["K212"][1]
    assert sum("concentration" not in n for n in k["ingredients"]) == 4
    assert len(k["ingredients"]) == 32
    old, new = DOCS["B2805"]
    assert [n["concentration"] for n in old["ingredients"]] == [
        n["concentration"] for n in new["ingredients"][:-1]
    ]
    assert (
        new["ingredients"][-1]["preferred_term"] == "Distilled water"
        and "concentration" not in new["ingredients"][-1]
    )
    for field in (
        "target_organisms",
        "parent_media",
        "variant_relationship",
        "variant_modifications",
    ):
        assert new[field] == old[field]
    assert not any(r["reference"].startswith("doi:") for r in new["references"])
    assert "parent_media" not in DOCS["D212a"][1]


def test_corrected_stock_remains_a_byte_exact_noop():
    assert ITEMS["S608"]["before_text"] == ITEMS["S608"]["after_text"]
    assert all(c["status"] == "verified" for c in ITEMS["S608"]["claims"])


def test_unknown_application_mode_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="Invalid mode"):
        repair.process(tmp_path, tmp_path / "plan.json", "unknown")


@pytest.mark.parametrize("constant", ["CONTEXT_SHA", "DECISIONS_SHA", "IDENTITY_SHA"])
def test_pinned_source_and_decision_hashes_are_mandatory(monkeypatch, constant):
    monkeypatch.setattr(repair, constant, "0" * 64)
    with pytest.raises(ValueError, match="drift"):
        repair.frozen()


def test_nickel_form_is_preserved_without_rejected_replacement_mapping():
    for key in ("K212", "D212", "D212a", "B2805", "S595"):
        path, node = next(
            (p, n)
            for p, n in audit.walk(DOCS[key][1])
            if n.get("preferred_term") == "NiCl2 x 6 H2O"
        )
        assert "REJECTED" in node["notes"]
        assert "chebi_term" not in node and "mediaingredientmech_chebi_term" not in node
        if key == "S595":
            assert node["term"] == {"id": "mediadive.compound:40", "label": "NiCl2 x 6 H2O"}
        else:
            assert "term" not in node
        assert node["concentration"]
        assert len(
            [
                c
                for c in ITEMS[key]["claims"]
                if c["kind"] == "chemical_form" and c["pointer"][:-1] == list(path)
            ]
        ) == (2 if key == "S595" else 3)


def test_successor_index_preserves_the_historical_review():
    assert repair.identity_review() == json.loads(
        (repair.HERE / "identity-review.json").read_text()
    )


def test_unreviewed_index_bytes_are_rejected(tmp_path, monkeypatch):
    relative = "src/culturemech/data/mediaingredientmech/label_index.csv"
    target = tmp_path / relative
    target.parent.mkdir(parents=True)
    target.write_bytes((repair.ROOT / relative).read_bytes() + b"\n")
    monkeypatch.setattr(repair, "ROOT", tmp_path)
    with pytest.raises(ValueError, match="Identity index drift"):
        repair.identity_review()


def test_successor_assessment_hash_is_mandatory(monkeypatch):
    monkeypatch.setattr(repair, "INDEX_COMPATIBILITY_SHA", "0" * 64)
    with pytest.raises(ValueError, match="Index compatibility drift"):
        repair.identity_review()


def test_same_index_with_changed_resolution_is_rejected(monkeypatch):
    original = repair.MIMLabelIndex.resolve_label

    def changed(index, label):
        return replace(original(index, label), mapping_status="MAPPED")

    monkeypatch.setattr(repair.MIMLabelIndex, "resolve_label", changed)
    with pytest.raises(ValueError, match="Identity resolution drift"):
        repair.identity_review()


def test_unchanged_amounts_are_evidence_only_not_numerical_corrections():
    for item in ITEMS.values():
        for claim in item["claims"]:
            if (
                claim["pointer"][-1] == "concentration"
                and claim["new"] is not None
                and claim["old"] == claim["new"]
            ):
                assert claim["status"] in {"verified", "evidence_only"}
    rows = [c for c in ITEMS["B2805"]["claims"] if c["pointer"][-1] == "concentration"]
    assert sum(c["status"] == "evidence_only" for c in rows) == 32
    assert rows[-1]["status"] == "not_quantified"


@pytest.mark.parametrize("target", ["K212", "D212a", "S608"])
@pytest.mark.parametrize("mutation", ["concurrent", "symlink"])
def test_changed_file_or_symlink_blocks_every_preview_write(tmp_path, target, mutation):
    paths = {}
    for key, item in ITEMS.items():
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
        paths[key] = path
    if mutation == "concurrent":
        paths[target].write_text(paths[target].read_text() + "# concurrent change\n")
    else:
        outside = tmp_path / "outside.yaml"
        outside.write_bytes(paths[target].read_bytes())
        paths[target].unlink()
        paths[target].symlink_to(outside)
    before = {k: p.read_bytes() for k, p in paths.items()}
    with pytest.raises(ValueError, match="Cohort (baseline drift|symlink)"):
        repair.process(tmp_path, tmp_path / "proposal.json")
    assert not (tmp_path / "proposal.json").exists()
    assert before == {k: p.read_bytes() for k, p in paths.items()}


def fixture_repo(tmp_path, monkeypatch):
    context, _ = repair.frozen()
    for item in context["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "init", "--quiet"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "data/normalized_yaml"], cwd=tmp_path, check=True)
    original = subprocess.check_output
    monkeypatch.setattr(
        subprocess,
        "check_output",
        lambda args, **kwargs: (
            PLAN["commit"] + "\n"
            if args == ["git", "rev-parse", "HEAD"]
            else original(args, **kwargs)
        ),
    )

    def builder(before, key, timestamp):
        assert before == DOCS[key][0] and timestamp == PLAN["created_at"]
        return copy.deepcopy((DOCS[key][1], ITEMS[key]["claims"], ITEMS[key]["lineage"]))

    monkeypatch.setattr(repair, "build", builder)
    plan = tmp_path / "plan.json"
    plan.write_bytes(repair.PLAN_PATH.read_bytes())
    return plan, {item["key"]: tmp_path / item["path"] for item in context["records"]}


def test_guarded_apply_readback_and_noop(tmp_path, monkeypatch):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 21
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 22
    before = {key: path.read_bytes() for key, path in paths.items()}
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert before == {key: path.read_bytes() for key, path in paths.items()}


@pytest.mark.parametrize("target", ["K212", "D212a", "S608"])
@pytest.mark.parametrize("mutation", ["concurrent", "symlink"])
def test_concurrent_edit_or_symlink_blocks_every_application_write(
    tmp_path, monkeypatch, target, mutation
):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    if mutation == "concurrent":
        paths[target].write_text(paths[target].read_text() + "# concurrent change\n")
    else:
        outside = tmp_path / "outside.yaml"
        outside.write_bytes(paths[target].read_bytes())
        paths[target].unlink()
        paths[target].symlink_to(outside)
    before = {key: path.read_bytes() for key, path in paths.items()}
    with pytest.raises(ValueError, match="Concurrent edit|symlink"):
        repair.process(tmp_path, plan, "apply")
    assert before == {key: path.read_bytes() for key, path in paths.items()}


@pytest.mark.parametrize("mutation", ["removed_record", "changed_claim", "symlink"])
def test_unreviewed_plan_cannot_authorize_application(tmp_path, monkeypatch, mutation):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    if mutation == "symlink":
        plan.unlink()
        plan.symlink_to(repair.PLAN_PATH)
    else:
        changed = copy.deepcopy(PLAN)
        if mutation == "removed_record":
            changed["records"].pop()
        else:
            changed["records"][0]["claims"][0]["snippet"] = "invented"
        plan.write_text(json.dumps(changed))
    before = {key: path.read_bytes() for key, path in paths.items()}
    with pytest.raises(ValueError, match="Unreviewed plan|Plan symlink"):
        repair.process(tmp_path, plan, "apply")
    assert before == {key: path.read_bytes() for key, path in paths.items()}


def test_review_receipt_hash_cannot_be_bypassed(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    monkeypatch.setattr(repair, "REVIEW_SHA", "0" * 64)
    with pytest.raises(ValueError, match="review receipt drift"):
        repair.process(tmp_path, plan, "apply")


def test_frozen_validation_receipt_cannot_be_replaced(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    source = repair.HERE
    directory = tmp_path / "review"
    directory.mkdir()
    gate = json.loads((source / "validation-preview.json").read_text())
    (directory / "validation-preview.json").write_bytes(
        (source / "validation-preview.json").read_bytes()
    )
    for name in gate["receipt_sha256"]:
        (directory / (name + ".json")).write_bytes((source / (name + ".json")).read_bytes())
    (directory / "independent-successor-audit.json").write_text("{}")
    monkeypatch.setattr(repair, "HERE", directory)
    with pytest.raises(ValueError, match="Validation receipt drift"):
        repair.process(tmp_path, plan, "apply")


def test_runtime_merge_retains_all_four_distinct_medium_formulations(tmp_path):
    paths = []
    for key, item in ITEMS.items():
        path = tmp_path / (key + ".yaml")
        path.write_text(item["after_text"])
        paths.append(path)
    groups = RecipeMatcher().group_formulations(paths)
    assert sorted(p.stem for group in groups.values() for p in group) == [
        "B2805",
        "D212",
        "D212a",
        "K212",
    ]
    assert len(groups) == 4
    for group in groups.values():
        assert len(group) == 1
        expected = DOCS[group[0].stem][1]
        merged = RecipeMerger().merge_group(group)
        for field, value in expected.items():
            assert merged[field] == value
