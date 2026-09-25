# YAML Record Review: Brain Heart Infusion agar (amended with 5% (v/v) laked horse blood)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml
- Started UTC: 2026-09-21T23:33:55Z
- Finished UTC: 2026-09-21T23:35:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009466 |
| Label | Brain Heart Infusion agar (amended with 5% (v/v) laked horse blood) |
| Source accession | TOGO:M2932 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 643490b1f04f629a2d76c705ac79a3c757422ce861957698af9a79b17e88084a |

The reviewed file is generated from a single normalized owner. The generated
record and normalized owner currently agree, so formulation fixes belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml`
or in the TOGO importer rule that expanded the BHI agar base.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml --out /private/tmp/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- TOGO:M2932 resolves to Brain Heart Infusion agar amended with 5% (v/v) laked
  horse blood.
- The TOGO payload has no `src_url`, but an exact search for its cultivation
  sentence resolves to Miller et al. 2014, `Genome Biology and Evolution`, DOI
  `10.1093/gbe/evu249`, PMID `25381664`, PMCID `PMC4986449`.
- A gitignore-independent search for `TOGO:M2932`, `CultureMech:009466`, the
  merge fingerprint, the normalized slug, and the exact source label across
  `data`, `src`, `scripts`, `docs`, `.claude`, and `justfile` found one
  normalized owner plus the generated merge and generated indexes.
- The source recipe identity is correct, but the laked-horse-blood amount,
  basal BHI agar row, and gas atmosphere are not represented with the source's
  scope.

## Evidence

TOGO lists five source rows: 5% (v/v) laked horse blood, 1 L Brain Heart
Infusion agar from Becton Dickinson, carbon dioxide gas, nitrogen gas, and
hydrogen gas. Its comment, confirmed against Miller et al. 2014, says the
Campylobacter strains were cultured at 37 C on that BHI agar plus 5% laked
horse blood and that the incubation atmosphere was 5% H2, 10% CO2, and 85% N2.

The inspected primary article supports a growth condition, not a recipe in
which H2, CO2, and N2 are variable-concentration ingredients.

## Completeness

- Consequential gap: the record has no primary citation for Miller et al. 2014
  despite depending on that paper for the 37 C and 5/10/85 gas context.
- Consequential gap: the 37 C cultivation temperature is absent.
- Consequential gap: the gas percentages are absent.
- Empty `target_organisms` can remain empty until the exact Campylobacter strain
  set from the comparative-genomics paper is curated.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood` report, so
  this report did not overwrite an earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Laked horse blood is a volume-percent supplement, not a gram-per-liter mass. | TOGO M2932 imports `laked horse blood (Hema Resource & Supply, Aurora, OR)` with `volume: 5` and `unit: % (v/v)`, matching the primary paper's 5% (v/v) statement. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml` |
| Major | The basal `Brain Heart Infusion agar (Becton Dickinson, Sparks, MD)` row was replaced by inferred full-strength BHI constituents. This loses the source's 1 L opaque agar base and imports unsupported constituent rows from a generic MicrobeNotes page. | TOGO M2932 lists a 1 L `Brain Heart Infusion agar (Becton Dickinson, Sparks, MD)` row; the record has no opaque BHI agar ingredient or culturemech term for the agar base. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml`; likely also the TOGO/BHI premix expansion importer |
| Major | Incubation atmosphere gases are modeled as VARIABLE ingredients. | Miller et al. state an incubation atmosphere of 5% H2, 10% CO2, and 85% N2. The record puts those gases in `ingredients` without the percentages or atmosphere scope. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml` |
| Major | The record has no structured source reference for the primary article that TOGO mined. | TOGO has no `src_url`; the record cites only `https://togomedium.org/medium/M2932` and a MicrobeNotes page for generic BHI agar. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml` |

## Recommended Edits

1. Replace the expanded calf-brain, beef-heart, proteose-peptone, dextrose,
   sodium-chloride, and disodium-phosphate rows with an opaque 1 L `Brain Heart
   Infusion agar (Becton Dickinson, Sparks, MD)` base, or an explicit link to a
   curated BHI agar recipe if that is the repository pattern for opaque bases.
2. Change the laked-horse-blood amount to `5 PERCENT_V_V`.
3. Move H2, CO2, and N2 out of `ingredients` and record the atmosphere as 5%
   H2, 10% CO2, and 85% N2 at incubation scope.
4. Add a structured reference to Miller et al. 2014 with PMID `25381664`, DOI
   `10.1093/gbe/evu249`, or PMCID `PMC4986449`.
5. Capture the supported 37 C cultivation temperature and note that TOGO M2932
   is derived from Campylobacter growth conditions.
6. Regenerate the generated merge after the normalized owner or importer is
   corrected.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/brain_heart_infusion_agar_amended_with_5_v_v_laked_horse_blood.yaml`
  after curation.
- Rerun the focused LinkML, strict, term, and reference validators on the
  normalized owner and regenerated merge.
- Rerun `just verify-merges` to prove the merged record was regenerated from
  the corrected normalized source.
- Manually compare the corrected row set to TOGO M2932 and Miller et al. 2014
  to confirm that blood remains a v/v supplement and gases remain atmosphere
  conditions.

## Additional Notes

- The unsupported gas rows were added to `ingredients` by the historical import
  path before schema defaulting added VARIABLE concentrations.
- Optional empty organism slots were not treated as defects.
