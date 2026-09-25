# YAML Record Review: CYCLONATRUM PROTEILYTICUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyclonatrum_proteilyticum_medium__218fb205.yaml
- Started UTC: 2026-09-22T12:50:51Z
- Finished UTC: 2026-09-22T12:54:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002334 |
| Name | cyclonatrum_proteilyticum_medium |
| Source | JCM Medium 1161 |
| Media term | mediadive.medium:J1161, JCM Medium J1161 |
| Generated record | data/merge_yaml/merged/cyclonatrum_proteilyticum_medium__218fb205.yaml |
| Maintained input | data/normalized_yaml/bacterial/cyclonatrum_proteilyticum_medium.yaml |

The merged record is a single-source generated copy of the normalized
MediaDive/JCM import. Future repairs belong in the maintained input or in the
JCM import and solution-migration logic that failed to preserve the source
solution additions.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyclonatrum_proteilyticum_medium__218fb205.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyclonatrum_proteilyticum_medium__218fb205.yaml --out /private/tmp/cyclonatrum_proteilyticum_medium__218fb205.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyclonatrum_proteilyticum_medium__218fb205.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyclonatrum_proteilyticum_medium__218fb205.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The passing schema validators do not check unit arithmetic or stock-solution
boundaries against JCM Medium 1161.

## Identity and Grounding

The source identity is correct. `CultureMech:002334` denotes JCM Medium 1161,
`CYCLONATRUM PROTEILYTICUM MEDIUM`, and the live JCM page for `GRMD=1161`
uses that title. The local TOGO M1243 import independently points at the same
JCM source URL for `Cyclonatrum Proteilyticum Medium`.

A gitignore-independent search with `rg --no-ignore --hidden` over
`data/normalized_yaml`, `data/raw`, and the generated target found one older
JCM-derived normalized record with `mediadive.medium:J1161`, one newer
TOGO M1243 normalized record for the same JCM source, and no exact raw capture
for `GRMD=1161` or `mediadive.medium:J1161` under `data/raw`.

One grounding should be reviewed: the `NiCl2 x 6 H2O` row is grounded to
`CHEBI:34887` with label `nickel dichloride`, but the referenced JCM 1079 trace
element stock uses the hexahydrate.

## Evidence

JCM Medium 1161 supports this final base formulation before post-autoclave
supplements:

| Source component | Source amount | Record amount |
|---|---:|---:|
| Na2CO3 | 35 g/L | 1750 g/L |
| NaHCO3 | 25 g/L | 1250 g/L |
| K2HPO4 | 1 g/L | 50 g/L |
| Distilled water | to 1 L | missing |
| pH | 9.5 | 9.5 |

After autoclaving and cooling, the source adds 1 ml/L of 1 M MgCl2 solution,
1 ml/L of the JCM 1079 trace element solution, 1 ml/L of the JCM 197 trace
vitamins stock, 15 ml/L of 10% Tryptone solution, and 2 ml/L of 1% Yeast
extract solution. The generated record records `MgCl2` as 1 g/L, `Tryptone` as
15 g/L, and `Yeast extract` as 2 g/L, so it preserves the raw addition volumes
as if they were final grams per liter.

The referenced stock solutions are also flattened. The generated EDTA, FeSO4,
ZnSO4, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, and Na2MoO4 rows match the stock
strengths listed for the trace element solution in JCM 1079, not final
concentrations after a 1 ml/L addition. The generated biotin, folic acid,
pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium
pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid rows likewise
match the stock strengths in the trace vitamins table of JCM 197, not final
concentrations after a 1 ml/L addition.

## Completeness

- The record has no structured `references`, `source_data`,
  `target_organisms`, or `growth_metrics`. Empty target-organism and
  growth-metric slots are acceptable because JCM 1161 is a recipe record, not a
  primary growth assay.
- The generated record omits distilled water from the base medium and omits the
  trace-element and trace-vitamin stock water rows.
- The generated preparation sequence loses the post-autoclave addition
  boundaries and flattens the JCM 1079 pH-3.6 trace-element adjustment into the
  JCM 1161 final medium.
- The `high_metal: true` flag appears to be an artifact of raw stock
  concentrations being flattened into final-medium rows.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Direct final-medium salts are inflated. | JCM 1161 lists 35 g Na2CO3, 25 g NaHCO3, and 1 g K2HPO4 per liter; the record stores 1750, 1250, and 50 g/L. | `data/normalized_yaml/bacterial/cyclonatrum_proteilyticum_medium.yaml` and the JCM import |
| major | Post-autoclave stock additions were recorded as final grams per liter. | JCM 1161 adds 1 ml MgCl2 stock, 15 ml 10% Tryptone, and 2 ml 1% Yeast extract per liter; the record stores those raw volume numbers as `G_PER_L`. | JCM import and solution-migration logic |
| major | JCM 1079 and JCM 197 stock recipes were flattened into the JCM 1161 top-level ingredient list. | JCM 1161 references 1 ml/L trace element and trace vitamin stocks; the record lists the referenced stock ingredients directly at their stock concentrations. | JCM cross-reference import and solution-migration logic |
| major | Required water rows and source stock boundaries are missing. | The base, trace element, and trace vitamin recipes all have their own water or final-volume context; the generated record omits those rows and scopes. | `data/normalized_yaml/bacterial/cyclonatrum_proteilyticum_medium.yaml` |
| minor | Nickel chloride hexahydrate is grounded to an anhydrous nickel chloride label. | The referenced trace element stock uses `NiCl2 x 6 H2O`, while the record's ChEBI label is `nickel dichloride`. | Ingredient grounding for JCM 1161 imports |
| minor | The source URL is only in `notes`. | The JCM 1161 link exists in free text, but there is no structured `references` entry for reference validation. | `data/normalized_yaml/bacterial/cyclonatrum_proteilyticum_medium.yaml` |

## Recommended Edits

1. Re-import or repair JCM 1161 so direct salts are 35 g/L Na2CO3, 25 g/L
   NaHCO3, 1 g/L K2HPO4, and distilled water to 1 L at pH 9.5.
2. Preserve the 1 ml/L 1 M MgCl2, 15 ml/L 10% Tryptone, and 2 ml/L 1% Yeast
   extract additions as stock-solution additions, or dimensionally compute
   their final concentrations from the source strengths.
3. Link the JCM 1079 trace element solution and JCM 197 trace vitamin solution
   as nested 1 ml/L additions rather than flattening their stock ingredients
   into final JCM 1161 rows.
4. Drop the spurious `high_metal: true` flag after the trace stock is no longer
   represented as final metal concentrations.
5. Review the `NiCl2 x 6 H2O` grounding and prefer a hexahydrate-specific term
   if one is available.
6. Add structured references for JCM 1161 and the two referenced JCM stock
   recipes before regenerating the merged record.

## Follow-up Checks

- Re-run open-schema, closed-schema, reference, and term validation on the
  repaired normalized input and regenerated merged record.
- Diff the repaired record against JCM Medium 1161, JCM Medium 1079's trace
  element solution, and JCM Medium 197's trace vitamin solution.
- Compare the repaired older JCM-derived record with
  `data/normalized_yaml/bacterial/TOGO_M1243_Cyclonatrum_Proteilyticum_Medium.yaml`
  to verify that they now agree on the direct salts and solution additions.
- Re-run `rg --no-ignore --hidden` for `GRMD=1161` and
  `mediadive.medium:J1161` across `data/normalized_yaml` and `data/raw` to
  confirm that no stale inflated copy remains.

## Additional Notes

- The newer TOGO M1243 normalized input already has the direct Na2CO3,
  NaHCO3, and K2HPO4 rows at the correct amounts, but it still represents the
  referenced solution additions as empty `Unknown solution` stubs.
- The base-medium HCl adjustment is variable and does not need a final
  concentration.
