# YAML Record Review: Artificial Seawater Yeast Extract-Tryptone Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium.yaml`
- Started UTC: 2026-09-21T15:27:29Z
- Finished UTC: 2026-09-21T15:27:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007903` |
| Name | `artificial_seawater_yeast_extract_tryptone_medium` |
| Original name | Artificial Seawater Yeast Extract-Tryptone Medium |
| Category | `bacterial` |
| Source identity | `TOGO:M1365`, JCM `JCM_M1269` |
| Generated status | Generated single-source merge of `data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml` |

This review covers the bacterial TOGO-derived record. The fungal MediaDive/JCM
record with the same basename,
`data/normalized_yaml/fungal/artificial_seawater_yeast_extract_tryptone_medium.yaml`,
has a different ID and should be reviewed as a separate target.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium.yaml --out /private/tmp/artificial_seawater_yeast_extract_tryptone_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone records under `history/`. |

The documented `just` validators were bypassed because project `uv` attempts to
build `llvmlite==0.46.0` under Python 3.13 and exits before running the
requested focused check. The no-project commands above ran the validator
families needed for this one generated record.

## Identity and Grounding

The record identifies TOGO `M1365`, JCM `M1269`, and the label "Artificial
Seawater Yeast Extract-Tryptone Medium" consistently. The live JCM
`GRMD=1269` URL was fetchable but returned a "Nothing found" page, so the source
formulation was checked against TOGO's structured `gmdb_medium_by_gmid` payload.

Ingredient grounding is adequate for the direct main ingredients and artificial
seawater salts, except that `Artificial seawater (4x, see below)` is ungrounded
because it is really a nested 4x stock solution, not an atomic ingredient.
`N2` is grounded as dinitrogen, but the source uses nitrogen as the vessel
atmosphere for distribution and autoclaving, not as a variable-concentration
medium ingredient.

## Evidence

TOGO M1365 has two sections:

- a final main solution with 800 ml distilled water, 2 g yeast extract, 2 g
  tryptone, 200 ml artificial seawater 4x, and N2 atmosphere; and
- the 4x artificial seawater stock, prepared from 1 L water plus MgSO4.7H2O,
  NaCl, CaCl2.2H2O, K2HPO4, MgCl2.6H2O, KCl, NaHCO3, ammonium sulfate, NaBr,
  SrCl2.6H2O, and ammonium Fe(III) citrate.

The CultureMech record does not preserve that boundary. It lists
`Artificial seawater (4x, see below)` as a `200 G_PER_L` ingredient, lists the
4x-stock salts as direct ingredients at their undiluted stock grams per liter,
and merges the final 800 ml water with the stock 1 L water into
`801.0 G_PER_L`.

TOGO also reports final pH 7.0 and instructs distribution under an N2 gas
atmosphere, sealing with butyl rubber stoppers, and autoclaving. None of that
preparation detail appears in the generated record.

## Completeness

Material gaps:

- no nested representation for the 4x artificial seawater stock;
- no final 200 ml stock addition with a volume unit;
- no pH 7.0;
- no N2 distribution atmosphere, butyl-rubber-stopper seal, or autoclave step;
- no separation between the final medium's 800 ml water and the stock's 1 L
  water; and
- no final-medium dilution of the 4x artificial seawater salts.

Optional target-organism and growth-evidence slots are empty. I did not count
that as a defect because the inspected TOGO payload only establishes a medium
recipe.

Before reporting raw-source absence, I searched for `CultureMech:007903`,
`M1365`, `JCM_M1269`, and `Artificial Seawater Yeast Extract-Tryptone Medium`
with `rg --no-ignore --hidden` across `data`, `scripts`, `history`, `src`,
`reports`, and `references_cache`. That gitignore-independent search found the
normalized owner, generated merge, indexes, collision reports, and archived
reports, but no maintained raw YAML or source-specific import transform for
M1365.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The 4x artificial seawater stock has been flattened into the final medium. | TOGO represents artificial seawater 4x as a nested stock added at 200 ml; CultureMech keeps a `200 G_PER_L` stock row and also lists all stock salts as direct final-medium ingredients. | `data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml` |
| major | Water from unrelated contexts is merged into an invalid amount. | TOGO has 800 ml water in the final solution and 1 L water in the 4x stock; the record stores a single `801.0 G_PER_L` water row annotated as `[Merged 2 duplicates: 800.0, 1.0]`. | `data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml` |
| major | Final-medium salt concentrations are 4x-stock amounts rather than final amounts. | The 24 g MgSO4.7H2O, 80 g NaCl, 1.2 g CaCl2.2H2O, and other stock rows belong to the 1 L 4x artificial seawater stock that is added at 200 ml per final liter. | `data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml` |
| major | Source-critical pH and anaerobic preparation steps are absent. | TOGO M1365 reports pH 7.0 and a preparation instruction to distribute under N2, seal with butyl rubber stoppers, and autoclave. | `data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml` |

## Recommended Edits

1. Model `Artificial seawater (4x)` as a stock solution with a 200 ml addition to the final medium.
2. Move MgSO4.7H2O, NaCl, CaCl2.2H2O, K2HPO4, MgCl2.6H2O, KCl, NaHCO3, ammonium sulfate, NaBr, SrCl2.6H2O, ammonium Fe(III) citrate, and the stock's 1 L water into that nested 4x stock.
3. Preserve final-medium water as 800 ml, rather than merging it with stock water.
4. Remove the direct variable-concentration `N2` ingredient and represent the N2 vessel atmosphere in preparation/condition fields.
5. Add pH 7.0, butyl-rubber-stopper sealing, and autoclave instructions from TOGO M1365.
6. Regenerate `data/merge_yaml/merged/artificial_seawater_yeast_extract_tryptone_medium.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just validate-references data/normalized_yaml/bacterial/artificial_seawater_yeast_extract_tryptone_medium.yaml`.
- Run `just verify-merges` after regeneration.
- Manually compare the regenerated record against TOGO M1365 to confirm that the 4x artificial seawater stock remains nested and only its 200 ml addition appears in the final recipe.

## Additional Notes

- The cited JCM URL for `GRMD=1269` returned a "Nothing found" page when
  checked, so this review could not verify the source directly against JCM.
