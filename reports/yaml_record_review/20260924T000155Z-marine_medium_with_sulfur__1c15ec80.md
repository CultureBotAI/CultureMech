# YAML Record Review: marine_medium_with_sulfur

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_medium_with_sulfur__1c15ec80.yaml
- Started UTC: 2026-09-24T00:01:55Z
- Finished UTC: 2026-09-24T00:02:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_medium_with_sulfur__1c15ec80.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015401 |
| Label | marine_medium_with_sulfur |
| Source identity | mediadive.medium:J375, JCM Medium 375, MARINE MEDIUM WITH SULFUR |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/specialized/marine_medium_with_sulfur.yaml or the MediaDive importer rather than this file |

The generated record denotes JCM Medium 375 from MediaDive. Its source identity, pH, ingredient amounts, and H2-CO2/sulfur preparation prose mostly match JCM and MediaDive, but the final 1 L distilled-water row is absent and the sulfur ingredient is grounded to an atom-level ChEBI term.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_medium_with_sulfur__1c15ec80.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_medium_with_sulfur__1c15ec80.yaml --out /private/tmp/marine_medium_with_sulfur__1c15ec80.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_medium_with_sulfur__1c15ec80.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_medium_with_sulfur__1c15ec80.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:015401, `marine_medium_with_sulfur`, and `mediadive.medium:J375` agree on the intended source: JCM Medium 375, `MARINE MEDIUM WITH SULFUR`.
- MediaDive and the live JCM page agree on pH 6.0 and on all ten non-water ingredient amounts.
- NaCl, MgCl2 x 6 H2O, KCl, NH4Cl, NaNO3, KH2PO4, MES, CaCl2 x 2 H2O, and Na2S x 9 H2O are grounded to terms matching the JCM formulas.
- The 5 g/L `Sulfur` row is grounded to `CHEBI:26833`, `sulfur atom`. JCM describes a bulk sulfur addition that must be steamed for sterilization, not an atom-level chemical entity.

## Evidence

- JCM Medium 375 and MediaDive J375 support the 30 g NaCl, 3 g MgCl2 x 6 H2O, 0.5 g KCl, 0.5 g NH4Cl, 1 g NaNO3, 0.2 g KH2PO4, 1.95 g MES, 0.15 g CaCl2 x 2 H2O, 5 g sulfur, and 0.5 g Na2S x 9 H2O rows.
- JCM and MediaDive both list 1 L or 1000 ml distilled water after the sodium sulfide row; neither the generated YAML nor data/normalized_yaml/specialized/marine_medium_with_sulfur.yaml includes that row.
- The generated preparation step preserves the source handling of sulfur, the 5% Na2S x 9 H2O solution under N2, H2-CO2 distribution and pressurization, and pH 6.0 adjustment.
- No target organism or primary growth claim is asserted by this record.

## Completeness

- The formulation is materially incomplete until the 1 L distilled-water row is restored.
- The source's use of 5% Na2S x 9 H2O as a neutralized sterile solution is present in prose but not modeled as a stock solution. Because the table also gives the final 0.5 g/L sodium sulfide nonahydrate amount, this is a procedural rather than arithmetic defect.
- No target organism, incubation temperature, or growth result is asserted. Those absent optional slots are acceptable for this JCM formulation record.
- Exact gitignore-independent searches were run for `CultureMech:015401`, `marine_medium_with_sulfur`, `mediadive.medium:J375`, `JCM Medium 375`, and the merge fingerprint across the scoped specialized normalized YAML directory, this target merged YAML, and the specialized and recipe index files with `--no-ignore --hidden`; the searches found the maintained input, generated target, and expected index entries.
- An exact `find data/merge_yaml/merged -maxdepth 1 -name 'marine_medium_with_sulfur*.yaml' -print` search, which includes ignored files, found only this generated target.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_medium_with_sulfur__1c15ec80.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The final distilled-water row is missing. | JCM Medium 375 lists 1.0 L Distilled water, and MediaDive J375 lists 1000 ml Distilled water in `Main sol. J375`; the YAML has no water ingredient. | data/normalized_yaml/specialized/marine_medium_with_sulfur.yaml and the MediaDive importer |
| major | Bulk sulfur is grounded to an atom-level ChEBI term. | JCM instructs curators to steam the sulfur before adding it to culture vessels, but the YAML maps `Sulfur` to `CHEBI:26833`, `sulfur atom`. | data/normalized_yaml/specialized/marine_medium_with_sulfur.yaml |

## Recommended Edits

1. Add the missing 1000 ml distilled-water row to data/normalized_yaml/specialized/marine_medium_with_sulfur.yaml.
2. Replace the sulfur atom grounding with the exact repository-accepted term for bulk elemental sulfur, or leave sulfur explicitly ungrounded if no exact term exists.
3. Regenerate `data/merge_yaml/merged/` and verify the J375 output still has the same one-source identity and pH 6.0.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against the live JCM Medium 375 page and MediaDive J375 REST payload.
- Run open schema, strict schema, reference, and term validation on the maintained specialized input and regenerated merge.
- Confirm the regenerated output contains 1000 ml distilled water and no `CHEBI:26833` grounding on the sulfur row.

## Additional Notes

- None found.
