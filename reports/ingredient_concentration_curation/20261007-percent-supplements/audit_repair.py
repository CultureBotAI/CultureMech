"""Independent semantic inversion of the five reviewed percent-supplement repairs."""

import collections
import copy
import json


def provenance(node):
    result = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                result["new_" + key] += len(value)
            else:
                result.update(provenance(value))
    elif isinstance(node, list):
        for value in node:
            result.update(provenance(value))
    return result


def check(before, after, item):
    key, mid = item["key"], item["medium_id"]
    assert key in {"d618", "k618", "d956", "k956", "m956"}
    assert mid == ("618" if key.endswith("618") else "956")
    reference = f"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{mid}.pdf"
    mapping = (
        "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList"
    )
    is_komodo = key[0] != "d"
    result = collections.Counter()
    restored = copy.deepcopy(after)
    event = restored["curation_history"].pop()
    assert event["action"] == "CORRECTED_DSMZ618_956_BATCH_INPUTS_AND_PERCENT_ALTERNATIVES"
    assert event["curator"] == "codex" and event["source"] == reference
    assert restored["curation_history"] == before["curation_history"]
    assert event["changes"] == "; ".join(
        f"{c['old_field']} -> {c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} ({c['status']})"
        for c in item["claims"]
    )

    def scoped(entry, pointer, snippet):
        assert set(entry) == {"reference", "supports", "snippet", "explanation"}
        assert entry["reference"] == reference and entry["supports"] == "SUPPORT"
        assert entry["snippet"] == snippet and item["pdf_sha256"] in entry["explanation"]
        matching = [
            c
            for c in item["claims"]
            if c["evidence_pointer"] == pointer and c["reference"] == reference
        ]
        assert len(matching) == 1 and entry["explanation"] == matching[0]["explanation"]

    base = restored.pop("solutions")
    assert len(base) == 1
    base = base[0]
    assert set(base) == {"preferred_term", "source", "notes", "composition", "preparation_notes"}
    assert base["preferred_term"] == f"DSMZ {mid} base preparation" and base["source"] == reference
    assert (
        base["notes"]
        == "Curator-described preparation stage, not a separately accessioned stock. Composition records source batch inputs. The 1000 ml water is an input, not an explicit prepared-base or final-medium volume; no absolute base dose is inferred."
    )
    amounts = (
        ["5.0", "3.0", "2.0", "15.0"]
        if mid == "618"
        else ["2.000", "2.000", "0.125", "0.500", "0.002"]
    )
    quotes = (
        [
            "Casitone (Difco) 5.0 g",
            "Yeast extract (Difco) 3.0 g",
            "MgSO4 x 7 H2O 2.0 g",
            "For solid media add 15.0 g agar.",
        ]
        if mid == "618"
        else [
            "KH2PO4 2.000 g",
            "(NH4)2SO4 2.000 g",
            "MgSO4 x 7 H2O 0.125 g",
            "NaCl 0.500 g",
            "FeSO4 x 7 H2O 0.002 g",
        ]
    )
    prep = (
        "For solid media add 15.0 g agar. Dissolve ingredients and adjust the pH to 7.2. Sterilize by autoclaving. After sterilization add sterile Tween 80 to a final concentration of 1.0%."
        if mid == "618"
        else "pH 7.2. To the sterilised medium add sterile methanol (to a final concentration of 0.5%) or methylamine (to a final concentration of 0.3%)."
    )
    assert base["preparation_notes"] == (
        prep.partition(" After sterilization")[0]
        if mid == "618"
        else "pH 7.2. Prepare and sterilise the base before adding the selected supplement; the source does not specify a sterilisation method, temperature, or duration."
    )
    assert len(base["composition"]) == len(amounts) + 1
    for index, (amount, quote) in enumerate(zip(amounts, quotes, strict=True)):
        old = before["ingredients"][index]
        node = base["composition"][index]
        assert "concentration" not in node
        assert (
            node.pop("notes")
            == (
                old.get("notes", "")
                + " "
                + f"Source batch input: {amount} g; {quote} The recipe starts with 1000 ml distilled water before supplementation. No prepared-base or final-medium mass concentration is asserted."
            ).strip()
        )
        entries = node.pop("evidence")
        scoped(entries[-1], ["solutions", 0, "composition", index], quote)
        prior = old.get("evidence", [])
        assert len(entries) == len(prior) + 1
        for old_entry, entry in zip(prior, entries[:-1], strict=True):
            assert {k: v for k, v in entry.items() if k != "explanation"} == {
                k: v for k, v in old_entry.items() if k != "explanation"
            }
            assert entry["explanation"].startswith(
                "Historical provider-declared nominal rate only; this entry no longer supports a final-medium concentration."
            )
            assert f"solutions[0].composition[{index}].notes" in entry["explanation"]
            assert "The former final-medium concentration is withdrawn." in entry["explanation"]
            assert quote in entry["explanation"] and item["source_sha256"] in entry["explanation"]
            result["evidence_scopes_corrected"] += 1
        expected = {k: v for k, v in old.items() if k not in {"concentration", "notes", "evidence"}}
        assert node == expected
    water = base["composition"][-1]
    water_quote = "Distilled water 1000.0 ml" if mid == "618" else "Distilled water 1000.000 ml"
    assert len(water["evidence"]) == 1
    scoped(water.pop("evidence")[0], ["solutions", 0, "composition", len(amounts)], water_quote)
    assert water == {
        "preferred_term": "Distilled water",
        "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
        "concentration": {"value": "1", "unit": "L"},
        "notes": "Starting-water batch amount: 1000 ml / 1000 ml per L = 1 L. Not a final-volume make-up instruction or a mass concentration.",
    }

    if mid == "618" or key == "m956":
        assert len(restored["ingredients"]) == 1
        node = restored["ingredients"][0]
        old = before["ingredients"][4 if mid == "618" else 6]
        percent = "1.0" if mid == "618" else "0.3"
        assert "concentration" not in node
        assert node.pop(
            "notes"
        ) == f"After sterilisation add sterile {old['preferred_term']} to the source-stated final concentration of {percent}%. The percentage basis, supplement dose volume, and final receiving volume are unspecified. No mass concentration, density, or percent unit is inferred." + (
            " This source-specific variant selects methylamine and excludes methanol."
            if key == "m956"
            else ""
        )
        assert len(node["evidence"]) == 1
        scoped(node.pop("evidence")[0], ["ingredients", 0], prep)
        assert node == {k: v for k, v in old.items() if k not in {"concentration", "notes"}}
        assert "variants" not in restored
    else:
        assert restored["ingredients"] == []
        variants = restored.pop("variants")
        assert len(variants) == 2
        for index, (label, percent, other) in enumerate(
            (("Methanol", "0.5", "methylamine"), ("Methylamine", "0.3", "methanol"))
        ):
            variant = variants[index]
            assert set(variant) == {
                "name",
                "relationship",
                "description",
                "modifications",
                "purpose",
                "evidence",
            }
            assert (
                variant["name"] == label + " alternative"
                and variant["relationship"] == "SUPPLEMENTED_VARIANT"
            )
            assert variant["modifications"] == [
                f"After sterilisation add sterile {label.lower()} to a final concentration of {percent}% (percentage basis unspecified).",
                f"Use this alternative instead of {other}; do not add both.",
            ]
            assert variant[
                "description"
            ] == "One of two mutually exclusive source-supported supplements to the common base; not an assertion that the unsupplemented base supports growth." + (
                " The separately accessioned methylamine branch is CultureMech:006899."
                if index
                else ""
            )
            assert (
                variant["purpose"]
                == "Select one supplementation branch of the original DSMZ 956 recipe."
            )
            assert len(variant["evidence"]) == 1
            scoped(variant["evidence"][0], ["variants", index], prep)
        assert (
            restored.pop("notes")
            == before["notes"]
            + " DSMZ 956 defines mutually exclusive methanol and methylamine alternatives. This record retains their common base and both options in variants; choose exactly one, not both. The unsupplemented base is not asserted to support growth. The methylamine-specific record is CultureMech:006899."
        )
        restored["notes"] = before["notes"]
        result["supplement_nodes_moved_to_variants"] += 2
        result["inline_variant_options_added"] += 2

    if key == "d956":
        children = restored["variant_children"]
        assert children[:-1] == before["variant_children"]
        child = children.pop()
        assert child == {
            "path": "data/normalized_yaml/bacterial/medium_for_dsm_14457_and_14458_replace_methanol_with_methylamine.yaml",
            "id": "CultureMech:006899",
            "name": "medium_for_dsm_14457_and_14458_replace_methanol_with_methylamine",
            "relationship": "SUPPLEMENTED_VARIANT",
            "notes": "Existing source-specific record for the methylamine option of this common base; final 0.3% has unspecified basis and methanol is excluded.",
        }
        result["variant_links_added"] += 1
    if key == "m956":
        assert restored.pop("parent_media") == {
            "path": "data/normalized_yaml/bacterial/medium_for_dsm_14457_and_14458.yaml",
            "id": "CultureMech:002134",
            "name": "medium_for_dsm_14457_and_14458",
            "relationship": "SUPPLEMENTED_VARIANT",
            "notes": "Selects the methylamine option of DSMZ 956's common base; excludes methanol. Percentage basis is unspecified. The parent describes both exclusive options, not a methanol-plus-methylamine mixture.",
        }
        assert restored.pop("variant_relationship") == "SUPPLEMENTED_VARIANT"
        assert restored.pop("variant_modifications") == [
            "Select the methylamine alternative (source final concentration 0.3%, basis unspecified); do not add methanol."
        ]
        removed = [c for c in item["claims"] if c["status"] == "remove_alternative"]
        assert len(removed) == 1 and removed[0]["old"] == before["ingredients"][5]
        assert (
            removed[0]["reference"] == mapping
            and removed[0]["snippet"]
            == "MEDIUM FOR DSM 14457 AND 14458_replace_Methanol_with_Methylamine"
        )
        result["excluded_alternative_nodes_removed"] += 1
        result["variant_links_added"] += 1
    if is_komodo:
        steps = restored.pop("preparation_steps")
        description = (
            prep
            if key != "m956"
            else "pH 7.2. After sterilising the base, add sterile methylamine to a final concentration of 0.3% (percentage basis unspecified). Do not add methanol in this variant."
        )
        assert steps == [{"step_number": 1, "action": "MIX", "description": description}]
        result["preparation_steps_added"] += 1
    restored["ingredients"] = copy.deepcopy(before["ingredients"])
    root = restored.pop("evidence")
    assert len(root) == (2 if is_komodo else 1)
    assert (
        root[0]["reference"] == reference
        and root[0]["supports"] == "SUPPORT"
        and root[0]["snippet"] == prep
    )
    root_claims = [
        c for c in item["claims"] if not c["evidence_pointer"] and c["reference"] == reference
    ]
    assert root[0]["explanation"] == " ".join(
        c["explanation"] for c in root_claims
    ) + " Fields: " + ", ".join(c["field"] for c in root_claims)
    if is_komodo:
        assert root[1]["reference"] == mapping and root[1]["supports"] == "SUPPORT"
        assert item["mapping_sha256"] in root[1]["explanation"]
        accession = "956_replace_Methanol_with_Methylamine" if key == "m956" else mid
        title = (
            "TWEEN 80A medium"
            if mid == "618"
            else "MEDIUM FOR DSM 14457 AND 14458"
            + ("_replace_Methanol_with_Methylamine" if key == "m956" else "")
        )
        assert root[1]["snippet"] == " ".join(
            [
                accession,
                title,
                "7.2",
                "true" if mid == "618" else "false",
                "false",
                "false",
                reference.replace("https:", "http:"),
            ]
        )
    refs = restored["references"]
    new_refs = refs[len(before.get("references", [])) :]
    assert [r["reference"] for r in new_refs] == (
        [reference, mapping] if is_komodo else [reference]
    )
    assert all(set(r) == {"reference", "title", "notes"} for r in new_refs)
    assert (
        item["pdf_sha256"] in new_refs[0]["notes"]
        and "source_type=culture_collection_page" in new_refs[0]["notes"]
    )
    assert "publication year not supplied" in new_refs[0]["notes"]
    if is_komodo:
        assert item["mapping_sha256"] in new_refs[1]["notes"]
    del refs[len(before.get("references", [])) :]
    if "references" not in before:
        restored.pop("references")
    assert restored == before, "Unreviewed field changed"
    result.update(
        {
            "stock_nodes_relocated": len(amounts),
            "unsupported_quantity_slots_removed": len(before["ingredients"]),
            "new_quantity_slots": 1,
            "base_preparations_added": 1,
        }
    )
    new_counts, old_counts = provenance(after), provenance(before)
    result.update({k: new_counts[k] - old_counts[k] for k in new_counts.keys() | old_counts.keys()})
    return result
