# YAML Record Review: cytophaga_marine_medium__dc362a2f

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/cytophaga_marine_medium__dc362a2f.yaml`
- Started UTC: 2026-09-22T13:13:00Z
- Finished UTC: 2026-09-22T13:15:14Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated ID | `CultureMech:008882` |
| Name | `cytophaga_marine_medium` |
| Original name | `Cytophaga (marine) Medium` |
| Source term | `TOGO:M2296` / TOGO Medium M2296 |
| Original source | DSMZ Medium 172 |
| Generated from | `TOGO_M2296_Cytophaga_marine_Medium` |
| Merge fingerprint | `dc362a2ffba45d5646c667bdf6c9da995f477acdd445deb529ff29779f8907be` |

The reviewed file is generated from
`data/normalized_yaml/bacterial/TOGO_M2296_Cytophaga_marine_Medium.yaml`. That
normalized file, not this generated output, owns future ingredient repairs.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cytophaga_marine_medium__dc362a2f.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/cytophaga_marine_medium__dc362a2f.yaml --out /private/tmp/cytophaga_marine_medium__dc362a2f.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/cytophaga_marine_medium__dc362a2f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/cytophaga_marine_medium__dc362a2f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a harmless `eutils`/`pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` equivalent for `curation_history` | Not checked: the repository history validator targets standalone `history/*.yaml` records, not embedded generated `MediaRecipe.curation_history` events. |

## Identity and Grounding

- TOGO M2296 identifies `Cytophaga (marine) Medium`, points at the DSMZ
  Medium 172 PDF, and reports pH 7.2.
- DSMZ Medium 172 and the MediaDive REST record for medium 172 describe the
  same medium and support the generated salts, yeast extract, tryptone, and
  agar amounts.
- The generated record is not formula-faithful because it stores DSMZ/TOGO
  `Distilled water` at `1000 G_PER_L`; both sources state 1000 ml.
- The primary term for `MgSO4 x 7 H2O` is corrected to
  `CHEBI:31795` / magnesium sulfate heptahydrate, but the same ingredient's
  `mediaingredientmech_chebi_term` still points at generic
  `CHEBI:32599` / magnesium sulfate.
- A gitignore-independent search with `rg --no-ignore --hidden` over
  `data/raw`, `data/normalized_yaml`, and `data/merge_yaml/merged` found no raw
  TOGO or DSMZ capture for this exact M2296 import; it found the normalized
  TOGO M2296 source, generated record, source indexes, and other DSMZ 172
  records.

## Evidence

- Supported by TOGO M2296 and DSMZ Medium 172: `Distilled water` 1000 ml,
  `MgSO4 x 7 H2O` 6.3 g, `NaCl` 24.7 g, `CaCl2 x 2 H2O` 1.2 g,
  `MgCl2 x 6 H2O` 4.6 g, `KCl` 0.7 g, `NaHCO3` 0.2 g, `Agar (Difco)` 15 g,
  `Yeast extract (Difco)` 1 g, `Tryptone (Difco)` 1 g, and pH 7.2.
- Supported by TOGO M2296 and DSMZ Medium 172: the instruction to autoclave
  sodium bicarbonate and calcium chloride separately, each in a small volume of
  distilled water.
- Unsupported by TOGO or DSMZ: water represented as 1000 g/L. The source
  expresses water as a volume, and the record should not assume a density-based
  mass conversion.
- Unsupported in the generated record: generic magnesium sulfate in
  `mediaingredientmech_chebi_term` for the heptahydrate ingredient.
- No target-organism or growth-evidence claims are present.

## Completeness

- Missing condition: pH 7.2 is present in TOGO and DSMZ but absent from this
  generated record.
- Missing preparation: the separate autoclaving instruction for sodium
  bicarbonate and calcium chloride is present in TOGO and DSMZ but absent from
  this generated record.
- Missing true merge: this TOGO M2296 import is the same DSMZ 172 medium as
  `data/merge_yaml/merged/cytophaga_marine_medium.yaml`, but the bad water unit
  and source-order differences keep it isolated under a second merge
  fingerprint.
- Correctly empty: no explicit target organisms, growth metrics, variant links,
  or incubations are asserted by this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The water amount has the wrong dimension. | TOGO M2296 and DSMZ 172 list `Distilled water` as 1000 ml; the generated record stores `1000 G_PER_L`. | Fix `data/normalized_yaml/bacterial/TOGO_M2296_Cytophaga_marine_Medium.yaml` to preserve the volume unit, then regenerate merged YAML. |
| Major | Source pH and preparation are absent. | TOGO M2296 reports pH 7.2 and the same separate-autoclaving comment present in the DSMZ 172 PDF; the generated record has no `ph_value` or `preparation_steps`. | Add pH 7.2 and the separate sodium-bicarbonate/calcium-chloride autoclaving step to the normalized TOGO M2296 record, then regenerate. |
| Major | The heptahydrate ingredient has an inconsistent secondary CHEBI grounding. | The primary `term` for `MgSO4 x 7 H2O` is `CHEBI:31795`, but `mediaingredientmech_chebi_term` is still generic `CHEBI:32599`. | Refresh `mediaingredientmech_chebi_term` in the normalized TOGO M2296 record after preserving the exact heptahydrate form. |
| Major | DSMZ 172 is fragmented into two generated canonical records. | This generated record and `data/merge_yaml/merged/cytophaga_marine_medium.yaml` point at the same DSMZ Medium 172 source but have different merge fingerprints. | Normalize the TOGO M2296 formula and regenerate so equivalent DSMZ 172 imports merge together. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M2296_Cytophaga_marine_Medium.yaml`,
   change `Distilled water` from `1000 G_PER_L` to a representation of 1000 ml.
2. Add `ph_value: 7.2` and a preparation step for the separate sterilization of
   sodium bicarbonate and calcium chloride.
3. Update `MgSO4 x 7 H2O` so both its primary `term` and
   `mediaingredientmech_chebi_term` resolve to magnesium sulfate heptahydrate.
4. Regenerate the merged layer and verify TOGO M2296 coalesces with the
   normalized KOMODO/DSMZ 172 records, while DSMZ 172a / CY S2 remains separate.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the edited
  normalized source and regenerated merged record.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare the regenerated record with TOGO M2296, the DSMZ Medium 172
  PDF, and the MediaDive REST payload for medium 172.
- Manually inspect the regenerated merge set to ensure only DSMZ 172 equivalent
  records merged and `komodo.medium:172a` did not re-enter the group.

## Additional Notes

- The generated order mirrors the TOGO API order rather than the DSMZ PDF order;
  this is not a scientific blocker because the amounts and component identities
  are explicit.
- The generated record has no explicit `references`; the TOGO URL and DSMZ URL
  are only embedded in `notes`.
