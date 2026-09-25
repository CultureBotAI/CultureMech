# YAML Record Review: modified_yma_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_yma_medium.yaml
- Started UTC: 2026-09-24T13:50:22Z
- Finished UTC: 2026-09-24T13:50:58Z
- Verdict: needs curation

## Target

Reviewed merged generated record `CultureMech:004097`, `modified_yma_medium`, a KOMODO-centered merge of `KOMODO_1334_MODIFIED_YMA_medium`, DSMZ `modified_yma_medium`, and DSMZ `modified_yma_medium_hambi`.

## Validation

The generated record passed the focused open schema validator, which reported `No issues found`.

Strict validation passed with 0 errors. The TSV output contained only its header row.

Reference validation passed. The checker executed 0 reference checks for this record.

Term validation passed. The validator emitted the known `eutils` / `pkg_resources` warning before reporting success.

Embedded `curation_history` entries were not checked: `just validate-history` validates standalone `history/` content, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The KOMODO branch is grounded to `komodo.medium:1334` and explicitly notes DSMZ Medium 1334 as `mediadive.medium:1334`; its ingredient set matches the normalized DSMZ 1334 owner.

The DSMZ 1545 HAMBI branch is not a source duplicate of DSMZ 1334. MediaDive 1545 is named `MODIFIED YMA MEDIUM (HAMBI)` and has different mannitol, yeast extract, K2HPO4 hydrate, and agar quantities. The generated `synonyms` entry for `modified_yma_medium_hambi` therefore masks a formulation variant as a name synonym.

The generated `parent_media` assertion that KOMODO 1334 is a duplicate of DSMZ 1334 is supported by the local ingredients and by the KOMODO note that cites DSMZ Medium 1334.

## Evidence

The live MediaDive REST response for medium 1334 names the medium `MODIFIED YMA MEDIUM`, gives pH 7.0, and lists Yeast extract 0.5 g/L, Mannitol 7 g/L, K2HPO4 0.2 g/L, MgSO4 x 7 H2O 0.2 g/L, and Agar 15 g/L with the condition `for solid medium`. Its preparation step says to adjust pH to 7.0 and that the medium may be solidified by adding 15 g/L agar.

`data/normalized_yaml/bacterial/modified_yma_medium.yaml` carries the same DSMZ 1334 formula, with `CultureMech:000791` and `mediadive.medium:1334`.

`data/normalized_yaml/bacterial/KOMODO_1334_MODIFIED_YMA_medium.yaml` carries the same formula under `CultureMech:004097` and `komodo.medium:1334`, with a note that the KOMODO source cites DSMZ Medium 1334.

The live MediaDive REST response for medium 1545 names the medium `MODIFIED YMA MEDIUM (HAMBI)`, gives pH 7.0, and lists K2HPO4 x 3 H2O 0.6 g/L, MgSO4 x 7 H2O 0.2 g/L, Mannitol 10 g/L, Yeast extract 2.5 g/L, and Agar 20 g/L. The normalized HAMBI owner preserves those values under `CultureMech:001023` and `mediadive.medium:1545`.

## Completeness

The generated formula is complete for DSMZ Medium 1334 but incomplete for the merged source set because no DSMZ 1545 HAMBI concentrations survive in structured ingredients.

The generated recipe carries `Agar` as a fixed 15 g/L ingredient and `physical_state: SOLID_AGAR`. That is sufficient for a solid DSMZ 1334 variant but not for the base MODIFIED YMA medium, whose MediaDive step says agar may be added for solid medium.

## Findings

1. `modified_yma_medium_hambi` was merged as a source duplicate even though DSMZ 1545 is a different HAMBI formulation. Mannitol is 10 g/L instead of 7 g/L, yeast extract is 2.5 g/L instead of 0.5 g/L, the K2HPO4 source term and concentration differ, and agar is 20 g/L instead of conditionally 15 g/L.

2. The generated `synonyms` entry reduces DSMZ 1545 to a display synonym of the KOMODO/DSMZ 1334 record, so consumers cannot recover the HAMBI-specific formula from the merged artifact.

3. `Agar` is modeled as mandatory and the merged record is typed as `SOLID_AGAR`, although the DSMZ 1334 source only adds 15 g/L agar for solid medium.

4. The embedded KOMODO import history includes malformed timestamp `2026-01-27T01:15:02.fZ`; current MediaRecipe validation does not catch that nested history timestamp.

## Recommended Edits

Split DSMZ Medium 1545 / `modified_yma_medium_hambi` back out as a distinct variant record instead of merging it into `modified_yma_medium`.

Keep KOMODO Medium 1334 and DSMZ Medium 1334 linked as exact source duplicates, because KOMODO explicitly cites DSMZ Medium 1334 and the local formula matches.

Represent the DSMZ 1334 agar row as conditional or create separate liquid and solid variants so the base medium is not forced to `SOLID_AGAR`.

Repair the malformed KOMODO `curation_history.timestamp` at its normalized owner so future embedded-history validation will not fail.

## Follow-up Checks

After editing the normalized owners or merge relationship logic, regenerate the merged YAML and rerun open schema, strict, reference, and term validation for `modified_yma_medium` and the restored HAMBI variant.

Recompare the regenerated records against live MediaDive medium 1334 and 1545 and verify that 1334 keeps 7 g/L mannitol and optional 15 g/L agar while 1545 keeps 10 g/L mannitol and 20 g/L agar.

Check other merge groups where only the base name matches but the source name contains a parenthesized strain collection or provider suffix, such as `HAMBI`, because these are likely variants rather than synonyms.

## Additional Notes

An exact, ignored-file-inclusive search for `mediadive.medium:1334`, `mediadive.medium:1545`, `komodo.medium:1334`, and `modified_yma_medium_hambi` under `data/normalized_yaml` and `data/merge_yaml/merged` found the two MediaDive owners, the KOMODO owner, and this merged generated record.
