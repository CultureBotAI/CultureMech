# YAML Record Review: Bacto Marine Broth (Difco 2216)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacto_marine_broth_difco_2216.yaml
- Started UTC: 2026-09-21T18:21:59Z
- Finished UTC: 2026-09-21T18:21:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008923 |
| Name | bacto_marine_broth_difco_2216 |
| Original name | Bacto Marine Broth (Difco 2216) |
| Maintained canonical input | data/normalized_yaml/bacterial/TOGO_M2336_Bacto_Marine_Broth_Difco_2216.yaml |
| Merge participant | data/normalized_yaml/bacterial/TOGO_M2608_Bacto_Marine_Broth_Difco_2216.yaml |
| Source IDs | TOGO:M2336; TOGO:M2608 |
| Primary checked sources | TOGO API payloads for M2336 and M2608; DSMZ Medium 514 PDF |
| Generated status | Generated merge under data/merge_yaml/merged; future fixes belong in normalized inputs or the TOGO importer |

The generated record is a merge of two TOGO records named `Bacto Marine Broth (Difco 2216)`, both ultimately pointing to DSMZ Medium 514.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacto_marine_broth_difco_2216.yaml` | Passed with exit 0 |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bacto_marine_broth_difco_2216.yaml --out /private/tmp/bacto_marine_broth_difco_2216.strict.tsv --workers 1 --quiet` | Passed with exit 0 |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bacto_marine_broth_difco_2216.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bacto_marine_broth_difco_2216.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented; `just validate-history` targets standalone `history/` files. |

The repository `just` validators were not used for this target because the project environment currently fails while syncing the Python 3.13 dependency set. The equivalent no-project validators above ran against the checked-in schema and target file.

## Identity and Grounding

The source identity is clear: both TOGO payloads are for Bacto Marine Broth (Difco 2216) and cite DSMZ Medium 514. The duplicate merge between TOGO:M2336 and TOGO:M2608 is therefore reasonable.

Several ingredients no longer match their source quantities:

- DSMZ 514 and both TOGO payloads list H3BO3, Na2HPO4, `(NH4)NO3`, NaF, SrCl2, and Na-silicate in milligrams. The maintained TOGO YAML copied those numeric values to `G_PER_L` without converting by 1000.
- Distilled water is 1000 ml in TOGO and DSMZ, but the YAML row is `1000` `G_PER_L`.

Grounding is also incomplete in source rows that have exact local mappings:

- `Bacto yeast extract` is ungrounded despite an exact packaged mapping to `FOODON:03315426`.
- `Bacto peptone` is ungrounded despite an exact packaged mapping to `MICRO:0000178`.
- `Fe(III) citrate` has an exact packaged CHEBI mapping but still uses the legacy `mediaingredientmech_term` slot rather than `mediaingredientmech_chebi_term`.

`MgCl2 (anhydrous)` remains ungrounded. The exact ignored-inclusive label-index search used for this review found exact rows for the two Bacto nutrients and Fe(III) citrate, but no exact `MgCl2 (anhydrous)` row.

## Evidence

DSMZ Medium 514 supports 5 g Bacto peptone, 1 g Bacto yeast extract, 0.10 g Fe(III) citrate, 19.45 g NaCl, 5.90 g anhydrous MgCl2, 3.24 g Na2SO4, 1.80 g CaCl2, 0.55 g KCl, 0.16 g NaHCO3, 0.08 g KBr, and 1000 ml distilled water.

DSMZ and the TOGO API payloads support the trace salts only as milligram quantities: 34 mg SrCl2, 22 mg H3BO3, 4 mg Na-silicate, 2.4 mg NaF, 1.6 mg `(NH4)NO3`, and 8 mg Na2HPO4. The current generated record inflates these to 34, 22, 4, 2.4, 1.6, and 8 g/L respectively.

TOGO:M2336 carries the final pH as a range of `7.4 -7.8`; TOGO:M2608 carries it as `7.6 +/- 0.2`. Both point to the DSMZ statement that final pH should be 7.6 +/- 0.2 at 25 C. The generated record has no `ph_value` and no preparation note retaining the pH or temperature context.

## Completeness

- Final pH 7.6 +/- 0.2 at 25 C is absent from the generated record.
- The source note that complete Difco Marine Broth 2216 may be used at 37.40 g/L is absent. That is an alternate commercial preparation rather than a replacement for the expanded ingredient list, but it is useful source context for this named Difco formulation.
- M2608 has an additional TOGO comment about a synthetic-seawater agar variant and an alternative to medium 514; the generated record merges only the DSMZ 514 formulation, so that comment does not justify an ingredient change in this target.
- Empty organism, strain, and growth-evidence fields are not automatically defects because the inspected source is a medium protocol, not a growth study.

A gitignore-independent search of `reports/yaml_record_review` for `bacto_marine_broth_difco_2216|Bacto_Marine_Broth_Difco_2216|BACTO_MARINE_BROTH_DIFCO_2216` found no existing report for this target before this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Six milligram-scale trace salts were imported as grams per liter. | DSMZ 514 and both TOGO payloads list H3BO3, Na2HPO4, `(NH4)NO3`, NaF, SrCl2, and Na-silicate in mg, but both maintained TOGO inputs and the generated merge keep the raw numeric values with `unit: G_PER_L`. | TOGO import unit normalization for `data/normalized_yaml/bacterial/TOGO_M2336_Bacto_Marine_Broth_Difco_2216.yaml` and `data/normalized_yaml/bacterial/TOGO_M2608_Bacto_Marine_Broth_Difco_2216.yaml` |
| Major | The distilled-water unit is wrong. | TOGO and DSMZ specify 1000 ml; the YAML represents this as 1000 g/L. | TOGO import unit normalization |
| Major | Final pH and temperature context are missing. | Both TOGO records expose pH metadata equivalent to DSMZ's final pH 7.6 +/- 0.2 at 25 C; the generated record has no `ph_value` or preparation step for it. | TOGO import of `meta.ph` and DSMZ comments |
| Major | Bacto yeast extract and Bacto peptone are missing exact available groundings. | The packaged label index maps `Bacto yeast extract` to `FOODON:03315426` and `Bacto peptone` to `MICRO:0000178`; both generated rows are ungrounded. | Ingredient grounding in both TOGO normalized inputs, using the packaged label index |
| Minor | Fe(III) citrate still uses the legacy MIM slot. | The ingredient already has `term.id: CHEBI:144421`, and the packaged label index has an exact CHEBI-keyed Fe(III) citrate row, but the record still stores `mediaingredientmech_term: MediaIngredientMech:000186`. | Legacy-to-CHEBI MIM migration or targeted ingredient link refresh |

## Recommended Edits

1. Convert the six TOGO milligram ingredients to grams per liter: SrCl2 0.034, H3BO3 0.022, Na-silicate 0.004, NaF 0.0024, `(NH4)NO3` 0.0016, and Na2HPO4 0.008 g/L.
2. Preserve distilled water as 1000 ml/L, not 1000 g/L.
3. Import the DSMZ/TOGO final pH as pH 7.6 with the +/- 0.2 at 25 C tolerance retained in a preparation note or discussion field that does not overstate precision.
4. Link `Bacto yeast extract` and `Bacto peptone` to their exact packaged label-index terms.
5. Refresh the Fe(III) citrate MIM link to `mediaingredientmech_chebi_term` keyed by `CHEBI:144421`.
6. Regenerate `data/merge_yaml/merged/bacto_marine_broth_difco_2216.yaml` and generated pages from the corrected normalized TOGO inputs.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators on both edited TOGO inputs and on the regenerated merge.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regeneration to prove TOGO:M2336 and TOGO:M2608 still collapse to one canonical record.
- Manually compare the regenerated amounts against both TOGO API payloads to confirm every `mg` source amount was divided by 1000 exactly once.
- Inspect the regenerated merge to confirm the Bacto nutrients are grounded and Fe(III) citrate no longer has a stale `mediaingredientmech_term`.

## Additional Notes

- The two maintained TOGO inputs are identical for the inspected formulation fields; the generated merge is not the source of the unit error.
- DSMZ 514 also describes a Na2S2O3 x 5 H2O post-autoclave supplement for DSM 11879 and DSM 16960. That is a strain-specific variant and belongs in a separate variant record, not in this base Bacto Marine Broth record.
- The exact searches used to assert no prior report and no exact local `MgCl2 (anhydrous)` label-index mapping included ignored files.
