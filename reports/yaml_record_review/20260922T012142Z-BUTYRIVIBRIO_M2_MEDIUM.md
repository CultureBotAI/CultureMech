# YAML Record Review: BUTYRIVIBRIO M2 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml
- Started UTC: 2026-09-22T01:21:42Z
- Finished UTC: 2026-09-22T01:21:42Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:000772 |
| Label | butyrivibrio_m2_medium |
| Original label | BUTYRIVIBRIO M2 MEDIUM |
| Category | bacterial |
| Source accession | mediadive.medium:1310 |
| Generated path | data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/butyrivibrio_m2_medium.yaml |
| Merge fingerprint | 451eb15f5f62de2399f0e8b4b46eeb859860f416539d85a89b6b9301866ebd66 |

The reviewed target is a generated merge under `data/merge_yaml/merged`,
derived from the direct DSMZ/MediaDive 1310 owner and the KOMODO wrapper around
the same DSMZ medium.

## Validation

| Check | Result |
| --- | --- |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml --out /private/tmp/BUTYRIVIBRIO_M2_MEDIUM.strict.tsv --workers 1 --quiet` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 structured URL checks |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| `just validate-history data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml` | Not checked: `validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |

Direct `just validate-schema`, `just validate-strict`, `just validate-terms`,
and `just validate-references` were not rerun because the project uv environment
tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with
`TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The
equivalent no-project Python 3.11 validators above passed.

## Identity and Grounding

The DSMZ identity is coherent: MediaDive 1310 and the DSMZ Medium 1310 PDF both
identify the formulation as `BUTYRIVIBRIO M2 MEDIUM`, and the KOMODO duplicate
explicitly cites `DSMZ Medium: 1310`.

The direct ingredient rows are mostly source-faithful for final g/L amounts, but
two required volume rows are absent. DSMZ lists 200 ml clarified rumen fluid and
800 ml distilled water in the 1 L medium. The generated record carries the
clarified-rumen-fluid preparation text but has no structured `Clarified rumen
fluid` addition, and it has no distilled-water row.

The phosphate, ammonium sulfate, sodium chloride, hydrated calcium and magnesium
salts, carbonate, cysteine hydrate, and sulfide nonahydrate groundings preserve
the exact source forms. Sodium resazurin is grounded broadly to resazurin while
also losing the source's 0.5 ml of 0.1% w/v stock-solution context.

## Evidence

Supported:

| Claim | Source support |
| --- | --- |
| `mediadive.medium:1310` denotes DSMZ BUTYRIVIBRIO M2 MEDIUM | MediaDive 1310 and the DSMZ Medium 1310 PDF both identify medium 1310 as `BUTYRIVIBRIO M2 MEDIUM`. |
| Casitone, yeast extract, D-glucose, cellobiose, maltose, lactate, salts, carbonate, cysteine, and sulfide amounts | DSMZ Medium 1310 lists those labels at the same masses shown in the generated record. |
| pH 6.5-6.8 and anaerobic preparation | DSMZ says to cool under 100% CO2, dispense under the same gas, add carbonate, cysteine, and sulfide from sterile anoxic stocks, and adjust pH to 6.5-6.8 if necessary. |

Unsupported or incomplete:

| Generated claim | Problem |
| --- | --- |
| No `Clarified rumen fluid` row | DSMZ adds 200 ml clarified rumen fluid to the main medium; the generated record only carries the stock preparation prose. |
| No `Distilled water` row | DSMZ lists 800 ml distilled water in the main 1 L recipe. |
| `Sodium resazurin`, `0.0005 G_PER_L` as a plain ingredient | DSMZ adds 0.5 ml of a 0.1% w/v sodium resazurin solution; the generated value is the implied final mass, but it loses the stock-addition boundary. |
| No structured DSMZ or KOMODO source reference | The only source support is free text in `notes`; there is no `source_data` or reference object for DSMZ/MediaDive 1310. |

## Completeness

The maintained owner is incomplete because it omits 200 ml clarified rumen fluid
and 800 ml distilled water, two direct volume components needed to reconstruct
the 1 L medium. Carbonate, cysteine, sulfide, sodium resazurin, and clarified
rumen fluid should also be represented as stock additions or scoped preparation
reagents so the existing anoxic-stock prose has structured counterparts.

A gitignore-independent `rg --no-ignore --hidden` search of
`data/normalized_yaml`, `data/merge_yaml/merged`, the ID registry, the recipe
catalog, `reports`, and `data/import_tracking/reports` for
`CultureMech:000772`, `mediadive.medium:1310`, `KOMODO_1310_M2_medium`, and
merge fingerprint `451eb15f...` found the active DSMZ 1310 owner, the KOMODO
1310 source duplicate, this generated merge, expected generated indexes and
reports, and no existing YAML review report for this generated target. `find
reports/yaml_record_review -maxdepth 1 -type f -name '*BUTYRIVIBRIO_M2_MEDIUM.md'`
found no pre-existing report, including ignored files in the report directory.

Empty target-organism and growth-evidence slots are not defects for this
source-only recipe.

## Findings

| Severity | Finding | Maintained owner for a future fix |
| --- | --- | --- |
| Major | The direct 200 ml clarified-rumen-fluid addition is missing from the structured ingredients even though its preparation text is present. | `data/normalized_yaml/bacterial/butyrivibrio_m2_medium.yaml` and the MediaDive import path |
| Major | The direct 800 ml distilled-water row is missing. | `data/normalized_yaml/bacterial/butyrivibrio_m2_medium.yaml` |
| Minor | The 0.5 ml 0.1% w/v sodium-resazurin stock is represented only as an implied final `0.0005 G_PER_L` resazurin row. | `data/normalized_yaml/bacterial/butyrivibrio_m2_medium.yaml` |
| Minor | The record has no structured DSMZ/MediaDive 1310 source reference, so the reference validator had no source URL to check. | `data/normalized_yaml/bacterial/butyrivibrio_m2_medium.yaml` |

No blocker findings found.

## Recommended Edits

1. Add the 200 ml clarified-rumen-fluid addition to
   `data/normalized_yaml/bacterial/butyrivibrio_m2_medium.yaml` and keep its
   preparation text scoped to that stock.
2. Add the 800 ml distilled-water row from DSMZ Medium 1310.
3. Represent sodium resazurin as the 0.5 ml addition of 0.1% w/v stock, or
   retain the final amount with an explicit source note explaining the
   conversion.
4. Add structured DSMZ/MediaDive 1310 provenance.
5. Regenerate `data/merge_yaml/merged/BUTYRIVIBRIO_M2_MEDIUM.yaml` and verify
   the KOMODO 1310 duplicate still merges only after the same corrections are
   made there.

## Follow-up Checks

- Rerun focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/butyrivibrio_m2_medium.yaml`.
- Rerun `just verify-merges` after regeneration and inspect the generated M2
  diff to confirm rumen fluid, water, sodium resazurin, provenance, and duplicate
  linkage are fixed.
- Manually compare the regenerated owner against MediaDive 1310 and the DSMZ
  Medium 1310 PDF.

## Additional Notes

None found.
