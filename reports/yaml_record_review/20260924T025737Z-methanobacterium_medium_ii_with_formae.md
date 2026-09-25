# YAML Record Review: Methanobacterium Medium (II) With Formae

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_ii_with_formae.yaml
- Started UTC: 2026-09-24T02:57:13Z
- Finished UTC: 2026-09-24T02:57:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010133 |
| Label | methanobacterium_medium_ii_with_formae |
| Original label | Methanobacterium Medium (II) With Formae |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_ii_with_formae.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M725_Methanobacterium_Medium_II_With_Formae.yaml` |
| Merge lineage | `TOGO_M725_Methanobacterium_Medium_II_With_Formae` |
| Source identity | TOGO Medium M725 / JCM Medium 703 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_ii_with_formae.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_ii_with_formae.yaml --out /private/tmp/methanobacterium_medium_ii_with_formae.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_ii_with_formae.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_ii_with_formae.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies TOGO M725, a JCM Medium 703 record for a formate variant of Methanobacterium Medium (II). TOGO M725 reports the original source as `JCM_M703`, and MediaDive J703 reports the same medium name and JCM GRMD 703 URL. The generated merge contains one maintained TOGO owner, `TOGO_M725_Methanobacterium_Medium_II_With_Formae`.

The live JCM GRMD 703 URL now returns `Nothing found`, so the JCM page itself could not be used for formula verification. TOGO M725 preserves the expanded ingredient table and comments, and MediaDive J703 preserves the key variant instruction: use Medium No. 702, add 0.3% final sodium formate, and replace the gas phase with N2-CO2 80:20 at normal pressure.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M725`, `JCM_M703`, `GRMD=703`, and `mediadive.medium:J703` found this TOGO owner and a separate normalized MediaDive J703 owner at `data/normalized_yaml/archaea/methanobacterium_medium_ii_with_formae.yaml`.

## Evidence

TOGO M725 supports the basal M702 ingredient list plus 0.3% final sodium formate, but the formate concentration was lost. The API gives sodium formate as a 0.3% solution/final supplement and the comments describe Medium 702 supplemented with 0.3% final sodium formate; the YAML stores `sodium formate` as `VARIABLE`.

The M725 owner inherited the same unresolved stock additions as the preceding M724 owner. TOGO lists 10 ml trace minerals, 10 ml trace vitamins, 25 ml 8% NaHCO3, and 10 ml 3% Na2S x 9 H2O; the YAML stores them as empty `solutions` entries with `name: Unknown solution` and values of `10`, `10`, `25`, and `10 G_PER_L`.

The water and resazurin rows are dimensionally wrong. TOGO lists 1 L distilled water and 0.5 mg resazurin in the basal solution; the YAML stores `1 G_PER_L` and `0.5 G_PER_L`.

The TOGO M725 comments describe N2-CO2 80:20 as the cooling, dispensing, and final normal-pressure gas phase for the formate variant. The YAML instead represents carbon dioxide gas and nitrogen gas as variable final-medium ingredients.

The preparation comments were not migrated. The source includes the M702 boiling, cooling, dispensing, autoclaving, sterile anaerobic stock-addition, final pH check, and gas-pressurization steps plus the formate-specific gas replacement. None are represented as structured preparation or pH fields.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. The inspected TOGO and MediaDive records are source formulations, not primary growth studies.

The source explicitly defines M725/J703 as a variant of M702/J702, but the generated record has no parent/variant relationship to either `TOGO_M724_Methanobacterium_Medium_II` or the MediaDive J702 owner.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The 0.3% final sodium formate supplement was reduced to an unconstrained variable ingredient. | TOGO M725 and MediaDive J703 both scope the variant to a final 0.3% sodium formate supplement; the YAML stores `sodium formate` with `unit: VARIABLE`. | `data/normalized_yaml/archaea/TOGO_M725_Methanobacterium_Medium_II_With_Formae.yaml`, or the TOGO importer. |
| major | Several non-gram quantities were imported as gram-per-liter concentrations. | TOGO gives 1 L water, 0.5 mg resazurin, and four milliliter stock additions. The YAML stores water, resazurin, trace minerals, trace vitamins, bicarbonate stock, and sulfide stock with `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M725_Methanobacterium_Medium_II_With_Formae.yaml`, or the TOGO unit parser. |
| major | Stock additions are empty anonymous solutions. | The four `solutions` entries have `composition: []` and `name: Unknown solution`; the referenced trace stocks and the bicarbonate/sulfide stock percentages are not represented as structured stock recipes. | `data/normalized_yaml/archaea/TOGO_M725_Methanobacterium_Medium_II_With_Formae.yaml`, or the TOGO solution migrator. |
| major | N2-CO2 atmosphere requirements were modeled as variable final ingredients. | TOGO M725 uses N2-CO2 80:20 while cooling, dispensing, and replacing the final gas phase at normal pressure; the generated record represents `Nitrogen gas` and `Carbon dioxide gas` as ordinary `ingredients`. | `data/normalized_yaml/archaea/TOGO_M725_Methanobacterium_Medium_II_With_Formae.yaml`, or the TOGO importer. |
| major | Preparation, pH, and parent-variant context were dropped. | M725 is defined by the M702 base preparation plus sodium formate and a gas-phase replacement, but the YAML has no `preparation_steps`, pH field, or link to the M702 parent recipe. | `data/normalized_yaml/archaea/TOGO_M725_Methanobacterium_Medium_II_With_Formae.yaml`, or variant-link curation for JCM/TOGO media. |
| major | The same JCM variant is represented by a duplicate MediaDive owner. | `data/normalized_yaml/archaea/methanobacterium_medium_ii_with_formae.yaml` also imports MediaDive J703 / JCM Medium 703. | Merge/de-duplication logic for JCM media imported through both MediaDive and TOGO. |

## Recommended Edits

1. Restore sodium formate as a 0.3% final supplement instead of a variable ingredient.
2. Preserve the trace-mineral, trace-vitamin, bicarbonate, and sulfide additions as structured stock additions with milliliter addition volumes and stock concentrations.
3. Preserve 1 L water and 0.5 mg resazurin without converting them to `G_PER_L`.
4. Move the N2-CO2 gas mixture out of final `ingredients` and into preparation or atmosphere fields that preserve the 80:20 composition and normal-pressure final gas phase.
5. Add the M702-derived preparation sequence, pH check, and formate-specific gas replacement instructions to the maintained TOGO M725 owner.
6. Link the M725 record to its M702 parent and reconcile it with the MediaDive J703 owner so JCM Medium 703 has one canonical representation.
7. Regenerate `data/merge_yaml/merged/methanobacterium_medium_ii_with_formae.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected TOGO M725 owner and regenerated merged file.
2. Compare the regenerated recipe against TOGO M725, TOGO M724, MediaDive J703, and MediaDive J702 to confirm the formate supplement and N2-CO2 gas replacement are the only M725-specific differences.
3. Re-run an exact duplicate search for `TOGO:M725`, `mediadive.medium:J703`, and `GRMD=703` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated page to confirm the formate supplement, gas phase, stock additions, and M702 parent relationship display at the right scope.

## Additional Notes

The JCM GRMD 703 URL was checked directly and returned `Nothing found`; formula review therefore relied on TOGO's preserved M725 payload and MediaDive J703.
