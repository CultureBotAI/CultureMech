# YAML Record Review: aminivibrio_asinoensis_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/aminivibrio_asinoensis_medium__287e5edd.yaml`
- Started UTC: 2026-09-21T11:23:43Z
- Finished UTC: 2026-09-21T11:24:34Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:003288` |
| Name | `aminivibrio_asinoensis_medium` |
| Original name | `AMINIVIBRIO ASINOENSIS MEDIUM` |
| Source identity | JCM Medium J940, `mediadive.medium:J940` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/aminivibrio_asinoensis_medium__287e5edd.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/aminivibrio_asinoensis_medium.yaml` |

The generated record is a one-source merge and matches the normalized JCM owner. It has a separate TOGO sibling at `data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml` for the same original JCM_M940 recipe.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/aminivibrio_asinoensis_medium__287e5edd.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/aminivibrio_asinoensis_medium__287e5edd.yaml --out /private/tmp/aminivibrio_asinoensis_medium__287e5edd.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/aminivibrio_asinoensis_medium__287e5edd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/aminivibrio_asinoensis_medium__287e5edd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The record's top-level identity matches JCM J940:

- `id: CultureMech:003288`
- `name: aminivibrio_asinoensis_medium`
- `media_term.preferred_term: JCM Medium J940`
- `media_term.term.id: mediadive.medium:J940`
- `notes: Source: JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940`

The ingredient model does not match JCM J940 because it treats several post-autoclave or cross-referenced stock additions as final-medium ingredients:

- `NaHCO3: 30 G_PER_L` comes from a 30 ml/L addition of an 8% NaHCO3 stock.
- `Na2S x 9 H2O: 7 G_PER_L` comes from a 7 ml/L addition of a 5% sulfide stock.
- `p-Aminobenzoic acid`, `Biotin`, `Thiamine HCl`, and `Vitamin B12` are entries in the vitamin stock, which is added at 1 ml/L.
- `HCl`, `FeCl2 x 4 H2O`, trace metals, `NaOH`, `Na2SeO3 x 5 H2O`, and `Na2WO4 x 2 H2O` belong to JCM 187 or JCM 431 stocks, each added at 1 ml/L.

Grounding is exact for the basal salts, sodium pyruvate, resazurin, and most stock components. `Yeast extract` is still ungrounded, and `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887`.

## Evidence

Inspected source documents:

- JCM J940 at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940`
- JCM 187 at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187`
- JCM 431 at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431`
- TOGO Medium M987 API at `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987`

Supported claims:

- JCM J940 and TOGO M987 support the Aminivibrio asinoensis medium identity and the JCM_M940 accession.
- JCM J940 supports the basal ingredient amounts: 0.2 g KH2PO4, 0.25 g NH4Cl, 1 g NaCl, 0.5 g KCl, 0.4 g MgCl2 x 6 H2O, 0.15 g CaCl2 x 2 H2O, 1.1 g sodium pyruvate, 2 g yeast extract, 0.4 mg resazurin, and 1 L distilled water.
- JCM J940 supports 1 ml/L FeCl2 solution from JCM 187, 1 ml/L trace-element solution from JCM 187, 1 ml/L selenite-tungstate solution from JCM 431, 30 ml/L 8% NaHCO3 solution, 1 ml/L vitamin solution, and 7 ml/L 5% Na2S x 9H2O solution.
- JCM J940 supports autoclaving under an N2-CO2 80:20 gas atmosphere, adding the bicarbonate and vitamin stocks after cooling, distributing under the same gas mixture, and finally adding sulfide stock.

Unsupported or mismatched claims:

- The record does not support final `30 G_PER_L` NaHCO3 or final `7 G_PER_L` Na2S x 9 H2O.
- The JCM 187 and JCM 431 stock ingredients are not final-medium ingredients at the concentrations listed.
- The vitamin stock ingredients are off by the 1 ml/L stock dilution.
- Both preparation steps are truncated immediately before a source table of stock additions.

## Completeness

Consequential gaps:

- Six JCM stock additions are missing as stock `solutions`.
- Stock strengths and volumes are mixed into the final-medium ingredient list.
- The stock-addition tables are absent from `preparation_steps`.
- The JCM and TOGO copies of the same JCM_M940 recipe are not reconciled.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim.
- JCM J940 did not specify a final pH value.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*aminivibrio_asinoensis_medium__287e5edd.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the Aminivibrio slug, label, and `287e5edd` found this JCM owner, the adjacent TOGO M987 owner, the generated JCM output, and the older uppercase TOGO generated artifact.

## Findings

### Blocker

1. **JCM stock solutions are flattened as final grams per liter.**

   Evidence: JCM J940 lists 1 ml/L FeCl2 solution from JCM 187, 1 ml/L trace-element solution from JCM 187, 1 ml/L selenite-tungstate solution from JCM 431, 30 ml/L 8% NaHCO3 solution, 1 ml/L vitamin solution, and 7 ml/L 5% Na2S x 9H2O solution. The CultureMech root ingredient list contains those stock components directly, including `NaHCO3: 30 G_PER_L`, `Na2S x 9 H2O: 7 G_PER_L`, `FeCl2 x 4 H2O: 1.5 G_PER_L`, `Thiamine HCl: 0.2 G_PER_L`, and `Vitamin B12: 0.05 G_PER_L`.

   Owner: re-curate `data/normalized_yaml/bacterial/aminivibrio_asinoensis_medium.yaml` with explicit stock solutions for JCM 187, JCM 431, 8% NaHCO3, vitamins, and 5% sulfide; remove stock-only ingredients from the top-level final recipe; then regenerate.

### Major

1. **The stock-addition preparation tables are missing.**

   Evidence: generated step 1 ends after "add the following solutions from anaerobic stocks (filter-sterilized):" and generated step 2 ends after "add per liter the following solution from an anaerobic stock:". JCM J940 lists the 8% NaHCO3 and vitamin stocks after step 1 and the 5% sulfide stock after step 2.

   Owner: preserve those stock-addition tables either as complete `solutions` or as explicit preparation substeps in the normalized JCM owner.

2. **The JCM and TOGO imports of JCM_M940 are unreconciled and both stock-broken.**

   Evidence: `data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml` names the same JCM_M940 source but stores JCM's stock additions as six empty `Unknown solution` rows with `G_PER_L` amounts; it also stores the vitamin stock components as undiluted root ingredients with 20 to 200 `G_PER_L` values. Those artifacts keep it separate from the JCM generated output.

   Owner: repair TOGO M987 using the same JCM stock model and reconcile it with the JCM import during merge generation.

3. **One exact hydrated stock ingredient is misgrounded.**

   Evidence: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride, not to the exact hexahydrate in the JCM 187 trace-element stock.

   Owner: preserve the exact hydrated label and replace or clear the ChEBI mapping unless an exact nickel chloride hexahydrate term is available.

### Minor

1. **Yeast extract is ungrounded.**

   Evidence: JCM J940 supports the 2 g/L yeast-extract row, but the row lacks an ontology term and `mediaingredientmech_chebi_term`.

   Owner: ground yeast extract during ingredient enrichment if an exact accepted term is available.

## Recommended Edits

1. Model FeCl2 solution, JCM 187 trace-element solution, JCM 431 selenite-tungstate solution, 8% NaHCO3 solution, JCM J940 vitamin solution, and 5% Na2S x 9H2O solution as explicit `solutions` with ML_PER_L addition volumes.
2. Remove HCl, FeCl2, trace metals, NaOH, selenite, tungstate, vitamin rows, bicarbonate stock, and sulfide stock from the final ingredient list.
3. Complete the two preparation steps so the source stock-addition tables are retained.
4. Apply the same stock modeling to `data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml` and reconcile duplicate JCM_M940 imports.
5. Fix or clear the `NiCl2 x 6 H2O` grounding and ground yeast extract.
6. Regenerate generated merge records and rendered products.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected JCM and TOGO normalized owners plus the regenerated output.
- Rerun concentration plausibility and verify the Aminivibrio vitamin and FeCl2 stock-strength findings disappear.
- Rerun duplicate merging and confirm the JCM and TOGO copies of JCM_M940 no longer remain separate canonical generated records.
- Manually compare the regenerated record against JCM J940, JCM 187, and JCM 431 to verify each stock is nested and added at the source volume.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/aminivibrio_asinoensis_medium__287e5edd.yaml`, its normalized owner, the TOGO sibling, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/aminivibrio_asinoensis_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml`, and the JCM/TOGO importer logic that currently flattens or empties stock solution references.
