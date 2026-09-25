# YAML Record Review: m_tge_gp_medium

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml`
- Started UTC: `2026-09-23T22:31:10Z`
- Finished UTC: `2026-09-23T22:31:11Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:003197` |
| Record name | `m_tge_gp_medium` |
| Original name | `m TGE-GP MEDIUM` |
| Source accession | `mediadive.medium:J851` |
| Source label | `m TGE-GP MEDIUM` |
| Original source | JCM Medium 851 |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/m_tge_gp_medium.yaml` |
| Generated record | `data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml` |

`data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml` is a generated merge
from an older state of `data/normalized_yaml/bacterial/m_tge_gp_medium.yaml`
with fingerprint `acb4df1dfe69612c0f56127025d4ba612bac6f6ed842d79669facf544537e9c9`.
The maintained normalized input has since been repaired.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml` | Passed; `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml --out /private/tmp/m_tge_gp_medium__acb4df1d.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/m_tge_gp_medium__acb4df1d.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct at the medium level: `CultureMech:003197`,
  `media_term.term.id: mediadive.medium:J851`, and JCM `GRMD=851` all denote
  m TGE-GP Medium.
- An ignored-file-inclusive exact search for `CultureMech:003197`,
  `mediadive.medium:J851`, and the `acb4df1d...` merge fingerprint across
  `data/normalized_yaml`, `data/merge_yaml`, `reports`, `src`, `tests`,
  `conf`, `scripts`, `.claude`, `pyproject.toml`, `justfile`, and `README.md`
  found one live maintained input at
  `data/normalized_yaml/bacterial/m_tge_gp_medium.yaml`; the older
  `JCM_J851_m_TGE-GP_MEDIUM.yaml` name appeared only in archived validation
  reports.
- The inspected JCM `GRMD=851` source identifies this recipe as a supplemented
  variant of JCM Medium 795 with 5.0 g/L final glycerol and 0.1 mM final
  `KH2PO4`.
- The generated merge misstates the relationship to JCM 795. It records the
  parent broth as a `SOURCE_DUPLICATE` child and as a synonym, even though JCM
  851 is a supplemented variant of JCM 795 rather than a duplicate of it.

## Evidence

- JCM `GRMD=851` supports four material components for the final recipe:
  18 g/L `Bacto m TGE broth (BD-Difco)` and 1 L distilled water from JCM 795,
  plus 5.0 g/L glycerol and 0.1 mM final `KH2PO4` from JCM 851.
- The generated merge keeps only a generic `Bacto m TGE broth` 18 `G_PER_L`
  ingredient. It omits distilled water, glycerol, and `KH2PO4`.
- The generated merge preserves the JCM 851 instruction as prose in
  `preparation_steps`, but that prose does not compensate for the missing
  structured glycerol and phosphate rows.
- `data/normalized_yaml/bacterial/m_tge_gp_medium.yaml` has already been
  source-repaired with the JCM 795 base rows, 5.0 `G_PER_L` glycerol,
  0.1 `MILLIMOLAR` `KH2PO4`, references to JCM 851 and JCM 795, and
  `parent_media` metadata marking the JCM 795 broth as a supplemented parent.

## Completeness

- Consequentially incomplete: the generated record lacks three of the four
  formula rows now present in the maintained input.
- Consequentially incomplete: the generated record lacks the source references
  and supported parent-media relationship now present in the maintained input.
- Empty optional target-organism and growth-evidence fields were not treated
  as defects; JCM 851 is a recipe source, not primary growth evidence for a
  named target organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale and omits source-repaired ingredients. | The maintained normalized record has JCM 795 water, 5.0 g/L glycerol, and 0.1 mM `KH2PO4`; the generated merge has only 18 g/L Bacto m TGE broth. | Regenerate `data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml` from `data/normalized_yaml/bacterial/m_tge_gp_medium.yaml`. |
| Major | The generated merge still marks JCM 795 as a source duplicate of JCM 851. | JCM 851 says to use JCM 795 with glycerol and phosphate supplements, so the correct relationship is `SUPPLEMENTED_VARIANT`, as already represented in the repaired normalized input. | Regenerate from the repaired normalized input and ensure merge logic does not collapse supplemented variants into source duplicates. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so this generated JCM 851 record
   carries the repaired JCM 795 base, glycerol, phosphate, JCM references, and
   `SUPPLEMENTED_VARIANT` parent-media relationship.
2. Audit the merge step that produced fingerprint
   `acb4df1dfe69612c0f56127025d4ba612bac6f6ed842d79669facf544537e9c9` and
   ensure a supplemented JCM 851 child is not collapsed with JCM 795 as a
   source duplicate.

## Follow-up Checks

- Run open-schema validation for the regenerated merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml`.
- Run strict validation for the regenerated merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml --out /private/tmp/m_tge_gp_medium__acb4df1d.strict.tsv --workers 1 --quiet`.
- Run reference and term validation on the regenerated merge to verify the
  restored JCM references and `MILLIMOLAR` phosphate row.
- Manually compare the regenerated record against JCM `GRMD=851` and `GRMD=795`
  and verify that the base medium plus glycerol and final 0.1 mM `KH2PO4`
  supplement are present as structured ingredients.

## Additional Notes

- The focused validators pass because a stale generated merge with missing
  ingredients can still satisfy the LinkML schema.
