#!/usr/bin/env python3
"""Account for residual condition-row ingredient labels (#683/#788, 2026-11-16).

Inputs: original pinned queue, prior coverage and inspected primary captures.
Output: exact-preimage proposal and all 104 original condition-row dispositions.
Manual decisions only; no recipe applies, inferred chemical IDs or liquid gas doses.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from prepare_evidence_completion_683 import BASE, NEW, OLD, QUEUE_SHA, ROOT, Proposal, digest
from prepare_model_completion_683 import CAPTURES as MODEL_CAPTURES

CAPTURES = {key: MODEL_CAPTURES[key] for key in ("matsui", "125", "kato")}
CAPTURES.update(
    {
        "carini": (
            "doi:10.1038/ismej.2012.122",
            "family-sources/carini-2013-html/source.html",
            "b9fa5f44ed26edc1d3323374ba097fbc17c10510893d36703f9328983c77c2d1",
            "Media preparation, autoclave and sequential gas sparging",
        ),
        "blumer": (
            "doi:10.1128/AEM.01400-10",
            "remaining-sources/blumer-2010/source.html",
            "ad092222c6d2e66bbd824e3d01ecc577c741cd64ac2eea89bcc43f5b2fa15cb8",
            "Methods: Bacterial strains and growth on sugar substrates",
        ),
        "11801": (
            "PMID:30413737",
            "new:synechococcus-11801/source.xml",
            "bc5b3e8e61aea59f4547670a0bced26074cfa9dd650595ccd7c3316c8b640b53",
            "Culture conditions and Figure 2A",
        ),
        "11802": (
            "PMID:31932622",
            "new:synechococcus-11802/source.xml",
            "fe274b564c95fb3895cdf8a2e2117ba7fe6fe6f14206101a4b9aef5bcc4fa62a",
            "Culture conditions and Figure 2C",
        ),
        "nostoc": (
            "PMID:36550226",
            "new:nostoc-bg110/metadata.json",
            "d883adb351252f53b31ab320203b6cbe3caf00677b580f776f9e924d9979b800",
            "Primary abstract only",
        ),
        "mrs": (
            "PMID:39353547",
            "new:mrs-oxygen/metadata.json",
            "ea40b43f5297f50541e3363ecc5559b07847715c4878aeeebb2e90e3df9c3bc3",
            "Primary abstract only",
        ),
    }
)


def ev(key, snippet, explanation, support="SUPPORT"):
    return {
        "reference": CAPTURES[key][0],
        "supports": support,
        "snippet": snippet,
        "explanation": explanation,
    }


def prepare(p):
    conditions = {n for n, r in p.coverage.items() if r["status"] == "CONDITION_ONLY"}
    if len(conditions) != 104:
        raise ValueError("Expected original 104 condition rows")
    for n in sorted(conditions):
        p.dispose(
            n,
            "CONTEXT_ONLY",
            "Re-read as condition, whole-medium/comparator name, organism, role, preparation warning or unresolved whole-formulation context. No additional named ingredient input/removal is asserted by this row beyond explicit linked/handled cases below. This does not recertify growth or the entire condition.",
        )
    for label, arm in (
        ("CO2", "high-CO2 1% v/v aeration"),
        ("ambient air", "ambient-air 0.04% v/v CO2 aeration"),
    ):
        p.change(
            7,
            "ADD",
            label,
            "Matsui2018 diatom culture; " + arm,
            [
                ev(
                    "matsui",
                    "constant aeration with 1% (v/v) CO2 (high CO2-grown cells) or ambient air containing 0.04% (v/v) CO2 (air-grown cells)",
                    "Culture Conditions. This record is a separate recipe coordinate from queue row30; alternative gas stages are not one co-supply event.",
                )
            ],
            notes="Gas supply only; no liquid concentration inferred.",
        )
    p.dispose(
        7, "STRUCTURED", "Explicit gas supplies supported in source-specific alternative stages."
    )
    p.mention(
        10,
        "sodium",
        "Primary Table S1 resolves formulation constituents, but the main Methods describing preacclimation were not accessible. This literal precursor-treatment claim is not inferred from the later low-sodium assay or mapped to a particular salt.",
        ["SOURCE_CLAIM", "IDENTITY_FORM", "QUANTITY"],
        stage="reported Tsuji2021 sodium preacclimation",
    )
    p.dispose(
        10,
        "HELD_EVIDENCE",
        "Named sodium preacclimation retained without inventing salt, dose or verified procedure.",
    )
    p.mention(
        51,
        "nitrate",
        "The primary abstract explicitly identifies nitrate absence in the separate BG110 comparator. No nitrate removal from this nitrate-replete BG11 variant or specific nitrate salt is inferred.",
        ["OPERATION", "IDENTITY_FORM"],
        "REMOVE",
        "Nostoc BG110 comparator only",
        items=[
            ev(
                "nostoc",
                "BG11 (i.e., in the presence of nitrate) and BG11<sub>0</sub> (in the absence of nitrate)",
                "Primary abstract contrast; negative comparator membership, not an operational change to the BG11 treatment.",
                "PARTIAL",
            )
        ],
    )
    p.dispose(
        51,
        "PARTIALLY_STRUCTURED",
        "Comparator nitrate absence retained separately from a positive or removal assertion on current variant.",
    )
    for n, linked in ((63, 62), (281, 280)):
        p.mention(
            n,
            "silicate",
            "The prior source-supported supplementation event remains intact. Total silicate including the unverified base is unspecified; no addition of a second dose or exact salt identity is inferred.",
            ["QUANTITY", "IDENTITY_FORM"],
            stage="total study-medium silicate, including unresolved base",
        )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED",
            f"Total/form uncertainty retained; supported supplementation remains at queue row {linked}.",
        )
        p.dispositions[n]["coverage_links"] = [
            {"queue_row_number": linked, "role": "supported supplement; not total medium"}
        ]
    p.mention(
        127,
        "oxygen",
        "Primary abstract supports anaerobic versus microaerophilic comparisons but gives no supplied gas species mixture, dose or addition/removal procedure. The oxygen condition is not converted into a liquid ingredient event.",
        ["OPERATION", "QUANTITY"],
        stage="MRS oxygen-condition experiments",
        items=[
            ev(
                "mrs",
                "varying oxygen concentration levels",
                "Primary abstract verifies oxygen-condition comparison only; full preparation method unavailable.",
                "PARTIAL",
            )
        ],
    )
    p.dispose(
        127, "PARTIALLY_STRUCTURED", "Oxygen context retained with operation/quantity uncertainty."
    )
    p.mention(
        135,
        "oxygen",
        "Anaerobic or reduced-oxygen incubation is a reported culture condition. It does not identify an oxygen supplementation/removal step or quantified gas mixture; no whole-medium chemical operation inferred.",
        ["OPERATION", "QUANTITY"],
        stage="reported Columbia blood agar anaerobic/reduced-oxygen incubation",
    )
    p.dispose(
        135,
        "PARTIALLY_STRUCTURED",
        "Literal oxygen context retained without inventing gas manipulation or concentration.",
    )
    for n in (132, 319):
        for label in ("methane", "air"):
            p.change(
                n,
                "ADD",
                label,
                "DSMZ125 methane-air 4:1 incubation atmosphere; alternative to methanol batch addition",
                [
                    ev(
                        "125",
                        "incubate under methane-air (4:1)",
                        "Official page1 preparation alternatives. Source ratio is gas composition only, with no pressure/total volume or dissolved concentration specified.",
                    )
                ],
                notes="Separate methane-air route; not combined with methanol option.",
            )
        p.dispose(
            n,
            "STRUCTURED",
            "Explicit source gas supplies represented at alternative incubation stage.",
        )
    carini_rows = (152, 159, 166, 173, 180, 187, 210, 217)
    for n in carini_rows:
        for label, stage, quote in (
            (
                "CO2",
                "first, after autoclaving: 0.1-micrometre-filtered CO2 sparging for 5 h",
                "sparged with 0.1 μm-filtered CO2 for 5 h",
            ),
            (
                "air",
                "second: air sparging for 10 h, before vitamins and organics",
                "followed by sparging with air for 10 h",
            ),
        ):
            p.change(
                n,
                "ADD",
                label,
                "Carini AMS1 source preparation; " + stage,
                [
                    ev(
                        "carini",
                        quote,
                        "Media preparation explicitly gives ordered gas supplies to establish the bicarbonate-based buffer. Carini2014 follows the cited Carini2013 base preparation. No supplied volume, final dissolved gas dose or whole-parent equivalence is inferred.",
                    )
                ],
            )
        if n in (210, 217):
            p.mention(
                n,
                "bicarbonate",
                "The source describes establishment of a bicarbonate-based buffer through CO2 then air sparging. This is not an explicit addition of a particular bicarbonate salt or measured final species concentration.",
                ["OPERATION", "IDENTITY_FORM", "QUANTITY"],
                stage="Carini AMS1 buffer after gas sparging",
            )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED" if n in (210, 217) else "STRUCTURED",
            "Sequential source gas operations represented; no liquid doses or unidentified salt additions inferred.",
        )
    for n, key, percent in ((233, "11801", "ambient 0.04%"), (235, "11802", "1%")):
        quote = (
            "when ambient air is bubbled in a multi-cultivator"
            if n == 233
            else "1% CO2, 38 °C and 1000 µmole photons.m−2.s−1 with bubbling in MC"
        )
        p.change(
            n,
            "ADD",
            "CO2",
            f"Synechococcus PCC{key} multi-cultivator gas supply; {percent} CO2",
            [
                ev(
                    key,
                    quote,
                    "Primary Methods and figure-associated text verify gas supplied by bubbling. This event is restricted to the multi-cultivator arm; it does not convert every shaker incubation into an active gas-addition claim or assert dissolved concentration.",
                )
            ],
        )
        p.dispose(
            n,
            "STRUCTURED",
            "Source-specific bubbled gas arm verified; culture results are not recertified beyond this input.",
        )
    p.change(
        259,
        "ADD",
        "N2",
        "Blumer-Schuette2010 modified DSMZ640 serum-bottle headspace",
        [
            ev(
                "blumer",
                "a 50-ml batch culture in a 125-ml serum bottle under N2 headspace for 24 h",
                "Methods: Bacterial strains and growth on sugar substrates. This is variant0, distinct from Shang2013 variant1 in the same recipe. No nitrogen purity, gas volume or dissolved concentration inferred.",
            )
        ],
    )
    p.dispose(
        259, "STRUCTURED", "N2 headspace source verified for the exact Blumer-Schuette variant."
    )
    # Duplicate context references point to actual source coordinates, not new events.
    links = {
        131: 130,
        133: 132,
        143: 144,
        145: 142,
        195: 194,
        314: 315,
        316: 313,
        318: 317,
        320: 319,
        14: 13,
        70: 69,
        288: 287,
    }
    for n, linked in links.items():
        p.dispose(
            n,
            "ALREADY_STRUCTURED",
            f"Context/alternative/uncertainty refers to the ingredient claim handled at queue row {linked}; no duplicate ingredient event.",
        )
        p.dispositions[n]["coverage_links"] = [
            {"queue_row_number": linked, "role": "existing or reviewed source claim"}
        ]
    for n, expected in ((304, "Na-acetate"), (305, "Na2-fumarate")):
        _, record, _, _ = p.target(n)
        ingredients = p.documents[record["path"]]["ingredients"]
        indices = [
            i for i, item in enumerate(ingredients) if item.get("preferred_term") == expected
        ]
        if len(indices) != 1:
            raise ValueError("Base-role occurrence must match exactly once")
        p.dispose(
            n,
            "ALREADY_STRUCTURED",
            "Role statement links to the existing authoritative base ingredient; no new dose or identity inference and no duplicate variant input.",
        )
        p.dispositions[n]["coverage_links"] = [
            {
                "source_path": record["path"],
                "field_path": f"ingredients[{indices[0]}]",
                "preferred_term": expected,
                "role": "existing base occurrence",
            }
        ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--coverage", type=Path, required=True)
    parser.add_argument("--prior-worktree", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or digest(args.queue.read_bytes()) != QUEUE_SHA:
        raise ValueError("Output must be new; original queue pin must match")
    csv.field_size_limit(16 * 1024 * 1024)
    with args.queue.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    with args.coverage.open(newline="") as stream:
        coverage = {int(r["queue_row_number"]): r for r in csv.DictReader(stream, delimiter="\t")}
    p = Proposal(rows, coverage)
    prepare(p)
    if set(p.dispositions) != {n for n, r in coverage.items() if r["status"] == "CONDITION_ONLY"}:
        raise ValueError("Residual condition scope mismatch")
    inspections = []
    for key, (reference, path, sha, locator) in CAPTURES.items():
        source = (
            ROOT / NEW / path[4:] if path.startswith("new:") else args.prior_worktree / OLD / path
        )
        if digest(source.read_bytes()) != sha:
            raise ValueError("Inspected source drift: " + key)
        inspections.append(
            {
                "key": key,
                "reference": reference,
                "path": str(source.relative_to(ROOT)) if source.is_absolute() else str(source),
                "sha256": sha,
                "locator": locator,
            }
        )
    payload = {
        "schema_version": 1,
        "base_commit": BASE,
        "source_queue_sha256": QUEUE_SHA,
        "scope": "All 104 original condition rows re-read; explicit gas inputs and residual held names represented, duplicate context linked, whole-formulation conditions retained. No whole-record recertification or recipe applies.",
        "source_inspections": inspections,
        "records": sorted(p.records.values(), key=lambda r: r["path"]),
        "dispositions": [p.dispositions[n] for n in sorted(p.dispositions)],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(
        json.dumps(
            {
                "path": str(args.output),
                "sha256": digest(args.output.read_bytes()),
                "records": len(payload["records"]),
                "rows": len(p.dispositions),
                "statuses": dict(Counter(d["status"] for d in p.dispositions.values())),
                "append_changes": sum(d["append_assertion_count"] for d in p.dispositions.values()),
                "append_mentions": sum(d["append_mention_count"] for d in p.dispositions.values()),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
