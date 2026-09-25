# YAML Record Review: granulicella_paludicola_medium__cc9b9562

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/granulicella_paludicola_medium__cc9b9562.yaml
- Started UTC: 2026-09-23T07:38:52Z
- Finished UTC: 2026-09-23T07:40:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:000749` |
| Name | `granulicella_paludicola_medium` |
| Original name | `GRANULICELLA PALUDICOLA MEDIUM` |
| Category | `bacterial` |
| Canonical media term | `mediadive.medium:1285` |
| Merged sources | `granulicella_paludicola_medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/granulicella_paludicola_medium__cc9b9562.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/granulicella_paludicola_medium__cc9b9562.yaml --out /private/tmp/granulicella_paludicola_medium__cc9b9562.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/granulicella_paludicola_medium__cc9b9562.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/granulicella_paludicola_medium__cc9b9562.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is the MediaDive DSMZ 1285 import. A gitignore-independent exact search for `mediadive.medium:1285`, `komodo.medium:1285`, `DSMZ_Medium1285`, `granulicella_paludicola_medium`, and `KOMODO_1285_GRANULICELLA_PALUDICOLA_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found a split KOMODO 1285 import generated separately as `data/merge_yaml/merged/GRANULICELLA_PALUDICOLA_MEDIUM.yaml`.

The present small-molecule groundings are narrow, and Casamino acids remain ungrounded as a mixture.

## Evidence

DSMZ Medium 1285 contains Fructose, Yeast extract, Casamino acids, MgSO4 x 7 H2O, CaCl2 x 2 H2O, KH2PO4, (NH4)2SO4, and 1000 ml Distilled water. It then says the medium may be solidified with 15 g/l agar and adjusted to pH 4.0-5.0 with alginic acid.

The generated record preserves all non-water solutes, the pH range, and the alginic-acid pH adjustment note. It omits the 1000 ml Distilled water row and represents the conditionally solidified agar form as an unconditional `SOLID_AGAR` recipe. The split KOMODO generated record also adds an ungrounded variable `alginic` top-level ingredient even though alginic acid is a pH adjuster rather than a quantified formula component.

## Completeness

The MediaDive formula is close, but the generated record is incomplete without final water and it overstates optional agar as a required solid formulation. The KOMODO DSMZ 1285 copy also needs to be repaired and merged into this duplicate group. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The final Distilled water row is missing. | MediaDive 1285 and the DSMZ Medium 1285 PDF include 1000 ml Distilled water; the generated ingredient list has no water row. | MediaDive DSMZ 1285 normalization. |
| Major | Conditional agar was made unconditional. | The source says the medium may be solidified with 15 g/l agar; the generated record is `SOLID_AGAR` and encodes Agar as an ordinary top-level ingredient, with only a note preserving `for solid medium`. | MediaDive DSMZ 1285 condition handling. |
| Major | KOMODO 1285 remains split from the MediaDive DSMZ 1285 duplicate group. | KOMODO 1285 cites DSMZ Medium 1285 and has the same source formula except for a mined variable `alginic` pH-adjuster ingredient, but it is generated separately as `GRANULICELLA_PALUDICOLA_MEDIUM.yaml`. | Duplicate grouping for KOMODO/MediaDive DSMZ 1285 records. |

## Recommended Edits

1. Restore the 1000 ml/l Distilled water row.
2. Represent 15 g/l Agar as a conditional solidifying addition or split the liquid and solid formulations explicitly.
3. Keep alginic acid as pH-adjustment metadata unless a quantified ingredient is provided by the source.
4. Repair the KOMODO 1285 parent by removing the spurious variable `alginic` ingredient and merging it with the MediaDive DSMZ 1285 source duplicate.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated DSMZ 1285 record.
- Compare the regenerated formula against MediaDive 1285, the DSMZ Medium 1285 PDF, and KOMODO 1285.
- Confirm conditional agar and alginic acid pH adjustment remain distinct from required basal ingredients.
- Re-run the exact gitignore-independent search for `mediadive.medium:1285`, `komodo.medium:1285`, `DSMZ_Medium1285`, `granulicella_paludicola_medium`, and `KOMODO_1285_GRANULICELLA_PALUDICOLA_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the duplicate group is intentional.

## Additional Notes

None found.
