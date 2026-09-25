# YAML Record Review: Chlamydia serpentis & poikilotherma Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chlamydia_serpentis_poikilotherma_medium.yaml
- Started UTC: 2026-09-22T07:00:24Z
- Finished UTC: 2026-09-22T07:02:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/chlamydia_serpentis_poikilotherma_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001238` |
| Name | `chlamydia_serpentis_poikilotherma_medium` |
| Original name | `Chlamydia serpentis & poikilotherma Medium` |
| Media term | `mediadive.medium:1793` / `Chlamydia serpentis & poikilotherma Medium` |
| Source | DSMZ Medium 1793 through MediaDive |
| Generated status | Single-source derived merge generated from `data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml` |

The reviewed file is a generated one-record merge. Substantive fixes belong in
`data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml`
or in the MediaDive importer that produced that normalized source.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chlamydia_serpentis_poikilotherma_medium.yaml` | Passed with no issues reported. |
| Strict closed-schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/chlamydia_serpentis_poikilotherma_medium.yaml --out /private/tmp/chlamydia_serpentis_poikilotherma_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/chlamydia_serpentis_poikilotherma_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/chlamydia_serpentis_poikilotherma_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: that recipe validates standalone `history/*.yaml` records against `HistoryRecord`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

I used the offline `uv` validator invocations above instead of the `just`
validator wrappers because the local project lock currently tries to build
`llvmlite==0.46.0` under Python 3.13 and fails inside setuptools before the
CultureMech validators run.

## Identity and Grounding

- The CultureMech identity, normalized name, original name, and `mediadive.medium:1793`
  grounding consistently identify DSMZ Medium 1793.
- The direct DSMZ PDF for Medium 1793 and the MediaDive medium 1793 JSON both
  use the same title and describe the recipe for cultivation in LLC-MK2 cells.
- The only maintained owner is
  `data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml`.
  An ignored-independent `rg --no-ignore --hidden` search for
  `chlamydia_serpentis`, `poikilotherma`, `mediadive.medium:1793`, and
  `CultureMech:001238` across `data/normalized_yaml` and
  `data/merge_yaml/merged` found only that owner and this generated target for
  the identifiers reviewed here.

## Evidence

I inspected the direct DSMZ Medium 1793 PDF plus MediaDive's medium and
composition JSON for medium 1793. They support the record's source identity and
the ingredient names, but the imported quantities are stock-solution or volume
values rather than final medium concentrations:

- The main DSMZ 1793 solution uses `500 ml` MEM-Medium plus Glutamine, `100 ml`
  fetal bovine serum, `6 ml` D-glucose solution, and `0.70 ml` Cycloheximid
  solution in an approximately `607 ml` main solution. The record stores
  MEM-Medium as `500 G_PER_L` and fetal bovine serum as `100 G_PER_L`, which are
  not source-supported gram-per-liter concentrations.
- DSMZ defines D-glucose solution separately as `3 g` D-Glucose in `50 ml`
  demineralized water. The record stores D-Glucose as `60 G_PER_L`, the stock
  concentration, while MediaDive's final composition reports about
  `0.593081 g/L` after adding `6 ml` of that stock to the main solution.
- DSMZ defines Cycloheximid solution separately as `10 mg` Cycloheximid in
  `10 ml` demineralized water. The record stores Cycloheximid as `1 G_PER_L`,
  the stock concentration, while MediaDive's final composition reports about
  `0.00115321 g/L`.
- The two stock water rows, `50 ml` and `10 ml`, are separate preparation
  volumes. The record has one demineralized-water ingredient at `60.0 G_PER_L`
  with `Merged 2 duplicates: 50.0, 10.0`, which is neither a final mass
  concentration nor a faithful representation of the two stocks.
- The two `Filtrate.` instructions belong to D-glucose solution and
  Cycloheximid solution. The record flattens both as top-level `MIX` steps.

## Completeness

- Consequential solution boundaries are missing. DSMZ and MediaDive distinguish
  a main solution, D-glucose solution, Cycloheximid solution, two filtration
  steps, and water volumes for the two stock solutions; the record has only a
  flat `ingredients` list and top-level `preparation_steps`.
- The record omits MediaDive's free-text source description, "For cultivation
  in LLC-MK2 cells", so the host-cell culture context appears only indirectly in
  the preparation text.
- No `target_organisms`, `growth_metrics`, or dedicated growth-evidence entries
  are present. That is not by itself a defect: DSMZ 1793 is an imported
  formulation, and the source recipe does not provide a strain-specific growth
  evidence block for CultureMech to cite.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock-solution ingredients and volume additions were flattened into unsupported `G_PER_L` concentrations. | DSMZ 1793 adds `6 ml` D-glucose solution and `0.70 ml` Cycloheximid solution to a 607 ml main solution, with glucose and cycloheximide prepared in separate 50 ml and 10 ml stocks. The record instead stores the stock concentrations, `60 G_PER_L` and `1 G_PER_L`, as direct ingredient concentrations. | Fix `data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml`, or the MediaDive importer if the normalized flattening is source-owned. |
| major | The merged demineralized-water row is a cleanup artifact that combines two unrelated stock-solution water volumes. | DSMZ has `50 ml` water in the D-glucose stock and `10 ml` water in the Cycloheximid stock. The record has one water row with `60.0 G_PER_L` and an explicit `Merged 2 duplicates: 50.0, 10.0` note. | Fix `data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml` so each water volume is scoped to its stock solution. |
| minor | Preparation actions are overgeneric or misleading after import flattening. | The exact text for seeding, infection-medium exchange, centrifugation, and incubation is present, but all four steps use `action: HEAT`; stock-specific filtration steps are present only as duplicate top-level `MIX` steps. | Correct actions while adding solution-scoped preparation steps in `data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml`. |

## Recommended Edits

1. Replace the flat stock ingredient rows with solution references in
   `data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml`.
   Preserve the DSMZ main solution as 500 ml MEM-Medium, 100 ml fetal bovine
   serum, 6 ml D-glucose solution, and 0.70 ml Cycloheximid solution.
2. Add D-glucose solution as a 50 ml stock containing 3 g D-Glucose in 50 ml
   demineralized water, and Cycloheximid solution as a 10 ml stock containing
   10 mg Cycloheximid in 10 ml demineralized water. Keep each `Filtrate.`
   instruction attached to the corresponding stock.
3. Preserve the cell-culture preparation sequence from DSMZ 1793 but replace the
   imported `HEAT` actions with actions that match the actual seed, exchange,
   centrifuge, and incubation operations as closely as the schema permits.
4. Regenerate `data/merge_yaml/merged/chlamydia_serpentis_poikilotherma_medium.yaml`
   from the normalized owner instead of editing the generated merge file.

## Follow-up Checks

- Run `just validate-strict data/normalized_yaml/bacterial/chlamydia_serpentis_poikilotherma_medium.yaml`.
- Run `just merge-recipes` and then `just verify-merges` to prove the generated
  single-source merge was refreshed from the corrected normalized input.
- Re-open the regenerated merged record and compare the MEM/fetal-serum
  volumes, stock volumes, glucose/cycloheximide dilution arithmetic, water
  scoping, and filtration steps against DSMZ Medium 1793.

## Additional Notes

- DSMZ and MediaDive both spell the stock as `Cycloheximid solution`; the
  ingredient grounding to `CHEBI:27641` / cycloheximide is chemically correct.
- No alternate normalized owner, sibling variant, or second merged copy was
  found in the ignored-independent identifier search described above.
