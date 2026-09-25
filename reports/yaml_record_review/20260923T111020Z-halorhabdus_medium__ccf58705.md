# YAML Record Review: HALORHABDUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halorhabdus_medium__ccf58705.yaml`
- Started UTC: 2026-09-23T11:08:00Z
- Finished UTC: 2026-09-23T11:10:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002651` |
| Name | `halorhabdus_medium` |
| Original name | `HALORHABDUS MEDIUM` |
| Category | `archaea` |
| Generated from | `data/normalized_yaml/archaea/halorhabdus_medium.yaml` |
| Source accession | `mediadive.medium:J294` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=294` |
| Merge fingerprint | `ccf58705821e62e8e70efd2d8e790adfe9a6bab96f7c471cfd7bc98c392b0551` |

I reviewed the generated merged record, its direct normalized owner, the JCM
294 HTML, and the MediaDive REST payload for `J294`.

I also searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `mediadive.medium:J294`,
`jcm_grmd?GRMD=294`, `GRMD=294`, `HALORHABDUS MEDIUM`, and
`halorhabdus_medium`. Ignored files were included. The search found this
direct MediaDive/JCM branch, a separate Togo `M288` branch derived from the
same JCM URL, the corresponding generated records, and incidental BM for
Tepidanaerobacter references to JCM 294; only `halorhabdus_medium.yaml` feeds
the reviewed `halorhabdus_medium__ccf58705.yaml` record.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halorhabdus_medium__ccf58705.yaml` reported `No issues found`. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halorhabdus_medium__ccf58705.yaml --out /private/tmp/halorhabdus_medium_ccf58705.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halorhabdus_medium__ccf58705.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halorhabdus_medium__ccf58705.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The top-level identity is correct. The record is the MediaDive import of JCM
medium 294, and the JCM page names the source recipe `HALORHABDUS MEDIUM`.
MediaDive `J294` resolves to the same JCM URL and the same pH 7.0, 1 L liquid
main solution.

Most direct main-medium salts retain exact JCM quantities and plausible
grounding:

| Ingredient | Source amount per 1 L | Generated amount |
|---|---:|---:|
| `NaCl` | 270 g | 270 g/L |
| `NaBr` | 0.1 g | 0.1 g/L |
| `MgSO4 x 7 H2O` | 20 g | 20 g/L |
| `KCl` | 5 g | 5 g/L |
| `NH4Cl` | 2 g | 2 g/L |
| `Tris-HCl buffer` | 12 g | 12 g/L |
| `Yeast extract` | 1 g | 1 g/L |
| `Glucose` | 2 g | 2 g/L |
| `KH2PO4` | 0.125 g | 0.125 g/L |
| `CaCl2 x 2 H2O` | 0.05 g | 0.05 g/L |

One chemical grounding is a near miss: the source and MediaDive both specify
`NiCl2 x 6 H2O`, but the generated record grounds that ingredient to generic
`CHEBI:34887` / `nickel dichloride` rather than the exact hexahydrate form.

## Evidence

The JCM source and the MediaDive JSON agree that JCM 294 contains 2 ml of a
separate trace metal solution in the 1 L main medium. The stock solution itself
contains 10 ml 32% HCl, 2 g `FeCl2 x 4 H2O`, 0.25 g `CoCl2 x 6 H2O`, 0.1 g
`MnCl2 x 4 H2O`, 0.07 g `ZnCl2`, 0.006 g `H3BO3`, 0.04 g
`Na2MoO4 x 2 H2O`, 0.07 g `NiCl2 x 6 H2O`, 0.002 g `CuCl2 x 2 H2O`,
0.025 g `AlCl3`, 0.006 g `Na2WO4 x 2 H2O`, and 1 L distilled water.

Those trace-stock compounds are not final-medium g/L ingredients. The generated
record flattens the MediaDive `g_l` values from the 1010 ml stock solution into
the final medium at full stock strength. It also sums stock and main additions
for the two duplicated metals:

| Generated ingredient | Generated amount | Source scope |
|---|---:|---|
| `FeCl2 x 4 H2O` | 1.9852 g/L | Unsupported merge of 5 mg in the main solution plus 1.9802 g/L in the trace stock. |
| `MnCl2 x 4 H2O` | 0.1040099 g/L | Unsupported merge of 5 mg in the main solution plus 0.0990099 g/L in the trace stock. |
| `HCl` | 3.16832 g/L | The MediaDive concentration inside the 1010 ml stock, not the 2 ml/L final-medium contribution. |
| `CoCl2 x 6 H2O` | 0.247525 g/L | The trace-stock concentration, not a top-level final-medium concentration. |
| `ZnCl2` | 0.0693069 g/L | The trace-stock concentration, not a top-level final-medium concentration. |
| `H3BO3` | 0.00594059 g/L | The trace-stock concentration, not a top-level final-medium concentration. |
| `Na2MoO4 x 2 H2O` | 0.039604 g/L | The trace-stock concentration, not a top-level final-medium concentration. |
| `NiCl2 x 6 H2O` | 0.0693069 g/L | The trace-stock concentration, not a top-level final-medium concentration. |
| `CuCl2 x 2 H2O` | 0.0019802 g/L | The trace-stock concentration, not a top-level final-medium concentration. |
| `AlCl3` | 0.0247525 g/L | The trace-stock concentration, not a top-level final-medium concentration. |
| `Na2WO4 x 2 H2O` | 0.00594059 g/L | The trace-stock concentration, not a top-level final-medium concentration. |

The preparation evidence is also over-scoped. JCM instructs the curator to add
components except yeast extract to distilled water, bring the volume to 1.0 L,
adjust to pH 7.0 with NaOH, filter-sterilize that mineral solution, autoclave
the yeast extract as a 10% w/v solution, and then aseptically add it. The
generated record stores the entire sentence as one `AUTOCLAVE` step, which
misstates the sterilization boundary.

## Completeness

The record is missing the 1 L distilled-water final-volume context from the
main recipe, the distilled water used to make the trace metal stock, and the
explicit 2 ml/L trace-stock reference that keeps stock amounts separate from
final-medium concentrations.

It also drops the `BD-Difco` qualifier on yeast extract from both the JCM source
text and the MediaDive `attribute` field.

No target organisms, growth evidence, incubation temperature, atmosphere, or
variant claims are present in the reviewed record. Those empty optional fields
are not defects in this source-only MediaDive import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The trace metal solution was flattened into final-medium `ingredients` at stock g/L concentration. | JCM lists `Trace metal solution (see below)` as a 2 ml main-medium addition and lists the HCl, Fe, Co, Mn, Zn, B, Mo, Ni, Cu, Al, W, and water rows under a separate trace-metal table. MediaDive preserves the same boundary as solution `3995` referenced by solution `3994` at 2 ml. | `data/normalized_yaml/archaea/halorhabdus_medium.yaml` or the MediaDive importer that produced it |
| Major | Main `FeCl2 x 4 H2O` and `MnCl2 x 4 H2O` were merged with chemically identical stock ingredients from a different solution scope. | JCM has 5 mg of each compound in the main 1 L medium and different Fe/Mn quantities inside the trace metal stock. The generated notes record duplicate merges of `0.005, 1.9802` and `0.005, 0.0990099`. | `data/normalized_yaml/archaea/halorhabdus_medium.yaml` or the duplicate-ingredient merge logic |
| Major | Preparation is collapsed to one `AUTOCLAVE` action and therefore autoclave-scopes steps that JCM assigns to filtration or aseptic addition. | The source distinguishes pH adjustment, filter sterilization of the mineral solution, separate autoclaving of a 10% w/v yeast extract solution, and aseptic addition. | `data/normalized_yaml/archaea/halorhabdus_medium.yaml` or the MediaDive preparation importer |
| Major | Water and final-volume structure are incomplete. | JCM says to bring the main medium to 1.0 L with distilled water and includes 1.0 L distilled water inside the trace metal stock. Neither water row is represented, and no solution reference carries the 2 ml/L stock addition. | `data/normalized_yaml/archaea/halorhabdus_medium.yaml` or the MediaDive importer |
| Minor | `Yeast extract` is missing the source's `BD-Difco` qualifier. | JCM labels the ingredient `Yeast extract (BD-Difco)`, and MediaDive carries `attribute: "BD-Difco"`. The generated record keeps only `Yeast extract`. | `data/normalized_yaml/archaea/halorhabdus_medium.yaml` or the MediaDive importer |
| Minor | `NiCl2 x 6 H2O` is grounded to generic `nickel dichloride`. | The source ingredient is a hexahydrate; `CHEBI:34887` is labeled `nickel dichloride` in the generated record. | `data/normalized_yaml/archaea/halorhabdus_medium.yaml` or the ingredient resolver |

## Recommended Edits

1. In `data/normalized_yaml/archaea/halorhabdus_medium.yaml` or the MediaDive
   import transform, preserve the JCM 294 trace metal solution as a separate
   stock solution and reference it from the main medium at 2 ml/L.
2. Keep the standalone 5 mg main-medium `FeCl2 x 4 H2O` and
   `MnCl2 x 4 H2O` ingredients distinct from the Fe/Mn rows in the trace metal
   stock; do not merge ingredients across solution scopes.
3. Restore the main-medium 1 L distilled-water final-volume context and the
   1 L distilled-water row inside the trace metal solution.
4. Split the imported free-text preparation into ordered, scoped actions:
   build the mineral solution except yeast extract, adjust pH to 7.0 with
   NaOH, filter-sterilize the mineral solution, autoclave yeast extract as a
   10% w/v stock, and aseptically add that stock to the mineral solution.
5. Preserve the `BD-Difco` qualifier on yeast extract.
6. Ground `NiCl2 x 6 H2O` to an exact nickel chloride hexahydrate term if one
   is available in the packaged MIM/CHEBI resolver; otherwise leave it
   explicitly unresolved rather than broadening to an anhydrous salt.
7. Regenerate merged recipes from the normalized owner after the curated source
   or importer is fixed; do not patch `data/merge_yaml/merged/` directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/halorhabdus_medium.yaml`
   after the normalized record or importer is corrected.
2. Run `just validate-references data/normalized_yaml/archaea/halorhabdus_medium.yaml`
   and `just validate-terms data/normalized_yaml/archaea/halorhabdus_medium.yaml`
   to confirm source identifiers and exact hydrate grounding.
3. Run `just verify-merges` to prove the generated
   `data/merge_yaml/merged/halorhabdus_medium__ccf58705.yaml` output can be
   recreated from the maintained normalized source.
4. Manually compare the regenerated record against JCM 294 and MediaDive `J294`
   to confirm the trace metal stock remains separate and the mineral-solution,
   yeast-stock, filtration, and autoclave actions are no longer collapsed.

## Additional Notes

The sibling Togo `M288` branch is derived from the same JCM 294 URL but is not
merged into this fingerprint. It should be reviewed independently rather than
used as evidence that the direct MediaDive import is correct.
