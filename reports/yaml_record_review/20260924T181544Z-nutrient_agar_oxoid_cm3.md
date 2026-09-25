# YAML Record Review: nutrient_agar_oxoid_cm3

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/nutrient_agar_oxoid_cm3.yaml
- Started UTC: 2026-09-24T18:14:19Z
- Finished UTC: 2026-09-24T18:15:44Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:001732 |
| Name | nutrient_agar_oxoid_cm3 |
| Original name | NUTRIENT AGAR (OXOID CM3) |
| Category | bacterial |
| Media term | mediadive.medium:605 / NUTRIENT AGAR (OXOID CM3) |
| Generated path | data/merge_yaml/merged/nutrient_agar_oxoid_cm3.yaml |
| Maintained source | data/normalized_yaml/bacterial/nutrient_agar_oxoid_cm3.yaml |
| Merge fingerprint | 34b02165361f625f01ac3e2a29707666fd4cef83561d327103c44925d1d9dd2a |
| Merged from | nutrient_agar_oxoid_cm3 |

This is a generated singleton for DSMZ Medium 605. The core non-water formula is correct, but the generated file predates the repaired maintained source and the KOMODO 605 mirror is misassigned to the DSMZ 605a phosphate branch.

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/nutrient_agar_oxoid_cm3.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validation with `scripts/validate_strict.py data/merge_yaml/merged/nutrient_agar_oxoid_cm3.yaml --out /private/tmp/nutrient_agar_oxoid_cm3.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header line. |
| Reference validation with `linkml-reference-validator validate data data/merge_yaml/merged/nutrient_agar_oxoid_cm3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 total checks and no failures. |
| Term validation with `linkml-term-validator validate-data data/merge_yaml/merged/nutrient_agar_oxoid_cm3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator validates standalone `history/` entries, not embedded generated `MediaRecipe.curation_history`. |

## Identity and Grounding

The generated record denotes DSMZ Medium 605, `NUTRIENT AGAR (OXOID CM3)`. Its label, bacterial category, complex solid-agar classification, and five non-water ingredient rows agree with the DSMZ 605 PDF and the MediaDive 605 REST payload.

An ignored-file-inclusive PCRE2 search for exact `mediadive.medium:605`, `komodo.medium:605`, `KOMODO_605_NUTRIENT_AGAR_OXOID_CM3`, `DSMZ Medium 605`, `NUTRIENT AGAR (OXOID CM3)`, and `nutrient_agar_oxoid_cm3` across `data/normalized_yaml` and `data/merge_yaml/merged` found the repaired direct DSMZ 605 source, the generated DSMZ 605 singleton, a KOMODO 605 normalized source, and DSMZ 605a phosphate-variant records. The KOMODO 605 normalized source is not a valid direct duplicate of this record because it already contains the KH2PO4 and Na2HPO4 x 12 H2O additions and pH 6.8 associated with DSMZ Medium 605a.

## Evidence

DSMZ Medium 605 lists Lab-Lemco beef extract 1.0 g, Yeast extract 2.0 g, Peptone 5.0 g, NaCl 5.0 g, Agar 15.0 g, and Distilled water 1000.0 ml. The generated record preserves the five non-water ingredient amounts exactly.

The maintained `data/normalized_yaml/bacterial/nutrient_agar_oxoid_cm3.yaml` has already been repaired to include the 1.0 L Distilled water row, direct source notes on each ingredient, a DSMZ reference, and a supplemented-variant link to DSMZ Medium 605a. The generated record is still a pre-repair singleton without those fields.

## Completeness

The formula is nearly complete: the only ingredient from DSMZ 605 missing in the generated record is 1000 ml Distilled water. The generated record also lacks the repaired provenance, references, and variant link to `nutrient_agar_oxoid_cm3_with_phosphate`.

Empty target-organism and citation slots are acceptable for this DSMZ provider formula. DSMZ Medium 605 does not name a strain-specific target organism.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The generated DSMZ 605 singleton is stale relative to its repaired maintained source. | The maintained source now includes 1.0 L Distilled water, DSMZ references, ingredient source notes, data-quality flags, and a `SUPPLEMENTED_VARIANT` link to DSMZ 605a; the generated record has only the old non-water MediaDive import rows. | Regenerate `data/merge_yaml/merged` from `data/normalized_yaml/bacterial/nutrient_agar_oxoid_cm3.yaml`. |
| Major | KOMODO `605` is mapped to the DSMZ 605a phosphate formula instead of DSMZ 605. | `data/normalized_yaml/bacterial/KOMODO_605_NUTRIENT_AGAR_OXOID_CM3.yaml` uses `komodo.medium:605` and label `NUTRIENT AGAR (OXOID CM3)` but contains KH2PO4, Na2HPO4 x 12 H2O, and pH 6.8; those phosphate additions belong to DSMZ 605a, not the inspected DSMZ 605 PDF. | KOMODO/DSMZ resolver for KOMODO 605 and 605a, then merge regeneration. |

## Recommended Edits

1. Regenerate the DSMZ 605 generated record so it carries the 1.0 L water row, DSMZ reference, repaired ingredient provenance, and the 605a supplemented-variant relationship from the maintained source.
2. Audit KOMODO 605 and KOMODO 605a source resolution so the unsuffixed KOMODO 605 record does not masquerade as the DSMZ 605a phosphate formulation.

## Follow-up Checks

1. Run the focused open schema, strict, reference, and term validators on the regenerated DSMZ 605 record.
2. Search with ignored files included for exact `mediadive.medium:605`, `komodo.medium:605`, and `DSMZ Medium 605` to confirm direct DSMZ 605 and KOMODO 605 records are either correctly merged or deliberately separated with a documented variant relationship.

## Additional Notes

DSMZ Medium 605a is correctly a phosphate-supplemented variant of DSMZ 605. The issue is the local KOMODO 605 record carrying the 605a ingredient signature while retaining the 605 identifier and label.
