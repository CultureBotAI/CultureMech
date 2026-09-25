# YAML Record Review: chthonomonas_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/chthonomonas_medium__5a3ad768.yaml`
- Started UTC: 2026-09-22T08:48:33Z
- Finished UTC: 2026-09-22T08:50:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/chthonomonas_medium__5a3ad768.yaml` |
| Stable ID | `CultureMech:000754` |
| Label | `chthonomonas_medium` |
| Source term | `mediadive.medium:1291` |
| Source document | `DSMZ_Medium1291.pdf` |
| Maintained owner | `data/normalized_yaml/bacterial/chthonomonas_medium.yaml` |
| Other merged source | `data/normalized_yaml/bacterial/t49_medium.yaml` |

The generated record was merged from the DSMZ owner and the KOMODO T49 mirror
on 2026-08-06. Both maintained records were later edited by
`apply_cocktail_nesting.py`, so future fixes belong in the normalized owners
followed by a merge regeneration.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Pass; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chthonomonas_medium__5a3ad768.yaml` reported `No issues found`. |
| Strict schema | Pass; `scripts/validate_strict.py data/merge_yaml/merged/chthonomonas_medium__5a3ad768.yaml --out /private/tmp/chthonomonas_medium__5a3ad768.strict.tsv --workers 1 --quiet` scanned one file and emitted zero error rows. |
| Reference validation | Pass with no semantic coverage; `linkml-reference-validator validate data data/merge_yaml/merged/chthonomonas_medium__5a3ad768.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported zero total checks because the record has no structured evidence references. |
| Term validation | Pass; `linkml-term-validator validate-data data/merge_yaml/merged/chthonomonas_medium__5a3ad768.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed successfully, aside from the expected `eutils` `pkg_resources` deprecation warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries. |

`just` wrappers were not used because the project environment attempts to build
`llvmlite==0.46.0` under Python 3.13 and fails before the focused validators
can run. The checks above ran the same validator entry points in an offline
Python 3.11 `uv` environment.

## Identity and Grounding

The DSMZ source identity is correct. `CultureMech:000754` points to
`mediadive.medium:1291`, DSMZ Medium 1291, and the inspected DSMZ PDF is
`1291: CHTHONOMONAS MEDIUM`.

The merge identity is only partly resolved. The merged `t49_medium` KOMODO
source says `KOMODO Medium 1291` and `DSMZ Medium: 1291`, and an August 2026
curation event says its composition reproduced MediaDive 1291 across 21 shared
compounds. However, `t49_medium.yaml` still carries `ph_value: 6.5`, while the
DSMZ owner carries the source range 5.0 to 5.3.

## Evidence

Supported by the inspected DSMZ Medium 1291 PDF:

- The basal medium contains 0.50 g Gellan Gum, 4.00 g ammonium sulfate,
  0.45 g K2HPO4, 0.15 ml CaCl2 x 2 H2O, 1.00 ml Trace element solution SL-11,
  1.00 g MgCl2 x 6 H2O, 0.01 g yeast extract, 1.00 ml Seven vitamins solution,
  and 1000 ml distilled water.
- The medium is adjusted to pH 5.0 to 5.3 and dispensed into Hungate-type tubes
  or similar vials under air up to 30% of their volume.
- MgCl2, yeast extract, and vitamins are added after autoclaving from sterile
  stock solutions.
- Trace element solution SL-11 is a 1000 ml stock containing Na2-EDTA,
  FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O,
  NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O.
- Seven vitamins solution is a 1000 ml stock containing Vitamin B12,
  p-aminobenzoic acid, biotin, nicotinic acid, calcium pantothenate,
  pyridoxine hydrochloride, and thiamine-HCl x 2 H2O.

Unsupported or stale in the current generated record:

- The generated record still exposes all trace-element and vitamin stock
  internals as parent ingredients. Its maintained owners now contain two
  `1 ML_PER_L` solution records, so the generated YAML predates the normalized
  August 2026 nesting repairs.
- The normalized stock nesting is incomplete: the DSMZ owner moved only FeCl2
  into Trace element solution SL-11 and only four of seven vitamins into Seven
  vitamins solution. The KOMODO owner has the same partial nesting.
- `CaCl2 x 2 H2O` is modeled as `0.15 G_PER_L`, but DSMZ lists `0.15 ml`.
- The source lists 1000 ml distilled water, but neither the generated record
  nor the DSMZ normalized owner keeps it.
- The generated merge hides the pH disagreement between the DSMZ owner
  and the KOMODO `t49_medium` owner.

## Completeness

The DSMZ owner is closer than the generated record because it now has explicit
Trace element solution SL-11 and Seven vitamins solution nodes. It is still
not complete enough to regenerate the source faithfully: six trace components
and three vitamins remain in the parent ingredient list, calcium chloride is
still a mass concentration, and the source water volume is absent.

An ignored-inclusive `rg --no-ignore --hidden` search over
`data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and
`reports` for exact `CultureMech:000754`, `mediadive.medium:1291`,
`DSMZ_Medium1291`, `5a3ad768`, and `chthonomonas_medium.yaml` tokens found the
DSMZ owner, the generated stale merge, the KOMODO `t49_medium` duplicate, a
separate TOGO `M2334` duplicate, and index/report entries.

Empty `target_organisms` and growth-evidence slots are acceptable for the DSMZ
source recipe; the source PDF does not assert a specific tested strain.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale relative to both normalized owners. | The generated merge still has 22 parent ingredients and no `solutions`; `chthonomonas_medium.yaml` and `t49_medium.yaml` both have August 2026 `NESTED_FLATTENED_COCKTAIL` events that moved stock-strength components into Trace element solution SL-11 and Seven vitamins solution. | Regenerate `data/merge_yaml/merged/` from `chthonomonas_medium.yaml` and `t49_medium.yaml` after finishing the stock fixes. |
| Major | Trace element and vitamin stock nesting is incomplete. | DSMZ defines a nine-component Trace element solution SL-11 and a seven-component Seven vitamins solution, each added at 1 ml/l. The DSMZ owner currently nests only FeCl2 and four vitamins. | `data/normalized_yaml/bacterial/chthonomonas_medium.yaml` and the same pattern in `data/normalized_yaml/bacterial/t49_medium.yaml`. |
| Major | Calcium chloride has the wrong amount type. | DSMZ lists `CaCl2 x 2 H2O` as `0.15 ml`; the YAML records `0.15 G_PER_L`, implying a solid salt mass. | `data/normalized_yaml/bacterial/chthonomonas_medium.yaml` and `data/normalized_yaml/bacterial/t49_medium.yaml`. |
| Minor | The 1000 ml source water volume is missing. | DSMZ lists `Distilled water 1000.00 ml`; neither normalized owner includes water in the basal recipe. | `data/normalized_yaml/bacterial/chthonomonas_medium.yaml` and `data/normalized_yaml/bacterial/t49_medium.yaml`. |
| Minor | The source-duplicate merge masks a pH conflict. | DSMZ Medium 1291 uses pH 5.0 to 5.3, while `t49_medium.yaml` still has `ph_value: 6.5`. | `data/normalized_yaml/bacterial/t49_medium.yaml` and merge conflict handling. |

## Recommended Edits

1. Complete `Trace element solution SL-11` in
   `data/normalized_yaml/bacterial/chthonomonas_medium.yaml` and
   `data/normalized_yaml/bacterial/t49_medium.yaml`: move Na2-EDTA, ZnCl2,
   MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and
   Na2MoO4 x 2 H2O from the parent ingredients into the stock already holding
   FeCl2.
2. Complete `Seven vitamins solution` in both owners by moving
   p-aminobenzoic acid, biotin, and calcium pantothenate into the stock that
   already holds Vitamin B12, nicotinic acid, pyridoxine, and thiamine.
3. Revisit `CaCl2 x 2 H2O` against MediaDive/DSMZ source data and preserve the
   0.15 ml amount as a stock-solution volume rather than a 0.15 g/l salt.
4. Add or explicitly account for the DSMZ 1000 ml distilled water volume.
5. Resolve the `t49_medium` pH 6.5 value before keeping it as a source
   duplicate of DSMZ Medium 1291.
6. Regenerate `data/merge_yaml/merged/` after the normalized owners are fixed
   so `chthonomonas_medium__5a3ad768.yaml` reflects the nested stocks.

## Follow-up Checks

- Run focused open-schema, strict, reference, and term validation on the edited
  DSMZ and KOMODO normalized records.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating merged YAML.
- Re-read the regenerated `chthonomonas_medium__5a3ad768.yaml` against DSMZ
  Medium 1291 and confirm that exactly nine trace components and seven vitamin
  components are nested under the two 1 ml/l stock additions.
- Inspect the separate TOGO `M2334` Chthonomonas record and decide whether it
  should merge after its stock volumes are repaired.

## Additional Notes

- `data/merge_yaml/merged/CHTHONOMONAS_MEDIUM.yaml` is a separate one-source
  TOGO `M2334` rendering of the same DSMZ PDF. It currently flattens three
  1000 ml water volumes into `3000 G_PER_L` and should not be merged with this
  record until those stock-scope errors are fixed.
- The source instruction to add MgCl2, yeast extract, and vitamins after
  autoclaving is partially captured only in prose. DSMZ does not provide
  explicit MgCl2 or yeast-extract stock recipes in the inspected PDF.
