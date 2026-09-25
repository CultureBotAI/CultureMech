# YAML Record Review: deferribacter_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml
- Started UTC: 2026-09-22T14:17:52Z
- Finished UTC: 2026-09-22T14:17:52Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:008235`, label
`deferribacter_medium`, original name `Deferribacter Medium`, under
`data/merge_yaml/merged/`.

The record is generated from TOGO Medium M1677 / NBRC Medium 882. Future edits
belong in `data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml`
and in the TOGO importer that maps NBRC nested stock solutions into
CultureMech ingredients and solutions.

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml --out /private/tmp/DEFERRIBACTER_MEDIUM.strict.tsv --workers 1 --quiet` | Pass |
| `linkml-reference-validator validate data data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| `just validate-history` | Not checked: the documented validator targets standalone files under `history/`; this generated record stores embedded `curation_history`. |

## Identity and Grounding

The TOGO API and NBRC source page both identify this record as NBRC Medium 882,
`Deferribacter Medium`, represented in TOGO as M1677. The generated
`media_term` matches that identity.

The exact ignored-file search
`rg --no-ignore --hidden -n "M1677|NBRC_M882|NO=882|Deferribacter Medium|deferribacter_medium" data/normalized_yaml data/merge_yaml`
covered normalized records, generated merged records, and generated indexes. It
found the M1677 normalized owner and generated record plus a separate DSMZ
`deferribacter_medium` owner for DSMZ Medium 935. DSMZ 935 is a same-label but
different formulation, so it is not a duplicate of NBRC M882 unless future
source review proves otherwise.

## Evidence

NBRC Medium 882 supports the final base rows: NH4Cl 0.535 g, KH2PO4 0.136 g,
MgCl2 x 6H2O 0.204 g, CaCl2 x 2H2O 0.147 g, Trace elements solution 1 ml,
Vitamin solution 1 ml, sodium acetate 0.82 g, sodium nitrate 0.85 g, NaHCO3
2.52 g, resazurin 1 mg, Na2S x 9H2O 0.5 g, and distilled water 1 L. TOGO M1677
preserves those rows and splits the trace and vitamin stocks into child
subcomponents.

The generated record does not preserve those stock boundaries. It stores the
two 1 ml stock additions as `1 G_PER_L` solutions, keeps every trace and vitamin
stock ingredient as if it were a final-medium ingredient, and merges stock water
with final water so the generated distilled-water value becomes `3.0 G_PER_L`.
The same flattening merges the base 0.147 g/L CaCl2 x 2H2O with 0.1 g/L CaCl2
x 2H2O from the trace stock to produce an unsupported final value of 0.247 g/L.

The TOGO unit conversion also promotes milligram values directly to grams.
NBRC specifies 1 mg resazurin in the final liter, but the generated record has
`1 G_PER_L`. In the vitamin stock, NBRC specifies 2 mg biotin, 1 mg
p-aminobenzoic acid, 5 mg thiamine-HCl, 5 mg Ca-pantothenate, 10 mg
pyridoxine-HCl, 2 mg folic acid, 0.01 mg vitamin B12, 5 mg riboflavin, and
5 mg nicotinic acid; the generated top-level vitamin rows carry those numeric
values as `G_PER_L`.

NBRC also supports preparation requirements that are absent from the generated
record: autoclave ingredients except vitamin solution and Na2S x 9H2O under an
H2/CO2 80/20 atmosphere, autoclave Na2S x 9H2O separately as a 5% solution under
N2, aseptically and anaerobically add filter-sterile vitamin solution and Na2S
solution, and pressurize inoculated bottles to 150 kPa with H2/CO2.

## Completeness

Consequential gaps:

- Final 1 L distilled water is normalized as `G_PER_L`, and generated output
  sums it with the 1 L waters from both stock recipes.
- `Trace elements solution` and `Vitamin solution` should be 1 ml/L additions,
  not `1 G_PER_L`.
- Trace and vitamin stock recipe rows are flattened into final top-level
  `ingredients` instead of retained as stock composition or scaled by 0.001.
- Milligram rows are off by a factor of 1000 even before the missing 1 ml/L
  stock dilution is considered.
- H2, CO2, and N2 gases plus NaOH stock-adjustment solution appear as variable
  top-level ingredients; they belong to gas atmospheres or stock preparation.
- NBRC preparation instructions are absent.

No target organisms or growth rates are supplied by NBRC Medium 882 or TOGO
M1677; their absence is not a defect.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | TOGO nested stock solutions are flattened into the final ingredient list. | NBRC and TOGO add only 1 ml of each stock; generated output contains unscaled trace/vitamin stock rows as final ingredients. | `data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml`; TOGO stock import |
| Major | Several milligram rows are represented as grams. | NBRC has resazurin 1 mg and vitamin-stock rows in mg, but the generated record has raw numeric values such as `1`, `2`, `5`, and `10` in `G_PER_L`. | TOGO unit normalization |
| Major | Solution volume and stock water rows are normalized to impossible mass units. | NBRC uses two 1 ml stock additions and three separate 1 L waters; generated output stores the additions as `G_PER_L` and merges waters to `3.0 G_PER_L`. | TOGO unit normalization; duplicate ingredient cleanup |
| Major | Gas atmosphere and stock pH adjustment reagents leak into final `ingredients`. | NBRC mentions H2/CO2 for autoclaving and bottle pressurization, N2 for the Na2S stock, and NaOH for trace-stock pH adjustment; generated output turns H2, CO2, N2, and NaOH into variable ingredients. | TOGO prose/subcomponent importer |
| Major | NBRC preparation requirements are not represented structurally. | The NBRC page gives H2/CO2 autoclaving, separate Na2S sterilization, filter-sterile vitamin addition, anaerobic addition, and 150 kPa pressurization instructions; the generated record has no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml` |

## Recommended Edits

- Keep the NBRC trace and vitamin stocks as `1 ML_PER_L` solution ingredients or
  scale their children by 0.001 while preserving the stock provenance.
- Convert NBRC `mg` rows to grams before storing any `G_PER_L` values; resazurin
  should be milligram-scale in the final medium, and vitamin-stock rows should
  be milligram-scale inside the stock.
- Preserve 1 L stock-solution water rows inside solution definitions and keep
  final distilled water as `1 L_PER_L` or `1000 ML_PER_L`.
- Move H2/CO2, N2, and NaOH out of top-level final ingredients into structured
  preparation or stock-adjustment data.
- Add preparation steps for the H2/CO2 autoclave atmosphere, separate 5% Na2S
  stock, filter-sterile vitamin addition, anaerobic additions, and 150 kPa
  H2/CO2 pressurization.
- Regenerate `data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml` after the
  maintained TOGO owner is repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated
  M1677 record.
- Search ignored files for `M1677`, `NBRC_M882`, `NO=882`, and
  `DEFERRIBACTER_MEDIUM` to confirm the repaired source has one generated
  NBRC M882 output and has not been merged with DSMZ Medium 935.
- Manually compare the regenerated base formula, solution quantities, vitamin
  mg values, trace-stock rows, and gas/preparation metadata against NBRC Medium
  882 and TOGO M1677.

## Additional Notes

- The exact absence and duplicate search included ignored and hidden files.
- `linkml-reference-validator` reported zero reference checks, so its pass does
  not exercise TOGO, NBRC, or MediaDive source identifiers.
