#!/usr/bin/env python3
"""Retain the unexecuted first version of the record08 draft author.

Provenance date: 2026-11-15.
Context: CultureMech #750 (DSM383/383a findings) and #752 (retain helper history).
This v1 was written and statically reviewed but never executed by its author;
record08's actual author execution used batch079_build_record08_review_v2.py.

Required inputs if independently authorized for replay: --issue with an existing
CultureMech issue URL, explicit checkout-root working directory, local Python
with PyYAML, and the exact EXPECTED/CAPTURES evidence under
.temp/batch079-scientific-20261114/record08. These include the target/two owners,
DSM383/383a PDF/JSON captures and receipts, original native logs/inspection,
chemical assessment/raw OLS pins, peer report, schema, MIM index and runner v2.
Outputs if run: exclusive claim-inventory.json, author-plan.json,
inspection-binding.json, review.yaml and author-direct-audit.json in record08,
plus one native inspect invocation through runner v2 and its retained streams.

Replay limits: this is historical source, not a recommended current entry point.
It embeds frozen scientific decisions and exact old hashes, requires absent
outputs and must not overwrite existing evidence. Native inspection is not a
validator or save; the script does neither. A fresh checkout without ignored
captures cannot reproduce the run. Earlier bundle-only publication prose is a
historical draft plan superseded by #752 and the provenance README.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RUN = Path(".temp/batch079-scientific-20261114")
D = RUN / "record08"
CHEM = D / "chemical-identity-tsb-20261115T080902116157Z"
TARGET = "CultureMech:001490"
GENERATED = "data/merge_yaml/merged/DESULFOTIGNUM_MEDIUM.yaml"
OWNER_A = "data/normalized_yaml/bacterial/desulfotignum_medium.yaml"
OWNER_B = "data/normalized_yaml/bacterial/desulfobacterium_medium.yaml"
PATHS = [GENERATED, OWNER_A, OWNER_B]
RUNNER = "scripts/batch079_run_check_v2.py"
EXPECTED = {
    GENERATED: "17434c3b989e7622368511f076130f37fac6b2e3ff2a28886b8af7b955f43a10",
    OWNER_A: "5fbbb84755411f193026cb2acca75c91a02edc72d9699dfb19756ac1d215a121",
    OWNER_B: "2a5157e6de5fbd44d2c33c8447a79a8b0372c02b2e2f800c34118869aca373ba",
    str(D / "medium383a.json"): "f37fad8036cde0c57171edc1279ed0881e18e2174e9b2222f00dffe556b9e876",
    str(D / "medium383.json"): "03e3daa513a4e5d92229a17092fc29bc6873c253d7a53d47ceb5f68da93b6b83",
    str(
        D / "DSMZ_Medium383a.pdf"
    ): "4b4f4c9bef3e2d44a03a8b8d696bef396a9aa1e8825af193bc330aa5fe87ceab",
    str(
        D / "DSMZ_Medium383.pdf"
    ): "90291ef8604727d3eccc28eb3b9734103d53a3aad1bf9233c965fc15a66c45de",
    str(D / "peer-review.md"): "6fcc4496c3ed383dd11e95a7f881494ca647292ab52ef410e94cd1374836d30f",
    str(D / "targets.yaml"): "aac83821854974323fa1c4ddae6033ac71b025a8c5b1aab6aea994e1f75ff842",
    str(
        D / "original-native/inspection.json"
    ): "c4033c465b0166a0165334815c62b5cb67c701588768ef6ab5e32f03a460d217",
    str(
        D / "original-native/RESULT.md"
    ): "5d889ac90072ef6eeb01e9a34a8101ca8f2da53b969de4a208a61c8113bad7d5",
    str(
        D / "original-native/schema.log"
    ): "7f6c83aa39bdbb10305b80868a767cd345f0b6beecce0de70fdaa684c8eda050",
    str(
        D / "original-native/strict.log"
    ): "0d6bd0d3ec67b8975dfcf2fb1feee1cc59cfb142a8586c29aa2236dd609e2df6",
    str(
        D / "original-native/strict.tsv"
    ): "4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b",
    str(
        D / "original-native/terms.log"
    ): "6d1e6d9197ee2e4862a8c3e955bf66380f33809345381a786040ec40180d52e0",
    str(
        D / "original-native/references.log"
    ): "254da7eee7ae518a1951f250278e1b86383cdd1cdc205bb7c4a17786a6c89954",
    str(
        CHEM / "chemical-identity-assessment.json"
    ): "2a988dae7af4d379fffbc2e2f2a5a8b7fec3c6cdbd86330f9bec196931c8906d",
    str(
        CHEM / "direct-pin-receipt.json"
    ): "8c91aa831bf2c8d7ce66f928ef5b92120f6a2f38b2baa6362b56f622ea9dc677",
    str(
        CHEM / "ols-capture-catalog.json"
    ): "7128a41d6cf46fecf7c36398b81139661678d1758fce03638578967b8bd64697",
    str(
        CHEM / "input-slots.json"
    ): "ed1a8fe08a2ec77fc8c719518dcc7825182361c55cc177afdc2312208f9561f6",
    str(
        CHEM / "mim-exact-label-rows.json"
    ): "78059fbf913cfeb6a0cd3545e8f7f6d336c24e88f51d2fb5dd21053dc16b8f41",
    "src/culturemech/data/mediaingredientmech/label_index.csv": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "src/culturemech/schema/culturemech.yaml": "43725a6b518253da59235a20fa684f0332f2fd83ef852b2463c9e4d0cf1be9d5",
    "schema/record_review.yaml": "229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb",
    "src/culturemech/merge/formulation.py": "985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab",
    RUNNER: "3655970eaa14fe87473cb7c79bd25f41d815401d95584706a70aab843f19dfd9",
}
CAPTURES = [
    (
        "20261115T080948377716Z-record08-fetch-primary383a.json",
        "3da05d3b565d415bc35887515ceb66b3a98894b1126f7161b225e9d80e4e2b46",
        "DSMZ_Medium383a.pdf",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium383a.pdf",
    ),
    (
        "20261115T080949290338Z-record08-fetch-primary383.json",
        "47758c1b5f9dd2c319f5ca742e1e0a5e9bf28e23cc2544817372662675207bf0",
        "DSMZ_Medium383.pdf",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium383.pdf",
    ),
    (
        "20261115T080950247722Z-record08-fetch-structured383a.json",
        "35b779025bfafe9aba0a2fef7ad3ccdacda1d438b7d23e0eb4428016306d3469",
        "medium383a.json",
        "https://mediadive.dsmz.de/download/medium/383a/json",
    ),
    (
        "20261115T080950811016Z-record08-fetch-structured383.json",
        "1ca6048f3159636f2be8fb11bb9c832f6f6439ff0d4bf36cd9d2ec1d0c8af53a",
        "medium383.json",
        "https://mediadive.dsmz.de/download/medium/383/json",
    ),
]
# Reviewed stage decisions are keyed by exact names, never inferred from index ranges.
STAGES = {
    "Solution A": [
        "Na2SO4",
        "KH2PO4",
        "NH4Cl",
        "NaCl",
        "MgCl2 x 6 H2O",
        "KCl",
        "CaCl2 x 2 H2O",
        "Sodium resazurin",
    ],
    "Solution B": ["Na2CO3"],
    "Solution C": ["Na-pyruvate"],
    "Solution E": ["Na2S x 9 H2O"],
    "Selenite-tungstate solution": ["NaOH", "Na2SeO3 x 5 H2O", "Na2WO4 x 2 H2O"],
    "Trace element solution SL-10": [
        "HCl",
        "FeCl2 x 4 H2O",
        "ZnCl2",
        "MnCl2 x 4 H2O",
        "H3BO3",
        "CoCl2 x 6 H2O",
        "CuCl2 x 2 H2O",
        "NiCl2 x 6 H2O",
        "Na2MoO4 x 2 H2O",
    ],
    "Wolin's vitamin solution (10x)": [
        "Biotin",
        "Folic acid",
        "Pyridoxine hydrochloride",
        "Thiamine HCl",
        "Riboflavin",
        "Nicotinic acid",
        "Calcium D-(+)-pantothenate",
        "Vitamin B12",
        "p-Aminobenzoic acid",
        "(DL)-alpha-Lipoic acid",
    ],
}
SOURCE_IDS = {
    "383a": {
        "main": 755,
        "Solution A": 756,
        "Solution B": 758,
        "Solution C": 759,
        "Solution D": 760,
        "Solution E": 761,
        "Selenite-tungstate solution": 777,
        "Trace element solution SL-10": 595,
        "Wolin's vitamin solution (10x)": 5980,
    },
    "383": {
        "main": 728,
        "Solution A": 729,
        "Solution B": 731,
        "Solution C": 732,
        "Solution D": 733,
        "Solution E": 734,
        "Selenite-tungstate solution": 777,
        "Trace element solution SL-10": 595,
        "Wolin's vitamin solution (10x)": 5980,
    },
}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    return json.loads((ROOT / path).read_text())


def write(path, value):
    with (ROOT / path).open("x") as h:
        json.dump(value, h, indent=2, ensure_ascii=False)
        h.write("\n")


def utc(value):
    return value.replace("+00:00", "Z")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue", required=True)
    args = parser.parse_args()
    assert (
        args.issue.startswith("https://github.com/CultureBotAI/CultureMech/issues/")
        and args.issue.rsplit("/", 1)[1].isdigit()
    )
    assert Path.cwd().resolve() == ROOT
    destinations = [
        D / "claim-inventory.json",
        D / "author-plan.json",
        D / "inspection-binding.json",
        D / "review.yaml",
        D / "author-direct-audit.json",
    ]
    assert all(
        not os.path.lexists(ROOT / p) for p in destinations
    ), "Existing output: preserve it and stop"
    started = datetime.now(timezone.utc)
    frozen = dict(EXPECTED)
    for p, h in frozen.items():
        assert digest(p) == h, p
    chem = load(CHEM / "chemical-identity-assessment.json")
    catalog = load(CHEM / "ols-capture-catalog.json")
    for pin in load(CHEM / "direct-pin-receipt.json")["pins"]:
        assert digest(pin["path"]) == pin["sha256"], pin["path"]
        frozen[pin["path"]] = pin["sha256"]
    captured = {}
    for basename, h, filename, url in CAPTURES:
        path = RUN / basename
        assert digest(path) == h
        rec = load(path)
        assert rec["exit"] == 0 and rec["cwd"] == str(ROOT)
        assert rec["argv"] == [
            "/usr/bin/curl",
            "-fL",
            "--max-time",
            "45",
            "-o",
            str(D / filename),
            url,
        ]
        frozen[str(path)] = h
        for stream in ["stdout", "stderr"]:
            assert digest(rec[stream]) == rec[stream + "_sha256"]
            frozen[rec[stream]] = rec[stream + "_sha256"]
        captured[filename] = rec
    docs = {p: yaml.safe_load((ROOT / p).read_text()) for p in PATHS}
    assert (
        docs[GENERATED]["id"] == TARGET
        and docs[OWNER_A]["id"] == TARGET
        and docs[OWNER_B]["id"] == "CultureMech:001489"
    )
    assert all(len(d["ingredients"]) == 33 and not d.get("solutions") for d in docs.values())
    old = load(D / "original-native/inspection.json")
    for item in old["source"]["inputs"]:
        assert digest(item["path"]) == item["sha256"]
    assert old["targets"] == yaml.safe_load((ROOT / D / "targets.yaml").read_text())["targets"]
    sources = {k: load(D / ("medium" + k + ".json")) for k in ["383a", "383"]}
    stage_by_name = {name: stage for stage, names in STAGES.items() for name in names}
    assert len(stage_by_name) == 33
    inventory = []
    for doc, d in docs.items():
        copied_key = "383a" if doc == OWNER_A else "383"
        identity_key = "383" if doc == OWNER_B else "383a"
        assert {x["preferred_term"] for x in d["ingredients"]} == set(stage_by_name)
        for idx, ing in enumerate(d["ingredients"]):
            name = ing["preferred_term"]
            stage = stage_by_name[name]
            source_rows = []
            for key in ["383a", "383"]:
                sol_matches = [
                    (si, s)
                    for si, s in enumerate(sources[key]["solutions"])
                    if s["id"] == SOURCE_IDS[key][stage]
                ]
                assert len(sol_matches) == 1
                si, s = sol_matches[0]
                matches = [(ri, r) for ri, r in enumerate(s["recipe"]) if r.get("compound") == name]
                assert len(matches) == 1
                ri, row = matches[0]
                source_rows.append(
                    {
                        "source": str(D / ("medium" + key + ".json")),
                        "sha256": digest(D / ("medium" + key + ".json")),
                        "reference": captured["medium" + key + ".json"]["argv"][-1],
                        "locator": f"$.solutions[{si}].recipe[{ri}]",
                        "solution_id": s["id"],
                        "solution_name": s["name"],
                        "solution_volume_ml": s["volume"],
                        "exact_object": row,
                    }
                )
            actual = next(
                x for x in source_rows if x["source"].endswith("medium" + copied_key + ".json")
            )
            assert (
                float(ing["concentration"]["value"]) == float(actual["exact_object"]["g_l"])
                and ing["concentration"]["unit"] == "G_PER_L"
            ), (doc, name)
            rationale = (
                "The numerical value matches the copied provider "
                + stage
                + " rate, but its root placement lacks that intermediate/stock boundary and the receiving addition. Preserve source amounts while correcting representation; no new final concentration is asserted."
            )
            if doc == GENERATED and stage in ["Solution A", "Solution C", "Solution E"]:
                rationale += " It follows DSM383 despite the target DSM383a identity; source-specific assembly and component amounts must remain distinct."
            if name == "HCl":
                rationale += " The provider explicitly gives 2.5 g/L stock; the primary 25% HCl dose has no declared percentage convention or density, so independent mass conversion is unresolved."
            if name == "Sodium resazurin":
                rationale += " The source separately states 0.1% w/v and 0.50 mL; salt identity is audited separately and is not proved by provider molarity."
            inventory.append(
                {
                    "document": doc,
                    "field": f"ingredients[{idx}].concentration",
                    "ingredient": name,
                    "retained_value": ing["concentration"],
                    "decision": "correct",
                    "rationale": rationale,
                    "declared_source_identity": identity_key,
                    "copied_rate_source": copied_key,
                    "sources": source_rows,
                }
            )
        for n, step in enumerate(d["preparation_steps"]):
            if n < 2:
                s = sources[identity_key]["solutions"][0]
                raw = s["steps"][n]
                decision = "evidence_only"
                why = (
                    "Retain the supported main staged gas/pH/sterilization sequence."
                    if n == 0
                    else "Retain the source optional dithionite range, explicit w/v stock example, transfer range and darkness; optional stimulation is not a universal growth claim."
                )
                loc = f"$.solutions[0].steps[{n}]"
            else:
                si, s = next(
                    (si, s)
                    for si, s in enumerate(sources[identity_key]["solutions"])
                    if s["id"] == 595
                )
                raw = s["steps"][0]
                loc = f"$.solutions[{si}].steps[0]"
                decision = "correct"
                why = "Exact SL-10 makeup text is supported, but it is unqualified at main-method scope; retain wording and make the stock boundary explicit."
            inventory.append(
                {
                    "document": doc,
                    "field": f"preparation_steps[{n}].description",
                    "retained_value": step["description"],
                    "decision": decision,
                    "rationale": why,
                    "sources": [
                        {
                            "source": str(D / ("medium" + identity_key + ".json")),
                            "sha256": digest(D / ("medium" + identity_key + ".json")),
                            "reference": captured["medium" + identity_key + ".json"]["argv"][-1],
                            "locator": loc,
                            "exact_object": raw,
                        }
                    ],
                }
            )
        for bound in ["min", "max"]:
            inventory.append(
                {
                    "document": doc,
                    "field": "ph_range." + bound,
                    "retained_value": d["ph_range"][bound],
                    "decision": "evidence_only",
                    "rationale": "Retain source final pH range 7.0–7.2; separate the preparative pH below 6.",
                    "sources": [
                        {
                            "source": str(D / ("medium" + identity_key + ".json")),
                            "sha256": digest(D / ("medium" + identity_key + ".json")),
                            "reference": captured["medium" + identity_key + ".json"]["argv"][-1],
                            "locator": "$.medium." + ("min_pH" if bound == "min" else "max_pH"),
                            "exact_value": sources[identity_key]["medium"][
                                "min_pH" if bound == "min" else "max_pH"
                            ],
                        }
                    ],
                }
            )
    assert len(inventory) == 114 and sum(".concentration" in x["field"] for x in inventory) == 99
    write(
        D / "claim-inventory.json",
        {
            "scope": "99 existing concentrations plus nine retained preparation paragraphs and six pH bounds; no values changed",
            "rows": inventory,
        },
    )
    extra = [
        "AGENTS.md",
        "docs/record-reviews.md",
        "docs/record-review-profile.md",
        "docs/DATA_LAYERS.md",
        "conf/record_review.yaml",
        ".claude/skills/review-yaml-record/SKILL.md",
        ".claude/skills/review-recipes/reference/validation-rules.md",
        ".claude/skills/review-ingredient-concentrations/references/evidence-contract.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        "scripts/record_review.py",
        "scripts/batch079_build_record08_review.py",
        str(D / "claim-inventory.json"),
    ]
    for p in extra:
        frozen[p] = digest(p)
    plan = {
        "started_at": utc(started.isoformat()),
        "reviewed_scientific_decisions": "Frozen by exact named ingredients and source IDs in helper STAGES/SOURCE_IDS; no positional decision heuristic",
        "issue": args.issue,
        "inputs": frozen,
        "native_diagnostics": "Original four streams reused on exact unchanged target/owner/schema hashes; exit status and ordering attributed to original RESULT.md, not newly timed child receipts.",
    }
    write(D / "author-plan.json", plan)
    frozen[str(D / "author-plan.json")] = digest(D / "author-plan.json")
    command = [
        str(ROOT / ".venv/bin/python"),
        "-B",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(D / "targets.yaml"),
    ]
    for p in sorted(frozen):
        command += ["--input", p]
    before = set((ROOT / RUN).glob("*-record08-inspect-final.json"))
    result = subprocess.run(
        [str(ROOT / ".venv/bin/python"), "-B", RUNNER, "record08-inspect-final", *command],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    after = set((ROOT / RUN).glob("*-record08-inspect-final.json"))
    new = after - before
    assert len(new) == 1, (result.returncode, result.stdout, result.stderr)
    rp = new.pop()
    receipt = load(rp)
    assert (
        result.returncode == 0
        and receipt["exit"] == 0
        and receipt["argv"] == command
        and receipt["cwd"] == str(ROOT)
    )
    for stream in ["stdout", "stderr"]:
        assert digest(receipt[stream]) == receipt[stream + "_sha256"]
    inspected = load(receipt["stdout"])
    assert (
        inspected["targets"] == old["targets"]
        and inspected["source"]["git_revision"] == "dda27db28f1e5f4f05da6d92fbd2cc1bd6e8add3"
    )
    observed = {x["path"]: x["sha256"] for x in inspected["source"]["inputs"]}
    assert observed == frozen, (set(observed) - set(frozen), set(frozen) - set(observed))
    for p, h in frozen.items():
        assert digest(p) == h, p
    binding = {
        "receipt_path": str(rp.relative_to(ROOT)),
        "receipt_sha256": digest(rp),
        "expected_argv": command,
        "actual_argv": receipt["argv"],
        "stdout": receipt["stdout"],
        "stdout_sha256": receipt["stdout_sha256"],
        "stderr": receipt["stderr"],
        "stderr_sha256": receipt["stderr_sha256"],
        "exit": receipt["exit"],
        "input_count": len(frozen),
        "all_expected_input_hashes_equal": True,
    }
    write(D / "inspection-binding.json", binding)
    instant = datetime.now(timezone.utc)
    finished = instant.strftime("%Y-%m-%dT%H:%M:%SZ")
    review_id = instant.strftime("%Y%m%dT%H%M%SZ") + "-batch079-record08-desulfotignum"
    owners = inspected["targets"][0]["owner_paths"]
    evidence = []

    def ev(
        id, kind, reference, summary, locator=None, support="context_only", sha=None, access=None
    ):
        x = {
            "evidence_id": id,
            "kind": kind,
            "reference": reference,
            "accessed_at": access or finished,
            "support": support,
            "summary": summary,
        }
        if locator:
            x["locator"] = locator
        if sha:
            x["snapshot_sha256"] = sha
        evidence.append(x)

    ev(
        "E-target",
        "record_content",
        GENERATED,
        "Complete generated record read: DSM383a identity but DSM383 ingredient array; 33 root components, no stock containers; existing variants and all ten history events retained.",
        "Entire YAML",
        sha=EXPECTED[GENERATED],
    )
    ev(
        "E-owner-a",
        "record_content",
        OWNER_A,
        "Complete maintained DSM383a owner: 33 root components, staged source preparation and eight historical events.",
        "Entire YAML",
        sha=EXPECTED[OWNER_A],
    )
    ev(
        "E-owner-b",
        "record_content",
        OWNER_B,
        "Complete maintained DSM383 owner, included as source/variant context rather than a second selected target; 33 root components and eight historical events.",
        "Entire YAML",
        sha=EXPECTED[OWNER_B],
    )
    for key in ["383a", "383"]:
        f = "DSMZ_Medium" + key + ".pdf"
        c = captured[f]
        ev(
            "E-primary-" + key,
            "primary_source",
            c["argv"][-1],
            "Read complete official PDF; generic formulation and printed stock sections used. DSM383 strain-specific substitutions are explicitly excluded from transfer.",
            "383a pages1–2; 383 pages1–3; separate A–E and embedded stock tables",
            support="partial",
            sha=digest(D / f),
            access=utc(c["started_at"]),
        )
        f = "medium" + key + ".json"
        c = captured[f]
        ev(
            "E-provider-" + key,
            "database",
            c["argv"][-1],
            "Read all nine distinct solution objects, recipes, additions and preparation. Rates are interpreted at their own stage; provider molar fields are not chemical-form evidence.",
            "$.medium and all $.solutions",
            support="partial",
            sha=digest(D / f),
            access=utc(c["started_at"]),
        )
    ev(
        "E-quantity",
        "record_content",
        str(D / "claim-inventory.json"),
        "All 99 existing concentration fields, nine preparation paragraphs and six pH bounds have explicit retained values, reviewed decisions and exact source-object locators.",
        "114 field decisions; source JSON objects and hashes",
        support="supports",
        sha=digest(D / "claim-inventory.json"),
    )
    ev(
        "E-chemistry",
        "authority",
        str(CHEM / "chemical-identity-assessment.json"),
        "All 192 slots/33 unique asserted ChEBI IDs: 28 compatible named chemicals, two broad identities, one constituent-only HCl identity and two exact-form mismatches.",
        "Every exact slot, current ontology object, raw hash and original capture time",
        support="partial",
        sha=digest(CHEM / "chemical-identity-assessment.json"),
    )
    ev(
        "E-mim",
        "record_content",
        "src/culturemech/data/mediaingredientmech/label_index.csv",
        "Complete packaged index scanned for all33 exact local names:36 rows. Nickel and cobalt have rejected preferred rows plus mapped synonyms; MAPPED sodium-resazurin still uses nonsodium8806. This is resolver-policy evidence, not chemical proof.",
        "Exact rows in mim-exact-label-rows.json; metadata source commit6643131b0f12ab40b66f98135245fca04027e0e9",
        sha=EXPECTED["src/culturemech/data/mediaingredientmech/label_index.csv"],
    )
    for c in catalog:
        t = c["exact_terms"][0]
        ev(
            "E-" + c["id"].replace(":", "-"),
            "authority",
            c["url"],
            t["label"]
            + "; exact current active term; formula="
            + str(t["annotation"].get("generalized_empirical_formula")),
            t["obo_id"],
            sha=c["sha256"],
            access=c["started_at"],
        )
    ev(
        "E-peer",
        "prior_review",
        str(D / "peer-review.md"),
        "Independent source review supplied by coordinating root; claims rechecked against full current files and captured primary tables before adoption.",
        "Full peer text",
        sha=digest(D / "peer-review.md"),
    )
    ev(
        "E-current-merge",
        "record_content",
        "src/culturemech/merge/formulation.py",
        "Full current body read: exact scientific assertions are required for consolidation, and mismatched formulations raise an error. Historical output collapse is not attributed to a current-code defect without replay.",
        "formulation_content, FormulationFingerprinter, merge_formulation_evidence",
        sha=EXPECTED["src/culturemech/merge/formulation.py"],
    )
    ev(
        "E-schema",
        "record_content",
        "src/culturemech/schema/culturemech.yaml",
        "high_metal is defined from total metal concentration >=1049.84mM. Stock-root conflation prevents treating the current flag as a verified final-medium calculation.",
        "MediaRecipe.high_metal; lines137–146",
        sha=EXPECTED["src/culturemech/schema/culturemech.yaml"],
    )
    ev(
        "E-native-result",
        "validation",
        str(D / "original-native/RESULT.md"),
        "Original recovery receipt reports all four record08 commands exited0, after07 canary; this is technical evidence only. Logs do not independently supply process exits/timing.",
        "Record08 row, exact command templates and scope paragraph",
        sha=digest(D / "original-native/RESULT.md"),
    )
    for name in ["schema", "strict", "terms", "references"]:
        ev(
            "E-native-" + name,
            "validation",
            str(D / "original-native" / (name + ".log")),
            "Full original log read on byte-identical current target/owners/schema; no rerun.",
            "Entire original stream",
            sha=digest(D / "original-native" / (name + ".log")),
        )
    ev(
        "E-inspect",
        "validation",
        binding["receipt_path"],
        "New native inspection executed once with exact expected argv and all frozen input hashes verified.",
        "Receipt plus stdout/stderr hashes; inspection-binding.json",
        support="supports",
        sha=binding["receipt_sha256"],
        access=utc(receipt["started_at"]),
    )
    checks = []
    summaries = {
        "schema": "Schema success only; does not establish source truth.",
        "strict": "Exactly one file; schema layer, zero errors and header-only TSV. No full-corpus QC claim.",
        "terms": "Configured term routes passed; chemical slots require the separate exact-form audit.",
        "references": "Zero evidence assertions checked. This is not completeness or scientific support.",
    }
    for name in ["schema", "strict", "terms", "references"]:
        cmd = "UV_NO_SYNC=1 UV_OFFLINE=1 just validate-" + name + " " + GENERATED
        if name == "strict":
            cmd += " --out workspace/reports/batch079-recovery-20261114/record08/strict.tsv --workers 1 --quiet"
        checks.append(
            {
                "check_id": "C-" + name,
                "name": "Original native " + name,
                "status": "passed",
                "required": True,
                "target_ids": [TARGET],
                "exit_code": 0,
                "command": cmd,
                "summary": summaries[name],
                "scope_note": "Command instantiated from the original recovery RESULT.md; exit0/order are receipt-reported, while the full retained logs and input byte equality were directly checked. No rerun or independently timed process receipt is claimed.",
                "evidence_ids": ["E-native-result", "E-native-" + name],
            }
        )
    checks += [
        {
            "check_id": "C-inspect",
            "name": "Fresh native input inspection",
            "status": "passed",
            "required": True,
            "target_ids": [TARGET],
            "exit_code": 0,
            "command": shlex.join(command),
            "summary": "All final evidence inputs bound before authoring the draft; exact receipt/argv/stream/input hashes retained.",
            "scope_note": str(D / "inspection-binding.json"),
            "evidence_ids": ["E-inspect"],
        },
        {
            "check_id": "C-science",
            "name": "Primary source and chemical scientific assessment",
            "status": "failed",
            "required": True,
            "target_ids": [TARGET],
            "summary": "Completed assessment finds identity and stock-representation blockers plus exact-form and preparation defects; needs_curation is retained.",
            "evidence_ids": ["E-primary-383a", "E-primary-383", "E-quantity", "E-chemistry"],
        },
        {
            "check_id": "C-history",
            "name": "Embedded history and current ownership review",
            "status": "passed",
            "required": True,
            "target_ids": [TARGET],
            "summary": "Read all26 embedded history events and current maintained/generated/variant relationships. These event statements do not independently prove historical execution or external report contents. No history edited.",
            "evidence_ids": ["E-target", "E-owner-a", "E-owner-b", "E-current-merge"],
        },
    ]
    assessments = []

    def assessment(id, area, topic, outcome, summary, refs, details=None):
        x = {
            "assessment_id": id,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": [TARGET],
            "evidence_ids": refs,
        }
        if details:
            x["details"] = details
        assessments.append(x)

    local = ["E-target", "E-owner-a", "E-owner-b"]
    sources_ev = ["E-primary-383a", "E-primary-383", "E-provider-383a", "E-provider-383"]
    assessment(
        "A-identity",
        "identity",
        "DSM383a versus distinct DSM383 formulation",
        "concern",
        "The selected CultureMech:001490 denotes DSM383a. Its ingredient array instead equals the DSM383 owner and its synonym/merged_from treat the two sources as duplicates despite the maintained concentration-variant relationship. This is a confirmed generated-artifact conflict; no current-merger defect is inferred.",
        local + sources_ev + ["E-current-merge"],
    )
    details = []
    for row in inventory:
        details.append(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
    assessment(
        "A-quantities",
        "quantity",
        "Every existing concentration and retained numeric preparation field",
        "concern",
        "Reviewed all99 concentration fields (33 per file), nine preparation paragraphs and six pH bounds. Existing numerical rates match their copied provider intermediate or stock objects; all99 concentration fields need stage representation correction. The generated target also imports distinct DSM383 rates under383a identity. Retained supported prose and pH bounds are credited separately.",
        local + sources_ev + ["E-quantity"],
        "\n".join(details),
    )
    assessment(
        "A-assembly",
        "representation",
        "A–E additions, embedded stocks and volume basis",
        "concern",
        "383a assembles962/20/4/1/13mL with provider main volume1000mL;383 assembles952/20/20/1/10mL and explicitly states final1003mL in its PDF. SolutionA also receives SL-10 and Se/W, whileD receives Wolin vitamins. Intermediate A, B, C, E and three embedded stock strengths are not final-medium concentrations. HCl stock2.5g/L is provider-declared; unspecified25% basis prevents an independent primary mass conversion.",
        local + sources_ev,
    )
    assessment(
        "A-forms",
        "grounding",
        "Every asserted ID and exact supplied form",
        "concern",
        "All33 IDs across192 slots are active; nickel hexahydrate is mapped to anhydrous34887 and sodium resazurin to nonsodium8806. Candidate53542 precisely encodes six waters. Explicit D-pantothenate matches31345; lipoic DL and genericB12 retain specificity limits. MIM statuses are kept separate from chemical proof.",
        ["E-chemistry", "E-mim"] + ["E-" + x["id"].replace(":", "-") for x in catalog],
        "\n".join(x["id"] + ": " + x["status"] + "; " + x["reason"] for x in chem["assessments"]),
    )
    assessment(
        "A-preparation",
        "scope",
        "Supported main controls and misplaced SL-10 makeup",
        "concern",
        "Gas mixtures, staged sterilization, finalpH7.0–7.2, darkness and optional dithionite/transfer prose are supported and retained. SL-10 makeup text is accurate but placed at preparation_steps[2] without explicit stock scope. Do not make optional dithionite mandatory or transfer DSM383 strain-specific substitutions.",
        local + sources_ev,
    )
    assessment(
        "A-classification",
        "identity",
        "Defined liquid formulation and biological claims",
        "supported",
        "DEFINED medium/composition and LIQUID physical state fit the generic chemically specified source. No structured strain-specific growth claim is asserted; generic cultivation and source stimulation prose do not establish optimality or broad organism growth.",
        local + sources_ev,
    )
    assessment(
        "A-metals",
        "quantity",
        "Unestablished high_metal derived flag",
        "unknown",
        "All three documents assert high_metal:true. The schema threshold concerns final total metal concentration, but present stock-root conflation supplies no valid final total. Re-evaluate after stage corrections; neither a false value nor a replacement total is asserted.",
        local + ["E-schema", "E-quantity"],
    )
    assessment(
        "A-variant",
        "consistency",
        "Concentration variant relation and denominator precision",
        "concern",
        "Retain the defensible source-specific concentration variant. NaCl15vs21g and pyruvate1vs2.5g are real batch differences. Both sources use3g magnesium hexahydrate and0.4g sulfide nonahydrate per batch; their A/E volumes and final1000-provider/1003-explicit bases differ. Current explanatory prose must distinguish batch masses from stage and final concentrations.",
        local + sources_ev,
    )
    assessment(
        "A-provenance",
        "provenance",
        "Claim linkage, embedded histories and generated ownership",
        "concern",
        "The full three records contain source URLs and histories but no evidence/reference arrays linking each formulation claim. The native reference pass checked zero assertions. Histories are retained as event statements; the current exact-formulation merger is read only as maintained ownership context, not proof of how the historical artifact was produced.",
        local + ["E-current-merge", "E-native-result", "E-native-references"],
    )
    findings = []

    def finding(id, category, severity, title, description, paths, refs, reason):
        findings.append(
            {
                "finding_id": id,
                "issue_key": "batch079-record08-" + id.lower(),
                "category": category,
                "severity": severity,
                "status": "open",
                "certainty": "confirmed",
                "title": title,
                "description": description,
                "target_ids": [TARGET],
                "field_paths": paths,
                "evidence_ids": refs,
                "owner_paths": owners,
                "rule_id": "CultureMech.single-record-checklist." + category,
                "native_severity": severity,
                "normalization_reason": reason,
                "external_issues": [args.issue],
            }
        )

    finding(
        "F-identity",
        "identity",
        "blocker",
        "DSM383 values are assigned to the DSM383a target",
        "Generated identity and source accession say383a, but its entire ingredient array follows383, including NaCl22.0588, pyruvate125 and sulfide40G_PER_L instead of383a provider-stage15.5925,250 and30.7692. Historical duplicate grouping must not erase the maintained variant. Correct authoritative boundaries and regenerate; do not infer a present code defect from this output.",
        ["media_term", "ingredients", "synonyms", "merged_from", "variant_children"],
        local + sources_ev + ["E-current-merge"],
        "Wrong source formulation makes the generated record denote a different recipe; this is an identity blocker regardless of valid YAML.",
    )
    finding(
        "F-stock",
        "representation",
        "blocker",
        "Intermediate and stock strengths are flattened into root ingredients",
        "All three fully read files omit solution containers and place A/B/C/E and trace/selenite/vitamin rates at root. Carbonate50G_PER_L is1g in20mL B, not a50g/L final-medium assertion. Restore each distinct component stage and addition basis before deriving final concentrations. Re-evaluate high_metal from a supported final total afterward.",
        ["ingredients", "solutions", "high_metal"],
        local + sources_ev + ["E-schema"],
        "Following flattened root strengths would materially change the source formulation; critical representation failure is a blocker, not an ordinary missing citation.",
    )
    finding(
        "F-forms",
        "grounding",
        "major",
        "Nickel hydrate and sodium-resazurin identities are not represented exactly",
        "All three files use34887 in both ingredients[21] term slots for NiCl2 x6H2O;53542 represents that exact hydrate. Their primary-only ingredients[7].term uses8806 without sodium for Sodium resazurin. Resolve the latter exact salt before replacing its ID. A MAPPED synonym does not certify supplied form.",
        [
            "ingredients[21].term",
            "ingredients[21].mediaingredientmech_chebi_term",
            "ingredients[7].term",
        ],
        local + ["E-chemistry", "E-mim", "E-CHEBI-34887", "E-CHEBI-53542", "E-CHEBI-8806"],
        "Exact-form errors undermine chemical interpretation and any molar calculation; all IDs exist, so this is a chemical grounding major, not native nonexistent-ID ruleP2.2.",
    )
    finding(
        "F-stock-method",
        "scope",
        "major",
        "SL-10 preparation is unqualified at main-medium scope",
        "preparation_steps[2] accurately preserves SL-10 dissolution and1000mL makeup but sits beside the main method without a named stock boundary in all three files. Retain the exact instructions and scope them to SL-10; preserve already-supported main gas, sterilization, final pH, optional supplementation and darkness.",
        ["preparation_steps[2]"],
        local + sources_ev,
        "Misapplying a stock makeup procedure to the completed medium changes preparation scope, warranting major severity while crediting the retained correct text.",
    )
    finding(
        "F-linkage",
        "evidence",
        "minor",
        "Source provenance lacks narrow formulation evidence links",
        "Complete current files have no evidence arrays or root bibliographic references for their individual concentration/preparation claims. Source URLs and import histories remain useful leads. Attach source-specific, exact-stage claim evidence during corrections and retain existing histories.",
        ["ingredients", "evidence", "references"],
        local + ["E-native-references", "E-quantity"],
        "The evidence gap is a bounded provenance defect alongside separately identified substantive formulation errors; it is not itself proof that every source-supported number is wrong.",
    )
    finding(
        "F-variant-basis",
        "consistency",
        "minor",
        "Variant explanation does not distinguish batch mass from concentration basis",
        "Keep the concentration-variant relation, but qualify the stated MgCl2 and sulfide axes: both sources use3g and0.4g per batch respectively. Different A/E volumes and final source bases produce different intermediate or final concentrations; do not describe those as changed batch masses.",
        [
            "variant_children[0].notes",
            OWNER_B + "::variant_modifications[0]",
            OWNER_B + "::parent_media.notes",
        ],
        local + sources_ev,
        "The scientific relationship is defensible; its explanatory basis needs a bounded wording correction without creating a new formulation or changing doses.",
    )
    actions = [
        {
            "action_id": "ACT-stages",
            "description": "In the maintained source records, represent all A–E stages and embedded stocks with their source-specific additions and volume bases. Scope SL-10 preparation explicitly, retain correct main controls, and re-evaluate high_metal only after final-medium composition is supported.",
            "finding_ids": ["F-stock", "F-stock-method", "F-linkage"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "acceptance_checks": [
                "Account for every current ingredient, every printed stock component and every source addition without double counting; preserve99 reviewed current concentration observations as the before-state.",
                "Use explicit source383a versus383 scopes; preserve1003mL explicit final383 versus1000mL provider383a basis without inventing density or percent convention.",
                "Attach exact PURL/object/table evidence to each changed amount or addition using existing schema slots; retain source-supported pH/gas/optional/darkness controls.",
                "Run documented native checks only after separately authorized curation and manually recheck all stage boundaries; calculate high_metal only from supported final totals.",
            ],
        },
        {
            "action_id": "ACT-forms",
            "description": "Correct verified nickel hydrate grounding and resolve the exact sodium-resazurin salt identity in authoritative inputs, retaining explicit D-pantothenate and DL/B12 breadth.",
            "finding_ids": ["F-forms"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "acceptance_checks": [
                "Verify both primary and secondary nickel slots against exact53542 formula/waters and all sodium-resazurin primary slots against an independently verified sodium salt.",
                "Use the immutable packaged MIM resolver policy; keep rejected preferred and mapped synonym distinctions explicit and do not treat chemical validation as an index rewrite.",
                "Do not infer molar concentrations from broadB12 or unspecified stereo/solution forms.",
            ],
        },
        {
            "action_id": "ACT-boundaries",
            "description": "Retain source383 and383a as distinct formulations/concentration variants, qualify the Mg/sulfide explanation and regenerate only through the maintained exact-formulation workflow after owner corrections.",
            "finding_ids": ["F-identity", "F-variant-basis"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "depends_on": ["ACT-stages", "ACT-forms"],
            "generator": "Maintained CultureMech merge workflow under src/culturemech/merge; preview source grouping and stable-ID effects before regeneration.",
            "acceptance_checks": [
                "Generated383a ingredients must derive from its correct maintained formulation; no synonym or merged_from declaration may silently collapse383.",
                "Keep3g magnesium salt and0.4g sulfide batch masses distinct from intermediate/final concentration differences.",
                "Run documented merge/freshness and ID gates at their actual scopes after authorized changes; do not infer a current-code bug or claim those gates ran during this review.",
            ],
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": review_id,
        "kind": "record",
        "repository": "CultureBotAI/CultureMech",
        "title": "Recovered batch079 record08: DSM383a source and chemical assessment",
        "started_at": utc(started.isoformat()),
        "finished_at": finished,
        "reviewer": {
            "identity": "Codex tsb_source_check",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Did not author or alter the existing scientific records. Full files, captured source objects/PDF text and exact chemical authorities were read; coordinating-root source review is attributed as peer context. This is not human approval.",
        },
        "skill": ".claude/skills/review-yaml-record/SKILL.md",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Completed record08 assessment with both maintained owners as context. Two blockers remain: DSM383 identity collapse in the generated383a target, and flattened intermediate/stock composition. Chemical-form and stock-preparation majors plus evidence/variant-prose minors remain. Original technical checks passed but do not establish scientific approval. No scientific file was changed.",
        "source": inspected["source"],
        "scope": {
            "description": "One selected generated target, both full maintained owners as source/variant context, all99 concentrations, retained numeric preparation/pH fields,192 asserted chemical slots and26 embedded history events.",
            "selection": "Recovered079 manifest explicitly selects CultureMech:001490 DESULFOTIGNUM MEDIUM; current exact target and owner paths/IDs were verified.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
            "exclusions": [
                {
                    "target": "Other batch079 records, PR692 and corpus/publication workflows",
                    "reason": "No broader completion, publication, admission or release verdict is made; record10 has not been started.",
                },
                {
                    "target": "DSM383 strain-specific substitutions and source media320/385/120 parent formulations",
                    "reason": "Use only the generic383 comparison and embedded stock definitions printed here; no strain-specific growth or parent recipe transfer.",
                },
                {
                    "target": "Historical external report bodies and historical process execution",
                    "reason": "Embedded current histories are read as stored event statements; this assessment does not certify execution of prior repairs or unseen reports.",
                },
            ],
        },
        "targets": inspected["targets"],
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Completed means the declared scope was assessed; two blocker, two major and two minor findings remain open. This is not a passing scientific verdict.",
            "Original canonical exits/order come from the coordinating recovery RESULT.md; retained logs and unchanged input hashes independently support their reuse, but separate timed execution receipts are absent. No canonical rerun occurred.",
            "Configured term checks do not establish exact chemical form, and reference checks examined zero evidence assertions.",
            "DSM383a provider main volume1000mL agrees with its assembly sum; its PDF does not independently print a final-volume statement. DSM383 PDF explicitly states1003mL. Neither claim is a measured final volume.",
            "No alternative sodium-resazurin salt ID was audited; no density, HCl percent convention, B12 vitamer or DL stereochemical proof was invented.",
            "high_metal remains unestablished until a correctly staged final composition is available; no substitute boolean or total is asserted.",
            "No recipe edits, generator reruns, corpus checks, structured-review validation, saver, Git mutation or publication were performed by this author helper. The parent owns subsequent independent review and persistence.",
        ],
        "notes": [
            "Claim inventory retains the actual current values and both source objects; correct decisions identify current field placement, not an instruction to alter already-supported stock masses.",
            "No current merger-code failure is inferred from the historical generated artifact.",
            "New evidence and this draft use exclusive paths; all prior recovery artifacts and source files remain unchanged.",
        ],
        "links": [args.issue],
        "tags": ["batch079", "record08", "needs_curation", "source_review"],
    }
    assert {x["severity"] for x in findings} == {"blocker", "major", "minor"}
    with (ROOT / D / "review.yaml").open("x") as h:
        yaml.dump(review, h, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=110)
    for p, h in frozen.items():
        assert digest(p) == h, p
    auditpins = [{"path": p, "sha256": h} for p, h in frozen.items()]
    for p in [
        str(rp.relative_to(ROOT)),
        receipt["stdout"],
        receipt["stderr"],
        str(D / "inspection-binding.json"),
        str(D / "review.yaml"),
    ]:
        auditpins.append({"path": p, "sha256": digest(p)})
    write(
        D / "author-direct-audit.json",
        {
            "finished_at": finished,
            "review_id": review_id,
            "scope": "Bounded author artifact integrity, not native review validation or independent scientific pass",
            "counts": {
                "inputs": len(frozen),
                "concentrations": 99,
                "quantity_and_numeric_note_decisions": 114,
                "chemical_slots": 192,
                "unique_chemical_ids": 33,
                "findings_by_severity": dict(Counter(x["severity"] for x in findings)),
            },
            "pins": auditpins,
            "native_inspect_receipt": binding,
            "canonical_reused": True,
            "scientific_source_mutations": False,
            "structured_validate_or_save_executed": False,
        },
    )
    print(
        json.dumps(
            {
                "draft": str(D / "review.yaml"),
                "review_sha256": digest(D / "review.yaml"),
                "inventory_sha256": digest(D / "claim-inventory.json"),
                "author_audit_sha256": digest(D / "author-direct-audit.json"),
                "inspect_receipt": binding["receipt_path"],
                "input_count": len(frozen),
                "finding_counts": dict(Counter(x["severity"] for x in findings)),
            }
        )
    )


if __name__ == "__main__":
    main()
