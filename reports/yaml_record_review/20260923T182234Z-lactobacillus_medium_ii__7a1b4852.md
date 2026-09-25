# YAML Record Review: Lactobacillus Medium II

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml
- Started UTC: 2026-09-23T18:21:51Z
- Finished UTC: 2026-09-23T18:22:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml` |
| Generated status | Generated canonical merge from `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml`; do not edit directly |
| Schema class | `MediaRecipe` |
| CultureMech ID | `CultureMech:010429` |
| Name | `lactobacillus_medium_ii` |
| Original name | `Lactobacillus Medium II` |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Source accession | `TOGO:M9` |
| Merge fingerprint | `7a1b4852c880736621b1e3100e91856a78d1a998ab0674b209fb4e4b81e7780c` |
| Maintained owner inspected | `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml` |

The reviewed YAML is the generated TOGO M9 record for JCM `GRMD=16`. It
contains a stale duplicate-water sum that was repaired upstream on September 2,
and both the generated record and the maintained normalized owner still flatten
JCM's nested `Salt solution R` stock into final-medium ingredient rows.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml` | Passed; no output |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml --out /private/tmp/lactobacillus_medium_ii__7a1b4852.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:010429` and `TOGO:M9` identify the TOGO import of JCM
  `GRMD=16`, `Lactobacillus Medium II`, at pH 6.3.
- The live JCM `GRMD=16` page is available and matches the TOGO M9 identity.
- MediaDive `J16` / `CultureMech:002529` is the same JCM original recipe
  through a different source transform, and it remains generated separately as
  `data/merge_yaml/merged/LACTOBACILLUS_MEDIUM_II.yaml`.
- KH2PO4, K2HPO4, sodium acetate, polysorbate 80, glucose, agar, magnesium
  sulfate heptahydrate, and iron(2+) sulfate heptahydrate groundings match their
  source labels.
- `MnSO4 xH2O` is intentionally grounded to generic manganese(II) sulfate; the
  source leaves the hydrate count variable.

An ignored-inclusive search with digit-bounded `TOGO:M9` and `GRMD=16` patterns
covered `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`. It
found the reviewed generated target, the current normalized `TOGO:M9` owner,
normalized source indexes, old archive references, the same-JCM
`JCM_J16_LACTOBACILLUS_MEDIUM_II.yaml` owner, and the separate generated
`LACTOBACILLUS_MEDIUM_II.yaml` output. It also found TOGO M14 because that
record is literally named `Lactobacillus Medium III`, not because the source
identifier patterns matched it.

## Evidence

Supported in inspected sources:

- The live JCM `GRMD=16` page lists Trypticase peptone 10 g, Yeast extract 5 g,
  Tryptose 3 g, KH2PO4 3 g, K2HPO4 3 g, 5 ml Salt solution R, Tween 80 1 ml,
  Sodium acetate 1 g, L-Cysteine HCl H2O 0.2 g, Agar 20 g, Glucose 5 g, and
  Distilled water 1 L in the main recipe, then says to adjust pH to 6.3.
- The same JCM page defines Salt solution R separately as MgSO4 7H2O 11.5 g,
  FeSO4 7H2O 0.68 g, MnSO4 xH2O 2.4 g, and Distilled water 1 L, with storage at
  4C.
- The JCM page states a default sterilization instruction of autoclaving media
  at 121 C for 15 minutes unless otherwise stated.
- Live TOGO M9 and MediaDive J16 both reproduce the same source boundary:
  5 ml Salt solution R in the main medium and a separate Salt solution R stock
  formula.

Unsupported or stale in the generated target:

- The generated target records the Salt solution R stock components as direct
  final-medium ingredients at stock concentration, then leaves an empty
  `solutions` entry for `Salt solution R`.
- The `Salt solution R` solution entry uses `5 G_PER_L`; JCM, TOGO, and
  MediaDive all report 5 ml of this stock.
- The generated target's `Distilled water` row is a stale duplicate sum,
  `2.0 G_PER_L`. The normalized owner has already collapsed it to `1.0`, but
  its unit is still wrong for a 1 L source volume.
- The target omits pH 6.3, the JCM default autoclave condition, the stock
  storage condition, and a `references` list.

## Completeness

Consequential gaps:

- The nested Salt solution R composition is not represented correctly.
- Main-medium and stock-solution water rows need to retain their source volume
  units instead of `G_PER_L`.
- The TOGO M9 and MediaDive J16 records are duplicate imports of the same JCM
  page but are not reconciled.
- Source-supported pH, autoclave, storage, and reference fields are absent.

Empty or absent fields that are not defects for this generated JCM recipe:

- `target_organisms`, growth metrics, genome assembly, atmospheric conditions,
  and shelf-life fields can stay empty until strain-specific evidence is added.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Major | Salt solution R was flattened into direct final-medium mineral ingredients. | JCM, TOGO M9, and MediaDive J16 all show 5 ml Salt solution R as a main-medium addition and MgSO4 7H2O, FeSO4 7H2O, MnSO4 xH2O, and water as a separate stock recipe. | `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml`, or the TOGO solution migrator if this flattening is systemic. |
| Major | The generated target carries a malformed empty solution row for Salt solution R. | The row has `composition: []`, `name: Unknown solution`, and `5 G_PER_L`; the source has a named stock solution with a 5 ml main-medium addition and four composition rows. | `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml`. |
| Major | Distilled water is stale and dimensionally wrong. | The generated row sums two duplicate 1.0 values into `2.0 G_PER_L`; the September 2 normalized repair collapsed the duplicate to `1.0`, but the source amount is 1 L, not a gram-per-liter concentration. | Regenerate `data/merge_yaml/merged/` for the stale sum, then fix water units in `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml`. |
| Major | pH, sterilization, storage, and references are missing. | JCM and TOGO support pH 6.3; JCM states default autoclaving at 121 C for 15 minutes and `Store at 4C` for Salt solution R. | `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml`. |
| Major | The same JCM `GRMD=16` recipe is duplicated as TOGO M9 and MediaDive J16 records. | Ignored-inclusive search found `data/normalized_yaml/bacterial/JCM_J16_LACTOBACILLUS_MEDIUM_II.yaml` and `data/merge_yaml/merged/LACTOBACILLUS_MEDIUM_II.yaml`; live MediaDive J16 and TOGO M9 both point to the same JCM URL. | Reconcile the two normalized owners through a source-identity or merge rule before regenerating the merge layer. |

## Recommended Edits

1. Rebuild `Salt solution R` as a nested stock in
   `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml`: the
   main medium should add 5 ml, and the stock composition should contain
   MgSO4 7H2O 11.5 g/L, FeSO4 7H2O 0.68 g/L, MnSO4 xH2O 2.4 g/L, and 1 L water.
2. Remove the stock-strength mineral salts from the top-level final-medium
   `ingredients` list once they are represented inside `Salt solution R`.
3. Correct all distilled-water source quantities so 1 L water is not modeled as
   `G_PER_L`; preserve enough detail to distinguish main-medium water from
   stock-solution water.
4. Add pH 6.3, the JCM default autoclave preparation, Salt solution R storage
   at 4C, and JCM/TOGO references.
5. Reconcile TOGO M9 with MediaDive J16 so the same JCM page does not keep two
   conflicting CultureMech source records.
6. Regenerate `data/merge_yaml/merged/` so the September 2 duplicate-water fix
   is reflected in `lactobacillus_medium_ii__7a1b4852.yaml`.

## Follow-up Checks

- Rerun the focused open, strict, reference, and term validators against
  `data/normalized_yaml/bacterial/TOGO_M9_Lactobacillus_Medium_II.yaml` after
  the nested-solution repair.
- Rerun source checks against JCM `GRMD=16`, TOGO M9, and MediaDive J16 and
  confirm the maintained record distinguishes main-medium additions from Salt
  solution R stock concentrations.
- Run `just merge-recipes`, then rerun the focused validators against
  `data/merge_yaml/merged/lactobacillus_medium_ii__7a1b4852.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm this generated
  file is not drifted.
- Search with ignored files included for exact `GRMD=16`, `TOGO:M9`, and
  `mediadive.medium:J16` after duplicate reconciliation to confirm only intended
  owners remain.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe
  schema section, the generated target, its normalized TOGO owner, live TOGO M9,
  live JCM `GRMD=16`, live MediaDive J16, and the normalized/generated MediaDive
  J16 sibling.
- `TOGO_M14_Lactobacillus_Medium_III.yaml` appears in broad label searches
  because its label is one roman numeral away; it is a separate JCM `GRMD=21`
  recipe and was not used to judge this `TOGO:M9` record.
