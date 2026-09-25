# YAML Record Review: pyrococcus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyrococcus_medium__6ffabef8.yaml
- Started UTC: 2026-09-24T23:43:30Z
- Finished UTC: 2026-09-24T23:44:29Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pyrococcus_medium__6ffabef8.yaml` as a generated `MediaRecipe` for `CultureMech:001478`, label `pyrococcus_medium`, with `media_term` `mediadive.medium:377`.

The maintained owner is the direct DSMZ/MediaDive file at `data/normalized_yaml/archaea/pyrococcus_medium.yaml`; this generated record is a one-input projection of that owner.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyrococcus_medium__6ffabef8.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyrococcus_medium__6ffabef8.yaml --out /private/tmp/pyrococcus_medium__6ffabef8.strict.tsv --workers 1 --quiet` | Passed; 1 TSV line, header only, 0 error rows. |
| Internal references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyrococcus_medium__6ffabef8.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were configured for this record. |
| Term grounding | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyrococcus_medium__6ffabef8.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the available validator covers standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

`mediadive.medium:377`, DSMZ Medium 377, and `DSMZ_Medium377.pdf` all identify `PYROCOCCUS MEDIUM`; the ID, label, category, type flags, physical state, and pH are aligned.

An ignored-file-inclusive boundary-aware search across `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports/yaml_record_review` for `mediadive.medium:377`, `DSMZ_Medium377.pdf`, `CultureMech:001478`, `PMID:21421788`, and the full `6ffabef86d2f97b3e756571112121d049ace2f657ff0fab84e92f5932bb1e8d3` fingerprint found the direct DSMZ 377 owner, this generated artifact, one TOGO projection of the same DSMZ PDF, a KOMODO 377 base, and KOMODO 377 strain-variant rows. The search pattern excluded the distinct 377a and 377b media.

The `Pyrococcus furiosus` organism and CF11-cellulose growth overlay are supported by PMID 21421788: NCBI E-utilities resolved the PMID to Oslowski et al. 2011, DOI `10.1128/AEM.01366-10`, and the abstract says P. furiosus was serially adapted for growth on CF11 cellulose with a 64 min doubling time.

## Evidence

DSMZ/MediaDive Medium 377 defines three solutions, not one flat ingredient table:

- Main solution: 13.85 g NaCl, 3.50 g `MgSO4 x 7 H2O`, 2.75 g `MgCl2 x 6 H2O`, 0.33 g KCl, 0.05 g NaBr, 15 mg H3BO3, 7 ml `SrCl2 x 6 H2O` 0.1% w/v, 10 mg ammonium sulfate, 5 ml citric acid 0.1% w/v, 0.5 ml KI 0.01% w/v, 0.75 g `CaCl2 x 2 H2O`, 0.5 g KH2PO4, 2 ml `NiCl2 x 6 H2O` 0.1% w/v, 10 ml Modified Wolin's mineral solution, 0.5 ml 0.1% sodium resazurin, 30 g powdered sulfur, 5 g BD Bacto peptone, 1 g OXOID yeast extract, 15 ml neutralized sulfide solution 3% w/v, and 960 ml distilled water.
- Modified Wolin's mineral solution: a 1 L stock added to the main solution at 10 ml.
- Neutralized sulfide solution 3% w/v: a 100 ml stock added to the main solution at 15 ml.

The generated YAML flattened both stocks into final-medium rows. It also summed exact-name duplicates between the main solution and Modified Wolin's stock, producing rows such as `NaCl: 14.85 G_PER_L`, `MgSO4 x 7 H2O: 6.5 G_PER_L`, `CaCl2 x 2 H2O: 0.85 G_PER_L`, `NiCl2 x 6 H2O: 0.032 G_PER_L`, and `H3BO3: 0.025 G_PER_L`; these sums do not match either the main-solution concentrations or the final concentrations after adding 10 ml of the stock.

The three DSMZ preparation notes are present, but without `solutions` they are attached at the top level and cannot be scoped to Modified Wolin's mineral solution or neutralized sulfide solution.

## Completeness

Empty optional fields are not defects.

Consequential omissions:

- No `solutions` array preserves the 10 ml Modified Wolin's stock addition.
- No `solutions` array preserves the 15 ml neutralized sulfide stock addition.
- The 960 ml main water row, 1000 ml Modified Wolin's stock water row, and 100 ml sulfide stock water row are all absent.
- No exact same-source link connects this direct DSMZ owner with the TOGO and KOMODO projections of DSMZ Medium 377.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Modified Wolin's mineral solution was flattened into top-level final-medium ingredients. | DSMZ 377 adds 10 ml of a separate 1 L Modified Wolin's stock. The YAML lists nitrilotriacetic acid, manganese sulfate, iron sulfate, cobalt sulfate, zinc sulfate, copper sulfate, potassium aluminium sulfate, molybdate, selenite, tungstate, and duplicate main salts as final-medium ingredient rows at stock strength. | `data/normalized_yaml/archaea/pyrococcus_medium.yaml` |
| Major | Duplicate salts from the main solution and Modified Wolin's stock were summed incorrectly. | The DSMZ source has separate `NaCl` 13.85 g main plus 1.0 g/L stock, `MgSO4 x 7 H2O` 3.50 g main plus 3.0 g/L stock, `H3BO3` 15 mg main plus 0.01 g/L stock, `CaCl2 x 2 H2O` 0.75 g main plus 0.1 g/L stock, and `NiCl2 x 6 H2O` 0.1% additions in the main plus 0.03 g/L in the stock. The YAML stores simple sums of each pair. | `data/normalized_yaml/archaea/pyrococcus_medium.yaml` |
| Major | Neutralized sulfide solution 3% w/v was flattened at stock concentration. | DSMZ 377 adds 15 ml of a stock made from 3 g `Na2S x 9 H2O` in 100 ml water. The YAML records `Na2S x 9 H2O` as a top-level `30 G_PER_L` ingredient. | `data/normalized_yaml/archaea/pyrococcus_medium.yaml` |
| Major | Solvent rows for the main solution and both stocks are absent. | DSMZ 377 has 960 ml distilled water in the main solution, 1000 ml in Modified Wolin's mineral solution, and 100 ml in neutralized sulfide solution. No `Distilled water` row survives in the YAML. | `data/normalized_yaml/archaea/pyrococcus_medium.yaml` |
| Major | Powdered sulfur is grounded to the sulfur atom instead of elemental sulfur. | The DSMZ row is powdered sulfur, a material ingredient, but the YAML maps it to `CHEBI:26833` `sulfur atom`. | `data/normalized_yaml/archaea/pyrococcus_medium.yaml` |
| Minor | KI still carries a legacy MediaIngredientMech identifier. | The ingredient has primary `CHEBI:8346` grounding but still uses `mediaingredientmech_term: MediaIngredientMech:000232`. | `data/normalized_yaml/archaea/pyrococcus_medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/archaea/pyrococcus_medium.yaml`, rehydrate Modified Wolin's mineral solution as a 10 ml stock addition and move its 16 component rows plus 1000 ml distilled water into that stock.

2. Rehydrate neutralized sulfide solution 3% w/v as a 15 ml stock addition and move `Na2S x 9 H2O` plus 100 ml distilled water into that stock.

3. Restore the main solution to only DSMZ 377 main rows, including 960 ml distilled water and the unsummed main-solution concentrations.

4. Attach the Modified Wolin's and sulfide preparation notes to their respective stock solutions once they exist.

5. Re-ground powdered sulfur from `CHEBI:26833` to the elemental sulfur material term and migrate KI to `mediaingredientmech_chebi_term`.

6. Reconcile this direct DSMZ 377 owner with the TOGO and KOMODO projections of the same DSMZ Medium 377 while keeping DSMZ 377a, DSMZ 377b, and true DSM-specific KOMODO variants out of the exact source-duplicate merge.

## Follow-up Checks

- Re-run the focused schema, strict, reference, and term validators on the repaired direct DSMZ 377 owner and regenerated merged YAML.
- Re-run an ignored-file-inclusive boundary-aware search for `mediadive.medium:377`, `DSMZ_Medium377.pdf`, and `TOGO_M2667_Pyrococcus_Medium` across `data/normalized_yaml` and `data/merge_yaml/merged` to confirm the repaired exact duplicate links do not collapse 377a, 377b, or KOMODO strain variants.
- Manually compare the regenerated YAML against live MediaDive 377 and `DSMZ_Medium377.pdf` to confirm both stock boundaries, all three water rows, and the unsummed main-solution salts are correct.
- Keep the existing PMID 21421788 check for the CF11-cellulose variant; the PubMed record should continue to resolve to DOI `10.1128/AEM.01366-10` with the abstract evidence for the 64 min doubling time.

## Additional Notes

PubMed's normal HTML page returned a browser proof-of-work challenge in `curl`, but NCBI E-utilities returned the PMID 21421788 XML directly.
