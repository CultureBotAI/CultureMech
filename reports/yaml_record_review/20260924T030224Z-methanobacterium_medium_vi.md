# YAML Record Review: Methanobacterium Medium (VI)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_vi.yaml
- Started UTC: 2026-09-24T03:02:02Z
- Finished UTC: 2026-09-24T03:02:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:007622 |
| Label | methanobacterium_medium_vi |
| Original label | Methanobacterium Medium (VI) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_vi.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M1103_Methanobacterium_Medium_VI.yaml` |
| Merge lineage | `TOGO_M1103_Methanobacterium_Medium_VI` |
| Source identity | TOGO Medium M1103 / JCM Medium 1038 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_vi.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_vi.yaml --out /private/tmp/methanobacterium_medium_vi.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_vi.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_vi.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies TOGO M1103, the TOGO import of JCM Medium 1038, `METHANOBACTERIUM MEDIUM (VI)`. The live JCM 1038 page and MediaDive REST J1038 both define it as a variant of JCM Medium 872 that lowers the final NaCl to 0.4 g/l and allows replacement of sludge fluid with a human fecal extract. The generated merge contains one TOGO source owner, `TOGO_M1103_Methanobacterium_Medium_VI`.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M1103`, `JCM_M1038`, `GRMD=1038`, and `mediadive.medium:J1038` found this TOGO owner plus a separate normalized MediaDive J1038 owner at `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml`.

## Evidence

TOGO M1103 expands the M872 formulation into a full basal ingredient table with 0.4 g/l NaCl and carries forward six M872 stock additions: 1 ml FeCl2 solution, 1 ml trace element solution, 50 ml sludge fluid, 20 ml fatty acid mixture, 10 ml 5% Na2S x 9 H2O, and 10 ml 5% L-cysteine HCl H2O. The YAML stores all six additions as empty `solutions` entries with their milliliter values coerced to `G_PER_L`.

The water and resazurin rows are dimensionally wrong. TOGO lists 930 ml distilled water and 1 mg resazurin; the YAML stores `930 G_PER_L` and `1 G_PER_L`.

The M1103-specific human fecal extract alternative is absent. JCM 1038 and MediaDive J1038 state that sludge fluid can be replaced with a human fecal extract made by autoclaving equal quantities of feces and water, centrifuging, adjusting the supernatant to pH 7.0-7.2, and sterilizing it under N2.

The M872-derived preparation context was not structured. TOGO M1103 preserves the inherited H2-CO2 cooling, NaHCO3 post-boil addition, dispensing, autoclaving, prior-to-inoculation stock additions, and 200 kPa H2-CO2 pressurization text, but the generated record has no `preparation_steps`; H2, CO2, and N2 appear as variable final-medium ingredients.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. The inspected JCM, TOGO, and MediaDive records are source formulations, not primary growth studies.

The source explicitly defines M1103/J1038 as an M872 variant, but the generated record has no parent/variant relationship to TOGO M911 or the MediaDive J872/J1038 owners.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Six stock additions were encoded as gram-per-liter concentrations. | TOGO M1103 gives milliliter additions for FeCl2 solution, trace element solution, sludge fluid, fatty acid mixture, 5% Na2S x 9 H2O, and 5% L-cysteine HCl H2O; every row appears in `solutions` with `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1103_Methanobacterium_Medium_VI.yaml`, or the TOGO unit parser. |
| major | Referenced FeCl2, trace-element, sludge-fluid, fatty-acid, sulfide, and cysteine stocks are empty anonymous solutions. | The six `solutions` entries have `composition: []` and `name: Unknown solution`, so the M180, M911, M258, sulfide, and cysteine stock definitions are not represented. | `data/normalized_yaml/archaea/TOGO_M1103_Methanobacterium_Medium_VI.yaml`, or the TOGO solution migrator. |
| major | Resazurin and distilled water were imported with mass units. | TOGO M1103 gives 1 mg resazurin and 930 ml distilled water; the YAML stores `1 G_PER_L` and `930 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1103_Methanobacterium_Medium_VI.yaml`, or the TOGO unit parser. |
| major | Gas-atmosphere and preparation details were dropped. | The source specifies H2-CO2 80:20 for cooling, dispensing, and 200 kPa final pressurization, and N2 for stock storage and fecal-extract sterilization; the YAML lists H2, CO2, and N2 as ordinary `ingredients` and has no structured preparation. | `data/normalized_yaml/archaea/TOGO_M1103_Methanobacterium_Medium_VI.yaml`, or the TOGO comment importer. |
| major | The JCM 1038 variant relationship and human-fecal-extract alternative were omitted. | JCM 1038 is defined as Medium 872 with final 0.4 g/l NaCl and states that sludge fluid can be replaced by a prepared human fecal extract; the YAML has no parent link to M872 and no representation of the alternative extract. | `data/normalized_yaml/archaea/TOGO_M1103_Methanobacterium_Medium_VI.yaml`, or variant-link curation for JCM/TOGO media. |
| major | The same JCM recipe is represented by a duplicate MediaDive owner. | `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml` also imports JCM Medium 1038 through MediaDive J1038 and renders as `data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml`. | Merge/de-duplication logic for JCM media imported through both MediaDive and TOGO. |

## Recommended Edits

1. Preserve FeCl2 solution, trace element solution, sludge fluid, fatty acid mixture, 5% Na2S x 9 H2O, and 5% L-cysteine HCl H2O as structured additions with their source milliliter addition volumes.
2. Populate or link exact stock definitions for the M180 FeCl2 and trace-element stocks, M911 sludge fluid, the M258 fatty acid mixture, and the sulfide and cysteine stocks.
3. Preserve the 930 ml water and 1 mg resazurin source units instead of coercing them to `G_PER_L`.
4. Add the JCM 872 preparation context, the final 0.4 g/l NaCl variant difference, and the human-fecal-extract sludge-fluid alternative at the right scope.
5. Link M1103/J1038 to its M872 parent and reconcile this TOGO owner with the MediaDive J1038 owner so JCM Medium 1038 has one canonical merged output.
6. Regenerate `data/merge_yaml/merged/methanobacterium_medium_vi.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected TOGO M1103 owner and regenerated merged file.
2. Compare the regenerated recipe against JCM Medium 1038, TOGO M1103, MediaDive J1038, and JCM Medium 872 to confirm only the M1103-specific NaCl and sludge-fluid alternative differ from the parent.
3. Re-run an exact duplicate search for `TOGO:M1103`, `mediadive.medium:J1038`, and `GRMD=1038` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated page to confirm the M872 stock additions and the human-fecal-extract alternative display at the right scope.

## Additional Notes

None found.
