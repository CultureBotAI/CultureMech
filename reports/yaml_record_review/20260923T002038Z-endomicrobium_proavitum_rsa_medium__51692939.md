# YAML Record Review: ENDOMICROBIUM PROAVITUM RSA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/endomicrobium_proavitum_rsa_medium__51692939.yaml
- Started UTC: 2026-09-23T00:15:00Z
- Finished UTC: 2026-09-23T00:20:38Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/endomicrobium_proavitum_rsa_medium__51692939.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:002234`
- Name: `endomicrobium_proavitum_rsa_medium`
- Original label: `ENDOMICROBIUM PROAVITUM RSA MEDIUM`
- Category: `bacterial`
- Medium term: `mediadive.medium:J1051` / `JCM Medium J1051`
- Generated status: generated merge record with fingerprint `51692939f9ed5c358605b9f908c638a7f7b947afb5bb296a61ac9eb56fb218c8`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/endomicrobium_proavitum_rsa_medium.yaml`

The merge record adds only the `merge_recipes.py` history entry, `merge_fingerprint`, and `merged_from` metadata on top of the maintained normalized record.

## Validation

Focused validation was clean.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/endomicrobium_proavitum_rsa_medium__51692939.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/endomicrobium_proavitum_rsa_medium__51692939.yaml --out /private/tmp/endomicrobium_proavitum_rsa_medium__51692939.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/endomicrobium_proavitum_rsa_medium__51692939.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/endomicrobium_proavitum_rsa_medium__51692939.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the run emitted the expected `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes JCM Medium 1051, `ENDOMICROBIUM PROAVITUM RSA MEDIUM`. JCM 1051, MediaDive J1051, and TOGO M1118 all agree on that medium identity.

The basic pre-autoclave salts and the four aromatic fatty acids are chemically aligned. One hydrate grounding is wrong: JCM Medium 187 defines the trace-element nickel source as `NiCl2 x 6 H2O`, but the reviewed record links it to `CHEBI:34887` / `nickel dichloride`.

The commercial LB Miller note is not grounded in JCM 1051 and makes the record look partly like a different medium.

## Evidence

JCM 1051 defines a base recipe in 945 ml water with NaCl, KCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, KH2PO4, and 0.4 mg resazurin. After autoclaving and cooling under N2-CO2, the source adds 30 ml 8 percent NaHCO3, 5 ml 1 M glucose, 10 ml 0.1 M L-cysteine HCl hydrate, 2 ml 10 percent yeast extract, 2 ml 10 percent Casamino acids, and five 1 ml stocks: trace element solution, FeCl2 solution, selenite-tungstate solution, trace vitamins solution, fatty acid mixture, and aromatic fatty acids solution. After pH adjustment, 4 ml 250 mM dithiothreitol solution is added per liter.

The reviewed record keeps the seven base rows at MediaDive's final-volume-adjusted g/L values, but then flattens almost every post-autoclave solution:

- Volume additions for NaHCO3, glucose, L-cysteine, yeast extract, Casamino acids, and dithiothreitol are encoded as `30`, `5`, `10`, `2`, `2`, and `4` g/L.
- FeCl2 solution, trace element solution, selenite-tungstate solution, fatty acid mixture, and aromatic fatty acids solution are expanded at stock strength.
- Aromatic fatty acids solution contributes the impossible merged `NaOH` value `100.4 G_PER_L` by adding 100 ml of 20 mM NaOH solution to the 0.4 g/L NaOH row from selenite-tungstate solution.
- The required trace vitamins solution is retained only as an empty `solutions` shell with `1 G_PER_L`.

JCM Medium 266 defines fatty acid mixture with valeric acid, isovaleric acid, alpha-methylbutyric acid, and isobutyric acid, but the reviewed record omitted alpha-methylbutyric acid. JCM Medium 187 supports the FeCl2 and trace-element stock recipes; JCM Medium 431 supports selenite-tungstate; JCM Medium 284 supports trace vitamins.

The JCM 1051 source does not contain LB Medium, LB Miller, tryptone, 10 g/L NaCl, or 5 g/L yeast extract. Those rows and the generic LB commercial-product provenance are unsupported additions.

## Completeness

The record is incomplete because source stock boundaries are missing or empty, one fatty-acid component is absent, and three LB-derived rows add unsupported composition. A user following the flat ingredient table would prepare the wrong medium by orders of magnitude.

No organism-growth claim, strain-specific claim, DOI, or PMID is present. Those empty optional areas are not defects for this imported JCM recipe. Exact local discovery used `find`, which includes ignored files, and found only the direct MediaDive/JCM owner plus the TOGO M1118 sibling for the same JCM medium.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | Post-autoclave solution additions are flattened at stock strength. | JCM 1051 adds bicarbonate, glucose, cysteine, yeast extract, Casamino acids, DTT, trace elements, FeCl2, selenite-tungstate, fatty acids, and aromatic fatty acids as volume additions after autoclaving; the reviewed record lists these as final g/L rows. | `data/normalized_yaml/bacterial/endomicrobium_proavitum_rsa_medium.yaml` |
| major | Unsupported LB Miller constituents were added. | JCM 1051 has no LB Medium or tryptone row; the reviewed record appends 10 g/L tryptone, 5 g/L yeast extract, and 10 g/L sodium chloride with a generic LB Miller product note. | `data/normalized_yaml/bacterial/endomicrobium_proavitum_rsa_medium.yaml` |
| major | Trace vitamins are an empty gram-per-liter solution. | JCM 1051 adds 1 ml trace vitamins solution from JCM Medium 284; the reviewed record stores `Trace vitamins solution (see Medium No. 284)` with empty `composition` and `unit: G_PER_L`. | `data/normalized_yaml/bacterial/endomicrobium_proavitum_rsa_medium.yaml` |
| major | Alpha-methylbutyric acid is missing from Fatty acid mixture. | JCM Medium 266 and MediaDive's `Fatty acid mixture` include valeric acid, isovaleric acid, alpha-methylbutyric acid, and isobutyric acid; the reviewed record has the other three but lacks alpha-methylbutyric acid. | `data/normalized_yaml/bacterial/endomicrobium_proavitum_rsa_medium.yaml` |
| major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | The trace-element source row is nickel chloride hexahydrate; the reviewed row links `CHEBI:34887` / `nickel dichloride`. | `data/normalized_yaml/bacterial/endomicrobium_proavitum_rsa_medium.yaml` |

## Recommended Edits

1. Remove the unsupported LB Miller decomposition and its supplier-catalog prose from `data/normalized_yaml/bacterial/endomicrobium_proavitum_rsa_medium.yaml`.
2. Restore all JCM 1051 post-autoclave additions as volume-based solutions instead of final g/L ingredient rows.
3. Populate FeCl2, trace element, selenite-tungstate, trace vitamins, fatty acid, and aromatic fatty acid stock compositions from JCM 187, 431, 284, 266, and 1051.
4. Add alpha-methylbutyric acid back to Fatty acid mixture.
5. Re-ground nickel chloride hexahydrate to a hydrate-specific term, or leave it ungrounded if no exact CHEBI term is available.
6. Regenerate merged YAML and downstream pages.

## Follow-up Checks

1. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/endomicrobium_proavitum_rsa_medium__51692939.yaml`.
2. Reopen JCM 1051 and the cross-referenced JCM 187, 431, 284, and 266 pages and manually verify every stock volume and component.
3. Confirm the regenerated record has no `LB Medium` supplier block and no 100.4 g/L NaOH artifact.

## Additional Notes

None found.
