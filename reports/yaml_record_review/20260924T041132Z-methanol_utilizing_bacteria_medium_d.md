# YAML Record Review: METHANOL-UTILIZING BACTERIA MEDIUM D

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanol_utilizing_bacteria_medium_d.yaml
- Started UTC: 2026-09-24T04:10:30Z
- Finished UTC: 2026-09-24T04:11:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002435 |
| Name | methanol_utilizing_bacteria_medium_d |
| Original name | METHANOL-UTILIZING BACTERIA MEDIUM D |
| Category | bacterial |
| Media term | mediadive.medium:J126 |
| Source | JCM Medium 126 through MediaDive J126 |
| Generated path reviewed | data/merge_yaml/merged/methanol_utilizing_bacteria_medium_d.yaml |
| Maintained owner | data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_d.yaml |

The reviewed file is generated output from the JCM/MediaDive Medium 126 owner.
The maintained owner was repaired on 2026-09-07 to model Medium D as a
supplemented variant of canonical Medium B, but the merge output still reflects
the earlier MediaDive import.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanol_utilizing_bacteria_medium_d.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanol_utilizing_bacteria_medium_d.yaml --out /private/tmp/methanol_utilizing_bacteria_medium_d.strict.tsv --workers 1 --quiet` exited 0 and the TSV contained only its header, so 0 strict errors were reported. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **Record identity is correct.** JCM `GRMD=126` lists medium 126 as
  `METHANOL-UTILIZING BACTERIA MEDIUM D`; MediaDive `medium/J126` reports the
  same name, source, and pH 9.0.
- **The generated file points at the right JCM source but is stale.** Its
  2026-08-06 merge predates the 2026-09-07 repair event in
  `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_d.yaml`.
- **Medium B should be a parent solution, not a chemical ingredient.** The
  source says to use 1.0 L Methanol-utilizing bacteria medium B. The repaired
  owner models this as `1000 ML_PER_L` with a `CultureMech:003144` link to the
  canonical Medium B record.
- **The carbonate addition is ungrounded and incomplete in the merge.** JCM and
  MediaDive say the pH is adjusted to 9.0 with filter-sterilized 10 percent
  `NaCO3` solution. TOGO M118 imports the solution component as
  `NaHCO3 solution` but keeps the `NaCO3` wording in the preparation comment.
  The reviewed merge has only a free-text preparation step and no carbonate
  solution row to curate or flag.

## Evidence

### Supported by inspected sources

- JCM `GRMD=126`, MediaDive `J126`, and TOGO M118 support the Medium D identity
  and pH 9.0.
- JCM and MediaDive support 1.0 L, or 1000 ml, Methanol-utilizing bacteria
  medium B as the base.
- JCM, MediaDive, and TOGO support pH adjustment with filter-sterilized
  10 percent NaCO3 solution, with no fixed addition volume.
- The JCM page supplies the default sterilization rule for JCM media:
  autoclave at 121 C for 15 min unless otherwise stated.

### Unsupported or over-scoped in the YAML

- The merge records `Methanol-utilizing bacteria medium B` as an ingredient at
  `1000 G_PER_L`. Medium B is a liter-volume parent recipe, not a 1000 g/L
  compound.
- The filter-sterilized 10 percent carbonate solution is not present as an
  ingredient or solution.
- The generated preparation has a single `FILTER_STERILIZE` action whose
  description also performs pH adjustment. It omits the separate autoclaving of
  Medium B.

## Completeness

- **Parentage is missing from the merge.** The inspected JCM source explicitly
  sends readers to Medium 79, and the repaired owner links
  `CultureMech:003144` as `parent_media`.
- **The variable carbonate solution is missing.** A future curation pass should
  preserve the unspecified final volume and either resolve the `NaCO3` versus
  `NaHCO3` discrepancy between the source row and preparation text or flag it.
- **The TOGO duplicate is not represented.** A gitignore-independent search for
  `methanol_utilizing_bacteria_medium_d|Methanol-Utilizing Bacteria Medium D`
  under `data/normalized_yaml/bacterial` and the reviewed merge found both the
  canonical JCM owner and TOGO M118 as source-duplicate/supplemented-variant
  records, plus parent links from Medium B.
- Empty target-organism, growth-evidence, and top-level ingredient sections are
  not defects once the base medium and carbonate addition are modeled as
  `solutions`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated Medium D merge publishes stale pre-repair data. | Its merge event is from 2026-08-06; the maintained JCM owner has a 2026-09-07 repair event adding parent-medium, carbonate-solution, references, and autoclaving structure. | Merge generation from `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_d.yaml` |
| Major | The 1.0 L parent Medium B is represented as `1000 G_PER_L` ingredient mass. | JCM M126 lists 1.0 L Medium B; MediaDive J126 lists 1000 ml. The merge stores 1000 `G_PER_L` and has no link to `CultureMech:003144`. | Already repaired in `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_d.yaml`; recurrent cause in parent-medium import/migration |
| Major | The filter-sterilized 10 percent carbonate solution is missing as a component. | JCM, MediaDive, and TOGO all mention the carbonate pH-adjusting solution. The merge has no solution row for it. | Already repaired in the normalized owner; the NaCO3/NaHCO3 identity needs curator review |
| Major | Sterilization is incomplete. | JCM requires autoclaving unless otherwise stated and the carbonate solution is filter-sterilized. The merge only keeps a `FILTER_STERILIZE` step. | Already repaired in the normalized owner; merge output needs regeneration |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/methanol_utilizing_bacteria_medium_d.yaml`
   from `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_d.yaml`
   so the merge receives the 2026-09-07 repair.
2. Keep `Methanol-utilizing bacteria medium B` in `solutions` with
   `1000 ML_PER_L` and a `culturemech_term` link to `CultureMech:003144`.
3. Keep the 10 percent carbonate solution as a variable-volume,
   filter-sterilized solution rather than erasing it into the preparation text.
4. Add or retain a discussion flag for the exact carbonate identity: the
   source preparation says `NaCO3`, while the TOGO component row has
   `NaHCO3 solution`.
5. Preserve the separate JCM autoclave default and pH-adjustment steps after
   regeneration.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the repaired
  normalized owner and regenerated merge.
- Re-run merge verification and inspect that `CultureMech:003144` is still the
  parent Medium B recipe.
- Manually compare the regenerated Medium D with JCM `GRMD=126`, MediaDive
  `J126`, and TOGO M118 for the 1.0 L Medium B parent, pH 9.0, and
  filter-sterilized 10 percent carbonate wording.

## Additional Notes

- The exact duplicate search used for this review included hidden and ignored
  files under `data/normalized_yaml/bacterial` plus the reviewed merge.
- No bounded search established the carbonate formula; the `NaCO3` versus
  `NaHCO3` mismatch needs chemical curation against the provider records.
