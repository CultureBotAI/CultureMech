# YAML Record Review: ELBE Methanotroph Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/elbe_methanotroph_medium__0f131258.yaml
- Started UTC: 2026-09-22T23:55:00Z
- Finished UTC: 2026-09-23T00:01:00Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/elbe_methanotroph_medium__0f131258.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:007820`
- Name: `elbe_methanotroph_medium`
- Original label: `ELBE Methanotroph Medium`
- Category: `bacterial`
- Medium term: `TOGO:M1286`
- Generated status: generated merge record with fingerprint `0f131258acee0a0f28ad8ed454e3a7d830407739477d38dd6e921f5efca8f445`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/TOGO_M1286_ELBE_Methanotroph_Medium.yaml`

This generated record is also stale relative to its maintained normalized owner: `TOGO_M1286_ELBE_Methanotroph_Medium.yaml` added a CHEBI grounding for `methane` on August 20, 2026, while the reviewed merge product was generated on August 6.

## Validation

Focused validation was clean.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/elbe_methanotroph_medium__0f131258.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/elbe_methanotroph_medium__0f131258.yaml --out /private/tmp/elbe_methanotroph_medium__0f131258.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/elbe_methanotroph_medium__0f131258.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/elbe_methanotroph_medium__0f131258.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the run emitted the expected `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

TOGO M1286 is JCM Medium 1200 rendered as the solid ELBE Methanotroph Medium path: the JCM 1200 source says to add 15.0 g/L agar before autoclaving for solid medium, and TOGO distinguishes M1286 from the liquid M1285 by extracting an additional `agar` component from that instruction.

The reviewed record's `TOGO:M1286` identity and `SOLID_AGAR` state are therefore distinct from the liquid sibling `TOGO:M1285`. A `find data/normalized_yaml -name '*elbe*' -o -name '*Elbe*' -o -name '*ELBE*'` search, which includes ignored files, found both TOGO siblings and a direct MediaDive/JCM `elbe_methanotroph_medium.yaml` record for `mediadive.medium:J1200`.

The sodium nitrate, potassium chloride, calcium chloride dihydrate, magnesium chloride hexahydrate, methane, and agar identities are chemically aligned in the maintained source record. The reviewed generated file is stale and lacks the newer methane grounding.

## Evidence

The source recipe has five simple pre-autoclave rows: 0.93 g MgCl2 x 6 H2O, 1.0 g KCl, 0.12 g CaCl2 x 2 H2O, 0.17 g NaNO3, and 992 ml distilled water. For solid medium, 15.0 g/L agar is added before autoclaving. After cooling to 55C, the medium receives 5.0 ml of 2 M HEPES buffer at pH 7.0, 0.15 ml of 1 M phosphate buffer, 1.0 ml FeCl2 solution, 1.0 ml trace element solution, and 1.0 ml filter-sterilized vitamin solution. The culture tubes should have more than 80 percent gas phase, then methane is added to 50 percent of the gas phase by volume.

The reviewed M1286 record keeps the four salts and water but loses or distorts most post-autoclave additions:

- `2 M HEPES buffer (pH 7.0)` is recorded as `5 G_PER_L`, not as 5 ml of a 2 M buffer.
- 1 M phosphate buffer, FeCl2 solution, trace element solution, and vitamin solution are empty solution shells with `G_PER_L` units instead of 0.15 ml, 1 ml, 1 ml, and 1 ml additions.
- The required 15.0 g/L agar is represented by a schema-defaulted `variable` concentration.
- Methane is represented as a variable soluble ingredient rather than as a 50 percent gas-phase condition.
- The generated record lacks the maintained methane CHEBI term because it predates the August 20 MIM grounding update.

## Completeness

The normalized TOGO record has enough source metadata to recover JCM 1200, but the structured recipe is incomplete. It leaves every referenced post-autoclave stock empty even though JCM 1200 links the phosphate and vitamin stocks through Medium 556 and the FeCl2 and trace-element stocks through Medium 187.

Empty organism-growth claims, DOI, PMID, and target organism lists are not defects for this imported TOGO recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | The 15 g/L agar addition that defines M1286 as the solid JCM 1200 variant is missing. | JCM 1200 says to add 15.0 g/L agar before autoclaving for solid medium; TOGO M1286 captured an agar row, but the reviewed record has a schema-defaulted `variable` concentration. | `data/normalized_yaml/bacterial/TOGO_M1286_ELBE_Methanotroph_Medium.yaml` |
| major | Post-autoclave buffer and stock additions are represented with mass units and no composition. | JCM 1200 adds 5 ml HEPES buffer, 0.15 ml phosphate buffer, 1 ml FeCl2 solution, 1 ml trace element solution, and 1 ml vitamin solution after cooling; the reviewed record has `5 G_PER_L` HEPES and four empty `solutions` entries with `G_PER_L` units. | `data/normalized_yaml/bacterial/TOGO_M1286_ELBE_Methanotroph_Medium.yaml` |
| major | Methane is modeled as an undefined ingredient instead of a gas-phase condition. | JCM 1200 says to leave more than 80 percent gas phase and add methane to 50 percent of the gas phase by volume; the reviewed record has `methane` with `value: variable`, `unit: VARIABLE`. | `data/normalized_yaml/bacterial/TOGO_M1286_ELBE_Methanotroph_Medium.yaml` |
| minor | The generated merge product is stale relative to its normalized source. | The maintained `TOGO_M1286_ELBE_Methanotroph_Medium.yaml` added `CHEBI:16183` for methane on August 20, 2026; the August 6 merge output lacks that term. | generated merge artifacts |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M1286_ELBE_Methanotroph_Medium.yaml`, replace the variable agar row with the JCM-supported 15 g/L agar addition.
2. Store 5 ml HEPES buffer, 0.15 ml 1 M phosphate buffer, 1 ml FeCl2 solution, 1 ml trace element solution, and 1 ml vitamin solution as post-autoclave additions with volume units; populate the cross-referenced stock compositions from JCM Medium 556 and Medium 187.
3. Move methane from `ingredients` into a preparation or atmosphere/gas-phase representation that preserves 50 percent by volume in a greater-than-80-percent tube headspace.
4. Regenerate merged YAML so the newer methane CHEBI grounding is not lost.

## Follow-up Checks

1. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/elbe_methanotroph_medium__0f131258.yaml`.
2. Reopen JCM 1200, TOGO M1286, JCM 556, and JCM 187 and manually verify agar, HEPES, phosphate buffer, FeCl2 solution, trace element solution, vitamin solution, and methane are modeled in the same preparation phases as the source.
3. Compare the regenerated M1286 output with the next M1285 liquid sibling and confirm the only solid-specific difference is the 15 g/L agar addition.

## Additional Notes

- JCM 1200 names the phosphate and vitamin stock source as Medium 556, while the TOGO API labels those cross-references as Medium M560; likewise JCM 1200 points to Medium 187 where TOGO labels Medium M180. The reviewed record follows the TOGO labels.
