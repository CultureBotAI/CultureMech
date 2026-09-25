# YAML Record Review: gracilibacillus_medium__42ee192f

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gracilibacillus_medium__42ee192f.yaml
- Started UTC: 2026-09-23T07:36:12Z
- Finished UTC: 2026-09-23T07:38:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:001946` |
| Name | `gracilibacillus_medium` |
| Original name | `GRACILIBACILLUS MEDIUM` |
| Category | `bacterial` |
| Canonical media term | `mediadive.medium:802` |
| Merged sources | `gracilibacillus_medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gracilibacillus_medium__42ee192f.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/gracilibacillus_medium__42ee192f.yaml --out /private/tmp/gracilibacillus_medium__42ee192f.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/gracilibacillus_medium__42ee192f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/gracilibacillus_medium__42ee192f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is the MediaDive DSMZ 802 import. A gitignore-independent exact search for `mediadive.medium:802`, `komodo.medium:802`, `DSMZ_Medium802`, `gracilibacillus_medium`, and `KOMODO_802_GRACILIBACILLUS_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found a split KOMODO 802 import generated separately as `data/merge_yaml/merged/GRACILIBACILLUS_MEDIUM.yaml`.

Most small molecules are narrowly grounded. `NiCl2 x 6 H2O` is grounded to an anhydrous nickel dichloride term rather than to a hexahydrate term.

## Evidence

DSMZ Medium 802 adds 2 ml Trace metals solution and 998 ml Distilled water to the final liter, then directs curators to add 10 ml KH2PO4 stock at 50 g/l, 5 ml CaCl2 stock at 100 g/l, 2 ml FeCl2/MnCl2 stock at 20 g/l each, and glucose to 2 g/l from sterile stocks after autoclaving.

The generated record expands the full trace-metals stock directly into top-level ingredients at stock strength, omits the 2 ml/l stock-addition row, and omits the final 998 ml water row. It also flattens the post-autoclave stocks incorrectly: the 10 ml of 50 g/l KH2PO4 should be 0.5 g/l final KH2PO4, not 23.4 g/l, and the 5 ml of 100 g/l CaCl2 should be 0.5 g/l final CaCl2, not 5 g/l.

## Completeness

The basal NaCl, MgSO4, KCl, NaBr, Yeast extract, Trypticase peptone, Tris-HCl, final glucose, and pH rows are present, but the stock handling is not complete enough for DSMZ 802 and the KOMODO 802 copy is split into a separate generated record. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Trace metals solution was flattened into the final formula at stock concentration. | DSMZ 802 adds 2 ml/l Trace metals solution; the generated record promotes stock-strength HCl, FeCl2 x 4 H2O, CoCl2 x 6 H2O, MnCl2 x 4 H2O, ZnCl2, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, AlCl3 x 6 H2O, and Na2WO4 x 2 H2O directly to top-level ingredients. | MediaDive DSMZ 802 solution expansion. |
| Blocker | Sterile post-autoclave stocks were converted to the wrong final concentrations. | The source calls for 10 ml of 50 g/l KH2PO4, 5 ml of 100 g/l CaCl2, and 2 ml of a FeCl2/MnCl2 stock at 20 g/l each; the generated record encodes 23.4 g/l KH2PO4, 5 g/l CaCl2, and sums the 20 g/l FeCl2 and MnCl2 stock concentrations with trace-solution rows. | MediaDive DSMZ 802 stock-addition normalization. |
| Major | Required water and stock-addition rows are missing. | The source has 2 ml/l Trace metals solution and 998 ml/l Distilled water as final rows; neither is structured in the generated ingredient list. | MediaDive DSMZ 802 nested-solution normalization. |
| Major | KOMODO 802 remains split from the MediaDive DSMZ 802 duplicate group. | KOMODO 802 cites DSMZ Medium 802 and is generated separately as `GRACILIBACILLUS_MEDIUM.yaml`, while this record only merges the MediaDive parent. | Duplicate grouping for KOMODO/MediaDive DSMZ 802 records. |
| Major | Nickel chloride hexahydrate is grounded to the anhydrous salt. | The trace-metals source row is `NiCl2 x 6 H2O`; the generated CHEBI term is `CHEBI:34887` / `nickel dichloride`. | CHEBI grounding for hydrate-specific salts. |

## Recommended Edits

1. Model Trace metals solution as a nested 2 ml/l stock addition with its own 1 L recipe.
2. Restore the 998 ml/l final Distilled water row.
3. Encode KH2PO4, CaCl2, and FeCl2/MnCl2 as sterile post-autoclave stock additions and calculate final concentrations only from the stock strength and added volume.
4. Keep the trace-metals FeCl2 and MnCl2 rows separate from the FeCl2/MnCl2 post-autoclave stock.
5. Reground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term if one is available.
6. Repair the KOMODO 802 parent and confirm it joins the same DSMZ 802 source-duplicate cluster.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated DSMZ 802 record.
- Compare the regenerated record against MediaDive 802, the DSMZ Medium 802 PDF, and KOMODO 802.
- Confirm Trace metals solution and FeCl2/MnCl2 solution remain nested stock contexts and are not flattened into final-liter concentrations.
- Re-run the exact gitignore-independent search for `mediadive.medium:802`, `komodo.medium:802`, `DSMZ_Medium802`, `gracilibacillus_medium`, and `KOMODO_802_GRACILIBACILLUS_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the duplicate group is intentional.

## Additional Notes

None found.
