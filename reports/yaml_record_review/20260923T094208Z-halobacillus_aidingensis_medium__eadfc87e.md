# YAML Record Review: HALOBACILLUS AIDINGENSIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacillus_aidingensis_medium__eadfc87e.yaml
- Started UTC: 2026-09-23T09:40:23Z
- Finished UTC: 2026-09-23T09:42:08Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacillus_aidingensis_medium__eadfc87e.yaml`,
a generated `MediaRecipe` with `id: CultureMech:002795`, `category: bacterial`,
`physical_state: SOLID_AGAR`, `ph_value: 7.5`, and
`media_term.term.id: mediadive.medium:J445`.

The generated record is a single-source merge from the maintained parent
`data/normalized_yaml/bacterial/halobacillus_aidingensis_medium.yaml`, which
imports JCM Medium J445 through MediaDive. Future fixes belong in that
normalized parent or in the JCM/MediaDive importer, then require regeneration
of `data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacillus_aidingensis_medium__eadfc87e.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacillus_aidingensis_medium__eadfc87e.yaml --out /private/tmp/halobacillus_aidingensis_medium__eadfc87e.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacillus_aidingensis_medium__eadfc87e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacillus_aidingensis_medium__eadfc87e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The reviewed record denotes the right medium. Its label, source URL, pH 7.5,
solid agar state, and eight listed ingredients match JCM GRMD 445 and the
MediaDive REST mirror for JCM Medium J445.

The inorganic ingredient groundings on NaCl, KCl, `MgSO4 x 7 H2O`, trisodium
citrate, and agar preserve the source identities closely enough for this
review. Trypticase peptone, yeast extract, and peptone are undefined complex
ingredients and are correctly not forced to ChEBI terms.

Two imported product qualifiers were lost: JCM and MediaDive identify
Trypticase peptone as BD-BBL and Yeast extract as BD-Difco, but the generated
record stores them as unqualified preferred terms.

## Evidence

Supported by inspected JCM and MediaDive sources:

- JCM 445 is `HALOBACILLUS AIDINGENSIS MEDIUM`.
- The recipe is adjusted to pH 7.5.
- The final medium contains 5 g Trypticase peptone, 10 g yeast extract, 5 g
  peptone, 50 g NaCl, 2 g KCl, 20 g `MgSO4 x 7 H2O`, 3 g trisodium citrate,
  and 20 g agar per 1 L.
- Components are added to distilled water and brought to 1.0 L.

Unsupported or incomplete evidence:

- The JCM default sterilization instruction says JCM media are autoclaved at
  121 C for 15 minutes unless otherwise stated, but the generated record has no
  sterilization step.
- Distilled water appears in the preparation text but not in the ingredients
  list, so the ingredient list is incomplete for renderers that do not parse
  preparation prose.
- BD-BBL and BD-Difco qualifiers are present in both JCM and MediaDive but are
  absent from the generated ingredient names.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for MediaDive or JCM.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `mediadive.medium:J445`, `JCM Medium J445`,
  the JCM GRMD 445 URL, and the source label found the maintained JCM/MediaDive
  parent plus a separate Togo import,
  `data/normalized_yaml/bacterial/TOGO_M446_Halobacillus_Aidingensis_Medium.yaml`.

## Findings

### Blocker

None found.

### Major

1. The generated direct JCM record is incomplete: it omits distilled water as a
   component and omits the JCM default autoclaving step. Owner:
   `data/normalized_yaml/bacterial/halobacillus_aidingensis_medium.yaml` or the
   JCM/MediaDive importer.

2. The same JCM GRMD 445 recipe is split across two generated records instead
   of one canonical merge. The reviewed JCM/MediaDive path generated
   `halobacillus_aidingensis_medium__eadfc87e`, while Togo M446 generated
   `data/merge_yaml/merged/HALOBACILLUS_AIDINGENSIS_MEDIUM.yaml` from the same
   JCM source URL. Owner: the Togo/JCM duplicate matching inputs or merge
   fingerprint logic.

### Minor

1. The Trypticase peptone and yeast extract source qualifiers were dropped even
   though JCM says BD-BBL and BD-Difco. Owner:
   `data/normalized_yaml/bacterial/halobacillus_aidingensis_medium.yaml` or the
   MediaDive attribute importer.

2. First-class `sources` are absent; the JCM URL and source accession are
   present only in free-text `notes` and `media_term`. Owner: the normalized
   parent or importer.

## Recommended Edits

1. Add distilled water and the default JCM autoclaving step to the
   JCM/MediaDive normalized parent while preserving the existing pH 7.5 and
   bring-to-1-L preparation steps.
2. Preserve `Trypticase peptone (BD-BBL)` and `Yeast extract (BD-Difco)` as
   exact ingredient labels or qualifiers.
3. Link or merge the JCM/MediaDive parent with
   `TOGO_M446_Halobacillus_Aidingensis_Medium.yaml`; before merging, repair the
   Togo water unit from `1 G_PER_L` to a volume-to-1-L representation and carry
   over its missing pH/preparation facts from Togo's own API comments.
4. Add first-class source entries for JCM GRMD 445 and MediaDive J445 if the
   importer supports them.
5. Regenerate merge products after the normalized inputs or duplicate rules are
   corrected.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/halobacillus_aidingensis_medium.yaml` and
  `data/normalized_yaml/bacterial/TOGO_M446_Halobacillus_Aidingensis_Medium.yaml`
  after any edit.
- Re-run the JCM GRMD 445 fetch and the Togo M446 API fetch to verify product
  qualifiers, pH, amounts, and comments against the maintained inputs.
- Run the merge freshness and duplicate-audit checks that cover
  `data/merge_yaml/merged/` to ensure the JCM and Togo imports collapse into
  one canonical record when their ingredient sets are reconciled.

## Additional Notes

The first direct JCM fetch failed with sandbox DNS resolution for
`www.jcm.riken.jp`; the same URL was fetched successfully with an escalated
`curl -L`.
