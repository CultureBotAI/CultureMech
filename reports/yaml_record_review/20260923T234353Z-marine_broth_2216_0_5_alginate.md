# YAML Record Review: marine_broth_2216_0_5_alginate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_broth_2216_0_5_alginate.yaml
- Started UTC: 2026-09-23T23:42:42Z
- Finished UTC: 2026-09-23T23:44:02Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_broth_2216_0_5_alginate.yaml |
| Class | MediaRecipe |
| ID | CultureMech:008288 |
| Label | marine_broth_2216_0_5_alginate |
| Source identity | TOGO:M1725, Marine Broth 2216 + 0.5% Alginate, original source NBRC_M934 |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/bacterial/marine_broth_2216_0_5_alginate.yaml or TOGO import logic rather than this file |

The generated merge has a single maintained owner and no synonym collapse. Its source identity matches NBRC medium 934.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_broth_2216_0_5_alginate.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_broth_2216_0_5_alginate.yaml --out /private/tmp/marine_broth_2216_0_5_alginate.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_broth_2216_0_5_alginate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_broth_2216_0_5_alginate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- TOGO M1725 reports `Marine Broth 2216 + 0.5% Alginate`, original medium ID `NBRC_M934`, and the NBRC source URL for medium 934.
- NBRC medium 934 reports the same name and formulation: 37.4 g Bacto Marine Broth 2216, 5 g sodium alginate, 15 g agar if needed, 1 L distilled water, and `pH unadjusted`.
- The CultureMech ID, name, source accession, and original source agree.
- Sodium alginate is correctly grounded to `CHEBI:53311`, and water is correctly grounded to `CHEBI:15377`.
- Bacto Marine Broth 2216 is a commercial undefined complex component and is left ungrounded; that explicit unresolved state is acceptable. `Agar (if needed)` is also left ungrounded.

## Evidence

- The inspected NBRC 934 and TOGO M1725 pages support the Bacto Marine Broth 2216, sodium alginate, and optional agar ingredient identities and amounts.
- The distilled-water ingredient is not evidence-faithful: the source says 1 L, but the record encodes `1 G_PER_L`.
- The source comment `pH unadjusted` is present in TOGO and NBRC but absent from the YAML.
- The source says `Agar (if needed)`, but the record has no optionality marker and classifies the entire recipe as `SOLID_AGAR`.

## Completeness

- No stock solutions, target organisms, growth metrics, or strain-specific growth claims are asserted by the inspected source, so the corresponding empty slots are not defects.
- The recipe is mostly complete for its NBRC source, aside from water volume semantics, optional agar state, and the missing pH comment.
- Exact gitignore-independent searches were run for `marine_broth_2216_0_5_alginate`, `TOGO:M1725`, `NBRC_M934`, and `874094932d882518030a7b1326e7e66f6266fcfe116f27de88787b0c97794d45` across the scoped normalized bacterial YAML, merged YAML, and TOGO/bacterial/recipe index files with `--no-ignore --hidden`; the only maintained YAML owner found for this source was data/normalized_yaml/bacterial/marine_broth_2216_0_5_alginate.yaml.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_broth_2216_0_5_alginate.md' -print` search, which includes ignored files, found no pre-existing review report for this record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The distilled-water volume is encoded as a mass concentration. | NBRC 934 and TOGO M1725 list 1 L distilled water; the YAML records `value: '1'` with `unit: G_PER_L`. | data/normalized_yaml/bacterial/marine_broth_2216_0_5_alginate.yaml and the TOGO importer |
| minor | The optional agar row is not represented as optional. | NBRC 934 and TOGO M1725 name `Agar (if needed)`, but the record sets `physical_state: SOLID_AGAR` and has no per-ingredient optionality flag. | data/normalized_yaml/bacterial/marine_broth_2216_0_5_alginate.yaml |
| minor | The NBRC pH comment was dropped. | NBRC 934 and TOGO M1725 include `pH unadjusted`; the maintained and merged YAML records do not represent it. | data/normalized_yaml/bacterial/marine_broth_2216_0_5_alginate.yaml |

## Recommended Edits

1. Preserve the distilled-water amount as a 1 L volume, or otherwise represent it as a solvent volume rather than `1 G_PER_L`.
2. Mark agar as an optional solidifying addition or revise physical-state modeling so broth with optional agar is not forced to an unconditional `SOLID_AGAR`.
3. Add the source pH note `pH unadjusted` to a structured pH/preparation field or source-scoped note.

## Follow-up Checks

- Compare the repaired normalized YAML row-by-row against NBRC 934 and TOGO M1725.
- Regenerate merged recipes and confirm the output still has only `marine_broth_2216_0_5_alginate` in `merged_from`.
- Run open schema, strict schema, reference, and term validation on the maintained normalized YAML and on the regenerated merged output.

## Additional Notes

- A first accession lookup accidentally used nearby IDs from another Marine Broth record. It was discarded; the exact `--no-ignore --hidden` search with TOGO:M1725 and NBRC_M934 is the search used for ownership.
