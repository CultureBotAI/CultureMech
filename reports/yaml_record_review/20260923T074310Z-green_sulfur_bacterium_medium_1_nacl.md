# YAML Record Review: green_sulfur_bacterium_medium_1_nacl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/green_sulfur_bacterium_medium_1_nacl.yaml
- Started UTC: 2026-09-23T07:41:16Z
- Finished UTC: 2026-09-23T07:43:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:008466` |
| Name | `green_sulfur_bacterium_medium_1_nacl` |
| Original name | `Green Sulfur Bacterium Medium (1% NaCl)` |
| Category | `bacterial` |
| Canonical media term | `TOGO:M1891` |
| Merged sources | `green_sulfur_bacterium_medium_1_nacl` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/green_sulfur_bacterium_medium_1_nacl.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/green_sulfur_bacterium_medium_1_nacl.yaml --out /private/tmp/green_sulfur_bacterium_medium_1_nacl.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/green_sulfur_bacterium_medium_1_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/green_sulfur_bacterium_medium_1_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is the single Togo/NBRC M1891 import. A gitignore-independent exact search for `TOGO:M1891`, `green_sulfur_bacterium_medium_1_nacl`, and `Green Sulfur Bacterium Medium (1% NaCl)` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the expected normalized parent, this generated record, and source index references.

Several salts are narrowly grounded, but `CoCl2 x 6H2O` and `NiCl2 x 6H2O` are grounded to anhydrous salts, and generic `Fructose` is grounded to `beta-D-fructofuranose`.

## Evidence

Togo M1891 has a main medium with basal salts, 1 L Distilled water, and 5 ml Ferric citrate solution, 2 ml Vitamin B12 solution, 2 ml Trace element solution SL-6, 10 ml Acetate solution, and 0.6 g neutralized Na2S x 9H2O as supplemental additions. It also has separate SL-6, Acetate, and neutralized sulfide stock recipes, each with its own 1 L Distilled water row.

The generated record is stale relative to the normalized parent repaired on 2026-09-02: its Distilled water row is still `4.0 G_PER_L`, which is the sum of the four source 1 L water rows. The record also flattens SL-6, Acetate solution, and neutralized sulfide ingredients into the top-level formula; sums stock Ammonium acetate at 25 g/l with the main-medium 0.5 g/l row; and keeps five empty `Unknown solution` entries whose final additions are encoded as `G_PER_L` even when the source additions are milliliters.

## Completeness

The single-source identity is sound, but the formula is not complete enough for M1891 while stock ingredients are flattened, water rows are summed, solution additions have mass units, and the source preparation comments are absent from structured steps. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Multiple stocks were flattened into top-level final ingredients. | SL-6, Acetate solution, and neutralized Na2S x 9H2O stock contents appear as ordinary ingredients; `Ammonium acetate` is summed from the main 0.5 g row and the 25 g/l Acetate stock row. | Togo M1891 stock and subcomponent normalization. |
| Major | The generated water concentration is a stale summed duplicate. | M1891 has four scoped 1 L water rows; the generated record still shows one `4.0 G_PER_L` Distilled water row even though the normalized parent was repaired to `1.0` on 2026-09-02. | Generated merge refresh for repaired Togo parents. |
| Major | Final stock additions are misunitized as mass concentrations. | M1891 adds 5 ml Ferric citrate solution, 2 ml Vitamin B12 solution, 2 ml SL-6, and 10 ml Acetate solution; generated `solutions` encode those as `5`, `2`, `2`, and `10` `G_PER_L` with empty `Unknown solution` composition. | Togo solution migration. |
| Major | Source preparation steps are missing. | Togo M1891 specifies mixing before Vitamin B12, Acetate, NaHCO3, and Na2S x 9H2O, autoclaving under N2/CO2, aseptic additions, Acetate pH 7.2 preparation, and neutralized sulfide pH adjustment; the generated record has no `preparation_steps`. | Togo comment-to-step normalization. |
| Major | Hydrate-specific cobalt and nickel chlorides are grounded to anhydrous salts. | The SL-6 source rows are CoCl2 x 6H2O and NiCl2 x 6H2O; the generated CHEBI labels are `cobalt dichloride` and `nickel dichloride`. | CHEBI grounding for hydrate-specific salts. |

## Recommended Edits

1. Rebuild M1891 from the repaired normalized parent before making further merge decisions.
2. Keep the main medium, SL-6, Acetate solution, and neutralized sulfide solution in separate scoped recipes.
3. Encode Ferric citrate solution, Vitamin B12 solution, SL-6, Acetate solution, and neutralized sulfide solution with their source quantities and volume units.
4. Preserve each 1 L Distilled water row in its own solution scope instead of summing water across stock recipes.
5. Convert Togo source comments into preparation steps for the anaerobic gas, autoclaving, aseptic-addition, acetate-stock, and sulfide-neutralization instructions.
6. Reground CoCl2 x 6H2O and NiCl2 x 6H2O to hydrate-specific CHEBI terms if available.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated M1891 record.
- Compare regenerated source scopes against the Togo M1891 API payload.
- Confirm the final medium no longer contains SL-6, Acetate, or sulfide stock contents as top-level final ingredients.
- Re-run the exact gitignore-independent search for `TOGO:M1891`, `green_sulfur_bacterium_medium_1_nacl`, and `Green Sulfur Bacterium Medium (1% NaCl)` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the single-source grouping still holds.

## Additional Notes

None found.
