# YAML Record Review: METHANOL-UTILIZING BACTERIA MEDIUM E

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e__c4c2a535.yaml
- Started UTC: 2026-09-24T04:12:50Z
- Finished UTC: 2026-09-24T04:13:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002446 |
| Name | methanol_utilizing_bacteria_medium_e |
| Original name | METHANOL-UTILIZING BACTERIA MEDIUM E |
| Category | bacterial |
| Media term | mediadive.medium:J127 |
| Source | JCM Medium 127 through MediaDive J127 |
| Generated path reviewed | data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e__c4c2a535.yaml |
| Maintained owner | data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml |

This generated file is derived from the canonical MediaDive/JCM J127 owner for
Methanol-Utilizing Bacteria Medium E. Unlike the TOGO M119 duplicate, this
owner has not received the September 2026 Methanol-Utilizing Medium E repair.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e__c4c2a535.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e__c4c2a535.yaml --out /private/tmp/methanol_utilizing_bacteria_medium_e__c4c2a535.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e__c4c2a535.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e__c4c2a535.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **Record identity is correct.** JCM `GRMD=127` lists medium 127 as
  `METHANOL-UTILIZING BACTERIA MEDIUM E`, and MediaDive `medium/J127` reports
  the same JCM identity.
- **The record content overstates the target formulation.** JCM Medium 127 has
  three rows: 1.0 L Medium B, 30.0 g NaCl, and 10.0 micrograms Vitamin B12.
  MediaDive exposes Medium B as nested `Main sol. J79`, but the YAML flattened
  all J79 ingredients into Medium E and lost the parent boundary.
- **The additive ontology terms are correct.** NaCl and vitamin B12 point at
  appropriate ChEBI terms.
- **The inherited Medium B rows are scoped incorrectly.** Their CHEBI terms are
  individually plausible, but they belong inside Medium B, not as direct
  Medium E additions.

## Evidence

### Supported by inspected sources

- JCM `GRMD=127`, MediaDive `J127`, and TOGO M119 support the same Medium E
  identity.
- The inspected JCM page supports 1.0 L Methanol-utilizing bacteria medium B,
  30.0 g NaCl, and 10.0 micrograms Vitamin B12. MediaDive `J127` supports the
  same structure with `Main sol. J79` as a nested solution and NaCl/Vitamin B12
  as J127-level additions.
- The JCM page supplies the default sterilization rule for this record:
  autoclave at 121 C for 15 min unless otherwise stated.

### Unsupported or over-scoped in the YAML

- `Vitamin B12` is represented as 10 g/L, not 10 micrograms.
- Methanol, ammonium sulfate, KH2PO4, Na2HPO4, MgSO4 x 7 H2O, ferric citrate,
  CaCl2 x 2 H2O, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, and thiamine HCl
  are inherited from JCM Medium 79 and should stay behind the Medium B parent
  reference.
- The inherited Medium B rows have the same MediaDive-derived unit problems as
  the stale JCM Medium B merge: methanol is 10 g/L instead of 10 ml, several
  masses use 1010 ml normalized `g_l` values instead of source amounts, and
  distilled water is missing.
- `preparation_steps` contains Medium B's thiamine substitution note and pH 7.1
  adjustment. JCM Medium 127 itself does not instruct another pH 7.1 adjustment.
- The JCM autoclave default is not represented for Medium E.

## Completeness

- **The Medium B parent is missing.** JCM points to Medium 79 and MediaDive
  nests `Main sol. J79`; no `solutions` or `parent_media` entry in the merge
  links Medium E to `CultureMech:003144`.
- **The TOGO M119 duplicate is missing.** A gitignore-independent search for
  `methanol_utilizing_bacteria_medium_e|Methanol-Utilizing Bacteria Medium E`
  under `data/normalized_yaml/bacterial` and the reviewed merge found a
  repaired TOGO M119 duplicate that models the same JCM 127 recipe with Medium
  B as a parent.
- **Autoclaving is missing.** The JCM default applies because no J127 exception
  is present.
- Empty target-organism, growth-evidence, local stock, and discussion sections
  are not defects for this supplement recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Medium E flattens its Medium B parent into direct ingredients. | JCM M127 lists 1.0 L Medium B, not Medium B's complete chemistry. MediaDive nests J79 under J127. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml` and MediaDive nested-solution import |
| Major | Vitamin B12 is off by a million-fold in dimensional terms. | JCM M127 lists 10.0 micrograms Vitamin B12; the merge stores 10 `G_PER_L`. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml` |
| Major | Inherited Medium B rows carry the stale J79 unit and water defects. | The merge has 10 g/L methanol, J79 computed `g_l` values, and no distilled-water row. JCM J79 lists 10.0 ml methanol and 1.0 L distilled water. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml`; recurrent cause in MediaDive import |
| Major | J127 and TOGO M119 remain separate duplicated records with inconsistent curation. | TOGO M119 has been repaired as `CultureMech:007725`; the JCM J127 owner remains stale as `CultureMech:002446`. Both denote JCM Medium 127. | Duplicate-link repair across the two Medium E normalized files |
| Major | Autoclave sterilization is missing. | The JCM page default says to autoclave at 121 C for 15 min unless otherwise stated. The merge only has inherited Medium B preparation text. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml` |
| Minor | The thiamine alternate is mis-scoped. | The note is attached to Medium B in JCM 79, but the JCM 127 merge publishes it as a Medium E `MIX` step. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml` |

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml`
   to match the repaired TOGO M119 structure: NaCl at 30.0 g/L, vitamin B12 at
   10.0 micrograms/L, and Medium B as a 1000 ml/L parent solution linked to
   `CultureMech:003144`.
2. Remove inherited J79 chemistry from Medium E's top-level `ingredients`; the
   chemistry belongs in Medium B.
3. Add Medium E autoclaving from the JCM page default.
4. Link or collapse the JCM J127 and TOGO M119 duplicate records so the same
   JCM Medium 127 formulation is not curated in two incompatible forms.
5. Fix the MediaDive nested-solution importer so a nested solution reference is
   represented as a solution or parent recipe instead of being flattened by
   default.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the repaired JCM J127
  owner and regenerated merge.
- Re-run merge verification and inspect that the JCM J127 and TOGO M119 records
  either merge together or remain explicitly linked as source duplicates.
- Manually compare regenerated Medium E against JCM `GRMD=127`, MediaDive
  `J127`, and TOGO M119 for the 1.0 L Medium B parent, 30.0 g NaCl, 10.0
  micrograms Vitamin B12, and default autoclaving.

## Additional Notes

- The exact duplicate search used for this review included hidden and ignored
  files under `data/normalized_yaml/bacterial` plus the reviewed merge.
- This record's `merge_fingerprint` is distinct from the TOGO M119 merge
  because the two source owners still encode materially different graphs for
  the same recipe.
