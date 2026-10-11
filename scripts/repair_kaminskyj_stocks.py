"""Preview and apply the primary-source Kaminskyj stock-boundary correction."""

import argparse
import collections
import copy
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-kaminskyj-stocks"
PLAN = HERE / "plan.json"
PATH = "data/normalized_yaml/bacterial/kaminskyj_minimal_medium.yaml"
BEFORE_SHA = "2eb1d7896cc9c9d60d73d1bc64246966f1d377e15ee79ee8abf6684fefbb310e"
SOURCE_SHA = "e4930dbee08d6d2885bade2cdd65cca6a2abe518efd164d8ab923050712a57e3"
ACTION = "RESTORED_KAMINSKYJ_PRIMARY_RECIPE_STOCK_BOUNDARIES"
MM, NITRATE, TRACE = "Minimal Medium (MM)", "20 X Nitrate salts", "1000 X Trace elements"
# Old ingredient index, source table/row, new field path, supplied-form correction.
SPECS = [
    (2, MM, 0, ["ingredients", 0], None),
    (0, NITRATE, 0, ["solutions", 0, "composition", 0], None),
    (11, NITRATE, 1, ["solutions", 0, "composition", 1], None),
    (10, NITRATE, 2, ["solutions", 0, "composition", 2], "Magnesium sulfate heptahydrate"),
    (13, NITRATE, 3, ["solutions", 0, "composition", 3], None),
    (12, TRACE, 1, ["solutions", 1, "composition", 0], "Zinc sulfate heptahydrate"),
    (8, TRACE, 2, ["solutions", 1, "composition", 1], None),
    (7, TRACE, 3, ["solutions", 1, "composition", 2], "Manganese chloride tetrahydrate"),
    (4, TRACE, 4, ["solutions", 1, "composition", 3], "Ferrous sulfate heptahydrate"),
    (3, TRACE, 5, ["solutions", 1, "composition", 4], "Cobalt chloride hexahydrate"),
    (6, TRACE, 6, ["solutions", 1, "composition", 5], "Cupric sulfate pentahydrate"),
    (5, TRACE, 7, ["solutions", 1, "composition", 6], "Sodium molybdate dihydrate"),
    (1, TRACE, 8, ["solutions", 1, "composition", 7], "Tetrasodium EDTA"),
    (9, MM, 3, ["solutions", 2, "composition", 0], None),
]
THIAMINE_NOTE = (
    "Source specifies a '1%' thiamine solution but does not define the percentage basis "
    "or supplied chemical form. Its 1 mL/L addition is known; stock mass/molar strength "
    "and final thiamine molarity remain unresolved. The former 0.03769 mM assertion is "
    "withdrawn. Existing identity links are retained, not certified as the supplied form."
)
LIMITS = [
    "Thiamine percentage basis and supplied form are unspecified; no fixed mass/molar strength.",
    "NaOH and KOH titration amounts are not quantified; water makeup is not a fixed input dose.",
    "Tetrasodium EDTA has no exact packaged MIM resolution; no hydrate or ontology ID inferred.",
    "Optional auxotroph supplements are strain-dependent and are not added to the base recipe.",
    "Existing bacterial filing, high_metal flag and generic applications are retained but not "
    "validated by this ingredient correction; the protocol concerns Aspergillus nidulans.",
    "No new taxa-media associations. No source-version merge with Hill's different formulation.",
]


def source():
    raw = (HERE / "source-review.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source review drift"
    s = json.loads(raw)
    assert s["tables"][MM][1:] == [
        ["20X nitrate salts (see below)", "50 ml"],
        ["Trace elements (see below)", "1 ml"],
        ["1% thiamine", "1 ml"],
    ]
    assert "Make to 1 liter with distilled water." in s["contexts"]["medium"]
    assert "Add distilled water to 1 liter." in s["contexts"]["nitrate"]
    assert "Adjust volume to 100 ml with distilled water." in s["contexts"]["trace"]
    return s


def at(doc, pointer):
    for part in pointer:
        doc = doc[part]
    return doc


def proof(s, snippet, explanation):
    return {
        "reference": s["url"],
        "supports": "SUPPORT",
        "snippet": snippet,
        "explanation": explanation + f" Source: {s['doi']}; accessed {s['accessed_on']}.",
    }


def amount(s, table, row):
    mass = Decimal(s["tables"][table][row][1].split()[0])
    return format(mass / (Decimal("0.100") if table == TRACE else Decimal("1")), "f")


def ingredient_proof(s, spec):
    old, table, row, pointer, _ = spec
    quote = " ".join(s["tables"][table][row])
    location = json.dumps(pointer)
    if old == 9:
        explanation = f"{location}: MM thiamine-solution row. {THIAMINE_NOTE}"
    else:
        context = "medium" if table == MM else "nitrate" if table == NITRATE else "trace"
        volume_quote = {
            "medium": "Make to 1 liter with distilled water.",
            "nitrate": "Add distilled water to 1 liter.",
            "trace": "Adjust volume to 100 ml with distilled water.",
        }[context]
        mass = s["tables"][table][row][1].split()[0]
        volume = "0.100" if table == TRACE else "1"
        explanation = (
            f"{location}.concentration and supplied form, locator: {table}, row {row + 1}. "
            f"Separate volume excerpt after that table: '{volume_quote}' "
            f"Calculation: {mass} g / {volume} L = {amount(s, table, row)} g/L "
            f"of {'final medium' if table == MM else 'this stock, not final medium'}. "
            "No molecular-weight conversion. Hydrate alternatives are not combined."
        )
    return proof(s, quote, explanation)


def stock_shells(s):
    return [
        {
            "preferred_term": NITRATE,
            "source": s["url"],
            "concentration": {"value": "50", "unit": "ML_PER_L"},
            "composition": [],
            "preparation_notes": "Prepare the four salts to a final volume of 1 L with distilled "
            "water. Autoclave and store at 4 C. Add 50 mL of this stock per final litre of MM. "
            "The anhydrous magnesium sulfate option is recorded separately as a variant.",
        },
        {
            "preferred_term": TRACE,
            "source": s["url"],
            "concentration": {"value": "1", "unit": "ML_PER_L"},
            "composition": [],
            "preparation_notes": "Start with 60 mL distilled water. Add the eight listed salts "
            "in source order. Boil; cool to 60 C; adjust to pH 6.5 with KOH. Cool to room "
            "temperature, then make up to 100 mL with distilled water. Resuspend the "
            "precipitate before use. Add 1 mL of this stock per final litre of MM. "
            "Stock concentrations use the 100 mL final volume, not the 60 mL initial water.",
        },
        {
            "preferred_term": "Thiamine solution (1%)",
            "source": s["url"],
            "concentration": {"value": "1", "unit": "ML_PER_L"},
            "composition": [],
            "notes": THIAMINE_NOTE,
        },
        {
            "preferred_term": "Sodium hydroxide solution (1 M)",
            "source": s["url"],
            "composition": [],
            "notes": "Add as needed to adjust MM to pH 6.5. "
            "Stock strength is 1 M; addition volume and final-medium NaOH amount are unspecified.",
        },
    ]


def additions(s):
    water = {
        "preferred_term": "Distilled water",
        "term": s["grounding"]["Water"]["term"],
        "notes": "Make the complete medium up to 1 L. This is a final volume, not a "
        "fixed 1 L water addition; the water makeup amount is not quantified.",
        "evidence": [
            proof(
                s,
                "Make to 1 liter with distilled water.",
                "ingredients[1]: MM preparation paragraph; final-volume makeup.",
            )
        ],
    }
    koh = {
        "preferred_term": "Potassium hydroxide",
        "term": s["grounding"]["Potassium hydroxide"]["term"],
        "notes": "Adjust the trace stock to pH 6.5 after cooling to 60 C. "
        "KOH amount and reagent concentration are unspecified.",
        "evidence": [
            proof(
                s,
                "Adjust pH to 6.5 with KOH.",
                "solutions[1].composition[8]: trace-stock preparation; "
                "titration only, not a fixed KOH dose.",
            )
        ],
    }
    naoh = {
        "preferred_term": "Sodium hydroxide",
        "term": s["grounding"]["Sodium hydroxide"]["term"],
        "concentration": {"value": "1", "unit": "MOLAR"},
        "evidence": [
            proof(
                s,
                "Adjust pH to 6.5 with 1M NaOH.",
                "solutions[3].composition[0].concentration: 1 M titrant strength "
                "from MM preparation, not its final-medium concentration. "
                "No fixed stock addition volume is given.",
            )
        ],
    }
    return water, koh, naoh


def formulation_proof(s):
    return proof(
        s,
        "20X nitrate salts (see below) 50 ml",
        "solutions[0].concentration: 50 mL nitrate stock / 1 L final MM = 50 mL/L. "
        "Other exact MM table excerpts: 'Trace elements (see below) 1 ml' and "
        "'1% thiamine 1 ml', supporting solutions[1] and [2] at 1 mL/L each. "
        f"Separate MM preparation paragraph: '{s['contexts']['medium']}' This supports "
        "ph_value=6.5, solutions[3] as an unquantified 1 M NaOH titrant, water makeup "
        "and preparation_steps including autoclaving, not the former 0.22 um filtration. "
        "No autoclave temperature or duration is specified. Optional supplements and "
        "solid-medium agar are not unconditional base ingredients. "
        f"Nitrate preparation excerpt: '{s['contexts']['nitrate']}' "
        f"Trace preparation excerpt: '{s['contexts']['trace']}' "
        "The trace table's separate 'distilled water 60 ml' is initial water, not "
        "the final stock volume. These excerpts support solutions[0:2].preparation_notes. "
        "Withdraw imported stock/final-medium mixing; do not convert through inferred "
        "molecular weights or substitute the CM vitamin solution or Hill formulation.",
    )


def variants(s):
    return [
        {
            "name": "Anhydrous magnesium sulfate option",
            "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
            "modifications": [
                "In the 20X nitrate stock, replace 10.4 g magnesium sulfate "
                "heptahydrate per 1 L stock with 5.2 g anhydrous magnesium sulfate "
                "per 1 L stock. Keep the stock addition at 50 mL/L final medium."
            ],
            "evidence": [
                proof(
                    s,
                    " ".join(s["tables"][NITRATE][2]),
                    "variants[0]: nitrate-stock magnesium row, source-explicit "
                    "alternative, not an extra ingredient. Separate volume excerpt: "
                    "'Add distilled water to 1 liter.' Thus 5.2 g / 1 L = 5.2 g/L "
                    "anhydrous salt in stock; 5.2 * 0.050 = 0.26 g/L final medium.",
                )
            ],
        },
        {
            "name": "Solid minimal medium",
            "relationship": "PHYSICAL_STATE_VARIANT",
            "modifications": [
                "Add 18 g agar to the one-litre MM preparation for solid medium; "
                "retain the source's autoclaving step."
            ],
            "evidence": [
                proof(
                    s,
                    "For solid medium add 18 g agar.",
                    "variants[1]: MM preparation, not CM (which instead specifies 15 g). "
                    "Separate excerpt: 'Make to 1 liter with distilled water.' "
                    "Source states 18 g per one-litre preparation; no separate "
                    "post-agar final volume is invented. Base remains LIQUID.",
                )
            ],
        },
    ]


def references(s):
    return [
        {
            "reference": ref,
            "title": s["title"],
            "authors": s["authors"],
            "year": s["year"],
            "notes": f"source_type={kind}; discovery_mode={s['discovery_mode']}; "
            f"accessed_on={s['accessed_on']}; DOI={s['doi']}; "
            f"protocol_html_sha256={s['raw_html_sha256']}; publisher_metadata_url={s['publisher_url']}; "
            f"publisher_html_sha256={s['publisher_sha256']}. Recipe quotations were inspected "
            "in the FGSC protocol HTML; publisher metadata establishes title, author, year and DOI. "
            "PDF not inspected.",
        }
        for ref, kind in ((s["url"], "journal_protocol_web_page"), (s["doi"], "journal_article"))
    ]


def preparation():
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Combine 10 g D-glucose, "
            "50 mL 20X nitrate stock, 1 mL trace stock and 1 mL 1% thiamine solution for "
            "one litre of MM. Add nutritional supplements only if required by the strain.",
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust to pH 6.5 using "
            "1 M sodium hydroxide. The amount required is not specified.",
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": "Make up to a final volume " "of 1 L with distilled water.",
        },
        {
            "step_number": 4,
            "action": "AUTOCLAVE",
            "description": "Autoclave. The source "
            "does not specify temperature or duration for this step.",
        },
    ]


def transform(before, s, timestamp):
    after = copy.deepcopy(before)
    after["ingredients"] = []
    after["solutions"] = stock_shells(s)
    for spec in SPECS:
        old, table, row, pointer, label = spec
        node = copy.deepcopy(before["ingredients"][old])
        if old == 9:
            node.pop("concentration")
            node["notes"] += " " + THIAMINE_NOTE
        else:
            node["concentration"] = {"value": amount(s, table, row), "unit": "G_PER_L"}
        if label:
            node["preferred_term"] = label
            if label in s["grounding"]:
                node["term"] = copy.deepcopy(s["grounding"][label]["term"])
                if "mediaingredientmech_chebi_term" in node:
                    node["mediaingredientmech_chebi_term"] = copy.deepcopy(node["term"])
        node["evidence"] = node.get("evidence", []) + [ingredient_proof(s, spec)]
        at(after, pointer[:-1]).append(node)
    water, koh, naoh = additions(s)
    after["ingredients"].append(water)
    after["solutions"][1]["composition"].append(koh)
    after["solutions"][3]["composition"].append(naoh)
    after["ph_value"] = 6.5
    after["preparation_steps"] = preparation()
    after["evidence"] = [formulation_proof(s)]
    after["variants"] = variants(s)
    after["references"] = references(s)
    changes = [
        f"ingredients[{old}] -> {json.dumps(pointer)}: "
        f"{json.dumps(before['ingredients'][old].get('concentration'))} -> "
        f"{json.dumps(at(after, pointer).get('concentration'))}"
        for old, _, _, pointer, _ in SPECS
    ]
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=s["doi"],
        notes="Restored source stock boundaries, doses and seven hydrate forms. Na4EDTA "
        "is tetrasodium EDTA without an inferred hydrate or ID. Added water makeup and "
        "unquantified KOH/NaOH titration contexts (NaOH stock is 1 M). Source pH and "
        "autoclaving replace generic filtration. Preserved optional agar and anhydrous "
        "magnesium sulfate as variants. Every ingredient, dose and preparation change "
        "has primary-protocol evidence. " + " ".join(LIMITS),
        changes="; ".join(changes),
    )
    return after


def claims(before, after):
    rows = []
    for old, _, _, pointer, _ in SPECS:
        node = at(after, pointer)
        rows.append(
            {
                "pointer": pointer,
                "old_pointer": ["ingredients", old],
                "ingredient": node["preferred_term"],
                "old": before["ingredients"][old]["concentration"],
                "proposed": node.get("concentration"),
                "status": "correct",
                "evidence": node["evidence"][-1],
            }
        )
    for pointer in (
        ["ingredients", 1],
        ["solutions", 1, "composition", 8],
        ["solutions", 3, "composition", 0],
    ):
        node = at(after, pointer)
        rows.append(
            {
                "pointer": pointer,
                "ingredient": node["preferred_term"],
                "old": None,
                "proposed": node.get("concentration"),
                "status": "add" if "concentration" in node else "not_quantified",
                "evidence": node["evidence"][0],
            }
        )
    for i, stock in enumerate(after["solutions"]):
        rows.append(
            {
                "pointer": ["solutions", i, "concentration"],
                "ingredient": stock["preferred_term"],
                "old": None,
                "proposed": stock.get("concentration"),
                "status": "add" if i < 3 else "not_quantified",
                "evidence": after["evidence"][0],
            }
        )
    for i, variant in enumerate(after["variants"]):
        rows.append(
            {
                "pointer": ["variants", i],
                "ingredient": variant["name"],
                "old": None,
                "proposed": variant["modifications"],
                "status": "add",
                "evidence": variant["evidence"][0],
            }
        )
    return rows


def check(before, after, item):
    """Invert the whitelisted edits; independently check stage arithmetic and membership."""
    s = source()
    assert item["action"] == ACTION and item["path"] == PATH
    assert item["target_class"] == "MediaRecipe"
    assert item["id"] == before["id"] == after["id"] == "CultureMech:007206"
    assert runner.sha(item["before_text"].encode()) == item["before_sha256"] == BEFORE_SHA
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert before["media_term"]["term"]["id"] == "MEDIADB:308"
    assert len(before["ingredients"]) == 14 and len(after["ingredients"]) == 2
    assert len(after["solutions"]) == 4
    assert [len(n["composition"]) for n in after["solutions"]] == [4, 9, 1, 1]
    assert sorted(spec[0] for spec in SPECS) == list(range(14))
    for spec in SPECS:
        old, table, row, pointer, label = spec
        node = copy.deepcopy(at(after, pointer))
        prior = before["ingredients"][old]
        assert node.pop("evidence") == prior.get("evidence", []) + [ingredient_proof(s, spec)]
        if old == 9:
            assert "concentration" not in node
            assert node["notes"] == prior["notes"] + " " + THIAMINE_NOTE
            node["notes"] = prior["notes"]
        else:
            quantity = node.pop("concentration")
            assert set(quantity) == {"value", "unit"} and quantity["unit"] == "G_PER_L"
            mass = Decimal(s["tables"][table][row][1].split()[0])
            denominator = Decimal("0.1") if table == TRACE else Decimal("1")
            assert Decimal(quantity["value"]) * denominator == mass
        node["concentration"] = prior["concentration"]
        if label:
            assert node["preferred_term"] == label
            node["preferred_term"] = prior["preferred_term"]
            if label in s["grounding"]:
                assert node["term"] == s["grounding"][label]["term"]
                node["term"] = prior["term"]
                if "mediaingredientmech_chebi_term" in prior:
                    assert node["mediaingredientmech_chebi_term"] == s["grounding"][label]["term"]
                    node["mediaingredientmech_chebi_term"] = prior["mediaingredientmech_chebi_term"]
        if "evidence" in prior:
            node["evidence"] = prior["evidence"]
        assert node == prior, (pointer, "Unreviewed ingredient change")
    water, koh, naoh = additions(s)
    assert after["ingredients"][1] == water
    assert after["solutions"][1]["composition"][8] == koh
    assert after["solutions"][3]["composition"][0] == naoh
    shells = copy.deepcopy(after["solutions"])
    for stock in shells:
        stock["composition"] = []
    assert shells == stock_shells(s)
    assert after["ph_value"] == 6.5 and after["preparation_steps"] == preparation()
    assert after["evidence"] == [formulation_proof(s)]
    assert after["variants"] == variants(s) and after["references"] == references(s)
    assert item["claims"] == claims(before, after)
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event == transform(before, s, event["timestamp"])["curation_history"][-1]
    restored = copy.deepcopy(after)
    for key in (
        "ingredients",
        "solutions",
        "ph_value",
        "preparation_steps",
        "evidence",
        "variants",
        "references",
        "curation_history",
    ):
        restored.pop(key)
        if key in before:
            restored[key] = before[key]
    assert restored == before, "Unreviewed root change"
    return collections.Counter(
        new_evidence=20,
        new_references=2,
        new_curation_history=1,
        stock_nodes_relocated=13,
        quantity_corrections=13,
        unsupported_quantity_slots_removed=1,
        new_quantity_slots=4,
        stock_descriptors_added=4,
        inline_variant_options_added=2,
        supplied_hydrate_identities_corrected=7,
        ingredient_labels_corrected=8,
        water_input_nodes_added=1,
        unquantified_ingredient_nodes_added=1,
        preparation_records_restored=1,
    )


def safe_path(root):
    parts = Path(PATH).parts
    assert not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))
    target = root / PATH
    assert target.resolve().is_relative_to(root / "data/normalized_yaml")
    return target


def preview(root=ROOT):
    raw = safe_path(root).read_bytes()
    assert runner.sha(raw) == BEFORE_SHA, "Record drift; new review required"
    before = runner.load_yaml(raw)
    assert not validate_recipe(before, target_class="MediaRecipe")
    s = source()
    timestamp = now_iso()
    after = transform(before, s, timestamp)
    assert not validate_recipe(after, target_class="MediaRecipe")
    output = runner.render(raw.decode(), after)
    item = {
        "path": PATH,
        "id": before["id"],
        "target_class": "MediaRecipe",
        "action": ACTION,
        "before_sha256": BEFORE_SHA,
        "after_sha256": runner.sha(output),
        "before_text": raw.decode(),
        "after_text": output.decode(),
        "claims": claims(before, after),
        "unresolved": LIMITS,
    }
    item["counts"] = dict(check(before, after, item))
    plan = {
        "version": 1,
        "action": ACTION,
        "source_sha256": SOURCE_SHA,
        "created_at": timestamp,
        "records": [item],
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
    }
    runner.safe_targets(root, plan)
    return plan


def apply(plan, root=ROOT, *, verify=False):
    root = root.resolve()
    assert plan["action"] == ACTION and plan["source_sha256"] == SOURCE_SHA
    assert len(plan["records"]) == 1
    runner.safe_targets(root, plan)
    item = plan["records"][0]
    before, after = (runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    assert check(before, after, item) == item["counts"]
    assert not validate_recipe(after, target_class="MediaRecipe")
    target = safe_path(root)
    raw = target.read_bytes()
    if runner.sha(raw) == item["after_sha256"]:
        return {"changed": 0, "already_applied": 1}
    assert not verify and runner.sha(raw) == BEFORE_SHA, "Concurrent edit or not yet applied"
    assert safe_path(root).read_bytes() == raw, "Concurrent edit during preflight"
    target.write_bytes(item["after_text"].encode())
    assert target.read_bytes() == item["after_text"].encode(), "Readback mismatch"
    return {"changed": 1, "already_applied": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=PLAN)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.apply or args.verify:
        print(json.dumps(apply(json.loads(args.plan.read_text()), verify=args.verify)))
    else:
        assert not args.plan.exists(), "Refuse to overwrite preview"
        result = preview()
        with args.plan.open("x") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
        print(json.dumps({"records_edited": 0, "proposed": result["records"][0]["counts"]}))


if __name__ == "__main__":
    main()
