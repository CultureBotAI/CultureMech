# YAML Record Review: marine_chloroflexi_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_chloroflexi_medium__0b1ebc83.yaml
- Started UTC: 2026-09-23T23:56:11Z
- Finished UTC: 2026-09-23T23:56:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_chloroflexi_medium__0b1ebc83.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015391 |
| Label | marine_chloroflexi_medium |
| Source identity | mediadive.medium:J1188, JCM Medium 1188, MARINE CHLOROFLEXI MEDIUM |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/specialized/marine_chloroflexi_medium.yaml or the MediaDive/JCM import path rather than this file |

The generated record denotes JCM Medium 1188 from MediaDive. Its identifier, label, source accession, ingredient salts, organic nutrients, and post-autoclave stock additions mostly match the live JCM 1188 page, but it omits the final 1 L distilled-water row and keeps a stale MediaDive preparation step that conflicts with the current JCM 1188 protocol.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_chloroflexi_medium__0b1ebc83.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_chloroflexi_medium__0b1ebc83.yaml --out /private/tmp/marine_chloroflexi_medium__0b1ebc83.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_chloroflexi_medium__0b1ebc83.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_chloroflexi_medium__0b1ebc83.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:015391, `marine_chloroflexi_medium`, and `mediadive.medium:J1188` agree on the intended source: JCM Medium 1188, `MARINE CHLOROFLEXI MEDIUM`.
- MediaDive REST identifies J1188 as JCM `MARINE CHLOROFLEXI MEDIUM` and links to the same JCM `GRMD=1188` page listed in the YAML notes.
- The live JCM 1188 page lists the same KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, NaCl, Yeast extract, Peptone, Trace vitamins, Trace mineral solution, Se/W solution, 1 M Sodium pyruvate, 8% NaHCO3, 5% L-Cysteine x HCl x H2O, and 5% Na2S x 9 H2O amounts encoded in the record.
- The exact hydrate groundings for magnesium chloride hexahydrate and calcium chloride dihydrate match JCM's stated formulas. NH4Cl, NaCl, and KH2PO4 also have exact ChEBI groundings.
- Peptone and the referenced trace, Se/W, bicarbonate, cysteine, and sulfide stock solutions remain only partly grounded or ungrounded.

## Evidence

- JCM Medium 1188 supports all 14 non-water rows and their g/L or ml/L amounts.
- JCM Medium 1188 also lists `Distilled water`, 1.0 L. The generated YAML and its maintained specialized input omit that row.
- JCM Medium 1188 says to mix components, adjust to pH 7.0, boil and cool under N2-CO2 at 4:1 v/v, distribute the medium under the same gas mixture, seal with butyl rubber stoppers, autoclave, then aseptically and anaerobically add the sodium pyruvate, NaHCO3, L-cysteine, and Na2S solutions.
- The generated preparation step instead says to use Medium No. 1187 with 10 mM final sodium pyruvate. That line is present in the current MediaDive J1188 REST payload but is not the current JCM 1188 page text, and Medium No. 1187 is `MARINE CLOSTRIDIUM MEDIUM`, not Medium 1188.
- The JCM 1188 page links Medium No. 284 for the trace vitamins solution and Medium No. 852 for the trace mineral and Se/W solutions; the generated record preserves the 2 ml/L, 1 ml/L, and 1 ml/L final additions but does not inline the stock compositions.

## Completeness

- The recipe is materially incomplete without 1 L distilled water.
- The preparation is materially incomplete without pH 7.0 adjustment, the N2-CO2 atmosphere, boiling and cooling, anaerobic vessel dispensing, butyl-stopper sealing, autoclaving, and post-cooling anaerobic stock additions.
- The trace vitamins, trace mineral, and Se/W solution compositions are recoverable from linked JCM media 284 and 852 but are not represented as nested `solutions`.
- No target organism or growth metric is asserted. That is acceptable for this JCM formulation record.
- Exact gitignore-independent searches were run for `CultureMech:015391`, `marine_chloroflexi_medium`, `mediadive.medium:J1188`, `JCM Medium 1188`, and the merge fingerprint across the scoped specialized normalized YAML directory, this target merged YAML, and the specialized and recipe index files with `--no-ignore --hidden`; the searches found the maintained input, generated target, and expected index entries.
- An exact `find data/merge_yaml/merged -maxdepth 1 -name 'marine_chloroflexi_medium*.yaml' -print` search, which includes ignored files, found only this generated target.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_chloroflexi_medium__0b1ebc83.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The JCM 1188 distilled-water row is missing. | JCM Medium 1188 lists 1.0 L Distilled water after the Se/W solution row; neither the generated YAML nor data/normalized_yaml/specialized/marine_chloroflexi_medium.yaml has a water ingredient. | data/normalized_yaml/specialized/marine_chloroflexi_medium.yaml and the MediaDive/JCM importer or expansion script |
| major | The preparation step is stale and omits the anaerobic JCM 1188 protocol. | JCM 1188 now gives a full pH 7.0, N2-CO2, sealed-vessel autoclaving, and anaerobic stock-addition protocol, while the YAML only says to use Medium No. 1187 with filter-sterilized 10 mM sodium pyruvate. | data/normalized_yaml/specialized/marine_chloroflexi_medium.yaml and the MediaDive/JCM importer or expansion script |
| minor | Linked JCM stock-solution formulas remain unnested. | JCM 1188 links Medium 284 for Trace vitamins and Medium 852 for Trace mineral and Se/W solutions; the final ml/L addition rows are present, but their stock compositions are absent. | data/normalized_yaml/specialized/marine_chloroflexi_medium.yaml |

## Recommended Edits

1. Add the 1 L distilled-water row to data/normalized_yaml/specialized/marine_chloroflexi_medium.yaml.
2. Replace the stale MediaDive 1187 preparation note with the current JCM 1188 pH 7.0, N2-CO2, sealed-vessel autoclaving, and anaerobic post-cooling stock-addition steps.
3. Consider representing the JCM 284 trace vitamins and JCM 852 trace mineral and Se/W formulas as nested solutions or linked solution records so the three stock additions are executable without leaving the record.
4. Regenerate `data/merge_yaml/merged/` and confirm the repaired generated record keeps the same CultureMech ID and JCM source identity.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against the live JCM Medium 1188 page.
- Re-fetch MediaDive J1188 after curation and record whether it still conflicts with JCM about Medium 1187.
- Run open schema, strict schema, reference, and term validation on the maintained specialized input and regenerated merge.
- Inspect the regenerated merged YAML for the 1 L distilled-water row and pH 7.0/N2-CO2 preparation sequence.

## Additional Notes

- JCM Medium 1187 is MARINE CLOSTRIDIUM MEDIUM and differs from 1188: it has 25 g NaCl, includes Resazurin, lacks the 1 M Sodium pyruvate addition, and uses pH 7.5 rather than pH 7.0.
