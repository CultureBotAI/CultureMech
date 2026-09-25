# YAML Record Review: chopped_meat_medium_with_carbohydrates

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__284e9255.yaml`
- Started UTC: 2026-09-22T08:28:38Z
- Finished UTC: 2026-09-22T08:32:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__284e9255.yaml` |
| Stable ID | `CultureMech:009854` |
| Label | `chopped_meat_medium_with_carbohydrates` |
| Source term | `TOGO:M466`, original source `JCM_M465` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M466_Chopped_Meat_Medium_With_Carbohydrates.yaml` |
| Merge status | Generated from one source recipe, `TOGO_M466_Chopped_Meat_Medium_With_Carbohydrates` |

The maintained owner has the same scientific content as the generated record
before the generated `merge_fingerprint` and `merged_from` footer, so future
fixes belong in the normalized TOGO owner or in the TOGO cross-reference import
logic rather than in `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Pass; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__284e9255.yaml` reported `No issues found`. |
| Strict schema | Pass; `scripts/validate_strict.py data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__284e9255.yaml --out /private/tmp/chopped_meat_medium_with_carbohydrates__284e9255.strict.tsv --workers 1 --quiet` scanned one file and emitted zero error rows. |
| Reference validation | Pass with no semantic coverage; `linkml-reference-validator validate data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__284e9255.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported zero total checks because the record has no structured evidence references. |
| Term validation | Pass; `linkml-term-validator validate-data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__284e9255.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed successfully, aside from the expected `eutils` `pkg_resources` deprecation warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries. |

`just` wrappers were not used because the project environment attempts to build
`llvmlite==0.46.0` under Python 3.13 and fails before the focused validators
can run. The checks above ran the same validator entry points in an offline
Python 3.11 `uv` environment.

## Identity and Grounding

The source identity is coherent. The record is `CultureMech:009854` for TOGO
Medium `M466`, TOGO reports original source `JCM_M465`, and the inspected JCM
page at `GRMD=465` is medium 465, `CHOPPED MEAT MEDIUM WITH CARBOHYDRATES`.
Both TOGO and JCM define this as JCM Medium 461 plus four carbohydrate
supplements.

The ontology grounding to `TOGO:M466` is therefore correct for this generated
record. The generated corpus also contains `CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml`
from `data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml`;
that duplicate describes the same JCM medium 465 source and should eventually
merge with this TOGO record, not with the unsupplemented JCM 461 base medium.

## Evidence

Supported by the inspected TOGO `M466` API response and JCM `GRMD=465` page:

- The label `Chopped Meat Medium With Carbohydrates` and the JCM source
  identity are supported.
- The recipe is a derivative of Chopped Meat Medium, JCM 461 / TOGO `M461`.
  TOGO encodes the referenced base as `reference_media_id: M461` with volume
  `1 L`.
- The four added carbohydrates are source-supported: glucose, cellobiose,
  maltose, and soluble starch. JCM specifies `0.4% glucose, 0.1% cellobiose,
  0.1% maltose and 0.1% soluble starch`, and TOGO carries the same percentage
  values as `0.4%`, `0.1%`, `0.1%`, and `0.1%`.

Unsupported or under-scoped in the current record:

- All four carbohydrate amounts have been replaced with
  `value: variable`, `unit: VARIABLE`, losing the exact source percentages.
- The Medium 461 base is represented as a `solutions` entry named
  `CHOPPED MEAT MEDIUM (see Medium [M461])` with empty `composition` and
  `1 G_PER_L`. The source says to use one liter of Medium 461, not one gram
  per liter of an unknown stock solution.
- The record has no preparation sequence even though the referenced M461 source
  provides pH 7.0, a nitrogen dispensing atmosphere, 7 ml anaerobic tube
  portions, and an autoclave condition of 121 C for 30 min after the meat
  infusion is supplemented.
- The related direct JCM import for `JCM_J465` lost the carbohydrate additions
  and was merged with `JCM_J461_CHOPPED_MEAT_MEDIUM`, producing a generated
  duplicate that denotes JCM 465 in its label and source history but contains
  the base JCM 461 composition.

## Completeness

The generated record is materially incomplete as a usable medium recipe. It
does not inline or link a resolved Medium 461 base, it does not preserve the
four carbohydrate concentrations, and it lacks the M461 preparation details
that make the medium anaerobic and set final pH.

An ignored-inclusive `rg --no-ignore --hidden` search over
`data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and
`reports` for exact `M466`, `M461`, `JCM_J461`, `GRMD=461`, and
`GRMD=465` tokens found the TOGO owner, the direct JCM 465 duplicate, the
TOGO and JCM 461 base records, index entries, and prior content-review reports.
Those hits confirm that the missing base recipe is not absent from the corpus;
the problem is that the M466 TOGO owner preserved its upstream cross-reference
as an unresolved empty solution.

Empty `target_organisms`, growth metrics, variants, and organism-specific
evidence are acceptable here. The inspected JCM 465 page is a source recipe and
does not assert a tested strain or a growth outcome.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Medium 461 base is modeled as an empty unknown solution at `1 G_PER_L`. | JCM 465 instructs users to use Medium 461 and TOGO encodes the base as `1 L`, `reference_media_id: M461`; neither source supports a mass concentration or an unresolved stock solution. | `data/normalized_yaml/bacterial/TOGO_M466_Chopped_Meat_Medium_With_Carbohydrates.yaml` and, if systematic, the TOGO cross-reference importer. |
| Major | The four carbohydrate concentrations are exact in the source but defaulted to `VARIABLE`. | JCM 465 and TOGO M466 both provide percentages for glucose, cellobiose, maltose, and soluble starch. | `data/normalized_yaml/bacterial/TOGO_M466_Chopped_Meat_Medium_With_Carbohydrates.yaml` and the TOGO percentage importer. |
| Major | Preparation, pH, atmosphere, and final dispensing context from the M461 base recipe are not reachable from this record. | The JCM 461 source carries pH 7.0, the meat infusion workflow, an N2 dispensing atmosphere, butyl-rubber-stoppered tubes, and 121 C for 30 min autoclaving; M466 is defined as M461 plus carbohydrates. | `data/normalized_yaml/bacterial/TOGO_M466_Chopped_Meat_Medium_With_Carbohydrates.yaml`, after the base `TOGO_M461_Chopped_Meat_Medium.yaml` record is curated source-faithfully. |
| Major | The corpus has an unreconciled JCM 465 duplicate that now merges with the wrong recipe. | `JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml` describes the same `GRMD=465` source, but its generated product is merged with `JCM_J461_CHOPPED_MEAT_MEDIUM` and contains only the unsupplemented base formulation. | `data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml` plus merge fingerprinting after its carbohydrate delta is restored. |
| Minor | `soluble starch` is grounded only to generic `CHEBI:28017` starch. | TOGO M466 has a GMO label of `Soluble starch`; the current record preserves the source wording in `preferred_term` but grounds the ingredient to the broader starch term. | `data/normalized_yaml/bacterial/TOGO_M466_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |

## Recommended Edits

1. Replace the empty `CHOPPED MEAT MEDIUM (see Medium [M461])` solution in
   `data/normalized_yaml/bacterial/TOGO_M466_Chopped_Meat_Medium_With_Carbohydrates.yaml`
   with a resolvable parent or variant relationship to source-faithful TOGO
   M461, or with the complete resolved M461 base composition if the schema
   expects an inline recipe.
2. Preserve the M466 carbohydrate amounts from the source: glucose at 0.4%;
   cellobiose, maltose, and soluble starch at 0.1% each. Avoid converting
   percent to grams per liter unless the curation event states the basis for
   the conversion.
3. Ensure the inherited M461 procedure is reachable from the final recipe:
   pH 7.0, meat infusion and filtration, final 1 L makeup, L-cysteine addition,
   N2 dispensing into meat-particle tubes, stopper sealing, and 121 C for
   30 min autoclaving.
4. Repair `data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml`
   so it includes the same four carbohydrate additions and no longer
   fingerprints as the unsupplemented JCM 461 medium.
5. Re-run the merge pipeline so `TOGO_M466...` and `JCM_J465...` collapse to
   one canonical generated recipe for JCM 465 while staying distinct from
   the base JCM 461 medium.
6. Revisit `soluble starch` with the packaged MediaIngredientMech label index;
   keep the source label explicit if no exact CHEBI class is available.

## Follow-up Checks

- Run focused open-schema, strict, reference, and term validation on the edited
  TOGO M466 and JCM J465 normalized records.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  `data/merge_yaml/merged/` to prove the two JCM 465 imports merge with each
  other rather than with JCM 461.
- Re-read the regenerated `chopped_meat_medium_with_carbohydrates` canonical
  record and compare it against both `https://togomedium.org/medium/M466` and
  `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465`.
- Re-check TOGO/JCM M461 after its own curation because M466 inherits its base
  composition and preparation semantics.

## Additional Notes

- The TOGO M461 owner has the L-cysteine and N2 tokens that the older direct
  JCM 461 import lacks, but it still flattens 25 ml of 1 N NaOH, 1 L water,
  1 mg resazurin, and nitrogen gas into ingredient concentrations. Do not use
  either base record uncritically when repairing M466.
- The `JCM_J465` direct import contains a single free-text preparation step
  with the carbohydrate instruction, but not structured carbohydrate
  ingredients. Its later reference-resolution event copied six base ingredients
  from JCM 461 and still left the carbohydrate delta unmodeled.
