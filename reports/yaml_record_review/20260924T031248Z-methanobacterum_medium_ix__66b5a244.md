# YAML Record Review: METHANOBACTERUM MEDIUM (IX)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml
- Started UTC: 2026-09-24T03:12:03Z
- Finished UTC: 2026-09-24T03:12:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002320 |
| Label | methanobacterum_medium_ix |
| Original label | METHANOBACTERUM MEDIUM (IX) |
| Category | bacterial |
| Generated path | `data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` |
| Merge lineage | `methanobacterum_medium_ix` |
| Source identity | MediaDive `J1147`; JCM Medium 1147 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml --out /private/tmp/methanobacterum_medium_ix__66b5a244.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record is the MediaDive import of JCM Medium 1147. MediaDive `J1147` and the live JCM `GRMD=1147` page agree on the misspelled `METHANOBACTERUM MEDIUM (IX)` label and on the same base recipe, post-cooling stock additions, pre-inoculation reductant additions, pH 7.5 readjustment, and 100 kPa H2-CO2 pressurization.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `mediadive.medium:J1147`, `TOGO:M1229`, `JCM_M1147`, `GRMD=1147`, `CultureMech:002320`, and `CultureMech:007757` found only the expected MediaDive J1147 owner and generated file plus the TOGO M1229 duplicate.

## Evidence

MediaDive `J1147` keeps its stock topology in the source payload: FeCl2 solution `3846`, trace element solution `3847`, fatty-acid mixture `3954`, and selenite-tungstate solution `4172` are separate recipes, while the main solution adds 1 ml, 1 ml, 20 ml, and 0.5 ml of them, respectively.

The generated record flattens all four stocks. HCl and FeCl2 x 4 H2O from solution `3846`, seven trace salts from solution `3847`, three fatty acids from solution `3954`, and NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O from solution `4172` all appear as top-level final ingredients at stock strength.

The fatty-acid mixture is incomplete. MediaDive solution `3954` has valeric acid, isovaleric acid, alpha-Methylbutyric acid, and isobutyric acid; the generated record has the other three fatty acids but dropped alpha-Methylbutyric acid.

Milliliter additions are stored as gram-per-liter final concentrations. The 50 ml 8% NaHCO3 stock, 6.3 ml 50% methanol stock, and two 10 ml 5% reductant stock additions appear as `50 G_PER_L`, `6.3 G_PER_L`, `10 G_PER_L`, and `10 G_PER_L` ingredient rows.

Unrelated LB Medium constituents contaminate the JCM recipe. JCM 1147 and MediaDive J1147 contain only a 1 g yeast-extract source row and do not contain LB Medium, tryptone, a separate 5 g/L LB yeast extract, or a 10 g/L LB sodium chloride row.

The fatty-acid stock's NaOH pH adjustment is scoped as a final-medium pH step. MediaDive attaches "Adjust pH to 7.5 with concentrated NaOH solution" to solution `3954`; the generated record emits it as `preparation_steps[3]` on the main medium.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. JCM 1147, TOGO M1229, and MediaDive J1147 are formulation sources, not primary growth studies.

MediaDive has enough structure to recover the intended record: all stock recipes and the three main-medium preparation steps are in the source JSON. The current normalized owner lost those stock boundaries and introduced non-source LB rows.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Four MediaDive stocks were flattened into the final ingredient list. | FeCl2 solution `3846`, trace element solution `3847`, fatty-acid mixture `3954`, and selenite-tungstate solution `4172` are separate MediaDive recipes but their members appear as top-level generated ingredients. | `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` |
| blocker | Milliliter stock additions are represented as gram-per-liter ingredient amounts. | The main recipe adds 50 ml 8% NaHCO3, 6.3 ml 50% methanol, and two 10 ml 5% reductant stocks; the generated record emits those as `50 G_PER_L`, `6.3 G_PER_L`, and two `10 G_PER_L` rows. | `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` |
| major | Unrelated LB Medium constituent rows contaminate the JCM 1147 formula. | The source has no tryptone, full-strength LB yeast extract, or full-strength LB sodium chloride rows, but the generated record includes all three with LB Medium supplier notes. | `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` |
| major | The fatty-acid stock is missing alpha-Methylbutyric acid. | MediaDive solution `3954` contains four fatty acids; only valeric, isovaleric, and isobutyric acids survived in the generated top-level list. | MediaDive stock importer for `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` |
| major | Stock-local NaOH and stock pH preparation are attached to the final recipe. | NaOH belongs to selenite-tungstate solution `4172`, and the pH 7.5 adjustment with concentrated NaOH belongs to fatty-acid mixture `3954`, not to the final JCM 1147 medium. | MediaDive stock importer for `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` |
| minor | The same JCM 1147 source has a separate TOGO duplicate. | An exact hidden/ignored search found TOGO `M1229` and MediaDive `J1147` owners for the same `GRMD=1147` source URL. | De-duplication between MediaDive and TOGO JCM imports. |
| minor | The normalized owner is filed under `bacterial`, even though it is a methanogen medium from the Methanobacterium series. | The MediaDive owner path is `data/normalized_yaml/bacterial/...`, while the neighboring Methanobacterium medium records are archaeal methanogen recipes. | `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` |

## Recommended Edits

1. Rebuild FeCl2 solution `3846`, trace element solution `3847`, fatty-acid mixture `3954`, and selenite-tungstate solution `4172` as structured stock recipes linked from the main medium.
2. Represent 8% NaHCO3, 50% methanol, 5% Na2S x 9 H2O, and 5% L-Cysteine HCl x H2O as milliliter stock additions instead of final `G_PER_L` chemical rows.
3. Remove the non-source LB Medium tryptone, yeast-extract, and sodium-chloride rows.
4. Restore alpha-Methylbutyric acid to the fatty-acid mixture and keep the mixture's concentrated-NaOH pH adjustment scoped to that stock.
5. Keep NaOH scoped to the selenite-tungstate stock instead of publishing it as a final ingredient.
6. Review the category and normalized path; this record likely belongs under `archaea`, not `bacterial`.
7. Merge the corrected MediaDive J1147 and TOGO M1229 owners as true source duplicates, then regenerate `data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml`.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against both corrected normalized owners and regenerated merged files.
2. Compare the regenerated record against MediaDive `J1147` to confirm stock recipes `3846`, `3847`, `3954`, and `4172` remain structured.
3. Compare the rendered page against JCM 1147 to confirm the post-cooling stock table, the pre-inoculation reductant table, and the pH 7.5/100 kPa H2-CO2 final instruction remain visible.
4. Re-run exact duplicate searches for `mediadive.medium:J1147`, `TOGO:M1229`, and `GRMD=1147` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.

## Additional Notes

None found.
