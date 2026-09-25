# YAML Record Review: PYROBACULUM CALIDIFONTIS medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_calidifontis_medium__1debe1f9.yaml`
- Started UTC: 2026-09-24T23:24:49Z
- Finished UTC: 2026-09-24T23:25:37Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_calidifontis_medium__1debe1f9.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium.yaml` |
| Source identity | KOMODO 1090 enriched from DSMZ / MediaDive 1090 |
| Source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1090.pdf` |
| Merge fingerprint | `1debe1f97e5b9606bf3e255eec3c9f4c4f75754c9e9ae147d170ee9bdb93d5b2` |

The reviewed file is a generated merge from a single KOMODO owner. Future data edits belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream artifacts.

## Validation

| Validator | Result |
| --- | --- |
| Open LinkML schema | Passed; exited 0 with no diagnostics. |
| Strict validator | Passed with 0 ERROR rows; TSV had the header only. |
| Reference validator | Passed; 1 file, 0 checks. |
| Term validator | Passed; emitted only the expected `eutils` `pkg_resources` warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record points to KOMODO medium 1090 and was enriched from DSMZ / MediaDive medium 1090. Live MediaDive 1090 and the current DSMZ 1090 PDF identify `PYROBACULUM CALIDIFONTIS MEDIUM`, pH 7.0, and the same three non-water solutes.

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:003741`, `komodo.medium:1090`, `Source: KOMODO, ID: 1090`, `mediadive.medium:1090`, `DSMZ Medium: 1090`, the full merge fingerprint, and `KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium` found this KOMODO owner plus `data/normalized_yaml/archaea/pyrobaculum_calidifontis_medium.yaml`, a direct DSMZ 1090 owner for the same source. The same DSMZ recipe is therefore split into separate generated records.

## Evidence

DSMZ 1090 and MediaDive 1090 define a one-liter liquid recipe with 10 g Tryptone, 1 g yeast extract, 3 g Na2S2O3 x 5 H2O, and 1000 ml distilled water. The generated KOMODO YAML preserves the three non-water concentrations but omits the 1000 ml distilled water row.

DSMZ 1090 instructs curators to dissolve the ingredients and adjust to pH 7.0 with NaOH before autoclaving. The KOMODO YAML preserves `ph_value: 7.0` and adds variable NaOH from the pH-buffer note, but it has no `preparation_steps`.

The repaired direct DSMZ owner already grounds Tryptone to `MICRO:0000182` and Yeast extract to `FOODON:03315426`. The KOMODO owner still lacks `term` and `mediaingredientmech_chebi_term` or equivalent grounding on both undefined components.

## Completeness

The record is close to the DSMZ recipe in ingredient identity and concentration, but it is missing the water row and the source autoclaving instruction. It also needs the same Tryptone and Yeast extract grounding repair already applied to the direct DSMZ and JCM Pyrobaculum Calidifontis owners.

The direct DSMZ owner for MediaDive 1090 and the JCM 338 owner describe the same simple three-solute recipe under different source wrappers. The exact DSMZ 1090 duplicate needs to be reconciled with this KOMODO wrapper before the generated set has one DSMZ 1090 artifact.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Major | The source water row is absent. | DSMZ 1090 and MediaDive 1090 list 1000 ml Distilled water; the generated YAML has no water ingredient. | `data/normalized_yaml/archaea/KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium.yaml` |
| Major | The DSMZ preparation instruction is absent. | DSMZ 1090 says to dissolve the ingredients, adjust to pH 7.0 with NaOH, and autoclave; the YAML has only a variable NaOH ingredient and no `preparation_steps`. | `data/normalized_yaml/archaea/KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium.yaml` |
| Major | The same DSMZ 1090 source is split across two generated records. | Ignored-file-inclusive search found `data/normalized_yaml/archaea/pyrobaculum_calidifontis_medium.yaml`, a direct DSMZ 1090 owner with the same recipe and source PDF. | Merge identity/fingerprint logic plus both normalized owners |
| Minor | Tryptone and Yeast extract are ungrounded. | The KOMODO owner has no ontology terms for either undefined component, while the direct DSMZ and JCM owners already ground them to `MICRO:0000182` and `FOODON:03315426`. | `data/normalized_yaml/archaea/KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium.yaml` |
| Minor | The KOMODO import timestamp is malformed. | `curation_history[0].timestamp` is `2026-01-27T01:15:01.fZ`, which is not a valid fractional-second timestamp. | `data/normalized_yaml/archaea/KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium.yaml` |

## Recommended Edits

1. Restore the 1000 ml distilled water row.
2. Add the DSMZ 1090 dissolve, pH 7.0, and autoclave preparation instruction.
3. Ground Tryptone and Yeast extract using the same exact mappings already applied to the direct DSMZ and JCM owners.
4. Correct the malformed KOMODO import timestamp.
5. Reconcile the KOMODO and direct DSMZ owners so exact DSMZ 1090 duplicates merge or one wrapper is intentionally suppressed.
6. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open MediaDive 1090 and the DSMZ 1090 PDF to confirm the water row and autoclaving instruction are represented.
- Re-run an ignored-file-inclusive search for `komodo.medium:1090`, `mediadive.medium:1090`, and `DSMZ_Medium1090` to confirm exact DSMZ 1090 duplicate handling.

## Additional Notes

The exact search also found bacterial JXT records with stale `kg_microbe_match: mediadive.medium:1090` annotations. Those annotations point at DSMZ Pyrobaculum Calidifontis Medium rather than JXT Medium, but they are not same-source duplicates of this KOMODO record.
