# YAML Record Review: TOGO M1369 0.01% LB Seawater Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/0_01_lb_seawater_medium__c6dadec3.yaml`
- Started UTC: 2026-09-21T04:18:25Z
- Finished UTC: 2026-09-21T04:18:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/0_01_lb_seawater_medium__c6dadec3.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007907` |
| Name | `0_01_lb_seawater_medium` |
| Label | `0.01% LB Seawater Medium` |
| Source | TOGO Medium M1369, originally JCM Medium 1273 |
| Generated? | Yes; single-source merge from `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml` |

The record is generated from one normalized TOGO import. The generated record
retains the same scientific issues as the normalized file, so future fixes
belong in `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml`
or the TOGO import transform, then `data/merge_yaml/merged/` must be
regenerated.

## Validation

| Check | Result |
|---|---|
| Documented `just validate-*` validators | Not rerun for this second report: in the same checkout, the documented project `uv` path fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13. |
| No-project LinkML schema fallback | Passed: `linkml-validate` exited 0. |
| No-project strict-schema fallback | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| No-project reference fallback | Passed: 1 file validated, 0 reference checks, all validations passed. |
| No-project term fallback | Passed: `linkml-term-validator` reported `Validation passed`. |
| History validation | Not checked: this review did not create a `history/*.yaml` record. |

## Identity and Grounding

The source identity is correct. The record claims TOGO `M1369`,
`0.01% LB Seawater Medium`; the live TOGO response for `M1369` reports the same
name, links to JCM `GRMD=1273`, and carries pH 8.0. The JCM page for 1273 is
the same `0.01% LB SEAWATER MEDIUM` recipe.

Supported rows:

| Ingredient | Generated value | TOGO/JCM value | Review |
|---|---:|---:|---|
| `Tris(hydroxymethyl)aminomethane` | 1 g/L | 1 g/L | Supported |
| `HCl` | variable | pH-adjustment reagent | Supported as a preparation reagent, not as a solvating medium |

Every mg, ug, and liter source row was imported as `G_PER_L`, and the source
`LB Broth, Lennox (BD-Difco)` row was replaced by unsupported LB Miller
constituents.

## Evidence

The inspected sources were:

- live TOGO `gmdb_medium_by_gmid?gm_id=M1369` response;
- live JCM `GRMD=1273` HTML.

TOGO M1369 and JCM 1273 agree on the source formula:

| Source ingredient | Source amount | Generated representation |
|---|---:|---|
| `K2HPO4` | 5 mg | 5 g/L |
| `Biotin` | 1 ug | 1 g/L |
| `Thiamine-HCl` | 100 ug | 100 g/L |
| `Vitamin B12` | 1 ug | 1 g/L |
| `NaNO3` | 120 mg | 120 g/L |
| `Seawater` | 1 L | 1 g/L |
| `Tris(hydroxymethyl)aminomethane` | 1 g | 1 g/L |
| `Fe(III)-EDTA` | 259 ug | 259 g/L |
| `LB Broth, Lennox (BD-Difco)` | 0.1 g | Missing; replaced by full-strength LB Miller constituents |
| `Mn(II)-EDTA` | 332 ug | 332 g/L |
| `HCl` | variable pH adjuster | variable `HCl` ingredient |

The TOGO and JCM preparation text says to mix components, adjust pH to 8.0 with
HCl, and autoclave; it also says artificial seawater such as JCM medium 1118 can
replace natural seawater. The generated record carries `HCl` as a top-level
variable ingredient but lost both preparation comments.

## Completeness

The record retains the correct source medium and enough imported rows to see the
intended formula, but the usable formulation is incomplete:

- all source mg and ug rows use incorrect gram-per-liter units;
- 1 L seawater is represented as `1 G_PER_L`;
- the sole LB source ingredient is missing and was replaced with unsupported
  tryptone, yeast-extract, and sodium-chloride rows;
- the pH 8.0 HCl/autoclave instruction and artificial-seawater substitution note
  are absent from `preparation_steps`;
- `high_metal: true` appears to be derived from the inflated metal rows.

No target-organism or growth-evidence claims are present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | TOGO mg and ug quantities were imported as grams per liter. `K2HPO4` is 1000x too high, `NaNO3` is 1000x too high, and the vitamin/metal rows are 1,000,000x too high. | TOGO M1369 and JCM 1273 list K2HPO4 5 mg, NaNO3 120 mg, vitamin B12 1 ug, biotin 1 ug, thiamine HCl 100 ug, Fe(III)-EDTA 259 ug, and Mn(II)-EDTA 332 ug. | `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml` or TOGO unit conversion |
| Major | 1 L seawater was converted to `1 G_PER_L`. | TOGO and JCM list seawater as 1 L. | `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml` or TOGO volume conversion |
| Major | The 0.1 g/L `LB Broth, Lennox (BD-Difco)` source row is missing and has been replaced with unsupported full-strength LB Miller constituents. | TOGO M1369 and JCM 1273 have one `LB Broth, Lennox (BD-Difco)` row and do not decompose it into tryptone, yeast extract, and sodium chloride. | `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml` LB commercial-product enrichment |
| Major | Preparation is absent. | TOGO M1369 and JCM 1273 both state pH adjustment to 8.0 with HCl, autoclaving, and the artificial-seawater substitution note. | `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml` |
| Minor | `HCl` is mischaracterized with `Role: Solvating media`; it is only the pH-adjustment reagent in this recipe. | The source mentions HCl solely in `adjust pH to 8.0 with HCl`. | `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml` |
| Minor | The generic LB Miller supplier/catalog notes are not supported by this source. | JCM/TOGO specify `LB Broth, Lennox (BD-Difco)`. | `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M1369_0.01_LB_Seawater_Medium.yaml`,
   preserve TOGO's original units or convert them correctly to final
   concentrations.
2. Restore `LB Broth, Lennox (BD-Difco)` at 0.1 g/L and remove the unsupported
   full-strength LB Miller decomposition.
3. Represent seawater as a liter-volume final solvent, not `G_PER_L`.
4. Add the pH 8.0 HCl/autoclave step and the JCM 1118 artificial-seawater
   substitution note as preparation steps or a preparation note.
5. Keep HCl only as a pH-adjustment reagent, and correct or remove its solvating
   media role note.
6. Remove the generic `laboratorynotes.com` LB Miller note block.
7. Recompute or drop `high_metal` after fixing Fe/Mn microgram amounts.
8. Regenerate the merged corpus and indexes.

## Follow-up Checks

- Validate the normalized record with schema, strict, term, and reference
  checks after the authoritative edit.
- Compare the regenerated merged record against TOGO M1369 and JCM 1273 row by
  row, with special attention to mg/ug/L conversions.
- Run `just merge-recipes`, `just verify-merges`, and
  `just audit-merge-freshness`.

## Additional Notes

This generated TOGO record is not a duplicate of
`data/merge_yaml/merged/0_01_lb_seawater_medium.yaml` at the current fingerprint
level because the MediaDive and TOGO importers made different unit mistakes.
Both normalized source records will need parallel corrections or importer-level
repairs if they are meant to converge into one canonical 0.01% LB seawater
recipe.
