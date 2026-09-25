# YAML Record Review: deferribacter_abyssi_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.yaml
- Started UTC: 2026-09-22T14:09:46Z
- Finished UTC: 2026-09-22T14:09:46Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002724`, label
`deferribacter_abyssi_medium`, original name `DEFERRIBACTER ABYSSI MEDIUM`,
under `data/merge_yaml/merged/`.

The generated recipe points at JCM Medium J365 and is merged with
`caminibacter_medium` / JCM Medium J367 as a `SOURCE_DUPLICATE`; future edits
belong in maintained normalized records and merge logic, chiefly:

- `data/normalized_yaml/bacterial/deferribacter_abyssi_medium.yaml`
- `data/normalized_yaml/bacterial/caminibacter_medium.yaml`
- `data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml`
- the JCM/MediaDive transform that expands referenced solutions
- the generated duplicate merge that treats different JCM recipes as source
  duplicates

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.yaml --out /private/tmp/deferribacter_abyssi_medium__f0deb53f.strict.tsv --workers 1 --quiet` | Pass |
| `linkml-reference-validator validate data data/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass |
| `linkml-term-validator validate-data data/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| `just validate-history` | Not checked: the documented validator targets standalone files under `history/`; this generated record stores embedded `curation_history`. |

Term validation emitted only the known `eutils` `pkg_resources` deprecation
warning before `Validation passed`.

## Identity and Grounding

The primary identity is JCM Medium J365, `DEFERRIBACTER ABYSSI MEDIUM`, and the
JCM source page for GRMD 365 supports that name, pH 6.5, and the broad set of
base ingredients. The local identity is nevertheless unsafe because the
generated duplicate merge also folds in JCM Medium J367, `CAMINIBACTER MEDIUM`.
JCM 367 is a derivative of Medium 365, but it is not an identical source:
JCM 367 supplements Medium 365 with 0.2 g/L final yeast extract and 1.0 g/L
NaHCO3, omits sodium acetate, and adds H2-CO2 pressurization. A
`SOURCE_DUPLICATE` relationship erases those J367-specific requirements.

The exact ignored-file search
`rg --no-ignore --hidden -n "J365|GRMD=365|DEFERRIBACTER ABYSSI MEDIUM|deferribacter_abyssi_medium" data/normalized_yaml data/merge_yaml`
covered normalized records, generated merged records, and generated indexes. It
found the MediaDive/JCM 365 normalized owner, the generated merged record, the
TOGO M359 mirror still split as `DEFERRIBACTER_ABYSSI_MEDIUM.yaml`, the
referenced `mediadive_4086_Main_sol_J365.yaml` solution, generated index
entries, and reverse links from `caminibacter_medium.yaml`.

## Evidence

JCM GRMD 365 supports these top-level final recipe rows for
`DEFERRIBACTER ABYSSI MEDIUM`: NH4Cl 0.33 g, KCl 0.33 g, KH2PO4 0.33 g,
CaCl2 x 2H2O 0.33 g, MgCl2 x 6H2O 0.33 g, NaCl 30 g, yeast extract 0.1 g,
sodium acetate 3 g, sulfur 10 g, Trace minerals 10 ml, Trace vitamins 10 ml,
Na2S x 9H2O 0.5 g, and distilled water 1.0 L. It also supports the pH 6.5
preparation sequence for separately sterilizing Ca/Mg salts, sulfur, and a
neutralized 5% Na2S stock under N2.

JCM GRMD 151 supports the Medium 151 trace-minerals stock as a separate 1 L
stock containing 1.5 g nitrilotriacetic acid, 3.0 g MgSO4 x 7H2O, 0.5 g
MnSO4 x nH2O, 1.0 g NaCl, 0.1 g FeSO4 x 7H2O, 0.1 g CoSO4 x 7H2O, 0.1 g
CaCl2 x 2H2O, 0.1 g ZnSO4 x 7H2O, 0.01 g CuSO4 x 5H2O, 0.01 g AlK(SO4)2,
0.01 g H3BO3, 0.01 g Na2MoO4 x 2H2O, and 1.0 L water. JCM GRMD 197 supports
the Medium 197 trace-vitamins stock as a separate 1 L stock containing 2 mg
biotin, 2 mg folic acid, 10 mg pyridoxine HCl, 5 mg thiamine HCl, 5 mg
riboflavin, 5 mg nicotinic acid, 5 mg calcium pantothenate, 0.1 mg vitamin B12,
5 mg p-aminobenzoic acid, 5 mg lipoic acid, and 1.0 L water.

The generated record represents JCM 365 as 30 flat ingredients and therefore
treats both 10 ml stock additions as if their unscaled 1 L stock formulae were
top-level final-medium rows. It carries 1.5 g/L nitrilotriacetic acid and
3.0 g/L MgSO4 x 7H2O in the final medium, but JCM 365 adds only 10 ml of
Medium 151 to 1 L. It similarly carries vitamin stock rows at their 1 L
stock concentrations rather than their final 0.01x contributions.

## Completeness

Consequential gaps:

- The final 1.0 L distilled water row from JCM 365 is missing from the direct
  JCM path.
- JCM 365's referenced 10 ml `Trace minerals` and 10 ml `Trace vitamins` are
  missing as solution ingredients; their inner stock rows are over-expanded into
  the final medium.
- `CaCl2 x 2H2O` and `NaCl` each merge an outer JCM 365 row with an inner trace
  mineral stock row, erasing the stock boundary and yielding unsupported
  0.42352900000000004 g/L and 30.4118 g/L final values.
- The JCM 151 trace-minerals preparation step is copied into the JCM 365 record
  even though it prepares the stock solution, not the final Deferribacter Abyssi
  medium.
- `data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml` still represents the
  TOGO M359 mirror separately and retains raw volume rows as `G_PER_L`.

Empty target-organism slots and missing `growth_data` are non-defects for this
JCM-defined generated medium because the inspected JCM source gives only the
formula, not strain-specific growth measurements.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Blocker | The generated duplicate merge conflates JCM 365 and JCM 367. | JCM 367 is Medium 365 modified with extra final yeast extract, NaHCO3, sodium acetate omission, and H2-CO2 pressurization, while this generated record marks J367 as a `SOURCE_DUPLICATE` synonym of J365. | `data/normalized_yaml/bacterial/caminibacter_medium.yaml`; generated merge logic |
| Major | Referenced 10 ml/L stocks are expanded as unscaled final ingredients. | JCM 365 adds 10 ml of Medium 151 and 10 ml of Medium 197; the generated record carries Medium 151 and 197 stock concentrations as top-level final-medium g/L rows. | JCM/MediaDive reference-expansion transform for `data/normalized_yaml/bacterial/deferribacter_abyssi_medium.yaml` |
| Major | Solution-boundary loss merges distinct outer and stock rows. | The generated `CaCl2 x 2 H2O` value sums 0.323529 with 0.1, and `NaCl` sums 29.4118 with 1.0, even though 0.1 g CaCl2 and 1.0 g NaCl belong inside the Medium 151 trace-minerals stock. | JCM/MediaDive reference-expansion transform and duplicate-ingredient cleanup |
| Major | The direct JCM normalized owner omits the 1 L distilled-water row. | JCM 365 includes 1.0 L distilled water; `deferribacter_abyssi_medium.yaml` and the generated merged record have no water ingredient in the JCM path. | `data/normalized_yaml/bacterial/deferribacter_abyssi_medium.yaml`; importer |
| Major | The TOGO M359 mirror remains a split duplicate with volume-unit errors. | The exhaustive ignored search still found `DEFERRIBACTER_ABYSSI_MEDIUM.yaml`; its normalized TOGO owner carries the JCM 365 1 L water and 10 ml stock additions as `G_PER_L` placeholders. | `data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml`; TOGO import normalization |

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/caminibacter_medium.yaml` from the JCM
  367 source: model it as a derivative of JCM 365 that omits sodium acetate,
  raises final yeast extract by 0.2 g/L, adds 1.0 g/L NaHCO3, and captures the
  8% filter-sterilized NaHCO3 and H2-CO2 4:1 / 100 kPa instructions.
- Repair the JCM/MediaDive reference-expansion path so JCM 365 keeps `Trace
  minerals` and `Trace vitamins` as 10 ml/L solution ingredients or scales their
  children to final concentrations while preserving provenance and stock
  boundaries.
- Restore the JCM 365 1 L distilled-water ingredient in
  `data/normalized_yaml/bacterial/deferribacter_abyssi_medium.yaml`.
- Prevent duplicate-ingredient cleanup from merging outer final-medium rows with
  rows that came from nested stock recipes.
- Reconcile `data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml`
  with the repaired JCM 365 owner and convert its raw JCM volumes to `L_PER_L`
  or `ML_PER_L` instead of `G_PER_L`.
- Regenerate `data/merge_yaml/merged/` after maintained records are repaired and
  verify that JCM 365 and JCM 367 no longer merge as source duplicates.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated
  `deferribacter_abyssi_medium` and `caminibacter_medium` records.
- Search ignored files for `GRMD=365`, `J365`, `GRMD=367`, and `J367` to confirm
  that JCM 365, TOGO M359, and JCM 367 resolve to the intended canonical records
  and relationships.
- Manually compare regenerated solution rows with JCM 365, 151, and 197 to
  confirm that 10 ml stock additions are not represented at 1 L stock
  concentrations.
- Manually compare regenerated Caminibacter rows with JCM 367 to confirm sodium
  acetate omission, extra yeast extract, NaHCO3, and H2-CO2 handling.

## Additional Notes

- The validator suite catches none of these source-level arithmetic and merge
  defects because the flattened ingredients remain schema-conformant.
- The exact absence and deduplication search included ignored and hidden files.
