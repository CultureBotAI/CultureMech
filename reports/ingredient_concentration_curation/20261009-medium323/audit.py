"""Independently audit the four source-specific medium323 ingredient repairs."""

import copy
import json
from collections import Counter
from datetime import datetime
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from bs4 import BeautifulSoup

from culturemech.ingredients.mim_label_index import get_default_mim_label_index, resolve_ingredient
from culturemech.validation.recipe_references import literal_match, parse_recipe, recipe_source

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "reports/ingredient_concentration_curation"
DRAFT = BASE / "20261009-medium323-draft-v2/draft.json"
DRAFT_SHA = "52e20d8cf8f3b53b263bed58800e2dc194a9cca90510833c8736f4e02094d208"
CAPTURE = BASE / "20261009-synthrophomonas-family/next-323-captures-approved.json"
CAPTURE_SHA = "8c802303cf38982bebc07777a71a7d2dab5d4c01d44c0cc1d1c8136d866a39a4"
MIM_SHA = "a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262"
ACTION = "RESTORED_MEDIUM323_SOURCE_SPECIFIC_INGREDIENTS"
KEYS = {"K323", "D323", "S599", "S6552"}
LINK_QUOTE = "Instructions: http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium323.pdf"
LINK_REASON = (
    "Candidate cross-source relationship only: KOMODO323 links to DSMZ323 instructions, "
    "but its own compound table has NaHCO3 rather than Na2CO3, different rates and "
    "unquantified fatty-acid inputs. Neither exact duplication nor a historical direction "
    "of derivation is established. DSMZ is the catalog reference, not authority to overwrite "
    "the distinct KOMODO formulation; do not merge these records as identical."
)
MODIFICATIONS = [
    "KOMODO reports NaHCO3 at 5.67 g/L; DSMZ323 reports Na2CO3 at 2.49501 g/L.",
    "KOMODO gives different direct ingredient rates and null fatty-acid input amounts.",
    "KOMODO has no agar row; its required legacy physical_state remains unverified.",
]
CYSTEINE_ROW = "Cysteine-HCl x H2O Cysteine-HCl SEED-cpd00084#cpd00099## 1.13 0.01"
CYSTEINE_SEED_ROW = "cpd00084 L-Cysteine 0.006514835812130637"
CYSTEINE_REASON = (
    "Use the compound-table amount of 1.13 g/L for Cysteine-HCl x H2O. Its row "
    "explicitly includes SEED-cpd00084, which this same source names L-Cysteine "
    "in the SEED metabolite table. Retain the existing L-cysteine hydrochloride "
    "hydrate links on that source-specific identity evidence. The aggregate SEED "
    "molar concentration is quoted only to identify the row; it is not converted "
    "into a supplied-salt amount or substituted for the compound-table rate."
)
OLD_IDENTITY_SENTENCE = (
    "The record now uses the exact source chemical name. For cysteine, unsupported "
    "local L-specific links are withdrawn; the MIM exact answer still supplies "
    "L-specific identity, so publication stereochemistry remains unresolved."
)


def pinned(path, digest):
    raw = path.read_bytes()
    assert runner.sha(raw) == digest, f"Reviewed input drift: {path}"
    return json.loads(raw)


def reviewed():
    records = pinned(DRAFT, DRAFT_SHA)["records"]
    assert len(records) == 4 and {r["key"] for r in records} == KEYS
    return {r["key"]: r for r in records}


def sources():
    captures = pinned(CAPTURE, CAPTURE_SHA)["sources"]
    parsed = {}
    for key, source in captures.items():
        raw, meta = source["raw"], source["metadata"]
        assert runner.sha(raw.encode()) == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        datetime.fromisoformat(meta["accessed_at"])
        if meta.get("pdf_path"):
            assert runner.sha((ROOT / meta["pdf_path"]).read_bytes()) == meta["pdf_sha256"]
        parsed[key] = parse_recipe(recipe_source(meta["url"]), raw, meta)
    return captures, parsed


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for key, child in node.items():
            if key != "curation_history":
                yield from walk(child, (*path, key))
    elif isinstance(node, list):
        for i, child in enumerate(node):
            yield from walk(child, (*path, i))


def provenance(doc):
    counts = Counter()
    for _, node in walk(doc):
        for key in ("evidence", "references", "curation_history"):
            counts["new_" + key] += len(node.get(key, []))
    return counts


def relationship_evidence():
    captures, parsed = sources()
    assert literal_match(LINK_QUOTE, parsed["K323"].content)
    meta = captures["K323"]["metadata"]
    return {
        "reference": meta["url"],
        "supports": "SUPPORT",
        "snippet": LINK_QUOTE,
        "explanation": (
            LINK_REASON
            + f" Locator=medium features, Instructions; accessed={meta['accessed_at']}; "
            f"source SHA256={meta['sha256']}. Supports the candidate link, not equivalence."
        ),
    }


def relationship(target):
    spec = reviewed()[target]
    return {
        "id": spec["id"],
        "name": "treponema_saccharophilum_medium",
        "path": spec["path"],
        "relationship": "UNCERTAIN",
        "notes": LINK_REASON,
        "evidence": [relationship_evidence()],
    }


def limitations(key):
    values = reviewed()[key]["unresolved"]
    return values[:1] if key == "K323" else values


def cysteine_evidence():
    captures, parsed = sources()
    meta = captures["K323"]["metadata"]
    assert literal_match(CYSTEINE_ROW, parsed["K323"].content)
    # The concentration parser intentionally excludes aggregate SEED tables.
    # Inspect this separate table only for identity, never for supplied amounts.
    tables = BeautifulSoup(captures["K323"]["raw"], "html.parser").find_all("table")
    seed_rows = []
    for table in tables:
        rows = [
            [c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"], recursive=False)]
            for tr in table.find_all("tr")
        ]
        if rows and rows[0] == ["Seed ID", "Name", "Mol Concentration"]:
            seed_rows.extend(rows[1:])
    matching = [row for row in seed_rows if row[0] == "cpd00084"]
    assert matching == [["cpd00084", "L-Cysteine", "0.006514835812130637"]]
    assert " ".join(matching[0]) == CYSTEINE_SEED_ROW
    return {
        "reference": meta["url"],
        "supports": "SUPPORT",
        "snippet": CYSTEINE_ROW,
        "explanation": (
            "ingredients[9].concentration; ingredients[9].term; "
            "ingredients[9].mediaingredientmech_chebi_term: "
            + CYSTEINE_REASON
            + " Additional exact excerpt at the compound-table heading: "
            "Gram & Mol amounts are per Liter of medium. Trace metabolites & gases usually do not have amounts"
            + "\nAdditional exact excerpt at SEED metabolites list, cpd00084:\n"
            + CYSTEINE_SEED_ROW
            + f"\nLocator=compound and SEED metabolite tables; accessed={meta['accessed_at']}; "
            + f"source SHA256={meta['sha256']}."
        ),
    }


def finish_identity_review(before, proposed):
    """The complete source supports retaining the old L-specific cysteine links."""
    node = proposed["ingredients"][9]
    node["term"] = copy.deepcopy(before["ingredients"][9]["term"])
    node["mediaingredientmech_chebi_term"] = copy.deepcopy(
        before["ingredients"][9]["mediaingredientmech_chebi_term"]
    )
    assert node["term"]["id"] == node["mediaingredientmech_chebi_term"]["id"] == "CHEBI:91248"
    node["notes"] = CYSTEINE_REASON
    node["evidence"] = [cysteine_evidence()]
    resazurin = proposed["ingredients"][8]
    replacement = "The record now uses the exact source chemical name Resazurin; no sodium salt is asserted for this KOMODO input."
    for field in ("notes",):
        assert OLD_IDENTITY_SENTENCE in resazurin[field]
        resazurin[field] = resazurin[field].replace(OLD_IDENTITY_SENTENCE, replacement)
    for entry in resazurin["evidence"]:
        assert OLD_IDENTITY_SENTENCE in entry["explanation"]
        entry["explanation"] = entry["explanation"].replace(OLD_IDENTITY_SENTENCE, replacement)
    prefix = before["notes"].split("Commercial Product:", 1)[0].rstrip()
    proposed["notes"] = (
        prefix
        + "\n\nSource-specific KOMODO amounts are not copied from DSMZ323. "
        + CYSTEINE_REASON
        + " Unresolved: "
        + "; ".join(limitations("K323"))
        + "."
    )


def operations(before, after):
    """Complete semantic delta, excluding appended history to avoid self-reference."""
    result = []

    def visit(old, new, path):
        if old == new:
            return
        if isinstance(old, dict) and isinstance(new, dict):
            for key in sorted(set(old) | set(new)):
                if key == "curation_history":
                    continue
                if key not in old or key not in new:
                    result.append({"path": path + [key], "old": old.get(key), "new": new.get(key)})
                else:
                    visit(old[key], new[key], path + [key])
        elif isinstance(old, list) and isinstance(new, list):
            for i in range(max(len(old), len(new))):
                if i >= len(old) or i >= len(new):
                    result.append(
                        {
                            "path": path + [i],
                            "old": old[i] if i < len(old) else None,
                            "new": new[i] if i < len(new) else None,
                        }
                    )
                else:
                    visit(old[i], new[i], path + [i])
        else:
            result.append({"path": path, "old": old, "new": new})

    visit(before, after, [])
    return result


def event_changes(before, after):
    # Values stay in the pinned plan; history names every changed path and digest.
    changes = operations(before, after)
    return {
        "field_changes": [
            {"field": runner.field_name(c["path"]), "old": c["old"], "new": c["new"]}
            for c in changes
            if "evidence" not in c["path"] and "references" not in c["path"]
        ],
        "evidence_and_bibliography_changes": [
            runner.field_name(c["path"])
            for c in changes
            if "evidence" in c["path"] or "references" in c["path"]
        ],
        "full_semantic_delta_sha256": runner.sha(json.dumps(changes, sort_keys=True).encode()),
        "source_capture_sha256": CAPTURE_SHA,
        "old_evidence_preserved": True,
    }


def history_notes(key):
    return (
        "Source-specific ingredient quantities, stock stages, identities and preparation "
        "were reviewed against pinned official captures. Each changed formulation claim "
        "has a persistent source URL and exact evidence snippet. Earlier evidence, IDs "
        "and history are preserved. The source-linked medium relationship is uncertain, "
        "not an exact duplicate or proven direction of derivation. Remaining limitations: "
        + "; ".join(limitations(key))
    )


def stored(node, value, unit):
    amount = node["concentration"]
    assert set(amount) == {"value", "unit"} and amount["unit"] == unit
    assert Decimal(amount["value"]) == Decimal(str(value))


def source_projection(key, after, captures, parsed):
    if key == "K323":
        tables = BeautifulSoup(captures[key]["raw"], "html.parser").find_all("table")
        matches = []
        for table in tables:
            rows = [
                [c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"], recursive=False)]
                for tr in table.find_all("tr")
            ]
            if rows and rows[0] == [
                "Name",
                "Semi unique name",
                "Unique Name",
                "Gram Amount",
                "Mol Amount",
            ]:
                matches.append(rows[1:])
        (rows,) = matches
        expected = {r[0]: r for r in rows}
        aliases = {
            "Yeast extract": "Yeast extract (Oxoid)",
            "Trypticase peptone": "Trypticase (BBL)",
            "D-Glucose": "Glucose",
        }
        actual = {
            aliases.get(n["preferred_term"], n["preferred_term"]): n for n in after["ingredients"]
        }
        assert set(actual) == set(expected) and len(after["ingredients"]) == 21
        for name, node in actual.items():
            row = expected[name]
            (entry,) = [
                e for e in node["evidence"] if e["reference"] == captures[key]["metadata"]["url"]
            ]
            assert " ".join(row) in entry["snippet"] + "\n" + entry["explanation"]
            if row[3] == "null":
                assert node.get("concentration") == (
                    {"value": "variable", "unit": "VARIABLE"} if name == "KOH" else None
                )
            else:
                stored(node, row[3], "G_PER_L")
        cysteine = actual["Cysteine-HCl x H2O"]
        assert cysteine["evidence"] == [cysteine_evidence()]
        assert (
            cysteine["term"]["id"]
            == cysteine["mediaingredientmech_chebi_term"]["id"]
            == "CHEBI:91248"
        )
    else:
        raw = json.loads(captures[key]["raw"])["data"]
        groups = (
            [(after["composition"], raw)]
            if key.startswith("S")
            else [
                (after["ingredients"], raw["solutions"][0]),
                (after["solutions"][0]["composition"], raw["solutions"][1]),
            ]
        )
        for nodes, group in groups:
            rows = [r for r in group["recipe"] if r.get("compound_id") is not None]
            assert len(nodes) == len(rows)
            for node, row in zip(nodes, rows, strict=True):
                assert node["preferred_term"] == row["compound"]
                (entry,) = [
                    e
                    for e in node["evidence"]
                    if e["reference"] == captures[key]["metadata"]["url"]
                ]
                assert json.loads(entry["snippet"]) == row
                if key.startswith("S"):
                    assert node["term"]["id"] == f"mediadive.compound:{row['compound_id']}"
                if row.get("g_l") is not None:
                    stored(node, row["g_l"], "G_PER_L")
                elif row["compound"] == "Distilled water":
                    assert row["amount"] == 1000 and row["unit"] == "ml"
                    assert group["volume"] == 1002
                    stored(node, "998.003992015968", "ML_PER_L")
                else:
                    assert row["unit"] == "ml"
                    stored(node, Decimal(str(row["amount"])) / 1000, "L")
        if key in {"S599", "D323"}:
            (descriptor,) = after["solutions"]
            stored(descriptor, "0.0014", "L")
            assert descriptor["culturemech_term"] == {
                "id": reviewed()["S6552"]["id"],
                "label": "Fatty acid mixture",
            }
        if key == "S599":
            stored(after["composition"][8], "0.000499002", "G_PER_L")
            calculated = Decimal("0.0005") / Decimal("1.002")
            reported = Decimal(after["composition"][8]["concentration"]["value"])
            assert calculated.quantize(reported) == reported
    by_url = {s["metadata"]["url"]: parsed[k].content for k, s in captures.items()}
    for _, node in walk(after):
        for evidence in node.get("evidence", []):
            assert evidence["supports"] == "SUPPORT"
            assert literal_match(evidence["snippet"], by_url[evidence["reference"]])


def invert_nodes(before, after, key):
    """Invert fixed node lineage; only reviewed concentration/provenance fields vary."""
    if key.startswith("S"):
        lineage = [(i, ["composition", i]) for i in range(len(before["composition"]))]
        old_nodes = before["composition"]
    elif key == "K323":
        indices = [*range(10), 11, 13, 14, 18, 19, 20]
        lineage = [(old, ["ingredients", new]) for new, old in enumerate(indices)]
        old_nodes = before["ingredients"]
    else:
        lineage = [(i, ["ingredients", i]) for i in range(13)]
        lineage += [
            (old, ["solutions", 0, "composition", new])
            for old, new in ((13, 0), (14, 1), (18, 3), (19, 4))
        ]
        old_nodes = before["ingredients"]
    counts = Counter()
    restored_nodes = copy.deepcopy(old_nodes)
    for old_index, pointer in lineage:
        old = old_nodes[old_index]
        new = runner.get_node(after, pointer)
        permitted = {"concentration", "evidence", "notes"}
        if key == "K323" and old_index in {8, 9}:
            permitted.add("preferred_term")
        if key == "K323" and old_index == 9:
            permitted.update({"term", "mediaingredientmech_chebi_term"})
        if key == "D323" and old_index == 8:
            permitted.add("term")
        if key == "S599" and old_index == 8:
            permitted.add("chebi_term")
        restored = copy.deepcopy(new)
        assert new.get("notes", "").startswith(old.get("notes", ""))
        assert all(e in new.get("evidence", []) for e in old.get("evidence", []))
        for field in permitted:
            if field in old:
                restored[field] = copy.deepcopy(old[field])
            else:
                restored.pop(field, None)
        assert restored == old, "Unrelated ingredient annotation changed"
        restored_nodes[old_index] = restored
        a, b = old.get("concentration"), new.get("concentration")
        if a != b:
            counts[
                "unsupported_quantity_slots_removed" if b is None else "quantity_corrections"
            ] += 1
        counts["stock_nodes_relocated"] += pointer[0] == "solutions"
    assert restored_nodes == old_nodes
    if key.startswith("S"):
        counts["unsupported_quantity_slots_removed"] += 1
        counts["unsupported_flags_removed"] += 1
    elif key == "K323":
        counts["unsupported_quantity_slots_removed"] += 5
        counts["new_quantity_slots"] += 1
        counts["unquantified_carrier_nodes_added"] += 3
        counts["unquantified_ingredient_nodes_added"] += 1
        counts["ingredient_labels_corrected"] += 2
    else:
        counts["unsupported_quantity_slots_removed"] += 3
        counts["new_quantity_slots"] += 3
        counts["preparation_actions_corrected"] += 1
        counts["unsupported_primary_identities_removed"] += 1
        counts["stock_stage_concentrations_rebased"] += 4
    if key in {"S599", "D323"}:
        counts["stock_descriptors_added"] += 1
    if key == "S599":
        counts["new_quantity_slots"] += 1
        counts["unsupported_secondary_identities_removed"] += 1
        counts["bibliographic_entries_enriched"] += 1
    return counts


def check(before, after, item):
    spec = reviewed()[item["key"]]
    assert item["action"] == ACTION
    assert item["path"] == spec["path"] and item["id"] == spec["id"]
    assert item["target_class"] == spec["target_class"]
    assert item["claims"] == spec["old_quantity_claims"]
    assert before == runner.load_yaml(spec["before_text"]) == runner.load_yaml(item["before_text"])
    assert (
        runner.sha(item["before_text"].encode()) == item["before_sha256"] == spec["before_sha256"]
    )
    assert after == runner.load_yaml(item["after_text"])
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before["id"] == after["id"] == spec["id"]
    captures, parsed = sources()
    source_projection(item["key"], after, captures, parsed)
    expected = runner.load_yaml(spec["proposed_text"])
    expected["curation_history"] = copy.deepcopy(before["curation_history"])
    for _, node in walk(expected):
        for field in ("notes", "explanation"):
            if isinstance(node.get(field), str):
                node[field] = (
                    node[field]
                    .replace("The draft now", "The record now")
                    .replace("this pinned draft", "the pinned review")
                )
    key = item["key"]
    assert get_default_mim_label_index().metadata["sha256"] == MIM_SHA
    if key in {"K323", "D323", "S599"}:
        pointer = (
            ["ingredients", 9]
            if key == "K323"
            else ["composition" if key == "S599" else "ingredients", 8]
        )
        decision = resolve_ingredient(runner.get_node(after, pointer))
        assert decision.identifier == ("CHEBI:91248" if key == "K323" else "CHEBI:8806")
        assert decision.resolution_source == "mim_exact"
    if key == "K323":
        finish_identity_review(before, expected)
        expected["parent_media"] = relationship("D323")
        expected["variant_relationship"] = "UNCERTAIN"
        expected["variant_modifications"] = MODIFICATIONS
    if key == "D323":
        expected["variant_children"] = [relationship("K323")]
        expected["references"].append(
            copy.deepcopy(runner.load_yaml(reviewed()["K323"]["proposed_text"])["references"][0])
        )
    restored = copy.deepcopy(after)
    event = restored["curation_history"].pop()
    assert restored == expected, "Unreviewed full-record difference"
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert event["source"] == captures[key]["metadata"]["url"]
    assert datetime.fromisoformat(event["timestamp"]).tzinfo is not None
    assert "Draft only" not in event["notes"]
    assert event["notes"] == item["history_notes"] == history_notes(key)
    assert json.loads(event["changes"]) == event_changes(before, restored)
    assert item["field_changes"] == operations(before, restored)
    assert item["unresolved"] == limitations(key)
    assert item["publication_identity_resolved"] is False
    counts = invert_nodes(before, after, key)
    for field in (
        "ingredients",
        "composition",
        "solutions",
        "notes",
        "preparation_steps",
        "evidence",
        "references",
        "data_quality_flags",
        "parent_media",
        "variant_relationship",
        "variant_modifications",
        "variant_children",
    ):
        if field in before:
            restored[field] = copy.deepcopy(before[field])
        else:
            restored.pop(field, None)
    assert restored == before, "Unrelated root metadata or earlier history changed"
    old_counts, new_counts = provenance(before), provenance(after)
    for name in ("new_evidence", "new_references", "new_curation_history"):
        assert new_counts[name] >= old_counts[name]
        counts[name] = new_counts[name] - old_counts[name]
    counts["variant_links_added"] += key in {"K323", "D323"}
    return dict(counts)
