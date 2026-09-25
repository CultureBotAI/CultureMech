# YAML Record Review: alkaliphilus_crotonatoxidans_medium__05e4cdb7

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml`
- Started UTC: 2026-09-21T11:05:49Z
- Finished UTC: 2026-09-21T11:07:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002735` |
| Generated path reviewed | `data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml` |
| Maintained source path | `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` |
| Merge source | `alkaliphilus_crotonatoxidans_medium` |
| Category | `bacterial` |
| Source accession | `mediadive.medium:J378` |
| Source label | `ALKALIPHILUS CROTONATOXIDANS MEDIUM` / JCM Medium 378 |
| Source documents inspected | JCM Medium 378 live HTML; JCM Medium 197 live HTML for the referenced trace vitamins stock |

The reviewed file is a generated merge from one normalized MediaDive import. Future curation should change `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` or the MediaDive/JCM importer, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml` | Passed: `No issues found` |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml --out /private/tmp/alkaliphilus_crotonatoxidans_medium__05e4cdb7.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record |

## Identity and Grounding

The record identity is sound: `CultureMech:002735`, `mediadive.medium:J378`, and the label all identify JCM Medium 378, `ALKALIPHILUS CROTONATOXIDANS MEDIUM`.

JCM 378 has three formulation compartments that the root record collapses:

| Source compartment | JCM use | Current generated state |
|---|---|---|
| Base/final JCM 378 medium | 900 ml aqueous base with bicarbonate and later 0.1 volume filter-sterilized crotonic acid solution | Core rows are scaled from their source gram amounts by 50-fold |
| Trace metal solution | 10 ml/L stock from the inline JCM 378 subrecipe | Stock ingredients are top-level root `ingredients` at full stock strength |
| Trace vitamins | 10 ml/L stock from JCM Medium 197 | Stock ingredients are top-level root `ingredients` at full stock strength |

Ingredient identity gaps:

- `Yeast extract` and `Tryptone` are ungrounded despite direct packaged MediaIngredientMech mappings.
- `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` / `nickel dichloride`, so the hexahydrate form is not preserved.
- `MnSO4 x n H2O` is grounded to `CHEBI:86360` / manganese(II) sulfate. The variable hydrate should be left as supplied or explicitly de-grounded rather than narrowed to an anhydrous salt without evidence.
- `Na2SeO4` still has a legacy `mediaingredientmech_term` rather than a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Evidence

The JCM Medium 378 live page supports these root final-medium additions:

| Ingredient | JCM 378 value | Current record value |
|---|---:|---:|
| Yeast extract | 2.0 g | `100 G_PER_L` |
| Tryptone | 2.0 g | `100 G_PER_L` |
| Crotonic acid | 0.86 g as a 0.86 g/100 ml stock added at 0.1 volume | `43 G_PER_L` |
| KH2PO4 | 0.5 g | `25 G_PER_L` |
| MgCl2 x 6 H2O | 0.33 g | `16.5 G_PER_L` |
| NaCl | 0.4 g | `20 G_PER_L` |
| NH4Cl | 0.4 g | `20 G_PER_L` |
| CaCl2 x 2 H2O | 0.05 g | `2.5 G_PER_L` |
| NaHCO3 | 3.5 g | `175 G_PER_L` |
| L-Cysteine HCl x H2O | 0.5 g as a 5% stock | `25 G_PER_L` |
| Na2S x 9 H2O | 0.5 g as a 5% stock | `25 G_PER_L` |
| Resazurin | 1.0 mg | `0.05 G_PER_L` |

The importer appears to have divided these values by 0.02 L: every one of the JCM 378 final-medium rows above is 50-fold too high.

The inline JCM 378 trace metal stock and the JCM 197 trace vitamin stock were also flattened. JCM 378 adds 10 ml of the trace metal stock per liter, so the trace rows in the final medium should be diluted 100-fold if they are flattened at all. JCM 378 also adds 10 ml of JCM 197 trace vitamins per liter, so each vitamin-stock constituent should be diluted 100-fold if flattened.

JCM 378 supports the preparation narrative now present in step 1: omit crotonic acid, NaHCO3, L-cysteine HCl x H2O, and Na2S x 9H2O from the boiled base; cool under 80:20 N2-CO2; add NaHCO3; dispense under 80:20 N2-CO2; autoclave and stand overnight; add filter-sterilized crotonic acid at 0.1 volume; autoclave cysteine and sulfide as 5% solutions under N2; and add the crotonic acid, cysteine, and sulfide solutions aseptically and anaerobically before inoculation.

The `ph_value: 6.0` on the root record is not a final-medium pH from JCM 378. JCM 378 adjusts the base to pH 7.0-7.5 before boiling and the crotonic acid stock to pH 7.0; pH 6.0 belongs to the inline trace metal solution subrecipe.

## Completeness

Consequential gaps:

- The record has no `solutions` block for 10 ml/L trace metal solution, 10 ml/L JCM 197 trace vitamins, 0.1 volume crotonic acid stock, 5% L-cysteine HCl x H2O, or 5% Na2S x 9H2O.
- All JCM 378 base rows are 50-fold too concentrated.
- Trace metal and trace vitamin stock rows are present as stock-strength top-level root ingredients.
- The root `ph_value` is transposed from the trace metal stock's preparation.
- The `high_metal: true` flag is likely an artifact of treating the trace metal stock as final medium.
- JCM and MediaDive provenance is free text; JCM 197 provenance is absent even though that referenced vitamin stock supplies ten rows.

Correctly empty or not inherently defective:

- `target_organisms`, `growth_metrics`, and literature `evidence` are absent. The JCM recipe source does not itself prove a strain-specific growth outcome.
- `parents`, `variants`, and `discussion` are absent; the direct formulation defects above are the urgent work.
- `physical_state: LIQUID` agrees with the JCM recipe.

A gitignore-independent search with `rg --no-ignore --hidden` and `find` covered `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `alkaliphilus_crotonatoxidans_medium__05e4cdb7`, `CultureMech:002735`, `mediadive.medium:J378`, `mediadive.solution:4103`, `J378`, and the JCM 378 URL. It found this generated target, its normalized MediaDive parent, `mediadive_4103_Main_sol_J378.yaml`, a TOGO M373 sibling from the same JCM recipe, registry/catalog/index references, archived validation reports, and the REE/high-metal analysis entry. `find reports/yaml_record_review -name '*alkaliphilus_crotonatoxidans_medium__05e4cdb7.md'` found no prior report for this exact generated-record stem before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The JCM 378 root formulation was scaled by 50-fold. | JCM lists 2.0 g yeast extract, 2.0 g tryptone, 0.5 g KH2PO4, 3.5 g NaHCO3, and 1.0 mg resazurin; the record has 100, 100, 25, 175, and 0.05 `G_PER_L` respectively. | `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` or the MediaDive/JCM importer |
| major | Trace metal and trace vitamin stocks were flattened into final-medium ingredients. | JCM 378 lists 10 ml trace metal solution and 10 ml trace vitamins from JCM 197; the trace metal salts and JCM 197 vitamins are root rows at stock strength. | `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` or the MediaDive/JCM importer |
| major | Several preparation stocks are chemically inlined but not represented as stock solutions. | JCM 378 adds crotonic acid as a 0.86 g/100 ml filter-sterilized stock at 0.1 volume and autoclaves cysteine and sulfide as 5% solutions under N2; the record keeps only concentration-scaled root rows. | `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` |
| major | The root pH is wrong. | `ph_value: 6.0` comes from the trace metal solution subrecipe; JCM 378 supports pH 7.0-7.5 for the base and pH 7.0 for the crotonic acid stock, not final root pH 6.0. | `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` or the importer field mapping |
| major | `high_metal: true` is not supportable from the final medium. | The root trace-metal concentrations are 100-fold stock values. The final medium receives 10 ml/L of that stock, so the flag should be recomputed after stock structure is restored. | High-metal derivation over the regenerated normalized or merged record |
| minor | Exact ingredient grounding is incomplete. | `Yeast extract` and `Tryptone` are ungrounded despite MIM label-index hits; `NiCl2 x 6 H2O` is linked to anhydrous nickel dichloride; `Na2SeO4` still has only the legacy MIM field. | `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` plus the packaged MediaIngredientMech label index |
| minor | Source provenance is not structured. | JCM 378 is present only in `notes` and `media_term`; JCM 197 is not recorded near the flattened trace vitamin rows. | `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` or import provenance mapping |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml` from the live JCM 378 page using the JCM per-liter amounts, not `mediadive.solution:4103`'s `Original volume: 20 mL` scaling.
2. Replace full-strength trace metal components with a 10 ml/L `solutions` entry for the inline JCM 378 trace metal stock, with the stock composition kept under that solution.
3. Replace full-strength vitamin components with a 10 ml/L `solutions` entry for the JCM 197 trace vitamin stock.
4. Represent the crotonic acid, 5% L-cysteine HCl x H2O, and 5% Na2S x 9H2O additions as separate stocks or as accurately noted post-autoclave additions, rather than 50-fold root concentrations.
5. Remove `ph_value: 6.0` from the root medium unless a source for final medium pH 6.0 is found; keep pH 6.0 scoped to the trace metal stock.
6. Recompute or remove `high_metal` after stock nesting and final concentrations are fixed.
7. Ground `Yeast extract`, `Tryptone`, `NiCl2 x 6 H2O`, and `Na2SeO4` using exact packaged MediaIngredientMech entries.
8. Add structured source provenance for JCM 378 and JCM 197.
9. Regenerate `data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml`.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml`.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml` to confirm the 50-fold scaling is gone.
- Rerun `just validate-references data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml` once structured JCM 378 and JCM 197 references are added.
- Rerun `just validate-products` after regenerating pages and high-metal derived artifacts.
- Compare the regenerated medium against JCM Medium 378 and the regenerated trace vitamin stock against JCM Medium 197, especially the 10 ml/L trace metal and trace vitamin additions, 0.1 volume crotonic acid stock, and pH scopes.
- Re-run exact `rg --no-ignore --hidden` checks for `CultureMech:002735`, `mediadive.medium:J378`, and `jcm_grmd?GRMD=378` across `data`, `src`, `scripts`, `history`, and reports.

## Additional Notes

- `data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml` is a sibling import of the same JCM Medium 378 recipe and should be checked when its generated merge is reached.
- The search used to find prior reports included ignored files via `find`; there was no existing report with the exact `alkaliphilus_crotonatoxidans_medium__05e4cdb7` generated-record stem.
- `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` were not run directly because project `uv` currently tries to build `llvmlite==0.46.0` under Python 3.13 before reaching record validation. The equivalent no-project validator invocations above were used instead.
