# YAML Record Review: modified_thiocapsa_medium__88856503
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_thiocapsa_medium__88856503.yaml
- Started UTC: 2026-09-24T13:37:30Z
- Finished UTC: 2026-09-24T13:38:20Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_thiocapsa_medium`, CultureMech ID `CultureMech:003044`.

- Reviewed generated record: `data/merge_yaml/merged/modified_thiocapsa_medium__88856503.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/modified_thiocapsa_medium.yaml`
- Media term: `mediadive.medium:J699`, `MODIFIED THIOCAPSA MEDIUM`
- Source note: `JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=699`
- Merge fingerprint: `88856503ff6981b55e6ce23803314908c5f485a2c6cbebee947918184f925c17`
- `merged_from`: `modified_thiocapsa_medium`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The medium identity matches live JCM/MediaDive `J699`.

Most direct salts, trace salts, and vitamins have plausible CHEBI grounding. `NiCl2 x 6 H2O` is still grounded to generic `CHEBI:34887` nickel dichloride, which loses the hexahydrate state.

The main issue is not ontology identity but scope: `NaHCO3`, the modified trace elements, and the seven vitamins are recorded as if their stock concentrations were final ingredient concentrations.

## Evidence
Live JCM `GRMD=699` and MediaDive `J699` agree on this structure:

- `Main sol. J699`, 952 ml, with direct NaCl, MgCl2 x 6 H2O, KH2PO4, KCl, NH4Cl, CaCl2 x 2 H2O, Na2SO4, NaNO2, 1 ml Modified trace element solution SL-12, 1 ml Seven vitamins solution, and 950 ml distilled water.
- `NaHCO3 buffer`, 50 ml, with 2.5 g NaHCO3.
- `Modified trace element solution SL-12`, 1 L stock.
- `Seven vitamins solution`, 200 ml stock.
- pH adjustment instruction: add NaHCO3 buffer and adjust pH to 7.2 - 7.4 if necessary.

## Completeness
The generated YAML keeps the direct Main sol. J699 salts and pH handling note. It has no `solutions` array, so it loses all three named stocks and the volume relationships that make the formula executable.

`NaHCO3` is present at the 50 g/L buffer concentration, even though the buffer is a 50 ml addition. Modified SL-12 trace compounds are present at 1 L stock concentrations, even though only 1 ml stock is used. Seven vitamins are present at 200 ml stock concentrations, even though only 1 ml stock is used.

## Findings
1. Needs curation - the 50 ml NaHCO3 buffer was flattened at stock strength. The source buffer contains 2.5 g NaHCO3 in 50 ml water; the generated final ingredient says `NaHCO3` `50 G_PER_L`.

2. Needs curation - Modified trace element solution SL-12 was flattened at stock strength. H3BO3, FeSO4 x 7 H2O, CoCl2 x 6 H2O, MnCl2 x 4 H2O, ZnCl2, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and CuCl2 x 2 H2O are all stock rows for a 1 ml/L addition.

3. Needs curation - Seven vitamins solution was flattened at stock strength. The source adds 1 ml of a 200 ml vitamin stock; Vitamin B12, p-aminobenzoic acid, D-(+)-biotin, nicotinic acid, calcium pantothenate, pyridoxine hydrochloride, and thiamine-HCl x 2 H2O should not be emitted as final g/L rows at stock strength.

4. Needs curation - the record has no named `NaHCO3 buffer`, `Modified trace element solution SL-12`, or `Seven vitamins solution` structures.

5. Minor - the source pH is a range, 7.2 - 7.4, while the generated scalar `ph_value` is the midpoint 7.3.

6. Minor - `NiCl2 x 6 H2O` should be reviewed for a hydrate-specific CHEBI term.

## Recommended Edits
- Recurate `data/normalized_yaml/bacterial/modified_thiocapsa_medium.yaml` from JCM/MediaDive `J699` with the 952 ml main solution and all three named stocks.
- Preserve NaHCO3 as a 50 ml buffer addition, not as a 50 g/L final ingredient.
- Preserve the 1 ml/L Modified SL-12 and 1 ml/L Seven vitamins additions as solution references, or apply those dilution factors if a flattened final list is also emitted.
- Represent the 7.2 - 7.4 pH range without silently collapsing it to 7.3.
- Revisit `NiCl2 x 6 H2O` grounding during the repair.

## Follow-up Checks
- Re-fetch MediaDive `J699` and confirm that the repaired YAML contains `Main sol. J699`, `NaHCO3 buffer`, `Modified trace element solution SL-12`, and `Seven vitamins solution`.
- Confirm that no stock-only trace or vitamin concentration is emitted as a final concentration.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
None found.
