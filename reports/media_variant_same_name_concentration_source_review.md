# Same-Name Concentration And Source Variant Review

Date: 2026-05-14

## Scope

Reviewed three small same-name media families where the parsed ingredients
support either a source-duplicate link or a concentration-variant link.

## Applied Links

| Parent | Child | Relationship | Reviewed difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/JCM_J74_NUTRIENT_AGAR.yaml` | `data/normalized_yaml/bacterial/NBRC_NUTRIENT_AGAR.yaml` | `SOURCE_DUPLICATE` | Both records contain beef extract 3 g/L, peptone 5 g/L, and agar 15 g/L; the JCM parent records pH 7.0 while the NBRC child lacks pH metadata. |
| `data/normalized_yaml/bacterial/KOMODO_756a_MIXOTROPHIC_NITROBACTER_medium.yaml` | `data/normalized_yaml/bacterial/mixotrophic_nitrobacter_medium.yaml` | `CONCENTRATION_VARIANT` | Child increases yeast extract, peptone, and sodium pyruvate from 0.15/0.15/0.055 g/L to 1.5/1.5/0.55 g/L while the remaining parsed base ingredients are unchanged; pH differs from 8.6 to 7.4. |
| `data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml` | `data/normalized_yaml/bacterial/acidimicrobium_medium.yaml` | `CONCENTRATION_VARIANT` | Child rounds the inorganic salts to the same effective levels, lowers yeast extract from 2.5 g/L to 0.25 g/L, and changes pH from 1.7 to 2.0. |

## Notes

- The Nutrient Agar pair was treated as a source duplicate because the parsed
  formulation and physical state match exactly.
- The Mixotrophic Nitrobacter and Acidimicrobium pairs were treated as
  concentration variants because they share recognizable base formulations but
  have clear concentration deltas.
- Broader or less clean salt-name candidates were left unapplied when parsed
  ingredients did not expose the named salt axis or included unrelated deltas.

## Validation

- `just apply-media-variant-links --proposals /tmp/same_name_concentration_source_review_links.tsv`
- `just apply-media-variant-links --proposals /tmp/same_name_concentration_source_review_links.tsv --apply`
- Targeted `just validate-schema` checks passed for the six touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,335 parent-to-child links, 2,335 child-to-parent links, 0 errors, and 0
  warnings.
