# YAML Record Review: PYROBACULUM FERRIREDUCENS MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_ferrireducens_medium__9f828368.yaml`
- Started UTC: 2026-09-24T23:30:36Z
- Finished UTC: 2026-09-24T23:31:25Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_ferrireducens_medium__9f828368.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/pyrobaculum_ferrireducens_medium.yaml` |
| Source identity | DSMZ medium 1579 / `mediadive.medium:1579` |
| Source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1579.pdf` |
| Merge fingerprint | `9f82836846bd70766cae3a18f12563a2f1611d10c449b9369768b0e9702b91d6` |

The reviewed file is a generated merge from a single direct DSMZ/MediaDive owner. Future data edits belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream artifacts.

## Validation

| Validator | Result |
| --- | --- |
| Open LinkML schema | Passed; no schema issues found. |
| Strict validator | Passed with 0 ERROR rows; TSV had the header only. |
| Reference validator | Passed; 1 file, 0 checks. |
| Term validator | Passed; emitted only the expected `eutils` `pkg_resources` warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is the direct DSMZ/MediaDive owner for DSMZ medium 1579, `PYROBACULUM FERRIREDUCENS MEDIUM`. The live MediaDive 1579 REST response and the current DSMZ 1579 PDF agree on pH 6.5 to 6.8, the main 1003 ml recipe, and its 1 ml/L additions of Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x).

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:001053`, `mediadive.medium:1579`, `DSMZ_Medium1579`, `Source: DSMZ, ID: 1579`, the full merge fingerprint, and `pyrobaculum_ferrireducens_medium.yaml` found this direct DSMZ owner plus `data/normalized_yaml/archaea/TOGO_M2460_Pyrobaculum_Ferrireducens_Medium.yaml`, a TOGO wrapper around the same DSMZ 1579 PDF. The exact same DSMZ source is therefore split into two generated records.

## Evidence

DSMZ 1579 defines a 1003 ml main solution containing 0.33 g each of NH4Cl, KCl, KH2PO4, MgCl2 x 6 H2O, and CaCl2 x 2 H2O; 1 ml Trace element solution SL-10; 1 ml Selenite-tungstate solution; 1 g yeast extract; 1 g KNO3; 2 g NaHCO3; 1 ml Wolin's vitamin solution (10x); and 1000 ml distilled water. The generated YAML keeps the source's five 0.33 g salts, yeast extract, KNO3, NaHCO3, and pH range, but it has no final water row and no explicit rows for the three 1 ml stock additions.

All three referenced stocks were flattened into the top-level ingredient list at their stock concentrations. Examples include Trace element solution SL-10's 2.5 g/L HCl and 1.5 g/L FeCl2 x 4 H2O, Selenite-tungstate solution's 0.5 g/L NaOH, and Wolin's vitamin solution's 0.02 g/L biotin and 0.02 g/L folic acid.

The DSMZ 1579 main-solution preparation step is present, and the Trace element solution SL-10 preparation step is also present. The latter is scoped as a second top-level recipe step because the Trace element solution itself is missing as a nested stock.

The direct owner still lacks a term for Yeast extract, while other repaired Pyrobaculum records ground Yeast extract to `FOODON:03315426`.

## Completeness

The record preserves the DSMZ identity, pH range, main preparation, and many chemical groundings, but it is incomplete as an executable recipe. It needs the 1000 ml main water row and nested representations for Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x), each used at 1 ml per 1003 ml main solution.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Blocker | Three stock solution additions are missing and their members were flattened into the main recipe. | DSMZ 1579 uses 1 ml each of Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x); the YAML has no `solutions` and instead lists all stock-local compounds as top-level ingredients. | `data/normalized_yaml/archaea/pyrobaculum_ferrireducens_medium.yaml` |
| Blocker | Stock-local trace and vitamin concentrations are represented as final-medium concentrations. | The YAML stores SL-10 HCl as `2.5` `G_PER_L`, selenite-tungstate NaOH as `0.5` `G_PER_L`, and Wolin vitamin biotin as `0.02` `G_PER_L` even though only 1 ml of each stock is used in a 1003 ml main solution. | `data/normalized_yaml/archaea/pyrobaculum_ferrireducens_medium.yaml` |
| Major | The 1000 ml main-solution water row is absent. | DSMZ 1579 and MediaDive 1579 list 1000 ml Distilled water in Main sol. 1579; the YAML has no water ingredient for the main solution. | `data/normalized_yaml/archaea/pyrobaculum_ferrireducens_medium.yaml` |
| Major | The Trace element solution SL-10 preparation step is scoped to the main recipe. | The FeCl2/HCl dilution instruction belongs to the SL-10 stock, but the missing stock boundary leaves it as top-level `preparation_steps[1]`. | `data/normalized_yaml/archaea/pyrobaculum_ferrireducens_medium.yaml` |
| Major | The same DSMZ 1579 source is split across two generated records. | Ignored-file-inclusive search found `data/normalized_yaml/archaea/TOGO_M2460_Pyrobaculum_Ferrireducens_Medium.yaml` and generated `PYROBACULUM_FERRIREDUCENS_MEDIUM.yaml`, both pointing to `DSMZ_Medium1579.pdf`. | Merge identity/fingerprint logic plus both normalized owners |
| Minor | Yeast extract is ungrounded. | The direct DSMZ owner has no ontology term for Yeast extract. | `data/normalized_yaml/archaea/pyrobaculum_ferrireducens_medium.yaml` |

## Recommended Edits

1. Add the 1000 ml main-solution water row.
2. Rebuild Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) as populated nested stocks.
3. Represent the three DSMZ stock additions as 1 ml per 1003 ml main solution rather than top-level stock concentrations.
4. Keep the FeCl2/HCl preparation step attached to Trace element solution SL-10.
5. Ground Yeast extract with the repository's established Yeast extract mapping.
6. Reconcile the direct DSMZ owner with the TOGO M2460 wrapper so exact DSMZ 1579 duplicates merge or one wrapper is intentionally suppressed.
7. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open MediaDive 1579 and the DSMZ 1579 PDF to confirm all three 1 ml stock additions and the 1000 ml water row are represented.
- Re-run an ignored-file-inclusive search for `mediadive.medium:1579`, `DSMZ_Medium1579`, and `TOGO_M2460` to confirm exact DSMZ 1579 duplicate handling.
- Confirm vitamin and trace-element concentrations are no longer represented as final-medium top-level stock concentrations.

## Additional Notes

None found.
