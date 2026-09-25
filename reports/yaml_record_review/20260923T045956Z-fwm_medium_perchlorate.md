# YAML Record Review: fwm_medium_perchlorate

- Repository: CultureMech
- Record: data/merge_yaml/merged/fwm_medium_perchlorate.yaml
- Started UTC: 2026-09-23T04:58:30Z
- Finished UTC: 2026-09-23T04:59:56Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:001632` / `fwm_medium_perchlorate`, the direct MediaDive/DSMZ Medium 503b import.
- Compared it with maintained source `data/normalized_yaml/bacterial/fwm_medium_perchlorate.yaml`.
- Cross-checked the MediaDive REST payload for DSMZ 503b and the DSMZ Medium 503b PDF.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:503b` correctly identifies DSMZ Medium 503b, FWM MEDIUM (PERCHLORATE).
- Exact ignored-inclusive lookup for `mediadive.medium:503b`, `CultureMech:001632`, and `fwm_medium_perchlorate` covered normalized and generated YAML; it found this maintained DSMZ 503b owner, KOMODO 503b variant records for DSM 14691/14692, index entries, and the unsuffixed generated file.
- The generated file and maintained normalized owner are aligned, so the defects belong in `fwm_medium_perchlorate.yaml` or the MediaDive importer.
- NiCl2 x 6 H2O is grounded only to nickel dichloride, losing the source hexahydrate form.

## Evidence

- DSMZ 503b defines a 1001 ml final medium assembled from 950 ml Solution A, 30 ml Solution B, 10 ml Solution C, 1 ml Solution D, and 10 ml Solution E.
- Solution A contains KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, Na2SO4, 10 ml Modified Wolin's mineral solution, and 940 ml Distilled water. Generated base salts use MediaDive's 950 ml `g_l` values instead of preserving the source amounts.
- Modified Wolin's mineral solution is a 1 L stock added at 10 ml/L, but its ingredients are flattened at stock concentrations. Its 1 g/L NaCl and 0.1 g/L CaCl2 x 2 H2O rows were then summed into the Solution A NaCl and CaCl2 rows, producing 2.0526299999999997 g/L NaCl and 0.257895 g/L CaCl2 x 2 H2O.
- Solution B contains 1.5 g Na2CO3 in 30 ml water, Solution C contains 1.36 g Na-acetate in 10 ml water, and Solution E contains 1.22 g Sodium perchlorate in 10 ml water. The generated record exports all three stock concentrations as top-level 50, 136, and 122 g/L rows.
- Solution D is 1 ml Wolin's vitamin solution (10x), but all 10 vitamin-stock ingredients are flattened into top-level rows at their stock concentrations.
- DSMZ 503b lists strain-specific substitutions for DSM 12081, DSM 14691, DSM 14692, and DSM 27613; those notes are absent from the generated base record.

## Completeness

- Solution A, Solution B, Solution C, Solution D, Solution E, Modified Wolin's mineral solution, and Wolin's vitamin solution are not structurally represented.
- Solution-scoped NaCl and CaCl2 x 2 H2O rows were incorrectly merged across Solution A and Modified Wolin's mineral solution.
- Stock ingredients for carbonate, acetate, perchlorate, minerals, and vitamins are present at stock strength rather than final-medium concentration.
- DSMZ strain-specific variant notes are missing.

## Findings

- Major: DSMZ 503b's solution graph is flattened into one top-level ingredient list.
- Major: `NaCl` and `CaCl2 x 2 H2O` duplicate merges summed base-solution rows with Modified Wolin stock rows from a different scope.
- Major: Solution B, Solution C, Solution E, Modified Wolin's mineral solution, and Wolin's vitamin solution ingredients are emitted at stock concentration.
- Major: the generated record omits DSMZ's 10 ml/L and 1 ml/L stock-addition structure for Solutions B through E.
- Minor: strain-specific DSM 12081, DSM 14691, DSM 14692, and DSM 27613 substitutions are missing.
- Minor: NiCl2 x 6 H2O is grounded to an anhydrous nickel dichloride term.

## Recommended Edits

- Rebuild the maintained DSMZ 503b record with Solution A, Solution B, Solution C, Solution D, Solution E, Modified Wolin's mineral solution, and Wolin's vitamin solution as explicit nested solution structures.
- Restore Solution A salts to the source amounts in 950 ml and prevent duplicate collapsing across stock scopes.
- Represent Solution B, Solution C, Solution D, and Solution E as 30 ml, 10 ml, 1 ml, and 10 ml additions to sterile Solution A.
- Keep Modified Wolin's mineral and Wolin vitamin ingredients scoped to their stocks.
- Preserve DSMZ's strain-specific substitution notes or link them to the existing KOMODO 503b variant records.
- Regenerate `data/merge_yaml/merged/fwm_medium_perchlorate.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated DSMZ 503b YAML.
- Confirm top-level NaCl and CaCl2 x 2 H2O are not sums across base and mineral-stock scopes.
- Confirm Na2CO3, Na-acetate, Sodium perchlorate, Modified Wolin's mineral components, and Wolin vitamin components do not appear as final top-level stock-strength rows.
- Confirm the 1001 ml final assembly from 950/30/10/1/10 ml solution additions is represented.
- Confirm DSM strain-specific modification notes are preserved or explicitly linked.

## Additional Notes

- The generated file is derived data and is a one-source merge. The flattening defects and cross-scope duplicate sums are present in maintained normalized YAML.
