# YAML Record Review: brain heart infusion agar (containing 7% horse blood and 0.4% isovitalex)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml
- Started UTC: 2026-09-21T23:35:45Z
- Finished UTC: 2026-09-21T23:36:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009397 |
| Label | brain heart infusion agar (containing 7% horse blood and 0.4% isovitalex) |
| Source accession | TOGO:M2855 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 207df04305881ee199fc983f7bddca875367df166b9d13c05cdbb814975481dd |

The reviewed file is generated from a single normalized owner. The generated
record and normalized owner currently agree, so formulation fixes belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml`
or in the TOGO importer rule that expanded the BHI agar base.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml --out /private/tmp/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- TOGO:M2855 resolves to brain heart infusion agar containing 7% horse blood
  and 0.4% Isovitalex.
- The TOGO payload has no `src_url`, but an exact search for its H. pylori
  cultivation sentence resolves to Kersulyte et al. 2010, `PLoS ONE`, DOI
  `10.1371/journal.pone.0015076`, PMID `21124785`, PMCID `PMC2993954`.
- A gitignore-independent search for `TOGO:M2855`, `CultureMech:009397`, the
  merge fingerprint, the normalized slug, and the exact source label across
  `data`, `src`, `scripts`, `docs`, `.claude`, and `justfile` found one
  normalized owner plus the generated merge and generated indexes.
- The source recipe identity is correct, but the two percent-valued
  supplements, opaque BHI agar row, and atmosphere gases are not represented
  with source-supported units or scope.

## Evidence

TOGO lists 7% horse blood, 1 L brain heart infusion agar from Difco, 0.4%
Isovitalex, 10% CO2, and 5% O2. Its comment, confirmed against Kersulyte et al.
2010, says H. pylori was grown on BHI agar containing 7% horse blood and 0.4%
Isovitalex in a microaerobic atmosphere of 5% O2 and 10% CO2.

The inspected source supports a BHI agar recipe used for H. pylori cultivation,
not a formulation in which CO2 and O2 are variable-concentration ingredients.
It reports the blood and Isovitalex percentages without saying that either
percentage is weight/volume.

## Completeness

- Consequential gap: the record has no primary citation for Kersulyte et al.
  2010 despite depending on that paper for the H. pylori growth context.
- Consequential gap: the 5% O2 and 10% CO2 atmosphere percentages are absent.
- Consequential gap: the exact percent basis for horse blood and Isovitalex is
  unresolved; the record should not force `PERCENT_W_V` without evidence.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex`
  report, so this report did not overwrite an earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Horse blood and Isovitalex are both represented as `PERCENT_W_V`, but the inspected source only says `7% horse blood` and `0.4% isovitalex`. | TOGO M2855 and Kersulyte et al. 2010 both omit the percent basis for those two supplement values. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml` |
| Major | The basal `brain heart infusion agar (Difco)` row was replaced by inferred full-strength BHI constituents. This loses the source's 1 L opaque agar base and imports unsupported constituent rows from a generic MicrobeNotes page. | TOGO M2855 lists a 1 L `brain heart infusion agar (Difco)` row; the record has no opaque BHI agar ingredient or CultureMech link for the agar base. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml`; likely also the TOGO/BHI premix expansion importer |
| Major | Atmosphere gases are modeled as VARIABLE ingredients. | Kersulyte et al. state that growth used a microaerobic 5% O2 and 10% CO2 atmosphere. The record puts `CO2` and `O2` in `ingredients` without those percentages or atmosphere scope. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml` |
| Major | The record has no structured source reference for the primary article that TOGO mined. | TOGO has no `src_url`; the record cites only `https://togomedium.org/medium/M2855` and a MicrobeNotes page for generic BHI agar. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml` |

## Recommended Edits

1. Replace the expanded calf-brain, beef-heart, proteose-peptone, dextrose,
   sodium-chloride, and disodium-phosphate rows with an opaque 1 L `brain heart
   infusion agar (Difco)` base, or an explicit link to a curated Difco BHI agar
   recipe if that is the repository pattern for opaque bases.
2. Keep `horse blood` at 7% and `isovitalex` at 0.4%, but remove the unsupported
   `PERCENT_W_V` specificity unless a source establishes the percent basis.
3. Move O2 and CO2 out of `ingredients` and record a microaerobic atmosphere
   with 5% O2 and 10% CO2.
4. Add a structured reference to Kersulyte et al. 2010 with PMID `21124785`,
   DOI `10.1371/journal.pone.0015076`, or PMCID `PMC2993954`.
5. Regenerate the generated merge after the normalized owner or importer is
   corrected.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/brain_heart_infusion_agar_containing_7_horse_blood_and_0_4_isovitalex.yaml`
  after curation.
- Rerun the focused LinkML, strict, term, and reference validators on the
  normalized owner and regenerated merge.
- Rerun `just verify-merges` to prove the merged record was regenerated from
  the corrected normalized source.
- Manually compare the corrected row set to TOGO M2855 and Kersulyte et al.
  2010 to confirm the gas rows are only incubation-atmosphere conditions.

## Additional Notes

- Optional empty temperature and preparation slots were not treated as defects;
  the inspected source did not state a temperature or preparation procedure.
- `horse blood` is unresolved in the ingredient-grounding report, but this
  review did not force a CHEBI grounding for that complex undefined material.
