# YAML Record Review: cytophaga_marine_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/cytophaga_marine_medium.yaml`
- Started UTC: 2026-09-22T13:04:00Z
- Finished UTC: 2026-09-22T13:09:47Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated ID | `CultureMech:004200` |
| Name | `cytophaga_marine_medium` |
| Original name | `CYTOPHAGA (marine) medium` |
| Primary source term | `komodo.medium:172` / KOMODO Medium 172 |
| Category | `bacterial`, with merged `bacterial` and `specialized` sources |
| Generated from | `KOMODO_172a_CY_S2_medium`, `cytophaga_marine_medium`, `medium_172_modified_for_dsm_6480`, `cytophaga_marine_medium` |
| Merge fingerprint | `e8c012d38381b5b792bf92a45458aaf8c693969abe1c3a6b2becefb2809a6919` |

The reviewed file is a generated recipe under `data/merge_yaml/merged/`; future
fixes belong in the maintained normalized inputs under `data/normalized_yaml/`
or in the merge logic, followed by regeneration.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cytophaga_marine_medium.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/cytophaga_marine_medium.yaml --out /private/tmp/cytophaga_marine_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only `file	layer	category	detail	path	message`. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/cytophaga_marine_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/cytophaga_marine_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a harmless `eutils`/`pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` equivalent for `curation_history` | Not checked: the repository history validator targets standalone `history/*.yaml` records, not embedded generated `MediaRecipe.curation_history` events. |

Schema and term validation only prove that the generated YAML has valid shape
and known terms. They do not catch the false merge or the loss of DSMZ recipe
content below.

## Identity and Grounding

- The primary generated identity is DSMZ/KOMODO 172, `CYTOPHAGA (marine)
  MEDIUM`, pH 7.2. DSMZ Medium 172 and the MediaDive REST record agree on the
  nine listed solids, `Distilled water` at 1000 ml, and the instruction to
  adjust the pH to 7.2 while autoclaving sodium bicarbonate and calcium
  chloride separately.
- The `NaCl`, `KCl`, `MgSO4 x 7 H2O`, `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`,
  `NaHCO3`, and `Agar` CHEBI groundings in the reviewed record match the
  supplied chemical forms where those exact forms are represented.
- The merge is not identity clean. It includes
  `data/normalized_yaml/bacterial/KOMODO_172a_CY_S2_medium.yaml` as a duplicate
  and exposes `komodo.medium:172a` as a synonym. DSMZ/MediaDive 172a is
  `CY S2 MEDIUM`, has pH 7.0, and uses NH4Cl, KH2PO4, 1 g/L MgSO4 x 7 H2O,
  0.06 g/L CaCl2 x 2 H2O, 30 g/L NaCl, FeCl3 x 6 H2O, yeast extract, 1 g/L
  agar, plus sterile glucose, NaHCO3, and Na2S x 9 H2O additions. That formula
  is already present as `data/normalized_yaml/bacterial/cy_s2_medium.yaml` and
  generated separately as `data/merge_yaml/merged/CY_S2_MEDIUM.yaml`.
- A gitignore-independent search with `rg --no-ignore --hidden` over
  `data/raw`, `data/normalized_yaml`, and `data/merge_yaml/merged` found no
  raw capture for the KOMODO 172/172a imports; it found the normalized KOMODO
  172, KOMODO 172a, KOMODO 172_6480, DSMZ 172, DSMZ 172a, and TOGO M2296
  YAMLs plus generated/index mentions.

## Evidence

- Supported by DSMZ 172 and MediaDive 172: the generated record's DSMZ 172
  ingredient amounts for yeast extract, tryptone, NaCl, KCl, MgSO4 x 7 H2O,
  MgCl2 x 6 H2O, CaCl2 x 2 H2O, NaHCO3, and agar.
- Supported by DSMZ 172 and MediaDive 172: `physical_state: SOLID_AGAR` and
  `ph_value: 7.2`.
- Unsupported for the canonical DSMZ 172 identity: the synonym that equates
  `komodo.medium:172a` / `CY S2 medium` with `CYTOPHAGA (marine) medium`.
- Unsupported by the generated output: the 1000 ml distilled-water row and the
  special sterilization boundary for sodium bicarbonate and calcium chloride in
  DSMZ 172 are absent, even though a normalized DSMZ 172 input already carries
  the preparation sentence.
- No target-organism or growth-evidence claims are present, so no organism
  evidence could be over-scoped.

## Completeness

- Missing source content: DSMZ 172 lists distilled water in the main solution,
  but none of the KOMODO/DSMZ 172 normalized inputs in this generated group
  preserve that ingredient.
- Missing preparation: the generated merge dropped the DSMZ 172 preparation
  note from `data/normalized_yaml/specialized/cytophaga_marine_medium.yaml`.
  Following the generated record alone would not tell a curator to autoclave
  sodium bicarbonate and calcium chloride separately.
- Missing true duplicate: `data/normalized_yaml/bacterial/TOGO_M2296_Cytophaga_marine_Medium.yaml`
  also imports DSMZ 172 through TOGO M2296 and is generated separately as
  `data/merge_yaml/merged/cytophaga_marine_medium__dc362a2f.yaml`; it has not
  been unified with this DSMZ 172 group.
- Correctly empty: no `target_organisms`, `growth_metrics`, explicit
  solutions, variant links, quality flags, or discussions are present in this
  generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated canonical record falsely merges DSMZ 172a / CY S2 into DSMZ 172 / CYTOPHAGA marine medium. | `merged_from` contains `KOMODO_172a_CY_S2_medium`, the generated `synonyms` list contains `komodo.medium:172a`, and DSMZ/MediaDive 172a is a different medium with pH 7.0 and NH4Cl/KH2PO4/glucose/Na2S additions absent from DSMZ 172. | Correct `data/normalized_yaml/bacterial/KOMODO_172a_CY_S2_medium.yaml` against DSMZ/MediaDive 172a or merge it with `data/normalized_yaml/bacterial/cy_s2_medium.yaml`; regenerate `data/merge_yaml/merged/`. |
| Major | DSMZ 172 distilled water is absent. | DSMZ 172 and MediaDive 172 both include `Distilled water` at 1000 ml after agar. The reviewed generated record and its KOMODO/DSMZ normalized inputs stop at agar. | Restore the water row in the maintained DSMZ/KOMODO 172 inputs, especially `data/normalized_yaml/bacterial/cytophaga_marine_medium.yaml`, `data/normalized_yaml/bacterial/medium_172_modified_for_dsm_6480.yaml`, and `data/normalized_yaml/specialized/cytophaga_marine_medium.yaml`; keep it as 1000 ml, not 1000 g/L. |
| Major | DSMZ 172 preparation semantics are lost in the merge. | `data/normalized_yaml/specialized/cytophaga_marine_medium.yaml` says to adjust pH to 7.2 and autoclave sodium bicarbonate and calcium chloride separately in small volumes of distilled water, but the generated record has no `preparation_steps`. | Preserve source preparation steps when merging duplicate normalized recipes, then regenerate this record. |
| Major | A true DSMZ 172 duplicate remains split into `cytophaga_marine_medium__dc362a2f.yaml`. | TOGO M2296 points to the same DSMZ Medium 172 PDF but generates under a separate fingerprint because its imported formula stores distilled water as `1000 G_PER_L` and has ingredient-label differences. | Normalize `data/normalized_yaml/bacterial/TOGO_M2296_Cytophaga_marine_Medium.yaml` to the DSMZ/MediaDive 172 formula and make the merge rules group equivalent DSMZ 172 imports. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/KOMODO_172a_CY_S2_medium.yaml`
   from DSMZ/MediaDive 172a. Its current ingredient list is copied from DSMZ
   172, not CY S2, and that bad copy is what makes the merger group CY S2 with
   CYTOPHAGA marine medium.
2. Add the DSMZ 172 `Distilled water` row and pH 7.2 preparation boundary to
   each source-owned DSMZ 172 import that lacks it. Do the TOGO M2296 water
   repair with a volume representation, not the current `1000 G_PER_L`.
3. Fix `merge_recipes.py` so duplicate merges retain preparation steps from
   equivalent normalized inputs instead of dropping the DSMZ-owned step when a
   KOMODO record becomes canonical.
4. Regenerate `data/merge_yaml/merged/` so DSMZ 172, KOMODO 172, KOMODO
   172_6480, specialized DSMZ 172, and TOGO M2296 coalesce while DSMZ 172a /
   CY S2 remains in the separate CY S2 canonical record.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the repaired
  normalized inputs and regenerated merged records.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merged YAML.
- Manually compare the regenerated DSMZ 172 canonical record against the DSMZ
  Medium 172 PDF and MediaDive REST recipe to confirm the water row and
  separate-sterilization instruction survived the merge.
- Manually compare the regenerated CY S2 canonical record against DSMZ
  Medium 172a and MediaDive 172a to confirm no DSMZ 172 ingredients remain in
  its KOMODO 172a input.

## Additional Notes

- I inspected the DSMZ Medium 172 PDF, the MediaDive REST payload for medium
  172, the DSMZ Medium 172a PDF, and the MediaDive REST payload for medium
  172a.
- The generated `merged_from` list repeats `cytophaga_marine_medium` because
  both `data/normalized_yaml/bacterial/cytophaga_marine_medium.yaml` and
  `data/normalized_yaml/specialized/cytophaga_marine_medium.yaml` use that
  basename. This is ambiguous for humans but not itself the scientific error.
