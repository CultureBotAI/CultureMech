# YAML Record Review: chopped_meat_medium_with_carbohydrates

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__f2dd06fe.yaml`
- Started UTC: 2026-09-22T08:45:57Z
- Finished UTC: 2026-09-22T08:48:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__f2dd06fe.yaml` |
| Stable ID | `CultureMech:003811` |
| Label | `chopped_meat_medium_with_carbohydrates` |
| Source term | `komodo.medium:110`, DSMZ Medium 110 |
| Canonical maintained owner | `data/normalized_yaml/bacterial/KOMODO_110_CHOPPED_MEAT_medium_WITH_CARBOHYDRATES.yaml` |
| Other source owner | `data/normalized_yaml/bacterial/chopped_meat_medium_with_carbohydrates.yaml` |
| Merge status | Generated from 24 source recipes with fingerprint `f2dd06fe5d4a13fbef7f4ef518e1785912f001bb68c8d7d417eaddc9148df426` |

Future fixes belong in the KOMODO and DSMZ normalized owners, the KOMODO
DSMZ-enrichment import that copied DSMZ Medium 110 into strain-specific KOMODO
children, and merge fingerprinting. The generated merge should not be edited
directly.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Pass; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__f2dd06fe.yaml` reported `No issues found`. |
| Strict schema | Pass; `scripts/validate_strict.py data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__f2dd06fe.yaml --out /private/tmp/chopped_meat_medium_with_carbohydrates__f2dd06fe.strict.tsv --workers 1 --quiet` scanned one file and emitted zero error rows. |
| Reference validation | Pass with no semantic coverage; `linkml-reference-validator validate data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__f2dd06fe.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported zero total checks because the record has no structured evidence references. |
| Term validation | Pass; `linkml-term-validator validate-data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__f2dd06fe.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed successfully, aside from the expected `eutils` `pkg_resources` deprecation warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries. |

`just` wrappers were not used because the project environment attempts to build
`llvmlite==0.46.0` under Python 3.13 and fails before the focused validators
can run. The checks above ran the same validator entry points in an offline
Python 3.11 `uv` environment.

## Identity and Grounding

The root identity is DSMZ/KOMODO Medium 110, Chopped Meat Medium With
Carbohydrates. `KOMODO_110_CHOPPED_MEAT_medium_WITH_CARBOHYDRATES.yaml` and
the direct DSMZ owner both point at DSMZ Medium 110, and the inspected DSMZ
Medium 110 PDF supplies the same basal chopped-meat carbohydrate recipe.

The generated 24-source merge is over-broad. Most merged KOMODO children are
named `medium_110_modified_for_dsm_*`, one child is explicitly named
`medium_110_modified_for_dsm_3376_replace_rumen_fluid_with_sludge_fluid`, and
one child is a KOMODO `To make medium anoxic` fragment. The current merge treats
all of those as `SOURCE_DUPLICATE` records solely because their imported
ingredient signatures were made identical.

## Evidence

Supported by the inspected DSMZ Medium 110 PDF:

- The basal recipe contains 500 g fat-free ground beef, 1000 ml distilled
  water, 25 ml of 1 N NaOH, 30 g Casitone, 5 g yeast extract, 5 g K2HPO4,
  0.5 ml Na-resazurin solution at 0.1% w/v, 4 g D-glucose, and 1 g each of
  cellobiose, maltose, and soluble starch.
- The recipe is made anoxic with 100% N2, 0.5 g/l L-cysteine hydrochloride,
  pH 7.0 adjustment, 7 ml Hungate-type tube portions dispensed under the same
  gas, and 121 C for 30 min autoclaving.
- Agar is only for agar slants.
- Haemin plus Vitamin K1 or Vitamin K3 is only required in some catalogue
  cases and is added after autoclaving as 10 ml Haemin solution plus 10 ml of
  one vitamin K stock.

Unsupported or under-scoped in the current record:

- Agar, Haemin, Vitamin K1, and Vitamin K3 are unconditional parent
  ingredients, even though DSMZ marks agar and the Haemin/vitamin K branch as
  conditional.
- The K1 and K3 branches have been blended together; DSMZ says `Vitamin K1 or
  Vitamin K3`, not both in the same completed medium.
- `NaOH` is `26.0 G_PER_L`, a merge of the basal 25 ml 1 N NaOH and the
  Haemin-stock 1 ml 1 N NaOH.
- `Ethanol` is `959.5 G_PER_L`, a merge of the K1 and K3 ethanol stock
  internals.
- The canonical KOMODO owner has no preparation steps; the direct DSMZ owner
  has free-text steps, but those steps describe optional stock recipes that are
  also flattened into the ingredient list.
- KOMODO entries whose labels denote strain modifications or a procedural
  anoxic fragment have been merged as exact source duplicates after DSMZ
  enrichment erased their distinguishing modifications.

## Completeness

The record is not complete enough to execute. It conflates the DSMZ 110 base,
the agar-slant option, the K1 stock branch, the K3 stock branch, and numerous
KOMODO strain-specific records into one formula. A curator cannot tell which
catalogue cases need Haemin/K1, which need Haemin/K3, or which strain-specific
records were supposed to alter the base medium.

An ignored-inclusive `rg --no-ignore --hidden` search over
`data/normalized_yaml/bacterial`, `data/merge_yaml/merged`, and relevant
review/import reports for exact KOMODO 110 owner names, `to_make_medium_anoxic`,
the sludge-fluid variant stem, and the `f2dd06fe5d4a13fbef7f4ef518e1785912f001bb68c8d7d417eaddc9148df426`
fingerprint found the 24 merged owners, the direct DSMZ owner, the generated
merge, import warnings for merged duplicate NaOH and ethanol, and variant-link
proposals that had already singled out the sludge-fluid record as a
substituted-component variant. Those hits are sufficient to identify the merge
as source-owned rather than generated-only.

Empty `target_organisms` and growth-evidence slots are acceptable for the
KOMODO/DSMZ base record. They are not enough for the modified-for-DSM child
records if those are retained as strain-specific variants.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record unconditionally blends optional DSMZ 110 branches. | DSMZ marks agar as an agar-slant option and says Haemin plus Vitamin K1 or Vitamin K3 is catalogue-dependent; this record includes agar, Haemin, K1, K3, and stock ethanol as if all were basal ingredients. | `KOMODO_110_CHOPPED_MEAT_medium_WITH_CARBOHYDRATES.yaml`, `chopped_meat_medium_with_carbohydrates.yaml`, and the KOMODO DSMZ-enrichment import. |
| Major | Stock internals are merged into final-medium ingredient amounts. | Import tracking flags `NaOH 26.0 G_PER_L` as `25.0;1.0` and `Ethanol 959.5 G_PER_L` as `950.0;9.5`; those sub-amounts come from different preparation scopes rather than one final-medium concentration. | Same normalized owners plus the cleanup rule that merged duplicate ingredient names without stock-scope awareness. |
| Major | The merge collapses modified KOMODO recipes into a source duplicate. | `medium_110_modified_for_dsm_3376_replace_rumen_fluid_with_sludge_fluid.yaml` still carries the sludge-substitution source ID, but its ingredient list is identical to the parent after DSMZ enrichment, and the generated record lists it as `SOURCE_DUPLICATE`. | `data/normalized_yaml/bacterial/medium_110_modified_for_dsm_3376_replace_rumen_fluid_with_sludge_fluid.yaml` and sibling `medium_110_modified_for_dsm_*.yaml` files, plus the enrichment step that copied parent DSMZ 110 over their deltas. |
| Major | The `to_make_medium_anoxic` KOMODO fragment is modeled as a complete source duplicate. | `data/normalized_yaml/bacterial/to_make_medium_anoxic.yaml` has original name `To make medium anoxic`, `komodo.medium:110.1`, and `Aerobic: Yes`, but after enrichment it has the full DSMZ 110 ingredient list and is merged with the base medium. | `data/normalized_yaml/bacterial/to_make_medium_anoxic.yaml` and KOMODO import/enrichment logic. |
| Major | The canonical KOMODO owner lacks DSMZ preparation steps. | The direct DSMZ owner has six preparation steps; the KOMODO owner selected as canonical has none, so the generated recipe loses meat infusion, anoxic handling, pH adjustment, post-autoclave stock timing, and stock sterilization. | `data/normalized_yaml/bacterial/KOMODO_110_CHOPPED_MEAT_medium_WITH_CARBOHYDRATES.yaml` and merge field-selection rules. |

## Recommended Edits

1. Restore a source-faithful DSMZ Medium 110 base in
   `data/normalized_yaml/bacterial/chopped_meat_medium_with_carbohydrates.yaml`:
   keep agar, Haemin/K1, and Haemin/K3 as optional or child branches instead
   of unconditional parent ingredients.
2. Apply the same stock-scope corrections to
   `data/normalized_yaml/bacterial/KOMODO_110_CHOPPED_MEAT_medium_WITH_CARBOHYDRATES.yaml`
   or stop copying flattened DSMZ ingredients into the KOMODO parent if the
   direct DSMZ owner should be authoritative.
3. Rebuild Haemin, Vitamin K1, and Vitamin K3 as distinct stock solutions and
   remove their NaOH, water, ethanol, haemin, and vitamin internals from the
   parent ingredient list.
4. Audit every `medium_110_modified_for_dsm_*.yaml` owner that merged into this
   record against the corresponding KOMODO source. Preserve real DSM-specific
   substitutions, supplements, and condition changes before re-running merge
   fingerprinting.
5. Demote `to_make_medium_anoxic.yaml` from a complete `MediaRecipe` if it is a
   preparation fragment rather than an independent medium.
6. Re-run the merge pipeline so KOMODO 110, direct DSMZ 110, K1/K3 branches,
   agar slant variants, and DSM-specific modifications no longer collapse into
   a single generated formula.

## Follow-up Checks

- Run focused open-schema, strict, reference, and term validation on each
  corrected DSMZ 110 normalized owner and on any stock records introduced.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merged YAML.
- Re-read the regenerated generated records and verify that base DSMZ 110,
  Haemin/K1, Haemin/K3, `to_make_medium_anoxic`, and the
  `medium_110_modified_for_dsm_*` records have the expected distinct
  fingerprints.
- Compare `reports/media_variant_link_proposals.tsv` after regeneration; the
  sludge-fluid record should no longer be proposed as a source duplicate if
  its substitution is restored.

## Additional Notes

- `reports/media_content_review_manifest.tsv` marked the KOMODO 110 and direct
  DSMZ 110 owners as `PASS` because their ingredient/concentration signatures
  were dense, which illustrates why source-scope review is required here.
- The stale `reports/label_plausibility_2026-07-19.tsv` report records an old
  implausible `CHEBI:52891` grounding for `L-Cysteine HCl`; the current merged
  record now carries `CHEBI:91247`, so that exact warning has already been
  repaired.
