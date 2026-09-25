# YAML Record Review: deferribacter_desulfuricans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/deferribacter_desulfuricans_medium__99f27aac.yaml
- Started UTC: 2026-09-22T14:13:39Z
- Finished UTC: 2026-09-22T14:13:39Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009171`, label
`deferribacter_desulfuricans_medium`, original name
`Deferribacter Desulfuricans Medium`, under `data/merge_yaml/merged/`.

The record is generated from TOGO Medium M2602 / DSMZ Medium 935b. Future edits
belong in maintained TOGO and DSMZ owners plus the import and merge transforms:

- `data/normalized_yaml/bacterial/TOGO_M2602_Deferribacter_Desulfuricans_Medium.yaml`
- `data/normalized_yaml/bacterial/deferribacter_desulfuricans_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_935_DEFERRIBACTER_medium.yaml`
- `data/normalized_yaml/bacterial/medium_935_modified_for_dsm_14783.yaml`
- `data/normalized_yaml/bacterial/for_dsm_14813.yaml`

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/deferribacter_desulfuricans_medium__99f27aac.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/deferribacter_desulfuricans_medium__99f27aac.yaml --out /private/tmp/deferribacter_desulfuricans_medium__99f27aac.strict.tsv --workers 1 --quiet` | Pass |
| `linkml-reference-validator validate data data/merge_yaml/merged/deferribacter_desulfuricans_medium__99f27aac.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/deferribacter_desulfuricans_medium__99f27aac.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| `just validate-history` | Not checked: the documented validator targets standalone files under `history/`; this generated record stores embedded `curation_history`. |

Term validation emitted only the known `eutils` `pkg_resources` deprecation
warning before `Validation passed`.

## Identity and Grounding

The generated ID and label point at TOGO M2602, and the TOGO API confirms that
M2602 is named `Deferribacter Desulfuricans Medium`, points at DSMZ Medium 935b,
and records pH 7.0. The identity is a real medium, but its maintained TOGO owner
does not carry pH into `ph_value`; the generated record therefore omits a
source-supported pH 7.0 even though DSMZ 935b says the complete medium should be
pH 7.0.

The exact ignored-file search
`rg --no-ignore --hidden -n "M2602|DSMZ_Medium935b|Deferribacter Desulfuricans Medium|deferribacter_desulfuricans_medium|medium 935" data/normalized_yaml data/merge_yaml`
covered normalized records, generated merged records, and generated indexes. It
found the TOGO M2602 owner and this generated record, but also found a separate
DSMZ-imported `DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml` generated cluster with
same-name normalized owners. Those records must be reconciled with M2602 and
DSMZ 935b instead of left as independent same-name generated recipes.

## Evidence

DSMZ Medium 935b supports the final base recipe as NH4Cl 0.33 g, KCl 0.33 g,
CaCl2 x 2H2O 0.33 g, MgCl2 x 6H2O 0.33 g, KH2PO4 0.33 g, NaCl 25.00 g,
Modified Wolin's mineral solution 10.00 ml, KNO3 0.50 g, Na-acetate 2.00 g,
yeast extract 0.15 g, NaHCO3 0.30 g, Wolin's vitamin solution 10.00 ml, and
distilled water 1000.00 ml.

The TOGO API preserves the DSMZ base rows and separates the two stock solution
subcomponents. Modified Wolin's mineral solution is a stock recipe, not a set of
final top-level ingredients; likewise, Wolin's vitamin solution is a stock in
which biotin and folic acid are 2 mg per 1 L, pyridoxine hydrochloride is 10 mg
per 1 L, most other vitamins are 5 mg per 1 L, and vitamin B12 is 0.1 mg per
1 L.

The TOGO owner and this generated record flatten those stock rows into the final
ingredient list. The generated record has 1.5 g/L nitrilotriacetic acid and
3 g/L MgSO4 x 7H2O as final ingredients even though DSMZ 935b adds only 10 ml
of Modified Wolin's mineral solution. It also represents vitamin stock rows at
milligram numeric values in `G_PER_L`; for example, biotin is `2 G_PER_L` and
pyridoxine hydrochloride is `10 G_PER_L`, whereas the source rows are 2 mg/L and
10 mg/L inside a stock that is then added at 10 ml/L.

DSMZ also supports anoxic preparation text that is not represented structurally:
dissolve all ingredients except bicarbonate and vitamins, sparge with 100% N2
for 30-45 min, dispense under the same atmosphere into anoxic Hungate-type tubes
or serum vials and autoclave, add filter-sterilized vitamins from an anoxic
100% N2 stock, and add bicarbonate from a sterile anoxic stock prepared under an
80% N2 / 20% CO2 atmosphere.

## Completeness

Consequential gaps:

- The source-supported pH 7.0 is missing.
- DSMZ's anoxic sparging, dispensing, autoclaving, vitamin-filtration, and
  bicarbonate-stock instructions are missing from `preparation_steps`.
- `Modified Wolin's mineral solution` and `Wolin's vitamin solution` are present
  as solutions, but both 10 ml quantities are stored as `G_PER_L` instead of
  `ML_PER_L`.
- The stock rows are also duplicated as top-level final-medium ingredients.
- Stock-solution water rows are merged with final-medium water, yielding
  `3000.0 G_PER_L` distilled water in generated output.
- Outer NaCl and CaCl2 rows are merged with stock-solution NaCl and CaCl2 rows,
  yielding unsupported 26.0 g/L NaCl and 0.43000000000000005 g/L CaCl2 x 2H2O.
- A variable `N2` ingredient is created from gas-handling prose; nitrogen is an
  atmosphere/preparation condition here, not a medium ingredient.
- The separate same-name DSMZ generated cluster needs source reconciliation.

No target-organism or `growth_data` rows are required by DSMZ 935b or TOGO
M2602; leaving those optional sections absent is fine.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | Stock solution children are flattened into the final medium at unscaled concentrations. | DSMZ 935b adds only 10 ml of each Wolin stock, but the generated record promotes mineral and vitamin stock rows into final `ingredients`. | TOGO import and solution-migration paths for `TOGO_M2602_Deferribacter_Desulfuricans_Medium.yaml` |
| Major | Several mg stock rows are represented as g/L. | The source Wolin vitamin rows are mg per 1 L stock; the generated record has biotin `2 G_PER_L`, pyridoxine hydrochloride `10 G_PER_L`, and other vitamins at gram-scale values. | TOGO unit normalization for subcomponent rows |
| Major | Solution volume and water rows use mass units. | DSMZ 935b and TOGO M2602 use 10 ml stock additions plus 1000 ml final water; the generated record has stock additions as `10 G_PER_L` and distilled water as `3000.0 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M2602_Deferribacter_Desulfuricans_Medium.yaml`; merge recipe generation |
| Major | Source-supported pH and anaerobic preparation are missing. | DSMZ 935b and TOGO M2602 both support pH 7.0 plus N2 sparging and separate anoxic vitamin/bicarbonate addition. | `TOGO_M2602_Deferribacter_Desulfuricans_Medium.yaml`; TOGO comment importer |
| Major | Source-duplicate reconciliation is incomplete. | The ignored-file search found a separate DSMZ-imported same-name `DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml` cluster that points at the same DSMZ Medium 935b PDF. | direct DSMZ/MediaDive/KOMODO normalized owners and generated merge logic |

## Recommended Edits

- Keep Modified Wolin's mineral solution and Wolin's vitamin solution as
  `10 ML_PER_L` solution ingredients in
  `TOGO_M2602_Deferribacter_Desulfuricans_Medium.yaml`, or scale their child
  rows into the final recipe while preserving solution provenance.
- Correct TOGO subcomponent mg handling so Wolin's vitamin and trace rows are
  converted from mg/L to g/L before any final-medium scaling.
- Convert final distilled water to `1000 ML_PER_L` or `1 L_PER_L`; do not merge
  1 L stock-solution waters into the final medium.
- Restore pH 7.0 and structured preparation steps for N2 sparging, anoxic
  dispensing, filter-sterilized vitamin addition, and bicarbonate addition under
  80% N2 / 20% CO2.
- Represent N2 and N2/CO2 as atmospheres in preparation metadata, not as
  `ingredients`.
- Reconcile the direct DSMZ/MediaDive and KOMODO Medium 935 records with TOGO
  M2602 before regenerating generated merged YAML.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated M2602
  and DSMZ 935 records.
- Search ignored files for `M2602`, `DSMZ_Medium935b`, and
  `deferribacter_desulfuricans_medium` to verify the duplicate set is resolved.
- Manually compare the regenerated base formula and Wolin stock handling against
  DSMZ Medium 935b and the TOGO M2602 API.
- Manually confirm no standalone `N2` or `CO2` gas ingredient remains in the
  final ingredient list for this medium.

## Additional Notes

- The exact absence and duplicate search included ignored and hidden files.
- `linkml-reference-validator` reported zero reference checks, so its pass does
  not exercise TOGO, DSMZ, or MediaDive source identifiers.
