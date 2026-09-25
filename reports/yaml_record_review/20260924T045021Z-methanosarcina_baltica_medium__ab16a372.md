# YAML Record Review: methanosarcina_baltica_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosarcina_baltica_medium__ab16a372.yaml
- Started UTC: 2026-09-24T04:48:32Z
- Finished UTC: 2026-09-24T04:50:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009527 |
| Name | methanosarcina_baltica_medium |
| Original name | Methanosarcina Baltica Medium |
| Category | archaea |
| Generated record | data/merge_yaml/merged/methanosarcina_baltica_medium__ab16a372.yaml |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M300_Methanosarcina_Baltica_Medium.yaml |
| Source accession | TOGO:M300 |
| Original source | JCM_M305 |
| Merge fingerprint | ab16a3721268c45bf09bbfda02ed62b092b31126af5d2b92f0fba3a5903b44bd |

This generated record is a one-source merge of the TOGO M300 import. Its future fixes belong in `data/normalized_yaml/archaea/TOGO_M300_Methanosarcina_Baltica_Medium.yaml`, the TOGO cross-medium import logic that resolves M257, or the merge/deduplication layer; `data/merge_yaml/merged/methanosarcina_baltica_medium__ab16a372.yaml` is derived output.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosarcina_baltica_medium__ab16a372.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanosarcina_baltica_medium__ab16a372.yaml --out /private/tmp/methanosarcina_baltica_medium_ab16a372.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows; the TSV has only its header row. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanosarcina_baltica_medium__ab16a372.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanosarcina_baltica_medium__ab16a372.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded history | Not run: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in a merged record. |

`just` validators were not used because this checkout resolves `llvmlite==0.46.0` under Python 3.13 and fails during package build before reaching CultureMech validation. The focused Python 3.11 `uv --no-project --offline` commands above exercise the record-level schema, strict, reference, and term gates.

## Identity and Grounding

- `media_term` correctly identifies TOGO M300 and the TOGO API identifies M300 as `Methanosarcina Baltica Medium` from JCM `JCM_M305`; live JCM 305 and MediaDive J305 also describe `METHANOSARCINA BALTICA MEDIUM`.
- The `COMPLEX` and `UNDEFINED` classifications are appropriate because JCM 305 is a variant of Methanogenium Medium JCM 265, which contains yeast extract and trypticase peptone.
- The `kg_microbe_match: mediadive.medium:1640` value is wrong. MediaDive medium 1640 is a DSMZ `METHANOMASSILIICOCCUS ALVUS MEDIUM` record, with Anaerobe Basal Broth, 15% methanol stock, sodium resazurin, pH 7.4-7.6, and H2-CO2 overpressure, not JCM 305.
- This TOGO import is a duplicate identity of the direct JCM/MediaDive J305 normalized owner `data/normalized_yaml/archaea/methanosarcina_baltica_medium.yaml`, which generates `data/merge_yaml/merged/Methanosarcina_Baltica_Medium.yaml` with `CultureMech:002662`. An exact gitignore-independent search for `CultureMech:002662`, `JCM Medium J305`, and `mediadive.medium:J305` covered `data/merge_yaml/merged` plus that normalized JCM owner and found the direct duplicate.

## Evidence

- TOGO M300 and live JCM 305 both state that the recipe uses Medium 265 supplemented with 0.05% final methanol, then replaces the gas phase with N2-CO2 4:1 and pressurizes to 100 kPa.
- TOGO M300 preserves `METHANOGENIUM MEDIUM (see Medium [M257])` as a 1 L cross-reference; the generated `solutions` entry changes this to an empty `Unknown solution` at `1 G_PER_L`.
- TOGO M257 and live JCM 265 support the parent Methanogenium Medium formulation: 980 ml distilled water, KCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, NH4Cl, CaCl2 x 2 H2O, KH2PO4, NaCl, 10 ml Wolfe's mineral solution, 10 ml trace vitamins, Fe(NH4)2(SO4)2 x 6 H2O, NaHCO3, sodium acetate, yeast extract, trypticase peptone, 1 mg resazurin, post-autoclave 5% L-cysteine HCl H2O and 5% Na2S x 9 H2O additions, and H2-CO2 pressurization after inoculation.
- TOGO M257 further scopes Wolfe's mineral solution as a local stock that uses TOGO M142/JCM 151 trace minerals plus NiCl2 x 6 H2O, Na2SeO3, and Na2WO4 x 2 H2O; it scopes trace vitamins to TOGO M190/JCM 197. The M300 generated record drops all of these nested stock boundaries.
- MediaDive J305 is sparse and carries only the same JCM 305 variant instruction as a step under `Main sol. J305`; it does not provide ingredient rows that would support `mediadive.medium:1640` or an independent flattened formula.

## Completeness

- The record is not recipe-complete: all ingredients of Medium 265, Wolfe's mineral solution, and trace vitamins are absent.
- The final methanol concentration is absent even though the source says 0.05% final methanol.
- Preparation is absent even though M300/JCM 305 consists almost entirely of preparation context: replace the gas phase with N2-CO2 4:1 and pressurize to 100 kPa after supplementing Medium 265.
- Nitrogen and carbon dioxide are detached variable ingredients, so the gas ratio and headspace pressure that make them meaningful are not represented.
- Empty optional organism, growth, variant, discussion, and application-detail fields are not defects by themselves; the consequential omissions are the parent medium, stock solutions, final methanol percentage, and gas-phase instructions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | `kg_microbe_match` grounds JCM 305 to the wrong MediaDive medium. | `mediadive.medium:1640` resolves to DSMZ METHANOMASSILIICOCCUS ALVUS MEDIUM, while TOGO M300 and live JCM 305 identify Methanosarcina Baltica Medium. | `data/normalized_yaml/archaea/TOGO_M300_Methanosarcina_Baltica_Medium.yaml` or the KG-Microbe matching layer |
| major | The 1 L Methanogenium Medium parent was reduced to an empty gram-per-liter solution stub. | TOGO M300 points at `M257` with unit `L`; the generated record has `composition: []`, `name: Unknown solution`, and `unit: G_PER_L`. | TOGO cross-medium importer plus `data/normalized_yaml/archaea/TOGO_M300_Methanosarcina_Baltica_Medium.yaml` |
| major | All Medium 265 and nested stock components are absent. | TOGO M257/JCM 265 include base salts, Wolfe's mineral solution, trace vitamins, NaHCO3, sodium acetate, yeast extract, trypticase peptone, reducing solutions, and gas handling; none are present in the M300 generated record. | TOGO cross-medium importer |
| major | Methanol and the gas phase lost their quantitative source context. | TOGO M300/JCM 305 specify 0.05% final methanol and N2-CO2 4:1 at 100 kPa; the record stores methanol, carbon dioxide, and nitrogen only as `VARIABLE`. | `data/normalized_yaml/archaea/TOGO_M300_Methanosarcina_Baltica_Medium.yaml` |
| major | The same JCM 305 medium is represented as a second stable CultureMech record outside this merge. | The direct MediaDive/JCM owner `data/normalized_yaml/archaea/methanosarcina_baltica_medium.yaml` has `CultureMech:002662` and also points at JCM 305; this TOGO M300 owner has `CultureMech:009527`. | Merge deduplication and ID reconciliation |

## Recommended Edits

1. Remove or repair `kg_microbe_match: mediadive.medium:1640`; any MediaDive grounding for this record must be the JCM 305 source, not numeric DSMZ medium 1640.
2. Resolve TOGO M300 to Methanogenium Medium M257/JCM 265 as a 1 L parent medium or a fully represented nested recipe; do not leave it as an empty solution and do not convert 1 L to `G_PER_L`.
3. Preserve Medium 265's own nested stock structure: Wolfe's mineral solution, its TOGO M142/JCM 151 trace-mineral basis, the TOGO M190/JCM 197 trace vitamins, and the two 5% reducing-agent stocks should remain scoped rather than flattened into one final ingredient list.
4. Add source-backed preparation for 0.05% final methanol, N2-CO2 4:1 gas replacement, and 100 kPa pressurization in the TOGO M300 owner.
5. Reconcile the TOGO M300 and direct JCM/MediaDive J305 records so the regenerated corpus does not carry two stable CultureMech records for the same JCM medium.
6. Regenerate the merge YAML after the maintained owner, importer, and deduplication fixes land.

## Follow-up Checks

- Re-run the focused open schema, strict, reference, and term validators on the repaired TOGO M300 owner and the regenerated generated record.
- Inspect the regenerated M300 YAML to confirm M257 is either linked as a parent/solution reference with a liter quantity or expanded through preserved stock boundaries, never as an empty `G_PER_L` stub.
- Inspect all generated Methanosarcina Baltica outputs to confirm JCM 305 and TOGO M300 reconcile to one canonical generated record or carry an explicit, source-backed reason to remain separate.
- Verify no normalized Methanosarcina Baltica record keeps `mediadive.medium:1640` after the KG-Microbe match is repaired.

## Additional Notes

- The TOGO M300 API record, TOGO M257 API record, live JCM 305 page, live JCM 265 page, MediaDive J305 REST record, MediaDive numeric 1640 REST record, and direct JCM 305 normalized owner were inspected.
- The exact duplicate search for `CultureMech:002662`, `JCM Medium J305`, and `mediadive.medium:J305` used `rg --no-ignore --hidden` and included ignored files in the searched paths.
- This review did not create or edit GitHub issues, pull requests, or comments.
