# YAML Record Review: Pyrobaculum Calidifontis Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_calidifontis_medium__7c786a25.yaml`
- Started UTC: 2026-09-24T23:26:30Z
- Finished UTC: 2026-09-24T23:27:31Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_calidifontis_medium__7c786a25.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M2457_Pyrobaculum_Calidifontis_Medium.yaml` |
| Source identity | `TOGO:M2457`, original DSMZ medium 1090 |
| Source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1090.pdf` |
| Merge fingerprint | `7c786a257ee86906a7459841018b56403f80103604948e5f94f27a10c330f6a4` |

The reviewed file is a generated merge from a single TOGO owner. Future data edits belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream artifacts.

## Validation

| Validator | Result |
| --- | --- |
| Open LinkML schema | Passed; no schema issues found. |
| Strict validator | Passed with 0 ERROR rows; TSV had the header only. |
| Reference validator | Passed; 1 file, 0 checks. |
| Term validator | Passed; emitted only the expected `eutils` `pkg_resources` warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is a TOGO M2457 wrapper around DSMZ medium 1090. Live TOGO M2457, live MediaDive 1090, and the current DSMZ 1090 PDF agree on `Pyrobaculum Calidifontis Medium`, pH 7.0, 1000 ml water, 10 g Tryptone, 1 g yeast extract, and 3 g Na2S2O3 x 5 H2O.

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009035`, `TOGO:M2457$`, `togomedium.org/medium/M2457$`, `DSMZ_Medium1090`, `mediadive.medium:1090`, the full merge fingerprint, and `TOGO_M2457_Pyrobaculum_Calidifontis_Medium` found this TOGO owner plus the direct DSMZ 1090 owner `data/normalized_yaml/archaea/pyrobaculum_calidifontis_medium.yaml` and the KOMODO 1090 owner `data/normalized_yaml/archaea/KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium.yaml`. The same DSMZ source is therefore split into separate generated artifacts.

## Evidence

The generated YAML preserves all TOGO M2457 ingredient rows at the source amounts, including 1000 ml water. TOGO M2457 and DSMZ 1090 both carry a variable NaOH pH-adjustment component; the YAML represents that component as variable-concentration NaOH.

TOGO M2457 and DSMZ 1090 both instruct curators to dissolve the ingredients, adjust to pH 7.0 with NaOH, and autoclave. The generated YAML has no `preparation_steps`, so it loses the dissolve and autoclave operations and leaves the NaOH row without source procedure context.

The repaired direct DSMZ and JCM Pyrobaculum Calidifontis owners already ground Tryptone to `MICRO:0000182` and Yeast extract to `FOODON:03315426`. The TOGO M2457 owner still lacks terms for both undefined components.

## Completeness

The ingredient table and pH are faithful to TOGO M2457 and DSMZ 1090. The record still needs the DSMZ preparation instruction, Tryptone and Yeast extract grounding, and same-source deduplication with the direct DSMZ and KOMODO 1090 owners.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Major | The DSMZ preparation instruction is absent. | TOGO M2457 and DSMZ 1090 both say to dissolve ingredients, adjust to pH 7.0 with NaOH, and autoclave; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M2457_Pyrobaculum_Calidifontis_Medium.yaml` |
| Major | The same DSMZ 1090 source is split across multiple generated records. | Ignored-file-inclusive search found the direct DSMZ 1090 owner and the KOMODO 1090 owner in addition to TOGO M2457. | Merge identity/fingerprint logic plus all DSMZ 1090 normalized owners |
| Minor | Tryptone and Yeast extract are ungrounded. | The TOGO owner has no ontology terms for either undefined component, while the direct DSMZ and JCM owners already ground them to `MICRO:0000182` and `FOODON:03315426`. | `data/normalized_yaml/archaea/TOGO_M2457_Pyrobaculum_Calidifontis_Medium.yaml` |

## Recommended Edits

1. Add the DSMZ 1090 dissolve, pH 7.0 adjustment, and autoclave preparation instruction.
2. Ground Tryptone and Yeast extract using the same exact mappings already applied to the direct DSMZ and JCM owners.
3. Reconcile the TOGO, KOMODO, and direct DSMZ owners so exact DSMZ 1090 duplicates merge or redundant wrappers are intentionally suppressed.
4. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open TOGO M2457, MediaDive 1090, and the DSMZ 1090 PDF to confirm the ingredient rows and preparation instruction are represented.
- Re-run an ignored-file-inclusive search for `TOGO:M2457`, `DSMZ_Medium1090`, and `mediadive.medium:1090` to confirm exact DSMZ 1090 duplicate handling.

## Additional Notes

The exact search also found bacterial JXT records with stale `kg_microbe_match: mediadive.medium:1090` annotations. Those annotations point at DSMZ Pyrobaculum Calidifontis Medium rather than JXT Medium, but they are not same-source duplicates of this TOGO record.
