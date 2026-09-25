# YAML Record Review: BEIJERINCKIA MEDIUM (LMG 18)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/beijerinckia_medium_lmg_18.yaml
- Started UTC: 2026-09-21T19:44:10Z
- Finished UTC: 2026-09-21T19:46:12Z
- Verdict: needs curation

## Target

- Reviewed `data/merge_yaml/merged/beijerinckia_medium_lmg_18.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:001213`.
- Name: `beijerinckia_medium_lmg_18`.
- Original name: `BEIJERINCKIA MEDIUM (LMG 18)`.
- Source identity: `mediadive.medium:1736`, label `BEIJERINCKIA MEDIUM (LMG 18)`, source DSMZ.
- Generated status: derived merge output under `data/merge_yaml/merged/`; the maintained owner is `data/normalized_yaml/bacterial/beijerinckia_medium_lmg_18.yaml`.
- Merge metadata: one source record, `beijerinckia_medium_lmg_18`, on fingerprint `bcb39bb41beb6fe95a71e4bc4a8a68032ecce54c0e4bafaea737561fefe48ba3`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/beijerinckia_medium_lmg_18.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/beijerinckia_medium_lmg_18.yaml --out /private/tmp/beijerinckia_medium_lmg_18.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/beijerinckia_medium_lmg_18.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Failed: 2 errors, both `No content available for reference: doi:10.1007/BF01999703` at the target-organism and variant evidence snippets |
| `linkml-term-validator validate-data data/merge_yaml/merged/beijerinckia_medium_lmg_18.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:001213` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/beijerinckia_medium_lmg_18.yaml`.
- MediaDive JSON, the rendered MediaDive page, and the linked DSMZ PDF all identify DSMZ Medium 1736 as `BEIJERINCKIA MEDIUM (LMG 18)`, source DSMZ, pH 6.5.
- The DSMZ 1736 base formulation is distinct from DSMZ 111 `BEIJERINCKIA MEDIUM`, DSMZ 1847 `Beijerinckia medium for isolation`, and the Becking pH-5 medium described in the record's added variant.
- The source-supported hydrate and salt groundings for the DSMZ 1736 ingredients are exact.

## Evidence

- MediaDive 1736 and the DSMZ PDF support the 10 non-water ingredient rows in the current record: 10 g glucose, 0.8 g K2HPO4, 0.2 g KH2PO4, 0.1 g magnesium sulfate heptahydrate, 0.02 g ferrous sulfate heptahydrate, 1.3 mg manganese sulfate monohydrate, 5 mg zinc sulfate heptahydrate, 4 mg copper sulfate pentahydrate, 5 mg sodium molybdate dihydrate, and 15 g agar per 1000 ml.
- MediaDive 1736 and the DSMZ PDF support final pH 6.5.
- MediaDive 1736 and the DSMZ PDF list 1000 ml distilled water, which the current generated record omits.
- The DOI in the `target_organisms` and `variants` evidence resolves to the Brierley and Thornton 1979 paper about nitrogen-fixing bacteria in British soils, but Springer exposes only a paywalled preview. The accessible abstract mentions laboratory-culture testing of `Beijerinckia lactogenes`; it does not expose the record's claims about `Beijerinckia lactocogenes` NTCC 38849, omission of CaCO3, pH 5, or the exact Becking-medium variant.
- The two stored DOI snippets are not exact snippets from any inspected source. They are semicolon-joined summaries also present in `data/import_tracking/reports/top5-curation-proposals.json`.
- A gitignore-independent search over `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` for the exact CultureMech ID, digit-bounded `mediadive.medium:1736`, digit-bounded `DSMZ Medium 1736`, the LMG 18 slug and label, DOI `10.1007/BF01999703`, `becking_medium_ph5_no_caco3`, `Beijerinckia lactocogenes`, and `NTCC 38849` found only the normalized owner, generated merge, generated indexes, import-tracking proposals, and researched-media markers. It did not find a repository-owned raw MediaDive or Brierley paper capture for this record.

## Completeness

- Consequentially incomplete: the DSMZ 1736 1000 ml distilled-water row is absent from machine-readable composition.
- Consequentially over-scoped: the target-organism and variant block describes growth on a pH-5, CaCO3-free Becking-medium variant with different base amounts from DSMZ 1736; the inspected sources do not support treating it as a variant of `BEIJERINCKIA MEDIUM (LMG 18)`.
- The `organism_culture_type: isolate` value is consistent with the single strain currently asserted, but the strain assertion itself still needs direct paper support.
- No storage, application beyond microbial cultivation, or additional DSMZ variant is expected from the inspected DSMZ 1736 recipe.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | Both DOI evidence snippets fail focused reference validation and are not exact substrings of inspected article text. The accessible DOI page does not verify `Beijerinckia lactocogenes` NTCC 38849, pH 5, or omitted CaCO3. | `data/normalized_yaml/bacterial/beijerinckia_medium_lmg_18.yaml` |
| Major | The pH-5 no-CaCO3 Becking variant has different base-medium amounts from DSMZ 1736 and is not supported as a variant of `BEIJERINCKIA MEDIUM (LMG 18)`. | `data/normalized_yaml/bacterial/beijerinckia_medium_lmg_18.yaml` |
| Major | The 1000 ml distilled-water row from DSMZ Medium 1736 is missing. | `data/normalized_yaml/bacterial/beijerinckia_medium_lmg_18.yaml` |

## Recommended Edits

1. Remove the Brierley `target_organisms` and `variants` block from DSMZ 1736 unless the full Brierley and Thornton paper can be inspected and shown to support this exact parent-medium relationship.
2. If the pH-5 no-CaCO3 Becking formulation is useful, curate it as its own source-supported recipe or attach it to the correct Becking parent medium, not to DSMZ 1736 by implication.
3. Add the DSMZ 1736 1000 ml distilled-water row to the normalized owner.
4. Regenerate `data/merge_yaml/merged/beijerinckia_medium_lmg_18.yaml` after the normalized owner is corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on the normalized owner and the regenerated merged record.
- Manually compare the regenerated base formulation against the DSMZ Medium 1736 PDF or MediaDive 1736 JSON and verify that 1000 ml distilled water and final pH 6.5 are present.
- Rerun the focused reference validator after any DOI evidence is edited; it should have zero snippet errors before the evidence is retained.

## Additional Notes

- MediaDive JSON, the MediaDive rendered page, and the DSMZ PDF agreed for every inspected DSMZ 1736 ingredient, amount, pH value, and preparation step.
- The DOI landing page was sufficient to verify the Brierley and Thornton article identity, but not the exact organism, strain, medium, or snippet text in the current record.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.
