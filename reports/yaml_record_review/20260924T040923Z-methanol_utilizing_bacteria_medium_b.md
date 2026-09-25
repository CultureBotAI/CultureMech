# YAML Record Review: Methanol-Utilizing Bacteria Medium B

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml
- Started UTC: 2026-09-24T04:08:00Z
- Finished UTC: 2026-09-24T04:09:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010117 |
| Name | methanol_utilizing_bacteria_medium_b |
| Original name | Methanol-Utilizing Bacteria Medium B |
| Category | bacterial |
| Media term | TOGO:M70 |
| Source | TOGO Medium M70, imported from JCM_M79 |
| Generated path reviewed | data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml |
| Generated from | data/normalized_yaml/bacterial/TOGO_M70_Methanol-Utilizing_Bacteria_Medium_B.yaml |
| Canonical JCM duplicate | data/normalized_yaml/bacterial/methanol_utilizing_bacteria_medium_b.yaml |

The reviewed file is generated output from the TOGO M70 source record. The
normalized TOGO M70 record and the canonical JCM J79 duplicate were both
repaired on 2026-09-06, after this merge output was generated on 2026-08-06.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml --out /private/tmp/methanol_utilizing_bacteria_medium_b.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **Record identity is correct.** TOGO M70 identifies the recipe as
  `Methanol-Utilizing Bacteria Medium B`, imported from `JCM_M79`, with pH 7.1
  and the JCM Medium 79 URL. The live JCM page for `GRMD=79` lists medium 79 as
  `METHANOL-UTILIZING BACTERIA MEDIUM B`, and MediaDive REST `medium/J79`
  mirrors the same JCM formulation.
- **The maintained TOGO owner has already been repaired.**
  `data/normalized_yaml/bacterial/TOGO_M70_Methanol-Utilizing_Bacteria_Medium_B.yaml`
  carries the same `CultureMech:010117` ID, source duplicate metadata pointing
  to canonical JCM record `CultureMech:003144`, exact mg/ml units, pH 7.1,
  preparation steps, `DEFINED` medium classification, and a
  `repair_methanol_utilizing_score40.py` event.
- **The reviewed merge is stale.** It still has the January importer's
  `COMPLEX` and `UNDEFINED` classification, no `ph_value`, no preparation
  steps, and January unit coercions that encode several JCM milligram rows as
  `G_PER_L`.
- **Ontology grounding is mostly adequate where rows have terms.** Methanol,
  ammonium sulfate, KH2PO4, Na2HPO4, MgSO4 x 7 H2O, ferric citrate, hydrated
  calcium chloride, hydrated manganese chloride, hydrated zinc sulfate, and
  hydrated copper sulfate point at chemically specific ChEBI terms.
- **The thiamine row lost its term in the stale merge.** JCM and TOGO label the
  row as thiamine HCl with a see-below note, and the repaired owner maps it to
  thiamine hydrochloride. The reviewed generated file has no ontology term for
  `Thiamine HCl`.

## Evidence

### Supported by inspected sources

- JCM `GRMD=79`, TOGO M70, and MediaDive `J79` all support the medium identity,
  pH 7.1, 10.0 ml methanol, 3.0 g ammonium sulfate, 1.4 g KH2PO4, 3.0 g
  Na2HPO4, 0.2 g MgSO4 x 7 H2O, 30.0 mg ferric citrate, 30.0 mg
  CaCl2 x 2 H2O, 5.0 mg MnCl2 x 4 H2O, 5.0 mg ZnSO4 x 7 H2O, 0.5 mg
  CuSO4 x 5 H2O, 0.4 mg thiamine HCl, and 1.0 L distilled water.
- JCM and TOGO support the note that thiamine HCl can be replaced by 0.2 g
  yeast extract.
- The live JCM page states a default sterilization rule for JCM media: unless
  otherwise stated, sterilize by autoclaving at 121 C for 15 min. No M79-specific
  exception is present on the inspected page.

### Unsupported or over-scoped in the YAML

- `Ferric citrate` and `CaCl2 x 2H2O` are recorded as 30 g/L but are 30 mg in
  the JCM source.
- `MnCl2 x 4H2O` and `ZnSO4 x 7H2O` are recorded as 5 g/L but are 5 mg in the
  JCM source.
- `CuSO4 x 5H2O` is recorded as 0.5 g/L but is 0.5 mg in the JCM source.
- `Thiamine HCl` is recorded as 0.4 g/L but is 0.4 mg in the JCM source.
- `Methanol` is recorded as 10 g/L but JCM and TOGO specify 10.0 ml.
- `Distilled water` is recorded as 1 g/L but JCM and TOGO specify 1.0 L.
- The record says the medium is `COMPLEX` and `UNDEFINED`; JCM Medium 79 is a
  defined mineral and methanol recipe, and the repaired source records classify
  it as `DEFINED`.

## Completeness

- **pH is missing from the generated merge.** JCM, TOGO, and MediaDive all
  agree on pH 7.1.
- **Preparation is missing from the generated merge.** The live JCM page
  supplies the 121 C for 15 min default autoclave instruction and the M79 page
  supplies the pH adjustment.
- **The thiamine substitute note is missing.** The source allows 0.2 g yeast
  extract instead of the 0.4 mg thiamine HCl row; the repaired owners record the
  thiamine row but have not represented the yeast-extract alternate as a
  machine-readable variant.
- **The maintained duplicate graph is richer than the merge.** A
  gitignore-independent search for `methanol_utilizing_bacteria_medium_b|Methanol-utilizing bacteria medium B`
  under `data/normalized_yaml` and the reviewed merge found the repaired
  canonical JCM record, the repaired TOGO M70 source duplicate, and Medium D/E
  variants that use Medium B as their parent.
- Empty target-organism, growth-evidence, discussion, and stock-solution
  sections are not defects in this source recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The reviewed merge publishes stale pre-repair data for TOGO M70. | Its merge history is from 2026-08-06. The normalized TOGO M70 owner has a 2026-09-06 repair event with exact units, pH, autoclaving, and duplicate links. | Merge generation from `data/normalized_yaml/bacterial/TOGO_M70_Methanol-Utilizing_Bacteria_Medium_B.yaml` |
| Major | Six milligram source rows are inflated to g/L. | JCM M79 lists ferric citrate 30 mg, CaCl2 x 2H2O 30 mg, MnCl2 x 4H2O 5 mg, ZnSO4 x 7H2O 5 mg, CuSO4 x 5H2O 0.5 mg, and thiamine HCl 0.4 mg; the merge stores the same numeric values as `G_PER_L`. | Already repaired in `data/normalized_yaml/bacterial/TOGO_M70_Methanol-Utilizing_Bacteria_Medium_B.yaml`; recurrent cause in the TOGO importer |
| Major | Methanol and water have the wrong dimensions. | JCM M79 gives methanol as 10.0 ml and distilled water as 1.0 L. The merge stores them as 10 and 1 `G_PER_L`. | Already repaired in `data/normalized_yaml/bacterial/TOGO_M70_Methanol-Utilizing_Bacteria_Medium_B.yaml`; recurrent cause in unit normalization |
| Major | Source-supported pH and autoclave preparation are missing. | JCM M79 says adjust pH to 7.1 and the page default is autoclaving at 121 C for 15 min. The merge has no `ph_value`, `preparation_steps`, or `sterilization`. | Already repaired in `data/normalized_yaml/bacterial/TOGO_M70_Methanol-Utilizing_Bacteria_Medium_B.yaml`; merge output needs regeneration |
| Minor | Thiamine HCl is ungrounded in the generated merge. | The source row is thiamine HCl; the repaired normalized owners ground the row to `CHEBI:49105` thiamine hydrochloride. The reviewed merge has no term on that row. | Already repaired in the normalized owners; merge output needs regeneration |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml`
   from `data/normalized_yaml/bacterial/TOGO_M70_Methanol-Utilizing_Bacteria_Medium_B.yaml`
   so the published merge carries the September unit, pH, preparation, and
   source-duplicate fixes.
2. Confirm the merge pipeline preserves `CultureMech:010117` as a
   `SOURCE_DUPLICATE` child of canonical JCM record `CultureMech:003144`, or
   update duplicate/fingerprint routing so the repaired JCM and TOGO records do
   not re-diverge.
3. Backstop the TOGO unit importer so `mg`, `ml`, and `L` source units cannot
   be emitted as `G_PER_L` in other JCM-derived media.
4. Represent the source note that 0.4 mg thiamine HCl can be replaced by 0.2 g
   yeast extract, either as a curated variant or as a structured discussion
   note if the current schema cannot encode alternates cleanly.

## Follow-up Checks

- Re-run focused schema, strict, term, and reference validation on the repaired
  normalized TOGO M70 record and the regenerated merged output.
- Re-run merge verification to ensure the September 2026 repair event is
  reflected in `data/merge_yaml/merged/methanol_utilizing_bacteria_medium_b.yaml`.
- Manually compare regenerated Medium B against JCM `GRMD=79`, TOGO M70, and
  MediaDive `J79` for every mg, ml, and L value.
- Re-open Medium D and Medium E after regeneration to make sure their parent
  links still point at canonical `CultureMech:003144` rather than absorbing the
  stale TOGO duplicate.

## Additional Notes

- `https://mediadive.dsmz.de/rest/medium/79` denotes DSMZ Medium 79
  `LEUCOTHRIX MEDIUM`; the JCM record is available as MediaDive `medium/J79`.
- The exact gitignore-independent search used for duplicate context included
  hidden and ignored files under `data/normalized_yaml` plus the reviewed merge.
