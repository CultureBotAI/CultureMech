# YAML Record Review: Modified Baars Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_baars_medium__11a133e0.yaml
- Started UTC: 2026-09-24T10:16:34Z
- Finished UTC: 2026-09-24T10:16:34Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_baars_medium__11a133e0.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002336` |
| Name | `modified_baars_medium` |
| Original name | `MODIFIED BAAR'S MEDIUM` |
| Category | `bacterial` |
| Medium source | MediaDive / JCM `J1163` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_baars_medium.yaml` |
| Generated status | Generated merge output from one normalized MediaDive record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_baars_medium__11a133e0.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_baars_medium__11a133e0.yaml --out /private/tmp/modified_baars_medium__11a133e0.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_baars_medium__11a133e0.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_baars_medium__11a133e0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_baars_medium__11a133e0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:002336` and MediaDive / JCM `J1163` both identify MODIFIED BAAR'S MEDIUM.

An exact `find data/normalized_yaml -name 'modified_baars_medium.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/bacterial/modified_baars_medium.yaml` as the generated record's maintained owner.

Groundings for MgSO4 x 7 H2O, CaSO4, NH4Cl, ammonium nickel sulfate hexahydrate, and sodium lactate preserve the MediaDive ingredient identities. `Trisodium citrate x 2 H2O` is grounded to `CHEBI:53258` / `sodium citrate`, which does not preserve the dihydrate form.

## Evidence

MediaDive `J1163` supports the imported formula:

| Source claim | Record representation | Review |
| --- | --- | --- |
| The main solution is 1000 ml and contains 5 g trisodium citrate x 2 H2O, 2 g MgSO4 x 7 H2O, 1 g CaSO4, 1 g NH4Cl, 1 g yeast extract, 1 g ammonium nickel sulfate hexahydrate, 3.5 g sodium lactate, and 1000 ml distilled water. | The seven non-water rows are present with matching `G_PER_L` values; no distilled-water row is present. | Incomplete water import. |
| Final pH is 7.2. | `ph_value: 7.2` is present. | Supported. |
| Mix, adjust pH to 7.2, boil, cool, dispense under an N2 gas stream into Hungate tubes, seal with butyl rubber stoppers, and autoclave. | The same text is preserved as one `AUTOCLAVE` step. | Supported as prose; N2 is not structured as an atmosphere condition. |
| JCM `GRMD=1163` is the upstream source link retained by MediaDive. | The record still cites that JCM URL. | Historically plausible, but the live JCM URL now returns "Nothing found"; MediaDive preserves the formula. |

## Completeness

The generated record is mostly faithful to MediaDive `J1163`, including pH 7.2 and the Hungate-tube preparation text. The consequential source ingredient gap is the absent 1000 ml distilled-water row.

Empty target-organism and growth-evidence fields were not treated as defects. MediaDive `J1163` is a medium formulation page, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The 1000 ml distilled-water row is absent. | MediaDive `J1163` lists `Distilled water` at 1000 ml in `Main sol. J1163`; the YAML has no water row. | `data/normalized_yaml/bacterial/modified_baars_medium.yaml`; MediaDive water import. |
| major | `Trisodium citrate x 2 H2O` is grounded to an anhydrous/generic sodium citrate term. | MediaDive specifies the dihydrate form; the record links `CHEBI:53258` / `sodium citrate`. | `data/normalized_yaml/bacterial/modified_baars_medium.yaml`; compound grounding. |
| minor | The N2 gas stream is only represented in prose. | MediaDive says to dispense under an N2 gas stream; the generated record retains that sentence but has no structured atmosphere condition. | `data/normalized_yaml/bacterial/modified_baars_medium.yaml`; atmosphere curation. |
| minor | The original JCM URL no longer resolves to a formula. | The live `GRMD=1163` page returns `Nothing found`, although MediaDive still preserves the JCM-derived formula. | `data/normalized_yaml/bacterial/modified_baars_medium.yaml`; source provenance. |

## Recommended Edits

1. Add the 1000 ml distilled-water row from MediaDive `J1163` to `data/normalized_yaml/bacterial/modified_baars_medium.yaml`.
2. Re-ground `Trisodium citrate x 2 H2O` to the exact dihydrate form or leave it unresolved.
3. Structure the N2 gas stream as an atmosphere condition if the schema supports it while retaining the existing Hungate-tube preparation text.
4. Annotate the JCM source URL as currently unavailable if the repository has a pattern for stale source URLs.
5. Regenerate `data/merge_yaml/merged/modified_baars_medium__11a133e0.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_baars_medium.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against MediaDive `J1163`, checking all seven non-water ingredients, the 1000 ml distilled-water row, pH 7.2, and the N2 Hungate-tube preparation step.
3. Confirm that the JCM `GRMD=1163` unavailability is preserved as provenance rather than treated as evidence that the JCM accession was wrong.

## Additional Notes

The direct JCM `GRMD=1163` fetch returned a page with `Nothing found`; the search covered that exact URL from the record notes. MediaDive `J1163` remains the inspected source for the formula.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
