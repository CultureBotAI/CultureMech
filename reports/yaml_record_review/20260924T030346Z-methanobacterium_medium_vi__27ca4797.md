# YAML Record Review: METHANOBACTERIUM MEDIUM (VI)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml
- Started UTC: 2026-09-24T03:03:13Z
- Finished UTC: 2026-09-24T03:03:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002222 |
| Label | methanobacterium_medium_vi |
| Original label | METHANOBACTERIUM MEDIUM (VI) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml` |
| Maintained owners | `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml`; `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml` |
| Merge lineage | `methanobacterium_medium_iv`; `methanobacterium_medium_vi` |
| Source identity | MediaDive `J872` / JCM Medium 872 merged with MediaDive `J1038` / JCM Medium 1038 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml --out /private/tmp/methanobacterium_medium_vi__27ca4797.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record conflates two different JCM recipes. The primary `media_term` and stable ID are for MediaDive J1038 / JCM Medium 1038, which JCM and MediaDive define as Medium 872 with final 0.4 g/l NaCl plus an optional human-fecal-extract replacement for sludge fluid. `merged_from` also includes MediaDive J872 / JCM Medium 872, whose formula has 5 g NaCl and no fecal-extract alternative.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M1103`, `JCM_M1038`, `GRMD=1038`, and `mediadive.medium:J1038` found the J1038 owner at `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml` and its TOGO M1103 duplicate. Direct `find` searches under `data/normalized_yaml` for `*/methanobacterium_medium_iv.yaml` and `*/methanobacterium_medium_vi.yaml` found only the `archaea/` owners, so the generated `parent_media.path: data/normalized_yaml/bacterial/methanobacterium_medium_iv.yaml` and the J872 owner's symmetric `variant_children` path do not resolve.

## Evidence

JCM 1038 does not support the published NaCl amount. JCM 1038 and MediaDive J1038 say to use Medium 872 with final 0.4 g/l NaCl, but the generated record publishes the MediaDive J872 final concentration `4.89237 G_PER_L`, plus an unrelated LB Medium sodium chloride row at `10.0 G_PER_L`.

The J872/J1038 stock boundaries are absent. HCl and FeCl2 x 4 H2O from MediaDive solution 3846, trace salts from solution 3847, sludge-fluid ingredients from solution 208, fatty-acid members from solution 3954, and 5% cysteine and sulfide stock additions all appear as final-medium ingredients.

Unrelated LB Medium rows are present. Tryptone, an LB yeast-extract row, and an LB sodium-chloride row carry `LB Medium (Luria-Bertani, Miller formulation)` supplier notes, but none of those rows appear in JCM Medium 872 or 1038, TOGO M911 or M1103, or MediaDive J872 or J1038.

The MediaDive fatty-acid mixture was copied incompletely. MediaDive solution 3954 contains valeric acid, isovaleric acid, alpha-Methylbutyric acid, and isobutyric acid at 0.5 g in a 20 ml stock; the generated record has valeric, isovaleric, and isobutyric acids, but no alpha-Methylbutyric acid row.

The J1038-specific human-fecal-extract alternative is present only as a mandatory-looking `preparation_steps` entry. It is not scoped as an alternative to the sludge-fluid addition, and the copied `ph_value: 7.1` is not a final-medium pH: it comes from the 7.0-7.2 pH adjustment of the optional extract supernatant.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. JCM 872, JCM 1038, and their MediaDive and TOGO records are source formulations, not primary growth studies.

This merged record needs more than stock repair. J872 and J1038 need to be split or represented as a parent and a true low-NaCl variant, and the LB Medium rows need to be removed from the JCM formulation entirely.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The merge conflates JCM Medium 872 and JCM Medium 1038 as source duplicates. | JCM 1038 is defined as Medium 872 with final 0.4 g/l NaCl; J872 uses 5 g NaCl in 930 ml water. They are variants, not identical source records. | Merge/de-duplication logic and `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml`. |
| blocker | The generated J1038 record publishes the wrong NaCl concentration. | The J1038 source says final 0.4 g/l NaCl, while the generated record keeps J872's `4.89237 G_PER_L` MediaDive final concentration and also carries an LB Medium `10.0 G_PER_L` sodium-chloride row. | `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml` and the copied J872 composition. |
| blocker | The generated variant metadata points to non-existent bacterial paths. | Gitignore-independent `find` checks under `data/normalized_yaml` found only `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml` and `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml`, but the owner records point at `data/normalized_yaml/bacterial/...`. | Variant-link curation for `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml` and `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml`. |
| major | Unrelated LB Medium ingredients contaminate the JCM recipe. | Tryptone, LB yeast extract, and LB sodium chloride rows with LB Miller supplier notes are not present in any inspected JCM, TOGO, or MediaDive source for J872 or J1038. | `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml`; the J1038 owner copied them from J872. |
| major | MediaDive stocks were flattened into final-medium ingredients. | FeCl2 solution 3846, trace element solution 3847, sludge fluid 208, fatty-acid mixture 3954, and the 5% sulfide and cysteine additions are all represented as top-level `ingredients`. | `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml`; J1038 copied the flattened parent. |
| major | The fatty-acid mixture was copied incompletely. | MediaDive solution 3954 includes alpha-Methylbutyric acid; the generated record has the other three fatty-acid rows but omits that source component. | `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml`; J1038 copied the incomplete parent. |
| major | The human-fecal-extract alternative is scoped incorrectly. | The JCM 1038 text says sludge fluid can be replaced with a prepared human fecal extract; the generated record emits the extract preparation as a normal `AUTOCLAVE` step and stores the extract pH adjustment as `ph_value: 7.1`. | `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml`, or the MediaDive step importer. |

## Recommended Edits

1. Split J872 and J1038 out of the `SOURCE_DUPLICATE` merge and represent J1038 as a low-NaCl variant of the J872 parent.
2. Correct J1038 NaCl to final 0.4 g/l and prevent the J872 4.89237 g/l NaCl row from overriding it.
3. Repair the `parent_media` and `variant_children` paths to point at the `data/normalized_yaml/archaea/` owners.
4. Remove the LB Medium tryptone, yeast-extract, and sodium-chloride rows from the J872 and J1038 normalized owners.
5. Rebuild the inherited J872 composition with structured FeCl2, trace element, sludge-fluid, fatty-acid, sulfide, and cysteine stock additions.
6. Restore alpha-Methylbutyric acid to the fatty-acid stock and scope the optional human-fecal-extract preparation as a sludge-fluid alternative, not as a final-medium autoclave step.
7. Regenerate `data/merge_yaml/merged/methanobacterium_medium_vi__27ca4797.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against both corrected MediaDive owners and regenerated merged files.
2. Compare the regenerated J1038 record against JCM 1038 and MediaDive J1038 to confirm it has final 0.4 g/l NaCl, not J872's 5 g NaCl parent composition.
3. Re-run exact duplicate searches for `mediadive.medium:J872`, `mediadive.medium:J1038`, `GRMD=872`, and `GRMD=1038` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated pages to confirm J872 and J1038 are separate parent/variant records and neither page displays LB Medium rows.

## Additional Notes

None found.
