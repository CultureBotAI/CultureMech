# YAML Record Review: CYS MEDIUM FOR STRAIN SS

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cys_medium_for_strain_ss__6df02450.yaml
- Started UTC: 2026-09-22T12:54:27Z
- Finished UTC: 2026-09-22T12:57:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003067 |
| Name | cys_medium_for_strain_ss |
| Source | JCM Medium 722 |
| Media term | mediadive.medium:J722, JCM Medium J722 |
| Generated record | data/merge_yaml/merged/cys_medium_for_strain_ss__6df02450.yaml |
| Maintained input | data/normalized_yaml/bacterial/cys_medium_for_strain_ss.yaml |

The merged record is a single-source generated copy of the older
MediaDive/JCM import. Future repairs belong in that maintained input or in the
JCM import and solution-migration logic that flattened the trace mineral stock.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cys_medium_for_strain_ss__6df02450.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cys_medium_for_strain_ss__6df02450.yaml --out /private/tmp/cys_medium_for_strain_ss__6df02450.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cys_medium_for_strain_ss__6df02450.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cys_medium_for_strain_ss__6df02450.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The passing validators prove that the generated YAML is schema-valid. They do
not check whether the trace mineral stock is scoped correctly.

## Identity and Grounding

The source identity is correct. `CultureMech:003067` denotes JCM Medium 722,
`CYS MEDIUM FOR STRAIN SS`, and the live JCM page for `GRMD=722` uses the same
title. The local TOGO M745 import independently points at the same JCM source
URL for `CYS Medium For Strain SS`.

A gitignore-independent search with `rg --no-ignore --hidden` over
`data/normalized_yaml`, `data/raw`, and the generated target found one older
JCM-derived normalized record with `mediadive.medium:J722`, one newer
TOGO M745 normalized record for the same JCM source, and no exact raw capture
for `GRMD=722` or `mediadive.medium:J722` under `data/raw`.

Most small-molecule groundings are plausible. The `NiCl2 x 6 H2O` grounding is
again underspecified: it points at `CHEBI:34887` / nickel dichloride, while the
source stock row is nickel chloride hexahydrate.

## Evidence

JCM Medium 722 and TOGO M745 support the same top-level formulation: 3 g
Hy-Case Amino, 2 g Dried yeast extract S, 1 g soluble starch, 3 g NaCl, 10 ml
Trace mineral solution, and 1 L distilled water, adjusted to pH 7.5-7.7 with
1 N NaOH.

The generated bulk rows are internally consistent if they were back-calculated
over a 1.01 L final volume:

| Source component | Source amount | Record amount |
|---|---:|---:|
| Hy-Case Amino | 3 g per 1.01 L | 2.9703 g/L |
| Yeast extract | 2 g per 1.01 L | 1.9802 g/L |
| Starch | 1 g per 1.01 L | 0.990099 g/L |
| NaCl | 3 g per 1.01 L | 2.9703 g/L |
| Trace mineral solution | 10 ml/L | flattened as stock constituents |
| Distilled water, main solution | 1 L | missing |

The trace mineral rows are not back-calculated. JCM 722 defines the trace stock
as FeSO4, MgCl2, Na2MoO4, CoCl2, CaCl2, MnCl2, VOSO4, ZnSO4, NiCl2, and CuSO4
made up to 1 L, then adds 10 ml of that stock to the final medium. The
generated record lists those stock strengths directly under the final medium
as `G_PER_L`.

The pH scalar loses a little source detail. The source range is pH 7.5-7.7; the
record stores `ph_value: 7.6` but retains the full range in free-text
preparation steps.

## Completeness

- The record has no structured `references`, `source_data`,
  `target_organisms`, or `growth_metrics`. Empty target-organism and
  growth-metric slots are acceptable because JCM 722 is a recipe record, not a
  primary growth assay.
- The generated record omits distilled water from both the main medium and the
  Trace mineral solution.
- The generated record has no structured stock-solution edge for the 10 ml/L
  Trace mineral solution addition.
- The source pH is only represented completely in the free-text preparation
  step, not as a structured range.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The 10 ml/L Trace mineral solution was flattened into final-medium top-level metals. | JCM 722 lists the metals under a separate trace stock; the generated record lists the stock strengths directly in the final recipe. | `data/normalized_yaml/bacterial/cys_medium_for_strain_ss.yaml` and JCM solution import logic |
| major | Required distilled-water rows are missing. | JCM 722 lists 1 L distilled water for both the main recipe and Trace mineral solution; neither row is preserved in the generated record. | JCM import and solution-migration logic |
| minor | Structured pH loses the source range. | JCM states pH 7.5-7.7; the generated record stores midpoint `ph_value: 7.6`, with the range only in free text. | `data/normalized_yaml/bacterial/cys_medium_for_strain_ss.yaml` |
| minor | Nickel chloride hexahydrate is grounded to an anhydrous nickel chloride label. | The trace stock uses `NiCl2 x 6 H2O`, while the record's ChEBI label is `nickel dichloride`. | Ingredient grounding for JCM 722 imports |
| minor | The source URL is only in `notes`. | The JCM 722 link exists in free text, but there is no structured `references` entry for reference validation. | `data/normalized_yaml/bacterial/cys_medium_for_strain_ss.yaml` |

## Recommended Edits

1. Rework the maintained JCM 722 import so `Trace mineral solution` remains a
   separate 1 L stock that is added to the final medium at 10 ml/L.
2. Restore the 1 L distilled-water row in the main medium and in the trace
   stock.
3. Replace scalar `ph_value: 7.6` with `ph_range: {min: 7.5, max: 7.7}` while
   preserving the 1 N NaOH pH-adjustment instruction.
4. Review the `NiCl2 x 6 H2O` ChEBI grounding and prefer a hexahydrate-specific
   term if available.
5. Add structured `references` for JCM Medium 722 and regenerate
   `data/merge_yaml/merged/cys_medium_for_strain_ss__6df02450.yaml`.

## Follow-up Checks

- Re-run open-schema, closed-schema, reference, and term validation on the
  repaired normalized input and regenerated merged record.
- Diff the repaired record against JCM Medium 722 and TOGO Medium M745 to
  verify the top-level bulk amounts, the 10 ml/L trace stock boundary, and the
  pH range.
- Verify that the regenerated trace metals are not represented as final
  `G_PER_L` values unless they were intentionally back-calculated from the
  10 ml/L stock addition.
- Re-run `rg --no-ignore --hidden` for `GRMD=722` and `mediadive.medium:J722`
  across `data/normalized_yaml` and `data/raw` to ensure no stale flattened
  copy remains.

## Additional Notes

- `data/normalized_yaml/bacterial/TOGO_M745_CYS_Medium_For_Strain_SS.yaml`
  preserves the source top-level 3 g, 2 g, 1 g, and 3 g bulk rows, but it also
  imports the trace stock metals as top-level rows and stubs the stock addition
  as an empty `Unknown solution`.
- `VOSO4 x n H2O` is appropriately grounded to a hydrate-level vanadyl sulfate
  term.
