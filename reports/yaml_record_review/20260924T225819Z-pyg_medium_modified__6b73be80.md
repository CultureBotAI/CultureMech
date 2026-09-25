# YAML Record Review: PYG Medium (modified)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml
- Started UTC: 2026-09-24T22:58:19Z
- Finished UTC: 2026-09-24T22:59:31Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009153 |
| Name | pyg_medium_modified |
| Original name | PYG Medium (modified) |
| Category | bacterial |
| Generated file | data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml |
| Merge source | TOGO_M2585_PYG_Medium_modified |
| Source grounding | TOGO:M2585, DSMZ_Medium104 |

The reviewed file is a generated merge product. Future corrections should be
made in the maintained TOGO normalization and in the TOGO/MediaDive solution
migration that separated MediaDive solution headers while leaving their stock
components in the top-level ingredient list.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml` | Passed with `No issues found`. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml --out /private/tmp/pyg_medium_modified__6b73be80.strict.tsv --workers 1 --quiet` | Passed with 0 strict errors; `/private/tmp/pyg_medium_modified__6b73be80.strict.tsv` contained 1 line including the header. |
| LinkML references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file was validated and no reference checks were emitted. |
| LinkML terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils`/`pkg_resources` deprecation warning was printed. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml` is the generated
  TOGO M2585 branch for CultureMech:009153 and DSMZ medium 104
  `PYG Medium (modified)`.
- TOGO M2585 is grounded to the DSMZ Medium 104 PDF and reports pH 7.2.
- The MediaDive DSMZ 104 REST record confirms the same DSMZ medium 104
  identity, pH 7.2, main solution, Salt solution, Haemin solution, and
  Vitamin K1 solution.
- Exact ignored-file search across `data/**/*.yaml` for
  `mediadive.medium:104`, the exact DSMZ 104 PDF URL, and exact DSMZ 104
  importer IDs found the reviewed TOGO branch, the direct DSMZ branch, the
  KOMODO 104 branch, the DSMZ 1405 branch, and many strain-specific KOMODO
  variants derived from DSMZ 104.

## Evidence

- TOGO M2585 defines a main solution with 950 ml distilled water, 10 g yeast
  extract, 2 g K2HPO4, 1 mg resazurin, 1 ml Tween 80, 5 g glucose, 5 g beef
  extract, 5 g Trypticase peptone, 0.5 g cysteine-HCl.H2O, 5 g peptone,
  40 ml Salt solution, 0.2 ml Vitamin K1 solution, and 10 ml Haemin solution.
- TOGO M2585 also carries the source instruction to add Vitamin K1, haemin, and
  cysteine after boiling and cooling under CO2, adjust to pH 7.2 with 8 N NaOH,
  distribute under N2, and autoclave.
- TOGO M2585 separately defines Salt solution as 0.25 g CaCl2.2H2O,
  0.5 g MgSO4.7H2O, 1 g K2HPO4, 1 g KH2PO4, 10 g NaHCO3, 2 g NaCl, and 1 L
  distilled water.
- TOGO M2585 separately defines Haemin solution as 50 mg haemin and 1 ml
  1 N NaOH adjusted to 100 ml, and Vitamin K1 solution as 0.1 ml Vitamin K1 in
  20 ml 95% ethanol.
- The reviewed record preserves the TOGO M2585 identity and the main dry
  peptide/extract/glucose/cysteine amounts.
- The reviewed record stores Salt, Vitamin K1, and Haemin solutions as empty
  solution rows using `G_PER_L` values copied from ml source aliquots.
- The reviewed record stores all Salt, Haemin, and Vitamin K1 stock components
  as top-level final-medium ingredients.

## Completeness

- Empty optional fields beyond general microbial cultivation are not defects.
- The Salt, Haemin, and Vitamin K1 solution compositions are empty despite
  source-provided stock recipes.
- `ph_value` is missing even though TOGO gives pH 7.2.
- CO2 cooling, 8 N NaOH pH adjustment, N2 distribution, autoclaving, haemin
  stock preparation, and Vitamin K1 stock preparation are missing as
  preparation steps.
- DSMZ 104-equivalent direct DSMZ, KOMODO, and DSMZ 1405 branches remain
  separate.
- Exact ignored-file search included ignored files before assessing exact DSMZ
  104 duplicate and variant scope.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Three MediaDive solution aliquots use the wrong unit family and have empty compositions. | TOGO M2585 adds 40 ml Salt solution, 0.2 ml Vitamin K1 solution, and 10 ml Haemin solution; the YAML stores the three rows as 40, 0.2, and 10 `G_PER_L` and leaves their compositions empty. | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml; solution migration |
| Major | Salt, Haemin, and Vitamin K1 stock recipes were flattened into final-medium ingredients. | TOGO M2585 provides separate recipes for all three stocks; the reviewed YAML stores their salts, 1N NaOH, Haemin, 95% ethanol, and Vitamin K1 as top-level rows. | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml; solution migration |
| Major | Main, salt-stock, and haemin-stock water were merged. | TOGO M2585 has 950 ml main water, 1 L Salt solution water, and 100 ml Haemin solution water; the YAML merges them into one 2050 `G_PER_L` row. | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml; data-quality cleanup |
| Major | Milligram and milliliter main-medium rows were stored as grams per liter. | TOGO M2585 uses 1 mg resazurin and 1 ml Tween 80; the YAML stores both rows as 1 `G_PER_L`. | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml |
| Major | pH and source preparation context are absent. | TOGO M2585 gives pH 7.2 and describes CO2 cooling, 8 N NaOH adjustment, N2 distribution, autoclaving, and filter-sterilized haemin and Vitamin K1 stocks; the YAML has no `ph_value` or `preparation_steps`. | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml |
| Minor | The MgSO4.7H2O MediaIngredientMech CHEBI back-link is stale. | The row has primary `CHEBI:31795` magnesium sulfate heptahydrate but `mediaingredientmech_chebi_term` still points at generic `CHEBI:32599` magnesium sulfate. | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml; MediaIngredientMech enrichment |
| Minor | Equivalent DSMZ 104 branches remain separate generated records. | Exact ignored-file search found direct DSMZ, KOMODO 104, DSMZ 1405, and strain-specific KOMODO branches grounded to `mediadive.medium:104` or the DSMZ 104 PDF. | data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml; merge_recipes.py |

## Recommended Edits

1. Recurate `data/normalized_yaml/bacterial/TOGO_M2585_PYG_Medium_modified.yaml`
   so Salt, Haemin, and Vitamin K1 stock formulas are scoped under explicit
   solution rows with 40 ml, 10 ml, and 0.2 ml final aliquots.
2. Keep main water, Salt solution water, and Haemin solution water in their
   appropriate scopes.
3. Store resazurin as 1 mg and Tween 80 as 1 ml or as correct inline
   equivalents.
4. Add pH 7.2 and preparation steps for CO2 cooling, 8 N NaOH adjustment, N2
   distribution, autoclaving, haemin stock preparation, and Vitamin K1 stock
   preparation.
5. Refresh the MgSO4.7H2O MediaIngredientMech CHEBI link.
6. Regenerate the merged output and reconcile this TOGO M2585 branch with the
   equivalent direct DSMZ, KOMODO 104, and DSMZ 1405 branches after each branch
   preserves the same stock boundaries.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on
  `data/merge_yaml/merged/pyg_medium_modified__6b73be80.yaml`.
- Manually confirm the regenerated record has explicit Salt, Haemin, and
  Vitamin K1 solution boundaries.
- Run exact ignored-file searches for `mediadive.medium:104`,
  `DSMZ_Medium104.pdf`, `KOMODO_104_PYG-MEDIUM_modified`,
  `TOGO_M2585_PYG_Medium_modified`, and `DSMZ_1405_PYG_MEDIUM_MODIFIED` to
  verify the intended DSMZ 104 branches have converged.

## Additional Notes

- The local TOGO M2585 fetch initially failed with a sandbox DNS error. The
  official URL was then fetched successfully with the approved escalated
  `curl -L` rule.
