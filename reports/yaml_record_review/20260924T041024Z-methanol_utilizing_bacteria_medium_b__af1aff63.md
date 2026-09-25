# YAML Record Review: METHANOL-UTILIZING BACTERIA MEDIUM B

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b__af1aff63.yaml
- Started UTC: 2026-09-24T04:09:30Z
- Finished UTC: 2026-09-24T04:10:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003144 |
| Name | methanol_utilizing_bacteria_medium_b |
| Original name | METHANOL-UTILIZING BACTERIA MEDIUM B |
| Category | bacterial |
| Media term | mediadive.medium:J79 |
| Source | JCM Medium 79 through MediaDive J79 |
| Generated path reviewed | data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b__af1aff63.yaml |
| Maintained owner | data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_b.yaml |

This is the JCM/MediaDive side of the Methanol-Utilizing Bacteria Medium B
duplicate pair. The reviewed generated output was emitted on 2026-08-06, while
the maintained owner was repaired on 2026-09-06 and now records the source
amounts, pH, autoclaving, and TOGO duplicate/variant graph.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b__af1aff63.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b__af1aff63.yaml --out /private/tmp/methanol_utilizing_bacteria_medium_b__af1aff63.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b__af1aff63.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b__af1aff63.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **Record identity is correct.** The JCM `GRMD=79` page lists medium 79 as
  `METHANOL-UTILIZING BACTERIA MEDIUM B`; MediaDive REST `medium/J79` reports
  the same JCM identity, source link, pH 7.1, and recipe rows.
- **The generated file has the correct stable record ID but stale content.**
  `CultureMech:003144` is still the canonical JCM Medium 79 record, but the
  generated YAML predates the 2026-09-06 curation event that restored source
  mg/ml units, added the missing distilled-water row, added autoclaving, and
  linked the TOGO M70 source duplicate.
- **CHEBI grounding is sound for the rows that survived the stale import.**
  The generated row labels and ChEBI terms agree for methanol, ammonium
  sulfate, KH2PO4, Na2HPO4, MgSO4 x 7 H2O, ferric citrate,
  CaCl2 x 2 H2O, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, and
  thiamine HCl.
- **The record is incomplete as a recipe because it omits water.** JCM and
  MediaDive both list 1.0 L or 1000 ml distilled water in the main solution.

## Evidence

### Supported by inspected sources

- JCM `GRMD=79`, TOGO M70, and MediaDive `J79` support the same medium
  identity, pH 7.1, 10.0 ml methanol, 3.0 g ammonium sulfate, 1.4 g KH2PO4,
  3.0 g Na2HPO4, 0.2 g MgSO4 x 7 H2O, 30.0 mg ferric citrate, 30.0 mg
  CaCl2 x 2 H2O, 5.0 mg MnCl2 x 4 H2O, 5.0 mg ZnSO4 x 7 H2O, 0.5 mg
  CuSO4 x 5 H2O, 0.4 mg thiamine HCl, and 1.0 L distilled water.
- JCM and MediaDive support the thiamine substitution note: thiamine HCl can be
  replaced by 0.2 g yeast extract.
- The live JCM page supplies the collection-wide default for this record:
  autoclave at 121 C for 15 min unless otherwise stated.

### Unsupported or over-scoped in the YAML

- `Methanol` is recorded as 10 g/L even though the source gives 10.0 ml.
- `(NH4)2SO4`, `KH2PO4`, `Na2HPO4`, and `MgSO4 x 7 H2O` are recorded as
  2.9703, 1.38614, 2.9703, and 0.19802 g/L. Those are MediaDive computed
  `g_l` values normalized over a 1010 ml solution volume, not the 3.0, 1.4,
  3.0, and 0.2 g source amounts from JCM Medium 79.
- The ferric citrate, calcium chloride, manganese chloride, zinc sulfate,
  copper sulfate, and thiamine rows are recorded as decimal `G_PER_L` values
  from MediaDive `g_l`; JCM specifies 30.0, 30.0, 5.0, 5.0, 0.5, and 0.4 mg.
- The JCM default autoclave instruction is absent.
- The source thiamine replacement note is modeled as a `MIX` preparation step,
  but it is not an action in the source protocol.

## Completeness

- **Distilled water is missing.** This is a required source row for the final
  liter and appears in both JCM and MediaDive.
- **Autoclaving is missing.** JCM supplies the 121 C for 15 min default, and
  the maintained owner now represents it as `sterilization.method: AUTOCLAVE`.
- **The duplicate/variant graph is missing.** A gitignore-independent search for
  `methanol_utilizing_bacteria_medium_b|Methanol-utilizing bacteria medium B`
  under `data/normalized_yaml` and the reviewed merge found the repaired
  canonical JCM record, the repaired TOGO M70 source duplicate, and Medium D/E
  supplemented variants that point back to this parent.
- Empty target-organism, growth-evidence, discussion, and stock-solution
  sections are not defects in this source recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The reviewed merge publishes stale pre-repair MediaDive import output. | Its merge event is from 2026-08-06; the maintained JCM owner has a 2026-09-06 repair event with source units, distilled water, autoclaving, references, and children. | Merge generation from `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_b.yaml` |
| Major | Water was dropped from the recipe. | JCM M79 lists 1.0 L distilled water and MediaDive J79 lists 1000 ml distilled water; no water row appears in the generated merge. | Already repaired in `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_b.yaml`; recurrent cause in the MediaDive importer |
| Major | Source amounts and units were replaced by MediaDive-derived g/L values. | JCM lists gram and milligram amounts against 1.0 L distilled water; MediaDive additionally computes `g_l` over a 1010 ml solution. The generated merge kept only the computed `g_l` values. | Already repaired in the normalized owner; recurrent cause in the MediaDive importer |
| Major | Methanol has the wrong dimension. | JCM and MediaDive list 10.0 ml methanol; the merge stores 10 `G_PER_L`. | Already repaired in the normalized owner; recurrent cause in unit normalization |
| Major | Autoclave sterilization is missing. | The JCM page default says to autoclave at 121 C for 15 min unless otherwise stated; no M79 exception is present. | Already repaired in the normalized owner; merge output needs regeneration |
| Minor | The thiamine alternate is encoded as a false preparation action. | JCM says thiamine HCl can be replaced by 0.2 g yeast extract; the merge stores that text as `action: MIX`. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_b.yaml` if the alternate is promoted to structured data |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b__af1aff63.yaml`
   from `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_b.yaml`
   so the generated output receives the 2026-09-06 JCM repair.
2. Fix the MediaDive importer so original `amount` and `unit` fields remain
   available and water rows are not dropped when a solution also has computed
   `g_l` values.
3. Ensure JCM volume additives such as 10.0 ml methanol keep `ML_PER_L`, not
   `G_PER_L`, unless an inspected source explicitly gives mass or density.
4. Represent the 0.2 g yeast-extract substitution as a variant or structured
   note rather than a `MIX` step.
5. Regenerate merged recipes and parent/variant links so this JCM record,
   TOGO M70, and Medium D/E agree on `CultureMech:003144` as the parent
   Medium B recipe.

## Follow-up Checks

- Re-run focused schema, strict, term, and reference validation on the repaired
  normalized JCM owner and regenerated merged output.
- Re-run merge verification to confirm the source duplicate and child variant
  graph is present in the generated layer.
- Manually compare the regenerated Medium B against JCM `GRMD=79`, MediaDive
  `J79`, and TOGO M70 for water, methanol, every mg row, pH 7.1, and
  autoclaving.

## Additional Notes

- MediaDive `medium/J79` is the correct REST identity for JCM Medium 79.
  Numeric REST ID `79` is DSMZ `LEUCOTHRIX MEDIUM` and is unrelated to this
  record.
- The exact gitignore-independent search used for duplicate context included
  hidden and ignored files under `data/normalized_yaml` plus the reviewed merge.
