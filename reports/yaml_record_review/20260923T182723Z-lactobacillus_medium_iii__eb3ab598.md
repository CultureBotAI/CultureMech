# YAML Record Review: Lactobacillus Medium III

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml
- Started UTC: 2026-09-23T18:26:49Z
- Finished UTC: 2026-09-23T18:27:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml` |
| Generated status | Generated canonical merge from `data/normalized_yaml/bacterial/TOGO_M14_Lactobacillus_Medium_III.yaml`; do not edit directly |
| Schema class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008045` |
| Name | `lactobacillus_medium_iii` |
| Original name | `Lactobacillus Medium III` |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Source accession | `TOGO:M14` |
| Merge fingerprint | `eb3ab598a8446ca14c3c0c1cc6d6d65b667305877159cca2418f89cf62528f58` |
| Maintained owner inspected | `data/normalized_yaml/bacterial/TOGO_M14_Lactobacillus_Medium_III.yaml` |

The generated target is a TOGO import of JCM `GRMD=21`. It is source-identical
to the separate MediaDive `J21` owner, but it has severe quantity-unit errors
in the TOGO path for milligram and milliliter ingredients.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml` | Passed; no output |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml --out /private/tmp/lactobacillus_medium_iii__eb3ab598.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:008045` and `TOGO:M14` identify TOGO's import of JCM `GRMD=21`,
  `Lactobacillus Medium III`, with original media ID `JCM_M21`.
- The live JCM `GRMD=21` page is available and matches TOGO M14.
- MediaDive `J21` / `CultureMech:002581` is the same JCM original recipe through
  a different source transform. It remains a separate generated record,
  `data/merge_yaml/merged/LACTOBACILLUS_MEDIUM_III.yaml`.
- Exact groundings for water, magnesium sulfate heptahydrate, potassium
  phosphates, sodium acetate, polysorbate 80, ethanol, glucose, and agar are
  plausible for their source labels.
- `MnSO4 xH2O` is left generically grounded to manganese(II) sulfate because the
  hydrate count is variable.

An ignored-inclusive exact search covered `data/normalized_yaml`,
`data/merge_yaml`, and `reports/archive` for `CultureMech:008045`,
digit-bounded `TOGO:M14`, digit-bounded `GRMD=21`, the exact normalized
filename, the exact label, and the full merge fingerprint. It found the
reviewed generated target, its normalized owner, normalized TOGO indexes, old
archive entries, and the same-JCM MediaDive `J21` owner/generated output.

## Evidence

Supported in inspected sources:

- JCM `GRMD=21` lists Casein peptone tryptic digest 10 g, Yeast extract 5 g,
  Beef extract 2 g, Glucose 20 g, KH2PO4 0.5 g, K2HPO4 0.5 g,
  FeSO4 x 7 H2O 10 mg, MgSO4 x 7 H2O 0.2 g, MnSO4 xH2O 7.5 mg, Tween 80 1 ml,
  Ethanol 40 ml, Sodium acetate 20 g, DL-Mevalonic acid 30 mg, Agar 15 g, and
  Distilled water 1 L, followed by adjustment to pH 5.2.
- JCM also states the default sterilization condition for its pages: autoclave
  at 121 C for 15 minutes unless otherwise stated.
- Live TOGO M14 reproduces the same source rows with pH 5.2.
- Live MediaDive `J21` normalizes the same source recipe over a 1041 ml main
  solution and preserves pH adjustment to 5.2.

Unsupported or stale in the generated target:

- `FeSO4 x 7 H2O`, `MnSO4 xH2O`, and `DL--Mevalonic acid` keep their numeric
  milligram amounts but are marked `G_PER_L`, inflating 10 mg, 7.5 mg, and
  30 mg to 10 g/L, 7.5 g/L, and 30 g/L.
- `Tween 80` and `Ethanol` are milliliter rows in JCM and TOGO but are marked
  `G_PER_L`.
- `Distilled water` is a 1 L source row but is marked `G_PER_L`.
- The target lacks pH 5.2, pH adjustment, the JCM default autoclave instruction,
  and explicit references.

## Completeness

Consequential gaps:

- Milligram, milliliter, and liter source quantities are not represented with
  source-faithful units.
- Source-supported pH and autoclave steps are absent.
- The TOGO M14 and MediaDive J21 owners are source duplicates but remain
  reconciled only by label and external lookup, not by CultureMech parentage.
- Source references are absent.

Empty or absent fields that are not defects for this generated JCM recipe:

- `target_organisms`, growth metrics, genome assembly, atmospheric conditions,
  storage, and shelf-life fields can remain empty until strain-level evidence is
  added.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Blocker | Three milligram ingredients are represented as gram-per-liter amounts. | JCM and TOGO list FeSO4 x 7 H2O 10 mg, MnSO4 xH2O 7.5 mg, and DL-Mevalonic acid 30 mg; the target stores `10 G_PER_L`, `7.5 G_PER_L`, and `30 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M14_Lactobacillus_Medium_III.yaml`, or the TOGO importer if mg rows are systematically stamped as `G_PER_L`. |
| Major | Milliliter and liter ingredients are also forced into `G_PER_L`. | JCM and TOGO list Tween 80 1 ml, Ethanol 40 ml, and Distilled water 1 L; the target stores all three with `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M14_Lactobacillus_Medium_III.yaml`, or the TOGO importer. |
| Major | pH, sterilization, and references are missing. | JCM and TOGO support pH 5.2; JCM gives a default autoclave condition; neither the generated nor normalized TOGO record has `ph_value`, `preparation_steps`, `sterilization`, or `references`. | `data/normalized_yaml/bacterial/TOGO_M14_Lactobacillus_Medium_III.yaml`. |
| Major | The same JCM `GRMD=21` recipe exists as unlinked TOGO M14 and MediaDive J21 records. | Ignored-inclusive search found `data/normalized_yaml/bacterial/JCM_J21_LACTOBACILLUS_MEDIUM_III.yaml`; live TOGO M14 and MediaDive J21 point to the same JCM page. | Reconcile the two normalized owners through source identity or merge rules after the TOGO units are repaired. |

## Recommended Edits

1. Correct FeSO4 x 7 H2O, MnSO4 xH2O, and DL-Mevalonic acid so their milligram
   source amounts are not inflated to grams per liter.
2. Correct Tween 80, Ethanol, and Distilled water so their volume source amounts
   are not represented as `G_PER_L`.
3. Add pH 5.2, a pH-adjustment preparation step, JCM's default autoclave step,
   and JCM/TOGO references to the normalized TOGO M14 owner.
4. Reconcile TOGO M14 with MediaDive J21, preserving whether the record reports
   nominal 1 L source amounts or MediaDive's 1041 ml normalized concentrations.
5. Regenerate `data/merge_yaml/merged/` and verify
   `lactobacillus_medium_iii__eb3ab598.yaml`.

## Follow-up Checks

- Rerun the focused open, strict, reference, and term validators against
  `data/normalized_yaml/bacterial/TOGO_M14_Lactobacillus_Medium_III.yaml` after
  quantity and reference edits.
- Re-query JCM `GRMD=21`, TOGO M14, and MediaDive J21 while verifying each
  amount and unit.
- Run `just merge-recipes`, then rerun focused validators against
  `data/merge_yaml/merged/lactobacillus_medium_iii__eb3ab598.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm this generated file
  is not drifted.
- Search with ignored files included for exact `GRMD=21`, `TOGO:M14`, and
  `mediadive.medium:J21` after duplicate reconciliation to confirm only intended
  owners remain.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe
  schema section, the generated target, its normalized owner, live TOGO M14,
  live JCM `GRMD=21`, live MediaDive J21, and the normalized/generated MediaDive
  J21 sibling.
- This JCM `GRMD=21` recipe is distinct from DSMZ Medium 638 despite sharing the
  `Lactobacillus Medium III` label.
