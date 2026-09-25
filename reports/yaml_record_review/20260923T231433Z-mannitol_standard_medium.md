# YAML Record Review: mannitol_standard_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mannitol_standard_medium.yaml
- Started UTC: 2026-09-23T23:14:33Z
- Finished UTC: 2026-09-23T23:14:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009387 |
| name | mannitol_standard_medium |
| original_name | mannitol standard medium |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | TOGO:M2845, mannitol standard medium |
| generated path | data/merge_yaml/merged/mannitol_standard_medium.yaml |
| maintained owner | data/normalized_yaml/bacterial/mannitol_standard_medium.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the single normalized owner `mannitol_standard_medium`, and the terminal curation event reports an August 2026 merge on fingerprint `baefb53daf609077a1fecaa3de8ec9aa59f93f15545e2430c50029e425b897e2`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009387`, `TOGO:M2845`, `M2845`, and `mannitol standard medium` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or TOGO identifier.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mannitol_standard_medium.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/mannitol_standard_medium.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The record identity agrees with TOGO M2845 at the medium level: the TOGO accession and source name both point to `mannitol standard medium`.

TOGO M2845 supports:

| Ingredient | TOGO amount |
|---|---:|
| Distilled water | 1 L |
| yeast extract | 5 g/L |
| mannitol | 50 mM |
| peptone | 3 g/L |
| Hydrochloric acid | variable, to adjust pH |

The yeast extract, mannitol, peptone, and hydrochloric-acid rows are present at source-supported amounts or, for HCl, as a variable pH-adjustment reagent. Mannitol is grounded to CHEBI:29864, matching the TOGO component name. Distilled water is grounded to CHEBI:15377, but its source volume is represented with the wrong unit.

## Evidence

The generated record correctly preserves the 5 G_PER_L yeast extract, 50 MILLIMOLAR mannitol, 3 G_PER_L peptone, and a variable hydrochloric-acid adjustment from the inspected TOGO response.

Two material source details are missing or mistranscribed:

- TOGO M2845 lists `Distilled water` as `volume: 1`, `unit: L`; the record stores `1 G_PER_L`.
- TOGO M2845 has metadata `ph: 6.0`, and its source comment says the mannitol standard medium was at pH 6. The record has no structured pH.

The TOGO source comment also mentions Gluconobacter oxydans ATCC 621H and DSM 3504 growth at 30 C and 180 rpm. That is a lead for a later growth-evidence pass; it should not be generalized into a universal medium condition without the underlying source.

## Completeness

Missing or incomplete:

- Distilled water needs a volume unit, not `G_PER_L`.
- The source pH 6.0 is absent.

Complete enough:

- Hydrochloric acid has no fixed amount in TOGO because it is used only to adjust pH.
- No stock-solution references are required.
- No physical-state correction is needed; TOGO M2845 is a liquid medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source water volume was converted to a mass concentration. | TOGO M2845 lists 1 L distilled water; the generated record stores `Distilled water` as `value: '1'`, `unit: G_PER_L`. | data/normalized_yaml/bacterial/mannitol_standard_medium.yaml; if other TOGO imports repeat this pattern, the TOGO unit-normalization code should be fixed before regenerating them |
| major | The TOGO-supported pH is missing. | TOGO M2845 reports `ph: 6.0` and repeats pH 6 in its source comment, but neither the normalized owner nor the generated copy has a pH field. | data/normalized_yaml/bacterial/mannitol_standard_medium.yaml |

## Recommended Edits

1. Change the distilled-water row in `data/normalized_yaml/bacterial/mannitol_standard_medium.yaml` from `1 G_PER_L` to a schema-supported one-liter volume basis, for example `1000 ML_PER_L`.
2. Add the TOGO-supported pH 6.0 to the normalized owner.
3. Optionally inspect the underlying growth source before structuring Gluconobacter oxydans ATCC 621H or DSM 3504 target-organism evidence from the 30 C, 180 rpm TOGO comment.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the normalized owner and regenerated merged record.
- Regenerate `data/merge_yaml/merged/mannitol_standard_medium.yaml` and run the focused merge-freshness check or `just verify-merges`.
- Re-fetch TOGO M2845 and confirm the regenerated record keeps yeast extract, mannitol, peptone, and HCl unchanged while fixing only water units and pH.

## Additional Notes

None found.
