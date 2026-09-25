# YAML Record Review: Lactobacilli MRS Agar/Broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml
- Started UTC: 2026-09-23T18:17:51Z
- Finished UTC: 2026-09-23T18:19:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml` |
| Generated status | Generated canonical merge from `data/normalized_yaml/bacterial/lactobacilli_mrs_agar_broth.yaml`; do not edit directly |
| Schema class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008837` |
| Name | `lactobacilli_mrs_agar_broth` |
| Original name | `Lactobacilli MRS Agar/Broth` |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Source accession | `TOGO:M2249` |
| Merge fingerprint | `4fdc9ce6eb560ee7698f6b54a1df55178d71d69252951fbd769df560d1b6ed76` |
| Maintained owner inspected | `data/normalized_yaml/bacterial/lactobacilli_mrs_agar_broth.yaml` |

This generated record is stale. Its maintained owner has a September 11
`repair_togo_m2249_m2250_score15.py` event that expanded ATCC Medium 416's
scratch formulation, fixed DI water to `1.0 L`, removed the duplicate
`Lactobacilli MRS` wrapper ingredient, added final pH `6.5 +/- 0.2`, added
boil/autoclave preparation for the solid agar formulation, and recorded TOGO
M2249 plus ATCC Medium 416 references.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml` | Passed; `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml --out /private/tmp/lactobacilli_mrs_agar_broth__4fdc9ce6.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:008837`, `TOGO:M2249`, and the `SOLID_AGAR` physical state
  identify the solid agar TOGO import for ATCC Medium 416.
- A same-label liquid sibling, `TOGO:M2250` / `CultureMech:008839`, is present
  at `data/merge_yaml/merged/Lactobacilli_MRS_Agar_Broth.yaml`. This is not the
  reviewed record and should stay physically distinct because TOGO M2250 omits
  agar and is the broth formulation.
- The CHEBI groundings still present in the generated record are exact for agar,
  dextrose, sodium acetate, disodium hydrogenphosphate, and manganese sulfate
  monohydrate.
- The generated record is missing newer, source-supported FOODON/MICRO
  groundings for Proteose Peptone #3, Beef Extract, Yeast Extract, and DI Water
  from the maintained owner.
- The generated record correctly leaves Sorbitan Monooleate and Ammonium
  Citrate ungrounded; ATCC uses generic names and the normalized owner records
  that no specific ChEBI term was chosen.

Ignored-inclusive searches were run before treating siblings and owners as
resolved:

- `rg --no-ignore --hidden` over `data/normalized_yaml`, `data/merge_yaml`, and
  `reports/archive` for `CultureMech:008837`, `TOGO:M2249`, the exact label,
  `lactobacilli_mrs_agar_broth.yaml`, and fingerprint prefix `4fdc9ce6` found
  the reviewed generated target, its maintained normalized owner, normalized
  TOGO indexes, and archived validation mentions.
- A second ignored-inclusive search over the same roots for `CultureMech:008839`
  and `TOGO:M2250` found the same-label liquid sibling in normalized YAML,
  normalized indexes, the archive, and
  `data/merge_yaml/merged/Lactobacilli_MRS_Agar_Broth.yaml`.

## Evidence

Supported in inspected sources:

- The live TOGO M2249 payload identifies `Lactobacilli MRS Agar/Broth`, points
  to the ATCC Medium 416 PDF, reports final pH `6.5 +/- 0.2`, marks the recipe
  as `Agar Medium`, lists DI water and 15 g agar, and expands the Lactobacilli
  MRS subcomponent into the scratch broth ingredients.
- The ATCC Medium 416 PDF distinguishes Agar Medium from Broth Medium. The
  solid agar formulation uses commercial Lactobacilli MRS Agar powder plus
  1000 ml DI water with boiling and autoclaving; the broth formulation uses
  55.0 g commercial Lactobacilli MRS Broth plus 1000 ml DI water.
- The ATCC PDF also supplies the scratch Lactobacilli MRS Broth composition:
  10 g Proteose Peptone #3, 10 g Beef Extract, 5 g Yeast Extract, 20 g Dextrose,
  1 g Sorbitan Monooleate, 2 g Ammonium Citrate, 5 g Sodium Acetate, 0.05 g
  MnSO4 x H2O, 2 g Na2HPO4, and 1000 ml DI Water, with final pH `6.5 +/- 0.2`.

Unsupported or stale in the generated target:

- The generated target carries both `Lactobacilli MRS` at 55 g/L and every
  ingredient in the expanded scratch formula. That double-counts the MRS broth:
  ATCC presents the commercial broth powder and the scratch formula as
  alternatives, not additive ingredients.
- `DI Water` as `1000 G_PER_L` is dimensionally wrong for the source's
  1000 ml final-volume entry and was already corrected to `1.0 L` upstream.
- The generated target omits the final pH range, boil/autoclave steps, explicit
  `sterilization: AUTOCLAVE`, references, curated source notes, and
  intentionally-unmapped ingredient flags that are present in the maintained
  owner.

## Completeness

Consequential gaps:

- The generated target is missing the September 11 normalized repair.
- The generated target has 12 ingredients because it still includes both DI
  water and the commercial broth wrapper alongside the 10 scratch formulation
  rows; the maintained owner has the 11 rows appropriate for the TOGO M2249
  scratch-plus-agar representation.
- The generated target has no source references even though the TOGO page and
  ATCC PDF are both known and recorded upstream.

Empty or absent fields that are not defects for this generated ATCC recipe:

- `target_organisms`, growth metrics, genome assembly, salinity, atmosphere,
  storage, and shelf-life fields can remain empty until a strain-level growth
  source supports them.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Major | The reviewed generated record is stale relative to its normalized owner. | The generated file lacks the September 11 `repair_togo_m2249_m2250_score15.py` changes: pH, references, boil/autoclave steps, water-unit correction, wrapper removal, and curated FOODON/MICRO ingredient groundings. | Regenerate `data/merge_yaml/merged/` with `just merge-recipes`; if regeneration drops the repair, fix `src/culturemech/merge/merge_recipes.py` rather than the generated YAML. |
| Major | The generated ingredient list double-counts Lactobacilli MRS by retaining the 55 g/L commercial broth row and its expanded scratch ingredients. | ATCC Medium 416 presents the commercial broth powder and the scratch broth formulation as alternatives. The maintained owner already removed the `Lactobacilli MRS` wrapper from the expanded formula. | Already corrected in `data/normalized_yaml/bacterial/lactobacilli_mrs_agar_broth.yaml`; regenerate the merge output and verify the wrapper row disappears. |
| Major | `DI Water` uses an invalid mass-per-liter concentration. | TOGO and ATCC both state 1000 ml DI water. The stale generated YAML encodes that as `1000 G_PER_L`; the maintained owner encodes `1.0 L`. | Already corrected in `data/normalized_yaml/bacterial/lactobacilli_mrs_agar_broth.yaml`; regenerate the generated layer. |
| Major | Source evidence and preparation details are absent from the generated target. | TOGO M2249 exposes pH `6.5 +/- 0.2`; ATCC Medium 416 instructs boiling to dissolve agar and autoclaving at 121 C. The generated file has neither a `ph_range`, `preparation_steps`, `sterilization`, nor `references`. | Already corrected in `data/normalized_yaml/bacterial/lactobacilli_mrs_agar_broth.yaml`; regenerate the generated layer. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` with
   `just merge-recipes` and inspect
   `data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml`.
2. Verify the regenerated `TOGO:M2249` record has 11 ingredients: the 10 scratch
   broth components plus agar, with no `Lactobacilli MRS` wrapper row.
3. Verify `DI Water` is `1.0 L`, the final pH is represented as `6.3` to `6.7`,
   the solid medium keeps `Agar` at 15 g/L, and the record has the ATCC boil and
   autoclave preparation steps.
4. Preserve the intentionally unmapped Sorbitan Monooleate and Ammonium Citrate
   state unless a curator resolves the exact supplied salts from a stronger
   source.

## Follow-up Checks

- Run `just merge-recipes`, then rerun the focused open, strict, reference, and
  term validators against
  `data/merge_yaml/merged/lactobacilli_mrs_agar_broth__4fdc9ce6.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm
  `lactobacilli_mrs_agar_broth__4fdc9ce6.yaml` is not in the `changed`,
  `only_in_tracked`, or `only_in_fresh` lists.
- Run `just verify-merges` after regeneration.
- Re-query TOGO M2249 and the ATCC Medium 416 PDF after regeneration to make
  sure the generated record still represents the solid agar formulation rather
  than the liquid M2250 sibling.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe
  schema section, the generated target, its normalized owner, the same-label
  M2250 normalized and generated sibling, live TOGO M2249 and M2250 payloads,
  and the ATCC Medium 416 PDF.
- The source label `Lactobacilli MRS Agar/Broth` is shared by `TOGO:M2249` and
  `TOGO:M2250`, so source ID and physical state are the important
  disambiguators.
