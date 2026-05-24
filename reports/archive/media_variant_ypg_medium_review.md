# YPG Medium Variant Review

Date: 2026-05-13

## Decision

Applied parent/child `MediaRecipe` links for two source-duplicate YPG medium
pairs:

| Parent path | Child path | Relationship |
|---|---|---|
| `data/normalized_yaml/bacterial/DSMZ_1172_YPG_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_1172_YPG_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ypg_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1017_YPG_medium.yaml` | `SOURCE_DUPLICATE` |

These were kept as two parent groups rather than one broad YPG family because
DSMZ/KOMODO medium 1172 is a low-concentration YPG formulation, while
DSMZ/KOMODO medium 1017 is a high-glucose YPG formulation.

## Evidence From Local Records

- DSMZ Medium 1172 and KOMODO Medium 1172 both use 1 g/L yeast extract, 1 g/L
  peptone, 1 g/L glucose, and 15 g/L agar, with pH range 5.6-6.0.
- DSMZ Medium 1017 and KOMODO Medium 1017 both use 10 g/L yeast extract, 10
  g/L peptone, 70 g/L glucose, and 15 g/L agar at pH 6.0.
- KOMODO Medium 1017 additionally records HCl as a variable pH-adjuster
  extracted from source notes; this is not treated as a separate formulation.
- JCM Medium J404, NBRC YPG Medium, BCYE-like YPG derivatives, and NaCl-YPG
  derivatives were not linked in this batch because they have distinct
  ingredient identities, concentrations, salt additions, or source families.

## Validation

- Applied actions:
  - `add_variant_child`: 2
  - `add_parent_media`: 2
  - `set_variant_relationship`: 2
  - `add_variant_modification`: 2
- Targeted schema validation: 4/4 touched YPG medium YAML files passed after
  normalizing one pre-existing `curation_history` key from `date` to
  `timestamp` in `KOMODO_1017_YPG_medium.yaml`.
- Global parent/child reciprocal-link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 1,545
  - Child-to-parent links: 1,545
  - Errors: 0
  - Warnings: 0
