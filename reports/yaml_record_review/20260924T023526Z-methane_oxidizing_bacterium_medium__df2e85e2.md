# YAML Record Review: METHANE OXIDIZING BACTERIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methane_oxidizing_bacterium_medium__df2e85e2.yaml
- Started UTC: 2026-09-24T02:35:08Z
- Finished UTC: 2026-09-24T02:35:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002875 |
| Name | methane_oxidizing_bacterium_medium |
| Original name | METHANE OXIDIZING BACTERIUM MEDIUM |
| Category | bacterial |
| Medium term | mediadive.medium:J524, JCM Medium J524 |
| Source | JCM via MediaDive |
| Source URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=524 |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/methane_oxidizing_bacterium_medium.yaml |
| Merge fingerprint | df2e85e2d1654267e054d301884df965a48932f61e414ee307541611620695e5 |

This generated record is a single-source merge from `data/normalized_yaml/bacterial/methane_oxidizing_bacterium_medium.yaml`.
Future fixes belong in that maintained MediaDive/JCM owner, the MediaDive import path that flattened nested solutions, or source-alias rules that merge its TOGO M525 duplicate, then in regenerated `data/merge_yaml/merged/` outputs.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methane_oxidizing_bacterium_medium__df2e85e2.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methane_oxidizing_bacterium_medium__df2e85e2.yaml --out /private/tmp/methane_oxidizing_bacterium_medium__df2e85e2.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methane_oxidizing_bacterium_medium__df2e85e2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methane_oxidizing_bacterium_medium__df2e85e2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The MediaDive identity is correct: REST medium `J524` is named `METHANE OXIDIZING BACTERIUM MEDIUM`, links to JCM `GRMD=524`, and carries pH 6.2 for this defined bacterial medium.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found two maintained MediaRecipe owners for the same JCM 524 source: this MediaDive owner at `data/normalized_yaml/bacterial/methane_oxidizing_bacterium_medium.yaml` and the TOGO owner at `data/normalized_yaml/bacterial/TOGO_M525_Methane_Oxidizing_Bacterium_Medium.yaml`. No third exact MediaRecipe owner or generated medium was found in that bounded, ignored-file-inclusive search; the remaining J524 hits were indexes and the MediaDive `Main sol. J524` SolutionRecipe.

The ChEBI groundings are generally plausible for the stated salts and vitamins, but many of those terms are attached to rows at the wrong structural level because trace-mineral and vitamin stocks were flattened into the final medium.

## Evidence

The JCM 524 page and MediaDive payload agree on a main 1000 ml aqueous medium with 30 g NaCl, 0.14 g KH2PO4, 0.8 g CaCl2 x 2 H2O, 3.4 g MgSO4 x 7 H2O, 4.2 g MgCl2 x 6 H2O, 0.33 g KCl, 0.25 g NaNO3, 0.25 g NH4Cl, 0.2 g Na2SiO3 x 9 H2O, 20 mg Fe2(SO4)3 x n H2O, 0.5 mg Na2SeO3 x 5 H2O, and 0.5 mg NiCl2 x 6 H2O.

MediaDive correctly normalizes those main rows over its 1016 ml final-volume accounting. It also preserves the JCM instructions to adjust pH to 6.0 - 6.5 before autoclaving, add filter-sterilized solutions after cooling, use an N2-CO2 4:1 gas mix, pressurize the vessel with methane to 200 kPa, add O2 to 2% in the gas phase, and readjust pH to 6.0 - 6.3 if needed.

Several generated ingredient rows are unsupported:

- The source adds 3 ml Trace mineral solution and 1 ml Trace vitamins; the YAML flattens every mineral and vitamin stock component as a final-medium `G_PER_L` ingredient at the stock concentration.
- The source adds 10 ml of 5% NaHCO3 solution; the YAML records `NaHCO3` as `10 G_PER_L`, which is the source volume with the wrong dimension and no 5% stock-strength context.
- The source adds 2 ml of 1 mM CuSO4 solution; the YAML records `CuSO4` as `2 G_PER_L`, again copying a milliliter volume into a gram-per-litre concentration.
- The trace-mineral stock's nitrilotriacetic acid / KOH pH adjustment is appended as a final-medium preparation step, but it belongs to the stock.

## Completeness

The final-medium gas handling is present in prose rather than gas ingredients; that is acceptable because the JCM source states methane, N2-CO2, and O2 as headspace handling steps rather than formula solutes.

No target-organism, strain, literature growth, or variant claims are present, so there were no growth-evidence assertions to check.

The record has no `solutions` entry for the four filter-sterilized additions named by the source, so the preparation step refers to stocks that no longer exist structurally.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace mineral stock and Trace vitamins were flattened into final-medium ingredients at stock strength. | JCM 524 adds 3 ml Trace mineral solution and 1 ml Trace vitamins after cooling. The generated YAML records all trace mineral and vitamin compounds as direct `ingredients` with stock `g/L` values. | `data/normalized_yaml/bacterial/methane_oxidizing_bacterium_medium.yaml` and MediaDive importer stock handling. |
| Major | Liquid bicarbonate and copper sulfate additions use milliliter volumes as `G_PER_L` concentrations. | The source rows are 10 ml of 5% NaHCO3 solution and 2 ml of 1 mM CuSO4 solution; the YAML records `NaHCO3` at `10 G_PER_L` and `CuSO4` at `2 G_PER_L`. | `data/normalized_yaml/bacterial/methane_oxidizing_bacterium_medium.yaml`. |
| Major | The trace-mineral preparation step is scoped to the final medium. | The KOH pH-adjustment step belongs to the Trace mineral solution recipe, but the YAML appends it as top-level `preparation_steps[3]` after the final-medium gas-handling step. | `data/normalized_yaml/bacterial/methane_oxidizing_bacterium_medium.yaml`. |
| Major | JCM 524 is duplicated through MediaDive and TOGO import paths. | This owner and `data/normalized_yaml/bacterial/TOGO_M525_Methane_Oxidizing_Bacterium_Medium.yaml` both cite JCM `GRMD=524` and merge to separate generated files. | Source aliasing for MediaDive J524 and TOGO M525, plus a regenerated merge. |

## Recommended Edits

1. Preserve Trace mineral solution and Trace vitamins as nested stock recipes dosed at 3 ml and 1 ml, respectively.
2. Represent 10 ml of 5% NaHCO3 solution and 2 ml of 1 mM CuSO4 solution as liquid additions with stock strengths, not as `10 G_PER_L` and `2 G_PER_L` direct ingredients.
3. Attach the nitrilotriacetic acid / KOH pH adjustment to Trace mineral solution.
4. Add a source alias between MediaDive J524 and TOGO M525 so one generated Methane Oxidizing Bacterium Medium record is emitted for JCM 524.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/methane_oxidizing_bacterium_medium.yaml` and the regenerated merge output.
- Compare the regenerated final-medium rows and post-autoclave additions against live JCM `GRMD=524`, including the 3 ml, 1 ml, 10 ml, and 2 ml liquid addition rows.
- Search the regenerated YAML for exact unsupported concentrations `10 G_PER_L` on `NaHCO3` and `2 G_PER_L` on `CuSO4`; neither should remain.
- Search `data/merge_yaml/merged` with ignored files included for exact `GRMD=524`, `mediadive.medium:J524`, and `TOGO:M525` after merge regeneration; the same JCM source should not publish as both a MediaDive and TOGO record.

## Additional Notes

The TOGO M525 sibling has a different import failure: it leaves all four filter-sterilized additions as empty solution stubs and misimports the three milligram main rows as grams per litre. Fixing both import paths should still preserve the gas-phase preparation text from the MediaDive/JCM source.
