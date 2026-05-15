# Same-Name Duplicate And Agar Variant Review

Date: 2026-05-14

## Scope

Reviewed three low-cardinality same-name media pairs where the YAML showed
either exact duplicate source formulations or one clear agar concentration
axis. The selected records were modeled as source duplicates or child variants
under a shared parent medium.

## Applied Decisions

| Parent | Child | Relationship | Difference |
|---|---|---|---|
| `data/normalized_yaml/bacterial/dubos_salts_medium.yaml` | `data/normalized_yaml/bacterial/JCM_J155_DUBOS_SALTS_MEDIUM.yaml` | `SOURCE_DUPLICATE` | Same Dubos Salts Medium ingredient and concentration signature; pH 7.2 and agar state match |
| `data/normalized_yaml/bacterial/tua_acetobacter_medium.yaml` | `data/normalized_yaml/bacterial/JCM_J709_TUA_ACETOBACTER_MEDIUM.yaml` | `SOURCE_DUPLICATE` | Same TUA Acetobacter formulation with only import rounding-scale differences |
| `data/normalized_yaml/bacterial/JCM_J104_SUCROSE-BENNETT_S_AGAR.yaml` | `data/normalized_yaml/bacterial/sucrose_bennetts_agar.yaml` | `CONCENTRATION_VARIANT` | Agar increases from 15 g/L to 20 g/L while yeast extract, beef extract, N-Z amine, and sucrose remain unchanged |

## Deferred

- TSBY Salt Medium and Marinitoga same-name candidates were deferred because
  they contain larger concentration differences across reducing agents or salt
  components.
- Leibovitz L-15 with FBS and NaCl was deferred because source normalization
  differences obscure the concentration comparison.

## Validation

- `just apply-media-variant-links --proposals /tmp/same_name_duplicate_agar_variant_links.tsv`
- `just apply-media-variant-links --proposals /tmp/same_name_duplicate_agar_variant_links.tsv --apply`
- Targeted `just validate-schema` passed for all 6 touched YAML files.
- `just validate-media-variant-links` scanned 15,827 YAML records and reported
  2,329 parent-to-child links, 2,329 child-to-parent links, 0 errors, and
  0 warnings.
