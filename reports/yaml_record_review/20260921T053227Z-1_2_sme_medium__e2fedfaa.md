# YAML Record Review: 1_2_sme_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_2_sme_medium__e2fedfaa.yaml`
- Started UTC: 20260921T053119Z
- Finished UTC: 20260921T053227Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:009611` |
| Slug | `1_2_sme_medium` |
| Original name | `1/2 SME medium` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml` |
| Source accession | `TOGO:M3145` |
| Merge fingerprint | `e2fedfaa4f57e9ed1a9f48ef768b7832daabd0c2313c16f9fed4aa93822de970` |

Reviewed the singleton generated merge for TOGO M3145. A gitignore-independent exact search for `CultureMech:009611`, `TOGO:M3145`, `TOGO_M3145_1_2_SME_medium`, the merge fingerprint, and `https://togomedium.org/medium/M3145` found only the expected generated record, normalized owner, catalog/index rows, historical aggregate reports, and earlier review notes that flagged M3145 as a separate TOGO `1/2 SME` record needing its own review.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_2_sme_medium__e2fedfaa.yaml` | Passed with no output |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_2_sme_medium__e2fedfaa.yaml --out /private/tmp/1_2_sme_medium__e2fedfaa.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_2_sme_medium__e2fedfaa.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_2_sme_medium__e2fedfaa.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `curation_history` | Not checked | Not checked: no focused validator is documented for generated merge-file `MediaRecipe.curation_history`; the repository's `validate-history` target validates standalone history files under `history/`. |

The documented `just` validator wrappers remain blocked by the project `llvmlite==0.46.0` build under Python 3.13; the no-project `uv` commands above were used as focused equivalents.

## Identity and Grounding

- The record correctly denotes TOGO M3145, `1/2 SME medium`. The inspected live TOGO `gmdb_medium_by_gmid?gm_id=M3145` payload reports `gm: http://togomedium.org/medium/M3145`, `name: 1/2 SME medium`, empty `src_url`, and `ph: 5.5 - 6.0`.
- M3145 is not a duplicate of TOGO M563/JCM 559: its TOGO payload has no resazurin row, uses 5 g elemental sulfur instead of 10 g sulfur powder, uses 25 mg KI instead of 0.05 mg KI, omits N2, and includes sulfuric acid for pH adjustment.
- The generated record preserves all 18 TOGO components with exact primary CHEBI groundings for the water, salts, elemental sulfur, anhydrous Na2S, sulfuric acid, CO2, and H2 rows.
- Two TOGO milligram rows were imported with the same numeric values as `G_PER_L`: `SrCl2.6H2O` is `7.5 G_PER_L` instead of 7.5 mg/L, and `KI` is `25 G_PER_L` instead of 25 mg/L.
- The TOGO 1 L `Distilled water` row was imported as `1 G_PER_L`, which changes a final-volume row into a mass concentration.
- The variable-concentration `sulfuric acid`, `Carbon dioxide gas`, and `Hydrogen gas` rows are supported as components of the TOGO comments, but the record drops their context: adjust to pH 5.5-6.0 with sulfuric acid and grow in H2/CO2 at 250 kPa and 80:20 by volume.

## Evidence

- The inspected TOGO payload supports 1 L distilled water; MgSO4.7H2O 3.5 g; NaCl 13.85 g; CaCl2.2H2O 0.38 g; KH2PO4 0.5 g; MgCl2.6H2O 2.75 g; H3BO3 0.015 g; KCl 0.33 g; NaHCO3 0.16 g; (NH4)2SO4 0.25 g; Elemental sulfur 5 g; NaBr 0.05 g; SrCl2.6H2O 7.5 mg; KI 25 mg; Na2S 0.5 g; sulfuric acid; and the CO2 and H2 gas components.
- The same TOGO payload says reduction was done by adding 0.5 g Na2S and then adjusting pH at room temperature to pH 5.5-6.0 with sulfuric acid.
- TOGO's growth-condition comment says organisms were grown in 120 ml serum bottles containing 20 ml `1/2 SME medium`, pressurized with H2/CO2 at 250 kPa and 80:20 by volume, and incubated at 90 C under shaking.
- `src/culturemech/data/mediaingredientmech/label_index.csv` maps `SrCl2.6H2O`, `KI`, and sulfuric-acid synonyms to the same CHEBI IDs used as those ingredients' primary terms.
- A gitignore-independent exact search over the normalized owner and generated record found no top-level `references` or `reference` entries; the TOGO URL is preserved only as free text in `notes`.

## Completeness

- Consequential gap: the TOGO pH range of 5.5-6.0 is absent even though the schema exposes `ph_range`.
- Consequential gap: the TOGO reduction and pH-adjustment instructions are absent.
- Consequential gap: the TOGO H2/CO2 250 kPa gas atmosphere is flattened to variable CO2 and H2 ingredient rows.
- Consequential gap: two milligram rows and one water volume row need unit normalization before the formulation is quantitatively usable.
- Non-blocking provenance gap: TOGO M3145 has an empty `src_url`, and the normalized record has no structured `references`; only the TOGO database URL is recoverable from the record.
- The record has no target-organism evidence. That is acceptable for now because the inspected TOGO comment says "the organisms" but does not name the organisms, and the original publication behind the comment is not represented in TOGO M3145.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Two milligram salts are overstated 1000-fold. | TOGO M3145 lists SrCl2.6H2O at 7.5 mg and KI at 25 mg in the 1 L recipe. The generated record stores the same numeric values as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml` |
| Major | Distilled water uses a mass-concentration unit instead of the source's final-volume row. | TOGO lists 1 L distilled water, but the record stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml` |
| Major | The pH range and anaerobic H2/CO2 context are missing. | TOGO reports `ph: 5.5 - 6.0`, states that pH was adjusted with sulfuric acid after Na2S reduction, and gives H2/CO2 at 250 kPa and 80:20 by volume; the record has neither `ph_range` nor `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml` |
| Minor | The TOGO source is not represented as a structured reference, and its original source is unresolved. | The live TOGO payload has an empty `src_url`, the record only stores `https://togomedium.org/medium/M3145` in top-level `notes`, and reference validation had no structured objects to check. | `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml` |
| Minor | The medium is classified as `COMPLEX` / `UNDEFINED` despite being a chemically defined formulation. | The inspected TOGO component rows are salts, elemental sulfur, sulfuric acid, water, and named gases; no undefined extract, peptone, or biological digest appears in the recipe. | `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml` |

## Recommended Edits

1. Convert the TOGO milligram rows in `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml`: SrCl2.6H2O to `0.0075 G_PER_L` and KI to `0.025 G_PER_L`.
2. Convert `Distilled water` from `1 G_PER_L` to the repository's 1 L final-volume representation.
3. Add `ph_range: {min: 5.5, max: 6.0}`.
4. Add preparation or condition structures that preserve 0.5 g Na2S reduction, sulfuric-acid pH adjustment at room temperature, the H2/CO2 250 kPa 80:20 gas atmosphere, and 90 C shaking incubation.
5. Add a structured TOGO M3145 reference and a quality flag or discussion noting that TOGO did not publish the original `src_url`.
6. Reclassify the record as `DEFINED` / `DEFINED` unless a local convention deliberately treats gas-phase anaerobic media as complex.

## Follow-up Checks

- Re-run strict, term, and reference validation for `data/normalized_yaml/bacterial/TOGO_M3145_1_2_SME_medium.yaml`.
- Re-run merge generation and verify `data/merge_yaml/merged/1_2_sme_medium__e2fedfaa.yaml` carries the converted milligram rows, `1000 ML_PER_L` water, pH 5.5-6.0, TOGO M3145 structured reference, and anaerobic H2/CO2 context.
- Add or run a TOGO import regression check that proves `mg` rows are divided by 1000 and `L` water rows are not mapped to `G_PER_L`.
- Resolve the original publication behind TOGO's M3145 comments before adding named target organisms or Huber et al. growth-evidence claims.

## Additional Notes

- TOGO M563/JCM 559 and M3145 share the same public `1_2_sme_medium` slug after name normalization but have materially different formulas; they should remain distinct unless a curator can identify a source-level equivalence.
