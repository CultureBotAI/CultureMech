# YAML Record Review: Methanol-Utilizing Bacteria Medium E

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e.yaml
- Started UTC: 2026-09-24T04:11:45Z
- Finished UTC: 2026-09-24T04:12:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007725 |
| Name | methanol_utilizing_bacteria_medium_e |
| Original name | Methanol-Utilizing Bacteria Medium E |
| Category | bacterial |
| Media term | TOGO:M119 |
| Source | TOGO Medium M119, imported from JCM_M127 |
| Generated path reviewed | data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M119_Methanol-Utilizing_Bacteria_Medium_E.yaml |

The reviewed file is generated output from the TOGO M119 owner. The owner was
repaired on 2026-09-06 to model JCM Medium 127 as 1.0 L Medium B supplemented
with NaCl and vitamin B12, but this merge output was generated from the older
TOGO import on 2026-08-06.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e.yaml --out /private/tmp/methanol_utilizing_bacteria_medium_e.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **Record identity is correct.** TOGO M119 reports
  `Methanol-Utilizing Bacteria Medium E` from `JCM_M127`; the live JCM
  `GRMD=127` page and MediaDive `J127` report the same JCM medium.
- **The generated file is stale relative to the TOGO owner.** It predates the
  2026-09-06 repair that made M119 a `SUPPLEMENTED_VARIANT` of canonical
  Medium B, switched the parent reference to `1000 ML_PER_L`, added
  autoclaving, and corrected vitamin B12 to `MICROG_PER_L`.
- **The Medium B parent is not grounded.** The merge has an `Unknown solution`
  named `Methanol--utilizing bacteria medium B (see Medium [M70])` at
  `1 G_PER_L`. The source gives 1.0 L Medium B, and the repaired owner links
  that parent to `CultureMech:003144`.
- **NaCl and vitamin B12 have correct ontology terms.** The two top-level
  additive labels agree with `CHEBI:26710` sodium chloride and `CHEBI:176843`
  vitamin B12.

## Evidence

### Supported by inspected sources

- JCM `GRMD=127`, MediaDive `J127`, and TOGO M119 all support the Medium E
  identity and its three components: 1.0 L Methanol-utilizing bacteria medium B,
  30.0 g NaCl, and 10.0 micrograms Vitamin B12.
- JCM and MediaDive identify Medium B as JCM Medium 79; TOGO identifies the
  same parent as M70.
- The JCM page supplies the default sterilization rule for this recipe:
  autoclave at 121 C for 15 min unless otherwise stated.

### Unsupported or over-scoped in the YAML

- `Vitamin B12` is recorded as 10 g/L, while TOGO and JCM give 10.0 micrograms.
- The Medium B parent is recorded as an empty unknown solution at 1 g/L rather
  than as 1.0 L of the canonical Medium B recipe.
- The merge omits the JCM autoclave default.
- The generated file still classifies the record as `COMPLEX` and `UNDEFINED`.
  Medium E is a defined supplement of a defined parent, and the repaired TOGO
  owner classifies it as `DEFINED`.

## Completeness

- **Parentage is missing from the merge.** JCM explicitly points to Medium 79,
  MediaDive points to `Main sol. J79`, and TOGO points to M70. The generated
  `Unknown solution` does not let downstream consumers resolve the parent.
- **The Medium E duplicate pair is only partially repaired.** A
  gitignore-independent search for
  `methanol_utilizing_bacteria_medium_e|Methanol-Utilizing Bacteria Medium E`
  under `data/normalized_yaml/bacterial` and the reviewed merge found both this
  repaired TOGO owner and the canonical MediaDive/JCM J127 owner
  `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml`;
  the latter still has the stale flattened Medium B formulation and
  `CultureMech:002446`.
- Empty target-organism, growth-evidence, discussion, and local stock-solution
  sections are not defects for this supplement recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The reviewed merge publishes stale pre-repair TOGO M119 output. | Its merge event is from 2026-08-06; the maintained TOGO owner has a 2026-09-06 repair event with parent-medium, exact vitamin, autoclaving, and variant metadata. | Merge generation from `data/normalized_yaml/bacterial/TOGO_M119_Methanol-Utilizing_Bacteria_Medium_E.yaml` |
| Major | Vitamin B12 is off by a million-fold in dimensional terms. | JCM M127 and TOGO M119 list 10.0 micrograms. The merge stores `value: 10`, `unit: G_PER_L`. | Already repaired in the TOGO owner; recurrent cause in the TOGO importer |
| Major | The 1.0 L Medium B parent is an empty 1 g/L `Unknown solution`. | JCM M127 lists 1.0 L Medium B, and the repaired owner links `1000 ML_PER_L` to `CultureMech:003144`. | Already repaired in the TOGO owner; recurrent cause in solution migration |
| Major | JCM default autoclaving is missing. | JCM Medium 127 has no exception to the page default of autoclaving at 121 C for 15 min. The merge has no preparation step or sterilization object. | Already repaired in the TOGO owner; merge output needs regeneration |
| Major | A JCM J127 duplicate remains uncurated. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml` is the same JCM Medium 127 identity through MediaDive but still flattens Medium B ingredients and stores vitamin B12 as 10 g/L. | `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml` and duplicate-link repair logic |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/methanol_utilizing_bacteria_medium_e.yaml`
   from `data/normalized_yaml/bacterial/TOGO_M119_Methanol-Utilizing_Bacteria_Medium_E.yaml`
   so the merge receives the 2026-09-06 repair.
2. Preserve Medium B as a `1000 ML_PER_L` `solutions` row linked to
   `CultureMech:003144`.
3. Keep vitamin B12 as `10.0 MICROG_PER_L` and NaCl as `30.0 G_PER_L`.
4. Preserve the JCM default autoclave step in the generated merge.
5. Apply the same source-duplicate repair to
   `data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_e.yaml`
   so the MediaDive/JCM J127 record does not continue to publish a stale
   flattened copy of Medium B under `CultureMech:002446`.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the repaired TOGO
  M119 owner and regenerated merge.
- Re-run merge verification and inspect that Medium E points at canonical
  Medium B through `CultureMech:003144`.
- Manually compare the regenerated Medium E and its MediaDive/JCM duplicate
  against JCM `GRMD=127`, MediaDive `J127`, and TOGO M119 for the 1.0 L parent,
  30.0 g NaCl, 10.0 micrograms Vitamin B12, and default autoclaving.

## Additional Notes

- The exact duplicate search used for this review included hidden and ignored
  files under `data/normalized_yaml/bacterial` plus the reviewed merge.
- MediaDive J127 embeds the full J79 recipe as a linked solution; that inherited
  recipe should stay behind the Medium B parent boundary, not be flattened into
  Medium E.
