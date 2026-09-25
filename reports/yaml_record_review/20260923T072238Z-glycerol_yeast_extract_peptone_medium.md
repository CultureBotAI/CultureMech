# YAML Record Review: glycerol_yeast_extract_peptone_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_yeast_extract_peptone_medium.yaml
- Started UTC: 2026-09-23T07:21:30Z
- Finished UTC: 2026-09-23T07:22:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:010454` |
| Name | `glycerol_yeast_extract_peptone_medium` |
| Original name | `Glycerol-Yeast extract-Peptone Medium` |
| Category | `fungal` |
| Canonical media term | `mediadive.medium:1484` |
| Merged sources | `glycerol_yeast_extract_peptone_medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_yeast_extract_peptone_medium.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_yeast_extract_peptone_medium.yaml --out /private/tmp/glycerol_yeast_extract_peptone_medium.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_yeast_extract_peptone_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_yeast_extract_peptone_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is a single-source MediaDive import of DSMZ Medium 1484.

A gitignore-independent exact search for `CultureMech:010454`, `mediadive.medium:1484`, `DSMZ_Medium1484`, and `glycerol_yeast_extract_peptone_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected maintained parent, this generated record, and source indexes.

Most CHEBI grounding is narrow and matches DSMZ 1484 or the DSMZ medium 141 stock solutions. The exception is `NiCl2 x 6 H2O`, which is grounded to an anhydrous nickel dichloride term rather than to the hexahydrate named by DSMZ.

## Evidence

DSMZ Medium 1484 lists, per final liter, 3 g Bacto-peptone, 5 g Yeast extract, 1.25 g Betaine, 1.25 g Sodium pyruvate, optional 15 g Agar for solid medium, 10 ml Trace element solution from DSMZ medium 141, 10 ml Vitamin solution from DSMZ medium 141, 10 ml Glycerol, and 970 ml Distilled water, then pH 7.2.

MediaDive 1484 resolves the DSMZ 141 references to 10 ml/l Modified Wolin's mineral solution and 10 ml/l Wolin's vitamin solution. The generated record expands the ingredients of both 1 L stock solutions as if they were added directly to the final liter, omits the 10 ml/l stock rows, omits all stock-water rows, and omits the 970 ml final Distilled water row.

The generated record also converts the 10 ml Glycerol source volume into `10 G_PER_L`, even though the source unit is a volume. Agar is conditional in the source but the record is typed as `SOLID_AGAR` and contains agar as an ordinary ingredient row.

## Completeness

The record is not complete enough to use for DSMZ 1484 because the two DSMZ 141 stock additions are flattened at stock strength, glycerol has the wrong unit semantics, water is missing, and optional agar has become mandatory. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The 10 ml/l vitamin and trace-element stocks are flattened at 100x the final concentration. | DSMZ 1484 adds 10 ml each of Wolin's vitamin solution and Modified Wolin's mineral solution from DSMZ 141 per final liter; generated vitamin and mineral rows keep the 1 L stock concentrations such as 0.002 g/l Biotin and 1.5 g/l nitrilotriacetic acid. | MediaDive importer solution expansion for DSMZ 1484. |
| Major | Source water rows and stock identities are missing. | DSMZ 1484 has 970 ml final Distilled water plus 1 L water inside each DSMZ 141 stock; the generated record has no Distilled water row and no rows for the 10 ml/l stock additions. | MediaDive importer solution migration. |
| Major | Glycerol has a mass unit even though the DSMZ source uses a volume. | DSMZ 1484 and MediaDive 1484 list 10 ml Glycerol; the generated row is `10 G_PER_L`. | MediaDive importer unit conversion for ml compound rows. |
| Major | Conditional agar has been made mandatory. | DSMZ 1484 lists 15 g agar only for solid medium; the generated record has `physical_state: SOLID_AGAR` and an ordinary 15 g/l Agar ingredient. | MediaDive importer optional-condition handling. |
| Major | Nickel chloride hexahydrate is grounded to the anhydrous salt. | The Modified Wolin's mineral solution source row is `NiCl2 x 6 H2O`; the generated CHEBI term is `CHEBI:34887` / `nickel dichloride`. | CHEBI grounding for hydrate-specific salts. |

## Recommended Edits

1. Model `Modified Wolin's mineral solution` and `Wolin's vitamin solution` as 10 ml/l stock additions and keep their ingredient tables scoped to the stock recipes.
2. Restore the 970 ml/l final Distilled water row and stock-water rows.
3. Preserve the DSMZ source unit for Glycerol as 10 ml/l, or convert it with density rather than treating 10 ml as 10 g.
4. Represent the 15 g/l Agar row as a solid-medium option instead of making DSMZ 1484 intrinsically `SOLID_AGAR`.
5. Reground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term if one is available.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the repaired record.
- Compare the regenerated formula against the DSMZ Medium 1484 PDF and the MediaDive 1484 JSON.
- Check that the 10 ml/l DSMZ 141 stock additions dilute vitamin and trace-element ingredients by a factor of 100.
- Re-run the exact gitignore-independent search for `CultureMech:010454`, `mediadive.medium:1484`, `DSMZ_Medium1484`, and `glycerol_yeast_extract_peptone_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify no unexpected duplicates were introduced.

## Additional Notes

None found.
