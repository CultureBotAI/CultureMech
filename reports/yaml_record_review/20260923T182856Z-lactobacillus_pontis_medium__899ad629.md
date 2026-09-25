# YAML Record Review: LACTOBACILLUS PONTIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml
- Started UTC: 2026-09-23T18:28:17Z
- Finished UTC: 2026-09-23T18:28:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml` |
| Generated status | Generated canonical merge from `data/normalized_yaml/bacterial/lactobacillus_pontis_medium.yaml`; do not edit directly |
| Schema class | `MediaRecipe` |
| CultureMech ID | `CultureMech:002650` |
| Name | `lactobacillus_pontis_medium` |
| Original name | `LACTOBACILLUS PONTIS MEDIUM` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Source accession | `mediadive.medium:J292` |
| Merge fingerprint | `899ad629eef60c5363119daad3c8bfb95679aaf4d1619c5c9a050b2de6ca6fff` |
| Maintained owner inspected | `data/normalized_yaml/bacterial/lactobacillus_pontis_medium.yaml` |

The reviewed record is a JCM `GRMD=292` import. Its source has a main MRS broth
recipe plus two nested stocks, Maltose-hemin solution and Hemin solution, but the
generated target flattens both stock compositions into direct final-medium rows.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml` | Passed; `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml --out /private/tmp/lactobacillus_pontis_medium__899ad629.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:002650` and `mediadive.medium:J292` identify JCM
  `LACTOBACILLUS PONTIS MEDIUM`, pH 6.5.
- The live JCM `GRMD=292` page is available and matches MediaDive `J292`.
- The same JCM page is also present through TOGO `M286`, currently normalized at
  `data/normalized_yaml/bacterial/TOGO_M286_Lactobacillus_Pontis_Medium.yaml`
  and generated as `data/merge_yaml/merged/LACTOBACILLUS_PONTIS_MEDIUM.yaml`.
- The direct ingredient groundings for maltose, L-cysteine hydrochloride
  monohydrate, hemin, and triethanolamine are plausible for their source labels;
  their placement is the problem because they are stock-solution components, not
  direct top-level final-medium components.

An ignored-inclusive exact search covered `data/normalized_yaml`,
`data/merge_yaml`, and `reports/archive` for `CultureMech:002650`,
digit-bounded `mediadive.medium:J292`, digit-bounded `GRMD=292`, the exact
normalized filename, the exact source label, and the full merge fingerprint. It
found the reviewed generated target, its normalized owner, normalized indexes,
old archive entries, and the same-JCM TOGO `M286` owner/generated output.

## Evidence

Supported in inspected sources:

- JCM `GRMD=292` lists 55 g Lactobacilli MRS broth and 1 L Distilled water in
  the main medium, followed by pH adjustment to 6.5 and post-autoclave addition
  of 18 ml Maltose-hemin solution.
- The JCM Maltose-hemin stock contains Maltose 15 g, 50 ml Hemin solution,
  L-Cysteine HCl H2O 5 g, and Distilled water 100 ml, then is
  filter-sterilized.
- The nested Hemin solution contains Hemin chloride 0.1 g, Triethanolamine 4 ml,
  and Distilled water 96 ml, then is filter-sterilized and stored at 4C.
- MediaDive `J292` preserves the same three-solution structure and computes the
  100 g/L maltose, 33.3333 g/L L-Cysteine HCl H2O, and 1 g/L Hemin chloride
  values as stock concentrations, not final-medium concentrations.

Unsupported or stale in the generated target:

- Maltose, L-Cysteine HCl H2O, Hemin chloride, and Triethanolamine are emitted
  as direct medium ingredients even though they belong to nested stock
  solutions.
- The record omits 1 L main-medium water, 100 ml Maltose-hemin water, and 96 ml
  Hemin-solution water.
- `Triethanolamine` is stored as `4 G_PER_L`; the source amount is 4 ml in the
  Hemin solution stock.
- The record has post-autoclave text but no explicit autoclave preparation step
  and no `references` list.

## Completeness

Consequential gaps:

- Both nested stock-solution recipes are missing.
- All three source water rows are missing.
- The final-medium addition of 18 ml Maltose-hemin solution is missing as a
  structured solution reference.
- The nested 50 ml Hemin solution addition is missing as a structured solution
  reference inside Maltose-hemin solution.
- The same JCM source exists as a TOGO M286 normalized owner with empty malformed
  solution rows, so source reconciliation is incomplete.

Empty or absent fields that are not defects for this generated JCM recipe:

- `target_organisms`, growth metrics, genome assembly, atmospheric conditions,
  salinity, and shelf-life fields can stay empty until strain-level evidence is
  added.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Blocker | Nested stock components are flattened as direct final-medium ingredients. | JCM and MediaDive add only 18 ml Maltose-hemin solution to the main medium; Maltose, L-Cysteine HCl H2O, Hemin chloride, and Triethanolamine are stock components. | `data/normalized_yaml/bacterial/lactobacillus_pontis_medium.yaml`, or the MediaDive importer if nested JCM solutions are systematically flattened. |
| Major | The final and stock solution water rows are absent. | The inspected source has Distilled water 1 L in the main medium, 100 ml in Maltose-hemin solution, and 96 ml in Hemin solution; the target has no water rows. | `data/normalized_yaml/bacterial/lactobacillus_pontis_medium.yaml`. |
| Major | Triethanolamine has the wrong quantity unit. | The source row is 4 ml in Hemin solution; the record emits `4 G_PER_L`. | `data/normalized_yaml/bacterial/lactobacillus_pontis_medium.yaml`. |
| Major | Source preparation is only partially structured. | JCM and MediaDive require autoclaving the main medium, cooling it to 50C, aseptic addition of 18 ml Maltose-hemin solution, filter-sterilization of both nested stocks, and storage of Hemin solution at 4C; the target has unscoped filter steps but no nested stock objects or explicit autoclave step. | `data/normalized_yaml/bacterial/lactobacillus_pontis_medium.yaml`. |
| Major | JCM `GRMD=292` exists as unlinked MediaDive J292 and TOGO M286 records. | The ignored-inclusive search found `TOGO_M286_Lactobacillus_Pontis_Medium.yaml`, whose TOGO API payload points to the same JCM URL and same three solution sections. | Reconcile the two normalized owners after the MediaDive and TOGO solution shapes are repaired. |

## Recommended Edits

1. Rebuild the normalized MediaDive owner with a top-level 55 g/L Lactobacilli
   MRS broth row and an 18 ml Maltose-hemin solution addition.
2. Represent Maltose-hemin solution as a nested stock containing Maltose,
   Hemin solution, L-Cysteine HCl H2O, and 100 ml water.
3. Represent Hemin solution as a nested stock containing Hemin chloride,
   Triethanolamine, and 96 ml water.
4. Preserve main-medium 1 L water, pH 6.5 adjustment, autoclaving, cooling,
   filter-sterilization, Hemin-solution storage, and JCM/MediaDive references.
5. Repair or merge the TOGO M286 owner so it no longer has empty
   `Unknown solution` entries with `G_PER_L` volumes.
6. Regenerate `data/merge_yaml/merged/` and verify
   `lactobacillus_pontis_medium__899ad629.yaml`.

## Follow-up Checks

- Rerun the focused open, strict, reference, and term validators against
  `data/normalized_yaml/bacterial/lactobacillus_pontis_medium.yaml` after the
  nested-stock repair.
- Re-query JCM `GRMD=292`, MediaDive `J292`, and TOGO M286 and manually compare
  main-medium, Maltose-hemin, and Hemin-solution boundaries.
- Run `just merge-recipes`, then rerun focused validators against
  `data/merge_yaml/merged/lactobacillus_pontis_medium__899ad629.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm this generated file
  is not drifted.
- Search with ignored files included for exact `GRMD=292`, `mediadive.medium:J292`,
  and `TOGO:M286` after duplicate reconciliation to confirm only intended owners
  remain.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe
  schema section, the generated target, its normalized owner, live MediaDive
  J292, live JCM `GRMD=292`, live TOGO M286, and the normalized/generated TOGO
  M286 sibling.
