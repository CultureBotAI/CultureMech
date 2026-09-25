# YAML Record Review: CHLOROFLEXUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chloroflexus_medium__e1e4e80e.yaml
- Started UTC: 2026-09-22T07:13:30Z
- Finished UTC: 2026-09-22T07:15:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:002354 |
| Label | CHLOROFLEXUS MEDIUM |
| Generated record | data/merge_yaml/merged/chloroflexus_medium__e1e4e80e.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chloroflexus_medium.yaml |
| Source | MediaDive/JCM medium J1183, JCM GRMD 1183 |

The reviewed file is a generated merge product from one normalized MediaDive
import record. Future fixes belong in
`data/normalized_yaml/bacterial/chloroflexus_medium.yaml`, its companion
imported solution inputs, or the MediaDive/JCM import logic rather than in
`data/merge_yaml/merged/chloroflexus_medium__e1e4e80e.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chloroflexus_medium__e1e4e80e.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The record identity is internally coherent: `CultureMech:002354`,
`CHLOROFLEXUS MEDIUM`, `mediadive.medium:J1183`, and JCM GRMD 1183 all point to
the same JCM Chloroflexus formulation. No wrong-identity or wrong-source issue
was found.

An ignored-independent search with `rg --no-ignore --hidden` across
`data/normalized_yaml` and `data/merge_yaml/merged` for exact record, source,
fingerprint, and JCM identifiers found this generated record, its normalized
owner, the companion `mediadive_5295_Main_sol_J1183.yaml` solution input, and a
previously reviewed TOGO-derived `CHLOROFLEXUS_MEDIUM.yaml` record that also
cites JCM GRMD 1183 but is outside this merge fingerprint.

## Evidence

The JCM 1183 source supports the top-level salts and nutrients that the record
imports directly into the medium: `KH2PO4`, `NH4Cl`, `MgCl2 x 6H2O`, `KCl`,
`NaCl`, `Na2S2O3 x 5H2O`, BD-Difco yeast extract, HEPES, and distilled water.
It also supports a final pH of 7.5.

The record over-flattens several source subsolutions. JCM 1183 adds trace
vitamins solution at 1 mL/L and trace elements solution at 1 mL/L, with the
trace elements delegated to JCM Medium 310. Rows such as biotin, folic acid,
pyridoxine-HCl, vitamin B12, EDTA, FeSO4, and ZnSO4 therefore denote stock
solution members at stock strength, not direct per-liter medium additions. The
JCM trace vitamins quantities are consistent with 100 mL of stock, for example
2 mg biotin is 0.02 g/L stock and 0.5 mg vitamin B12 is 0.005 g/L stock; those
values should be nested under a trace vitamins solution and added to the medium
at 1 mL.

The record omits three post-autoclave additions that JCM 1183 places in the
top-level protocol: 1 mL of 5% `Na2S x 9H2O`, 1 mL of 5% `CaCl2 x 2H2O`, and
10 mL of 3% `NaHCO3`. Those are preserved in the normalized companion solution
preparation note but are absent as structured ingredients or nested stock
solutions.

`preparation_steps[1]`, `Adjust pH to 3 with HCl.`, is unsupported as a
top-level JCM 1183 medium instruction. It is consistent with a trace-element
stock preparation instruction that was flattened into the parent protocol.

## Completeness

The record should represent the trace vitamin, trace element, sulfide,
calcium-chloride, and bicarbonate stocks as structured solutions before it can
be treated as a complete JCM 1183 formulation. Its current direct-ingredient
rows are sufficient to expose many of the chemicals, but not the source's
mixing hierarchy or the final medium concentrations.

The empty `target_organisms` and growth-observation fields are not defects for
this imported source record.

## Findings

| Severity | Finding |
| --- | --- |
| Major | Trace vitamins and trace elements are flattened into the parent medium at stock strength. **Owner:** `data/normalized_yaml/bacterial/chloroflexus_medium.yaml`, the JCM import of stock solutions, or both. |
| Major | 5% `Na2S x 9H2O`, 5% `CaCl2 x 2H2O`, and 3% `NaHCO3` post-autoclave stocks are omitted from structured ingredients and solutions. **Owner:** `data/normalized_yaml/bacterial/chloroflexus_medium.yaml`, `data/normalized_yaml/bacterial/mediadive_5295_Main_sol_J1183.yaml`, or the import logic that links the companion solution. |
| Major | `Adjust pH to 3 with HCl.` appears in the top-level preparation despite not being a JCM 1183 parent-medium step. **Owner:** the JCM import logic that flattens cross-referenced stock preparation. |

## Recommended Edits

1. In the maintained normalized MediaDive/JCM inputs or importer, model
   `Trace vitamins solution` as a nested solution added at 1 mL/L with its
   JCM 1183 100 mL stock recipe.
2. In the maintained normalized MediaDive/JCM inputs or importer, model
   `Trace elements solution` as a nested JCM Medium 310 solution added at
   1 mL/L rather than flattening EDTA, ferrous sulfate, zinc sulfate, and the
   other trace element rows into the parent recipe.
3. Promote the post-autoclave 5% `Na2S x 9H2O`, 5% `CaCl2 x 2H2O`, and 3%
   `NaHCO3` additions from free text into structured nested stock solutions
   with the source-supported 1 mL, 1 mL, and 10 mL additions.
4. Keep the trace-element stock pH-3 hydrochloric acid adjustment attached only
   to the trace-element solution preparation, not to the JCM 1183 parent
   medium.
5. After changing the importer or normalized owners, regenerate the merged YAML
   and compare the result with the already reviewed TOGO M1268
   `CHLOROFLEXUS_MEDIUM.yaml`, which cites the same JCM 1183 source but is a
   separate generated record because of divergent importer artifacts.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually confirm the regenerated record against JCM GRMD 1183 and JCM
Medium 310:

1. The parent JCM 1183 medium contains only the direct salts, yeast extract,
   HEPES, trace-vitamin stock, trace-element stock, and water from GRMD 1183.
2. The three post-autoclave stock additions are represented structurally at the
   source volumes and percent concentrations.
3. The pH-3 HCl instruction is scoped only to the trace-element stock.

## Additional Notes

None found.
