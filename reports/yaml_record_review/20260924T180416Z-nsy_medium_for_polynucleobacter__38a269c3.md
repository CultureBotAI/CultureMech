# YAML Record Review: nsy_medium_for_polynucleobacter

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/nsy_medium_for_polynucleobacter__38a269c3.yaml
- Started UTC: 2026-09-24T18:02:33Z
- Finished UTC: 2026-09-24T18:04:16Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:007859 |
| Name | nsy_medium_for_polynucleobacter |
| Original name | NSY Medium For Polynucleobacter |
| Category | bacterial |
| Media term | TOGO:M1322 / NSY Medium For Polynucleobacter |
| Generated path | data/merge_yaml/merged/nsy_medium_for_polynucleobacter__38a269c3.yaml |
| Maintained source | data/normalized_yaml/bacterial/TOGO_M1322_NSY_Medium_For_Polynucleobacter.yaml |
| Merge fingerprint | 38a269c33f87569463f5747c7e4dbcec713cee8875acf8dadb5bb004fa027ea5 |
| Merged from | TOGO_M1322_NSY_Medium_For_Polynucleobacter |

This is a generated singleton TOGO record for JCM GRMD 1230. Fixes belong in the maintained TOGO import and source-equivalence merge logic, followed by merged-record regeneration.

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/nsy_medium_for_polynucleobacter__38a269c3.yaml` | Passed with "No issues found". |
| Strict validation with `scripts/validate_strict.py data/merge_yaml/merged/nsy_medium_for_polynucleobacter__38a269c3.yaml --out /private/tmp/nsy_medium_for_polynucleobacter__38a269c3.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header line. |
| Reference validation with `linkml-reference-validator validate data data/merge_yaml/merged/nsy_medium_for_polynucleobacter__38a269c3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 total checks and no failures. |
| Term validation with `linkml-term-validator validate-data data/merge_yaml/merged/nsy_medium_for_polynucleobacter__38a269c3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator validates standalone `history/` entries, not embedded generated `MediaRecipe.curation_history`. |

## Identity and Grounding

The intended identity is TOGO `M1322`, a mirror of JCM Medium 1230, `NSY MEDIUM FOR POLYNUCLEOBACTER`. The label, bacterial category, JCM source URL, solid-agar state, agar row, and complex ingredients agree with the JCM 1230 source page.

An ignored-file-inclusive search for `GRMD=1230`, `TOGO:M1322`, `JCM_M1230`, `NSY Medium For Polynucleobacter`, and `nsy_medium_for_polynucleobacter` across `data/normalized_yaml` and `data/merge_yaml/merged` found this TOGO source, the direct JCM `data/normalized_yaml/bacterial/JCM_J1230_NSY_MEDIUM_FOR_POLYNUCLEOBACTER.yaml`, a DSMZ 1167 record, a KOMODO mirror of DSMZ 1167, and three generated records. The direct JCM source points to the same `GRMD=1230` page and should collapse with TOGO `M1322`; the DSMZ/KOMODO pair describes a related but distinct DSMZ 1167 liquid medium.

## Evidence

The live JCM 1230 page lists Nutrient broth, Phytone peptone (BD-BBL), and Yeast extract (BD-Difco) at 1.0 g each; MgSO4 x 7 H2O at 75 mg; Ca(NO3)2 x 4 H2O at 43 mg; NaHCO3 at 16 mg; KCl at 5 mg; K2HPO4 at 3.7 mg; SL-4 trace element solution at 0.1 ml; distilled water at 1.0 L; pH adjustment to 7.2; and 15.0 g/L agar for solid medium. TOGO M1322 mirrors the same numeric values and units in its JSON.

The generated record does not preserve those units. It stores the milligram salts as `75`, `43`, `16`, `5`, and `3.7` `G_PER_L`, stores 1 L water as `1 G_PER_L`, and stores the 0.1 ml SL-4 trace element solution as an empty `Unknown solution` at `0.1 G_PER_L`. It also drops the source pH of 7.2 entirely.

## Completeness

The complex one-gram ingredients and solidifying agar are present and supported, but the inorganic salts are 1000-fold too high, the 1 L water row has the wrong concentration unit, the SL-4 cross-reference to Medium 340 is an empty shell with the wrong unit, and the JCM pH 7.2 instruction is missing.

Empty target-organism and citation slots are acceptable for this provider formula. No organism-specific evidence is present in the imported JCM or TOGO source.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | TOGO M1322 milligram and liter quantities were converted to `G_PER_L` without unit conversion. | JCM and TOGO list MgSO4 x 7 H2O at 75 mg, Ca(NO3)2 x 4 H2O at 43 mg, NaHCO3 at 16 mg, KCl at 5 mg, K2HPO4 at 3.7 mg, and distilled water at 1 L. The generated record stores `75`, `43`, `16`, `5`, `3.7`, and `1` all as `G_PER_L`. | TOGO import normalization for `data/normalized_yaml/bacterial/TOGO_M1322_NSY_Medium_For_Polynucleobacter.yaml`, then merged-record regeneration. |
| Major | The SL-4 trace element addition is represented as an empty stock with a gram-per-liter unit. | JCM 1230 adds 0.1 ml SL-4 trace element solution from JCM Medium 340; TOGO M1322 keeps that reference as `M335`. The generated `solutions` row has an empty composition, `name: Unknown solution`, and `0.1 G_PER_L`. | TOGO solution cross-reference handling, then merged-record regeneration. |
| Major | The pH 7.2 source instruction was dropped. | Both the live JCM 1230 HTML and the TOGO M1322 JSON carry pH 7.2. The generated record has no `ph_value`, `ph_range`, or pH preparation step. | TOGO import normalization for `data/normalized_yaml/bacterial/TOGO_M1322_NSY_Medium_For_Polynucleobacter.yaml`. |
| Major | The direct JCM import of the same GRMD 1230 page remains split into `data/merge_yaml/merged/NSY_MEDIUM_FOR_POLYNUCLEOBACTER.yaml`. | The ignored-file-inclusive search found `data/normalized_yaml/bacterial/JCM_J1230_NSY_MEDIUM_FOR_POLYNUCLEOBACTER.yaml`, whose `media_term` is `mediadive.medium:J1230` and whose `notes` point to the same `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1230` URL. | Merge key normalization or source-equivalence mapping for TOGO `JCM_M1230` and MediaDive/JCM `J1230`. |

## Recommended Edits

1. Convert TOGO milligram quantities to grams per liter for JCM 1230 instead of copying raw `mg` amounts into `G_PER_L`.
2. Represent 1 L distilled water as a liter volume, not `1 G_PER_L`, or omit it if solvent rows are intentionally excluded from this import class.
3. Preserve the 0.1 ml/L SL-4 trace element solution as a solution cross-reference to the JCM Medium 340 recipe with the correct volume unit.
4. Carry the TOGO/JCM pH 7.2 value into `ph_value` or an explicit pH adjustment step.
5. Add an equivalence rule so TOGO `M1322` / `JCM_M1230` and direct JCM `mediadive.medium:J1230` merge into one generated JCM 1230 record while remaining separate from DSMZ Medium 1167.

## Follow-up Checks

1. Regenerate normalized and merged YAML, then verify the reviewed record stores the inorganic salts at `0.075`, `0.043`, `0.016`, `0.005`, and `0.0037` g/L with pH 7.2 retained.
2. Search with ignored files included for `TOGO:M1322`, `JCM_M1230`, `mediadive.medium:J1230`, and `GRMD=1230` to confirm the TOGO and direct JCM sources now produce one merged record.
3. Run the focused open schema, strict, reference, and term validators on the regenerated record.

## Additional Notes

`data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml` is a separate generated record for the DSMZ 1167 / KOMODO 1167 pair. It should not be merged into the JCM 1230 record reviewed here because DSMZ 1167 uses tap water or a replacement inorganic solution, Soy peptone, no agar, and a different preparation note.
