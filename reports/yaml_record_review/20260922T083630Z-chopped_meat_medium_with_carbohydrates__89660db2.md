# YAML Record Review: chopped_meat_medium_with_carbohydrates

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__89660db2.yaml`
- Started UTC: 2026-09-22T08:33:01Z
- Finished UTC: 2026-09-22T08:36:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__89660db2.yaml` |
| Stable ID | `CultureMech:009294` |
| Label | `chopped_meat_medium_with_carbohydrates` |
| Source term | `TOGO:M2743` |
| Source document | `DSMZ_Medium110.pdf` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates.yaml` |
| Merge status | Generated from one source recipe, `TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates` |

The maintained owner has the same recipe content as the generated record before
the generated merge footer, so future fixes belong in the normalized TOGO owner
or in the TOGO import code that translates volumes, gas, and stock solutions.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Pass; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__89660db2.yaml` reported `No issues found`. |
| Strict schema | Pass; `scripts/validate_strict.py data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__89660db2.yaml --out /private/tmp/chopped_meat_medium_with_carbohydrates__89660db2.strict.tsv --workers 1 --quiet` scanned one file and emitted zero error rows. |
| Reference validation | Pass with no semantic coverage; `linkml-reference-validator validate data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__89660db2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported zero total checks because the record has no structured evidence references. |
| Term validation | Pass; `linkml-term-validator validate-data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__89660db2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed successfully, aside from the expected `eutils` `pkg_resources` deprecation warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries. |

`just` wrappers were not used because the project environment attempts to build
`llvmlite==0.46.0` under Python 3.13 and fails before the focused validators
can run. The checks above ran the same validator entry points in an offline
Python 3.11 `uv` environment.

## Identity and Grounding

The record identity is correct for TOGO `M2743`: TOGO names the source
`Chopped Meat Medium With Carbohydrates`, points to DSMZ Medium 110, and the
inspected DSMZ PDF is recipe 110 with the same medium name. The generated
record is not a merge of duplicates; it is a one-source product of
`TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates.yaml`.

This is the base DSMZ Medium 110 formulation. The same DSMZ PDF also describes
conditional post-autoclave Haemin plus Vitamin K1 or K3 additions, an agar-slant
option, and three strain-specific notes. Those branches should be modeled as
variants or optional child recipes, not inlined unconditionally into this base
TOGO `M2743` record.

## Evidence

Supported by the inspected TOGO `M2743` API payload and the DSMZ Medium 110 PDF:

- The source identity, medium name, pH 7.0, and source PDF URL are correct.
- The basal meat infusion starts with 500 g fat-free ground beef, 1000 ml
  distilled water, and 25 ml of 1 N NaOH.
- After boiling, cooling, skimming, filtering, and making the filtrate up to
  1000 ml, the recipe adds 30 g Casitone, 5 g yeast extract, 5 g K2HPO4,
  0.5 ml Na-resazurin solution at 0.1% w/v, 4 g D-glucose, and 1 g each of
  cellobiose, maltose, and soluble starch.
- The recipe becomes anoxic by boiling, cooling under a 100% N2 atmosphere,
  adding 0.5 g/l L-cysteine hydrochloride, adjusting to pH 7.0, dispensing 7 ml
  into Hungate-type tubes under the same gas, and autoclaving at 121 C for
  30 min.

Unsupported or under-scoped in the current record:

- `Distilled water` is stored as `1000 G_PER_L`; the source provides a
  1000 ml preparation volume and later says the filtrate is made up to a final
  volume of 1000 ml.
- `NaOH 1 N` is stored as `25 G_PER_L`; the source provides 25 ml of a
  1 N solution.
- `Na-resazurin solution (0.1% w/v)` is stored as an empty solution at
  `0.5 G_PER_L`; the source provides 0.5 ml of a 0.1% w/v stock solution.
- `N2` is an ingredient with `value: variable`, even though TOGO preserves
  the source value as 100% and the DSMZ PDF scopes nitrogen to the anoxic
  atmosphere.
- All source preparation steps have been dropped from the recipe.

## Completeness

The record has all major basal DSMZ 110 ingredients, but the recipe is not
complete enough to execute. A curator would not know from the YAML that the
first three materials form a boiled meat infusion, that the filtrate is made up
to 1000 ml before the soluble additions, that the medium must be boiled and
cooled under nitrogen, or that 0.5 ml of Na-resazurin stock is the redox
indicator addition.

The omissions of agar, Haemin, Vitamin K1, Vitamin K3, horse serum, and the two
alternate pH notes are not defects in this base record. DSMZ marks agar as an
agar-slant option, Haemin/vitamin K as catalogue-dependent, horse serum as a
DSM 22787 supplement, and pH shifts as DSM 100320 / DSM 103060 notes.

An ignored-inclusive `rg --no-ignore --hidden` search over
`data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and
`reports` for exact `CultureMech:009294`, `TOGO:M2743`, `M2743`, the
`89660db214c7d390eb54f543adb13178de4183437ddc6c6e7a054e7232275bf9`
fingerprint, and the `TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates` stem
found this single owner plus its generated product, indexes, and review
manifests. It did not find a second owner for exact TOGO `M2743`.

Empty `target_organisms` and growth-evidence slots are acceptable here because
the inspected DSMZ PDF is a source recipe and does not assert growth by a
particular organism on this medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three preparation volumes were flattened into gram-per-liter concentrations. | DSMZ and TOGO specify 1000 ml distilled water, 25 ml 1 N NaOH, and 0.5 ml 0.1% w/v Na-resazurin solution; the record stores all three as `G_PER_L`, and the Na-resazurin stock has no composition. | `data/normalized_yaml/bacterial/TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates.yaml` and, if systematic, the TOGO volume importer. |
| Major | The anoxic preparation workflow is missing. | DSMZ carries meat trimming, boiling, skimming, filtration, final 1000 ml makeup, N2 cooling, L-cysteine addition, pH adjustment, 7 ml Hungate-tube dispensing, and 121 C for 30 min autoclaving. None of those steps are represented. | `data/normalized_yaml/bacterial/TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |
| Major | Nitrogen gas is modeled as a variable ingredient instead of the exact gas atmosphere. | DSMZ scopes N2 to an anoxic gas atmosphere and TOGO encodes `conc_value: 100`, `conc_unit: %`; the migrated YAML lost the 100% value and the atmospheric role. | `data/normalized_yaml/bacterial/TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates.yaml` and, if systematic, the TOGO gas importer. |
| Minor | The L-cysteine ingredient still carries a legacy `mediaingredientmech_term` link and no CHEBI term. | The source ingredient is L-cysteine hydrochloride at 0.5 g/l; the ingredient identity is retained in `preferred_term`, but the June 2026 migration did not replace this one legacy MIM link with a CHEBI keyed link. | `data/normalized_yaml/bacterial/TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M2743_Chopped_Meat_Medium_With_Carbohydrates.yaml`,
   convert water and 1 N NaOH from concentration-like ingredients into the
   explicit meat-infusion preparation quantities stated by DSMZ.
2. Model `Na-resazurin solution (0.1% w/v)` as a 0.5 ml addition of the stated
   stock solution rather than as an unknown empty solution at `0.5 G_PER_L`.
3. Add the DSMZ preparation workflow in order: meat trimming, mixing meat with
   water and NaOH, boiling, skimming and filtering, final 1000 ml makeup,
   adding the second table of solutes, boiling and cooling under 100% N2,
   adding L-cysteine hydrochloride, adjusting to pH 7.0, dispensing under N2,
   and autoclaving at 121 C for 30 min.
4. Move nitrogen out of the ingredient list into a 100% N2 atmosphere field or
   equivalent structured condition.
5. Re-resolve `L-cysteine hydrochloride` through the packaged
   MediaIngredientMech label index so the ingredient has a current exact
   CHEBI-backed link or an explicit unresolved note.
6. Regenerate `data/merge_yaml/merged/` so the generated
   `chopped_meat_medium_with_carbohydrates__89660db2.yaml` reflects the
   normalized fix.

## Follow-up Checks

- Run focused open-schema, strict, reference, and term validation on the edited
  TOGO M2743 normalized record.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating merged YAML to prove this one-source generated record is fresh.
- Re-read the regenerated merged record against the DSMZ Medium 110 PDF and
  confirm that the optional agar, Haemin/K1, Haemin/K3, DSM 22787 horse-serum,
  DSM 100320 pH, and DSM 103060 pH branches remain separate from the base
  `M2743` recipe.

## Additional Notes

- The direct DSMZ owner at `data/normalized_yaml/bacterial/chopped_meat_medium_with_carbohydrates.yaml`
  covers the same PDF but currently inlines the optional agar, Haemin, Vitamin
  K1, and Vitamin K3 material. Do not merge those optional branches into M2743
  as unconditional base ingredients.
- TOGO M2743 preserves more of the base DSMZ 110 table than the older direct
  DSMZ import, but it still drops every free-text DSMZ preparation comment.
