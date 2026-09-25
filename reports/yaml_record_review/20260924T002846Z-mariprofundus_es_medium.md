# YAML Record Review: mariprofundus_es_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/mariprofundus_es_medium.yaml`
- Started UTC: 2026-09-24T00:27:57Z
- Finished UTC: 2026-09-24T00:28:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:000728` |
| Name | `mariprofundus_es_medium` |
| Original name | `MARIPROFUNDUS (ES) MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:1267a` |
| Generated status | Generated merge output from 2026-08-06 |
| Merge fingerprint | `82539896b44eaa5cb5b845bebce47bbac5251fd2a41a3dc93512f1ecf8080db9` |
| Maintained owners | `data/normalized_yaml/bacterial/mariprofundus_es_medium.yaml`, `data/normalized_yaml/bacterial/es_medium_marine.yaml` |

The reviewed record is a generated merge of MediaDive DSMZ 1267a with a KOMODO record that claims DSMZ 1267 provenance. Both normalized inputs also flatten nested stock solutions from the DSMZ/MediaDive recipe into root gram-per-liter ingredients, so fixes belong in normalized curation and in the stale source-duplicate topology before this generated YAML is regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mariprofundus_es_medium.yaml` | Passed with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mariprofundus_es_medium.yaml --out /private/tmp/mariprofundus_es_medium.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mariprofundus_es_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mariprofundus_es_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` validators were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The representative identity is correct for MediaDive / DSMZ 1267a: `CultureMech:000728`, `mediadive.medium:1267a`, `MARIPROFUNDUS (ES) MEDIUM`, pH 6.1-6.4, and the three-layer preparation all match the inspected MediaDive 1267a REST payload and DSMZ Medium 1267a PDF.
- The `SOURCE_DUPLICATE` relation to `data/normalized_yaml/bacterial/es_medium_marine.yaml` is wrong. That KOMODO record claims `komodo.medium:1267` / DSMZ 1267 provenance, and the inspected DSMZ 1267 source is `FERRIPHASELUS (ES) MEDIUM`, not `MARIPROFUNDUS (ES) MEDIUM`.
- The DSMZ 1267 and DSMZ 1267a formulas diverge in solution A, their mineral solution, the top-layer gas atmosphere, the aliquot volumes, and the inoculation protocol. They share Wolin's vitamin solution and ferrous sulfide sludge stock recipes, but shared stocks do not make the two top-level media source duplicates.
- An exact gitignore-independent scan found `CultureMech:000728` and exact `mediadive.medium:1267a` only in the reviewed generated file, `data/normalized_yaml/bacterial/mariprofundus_es_medium.yaml`, and MediaDive indexes. A bounded exact scan found `komodo.medium:1267` only in `data/normalized_yaml/bacterial/es_medium_marine.yaml`, this generated file's synonym, and KOMODO index entries.

## Evidence

- MediaDive 1267a and DSMZ 1267a support a top-level medium assembled from 901 ml Solution A, 1 ml Solution B, and 100 ml Solution C, where Solution B is Wolin's vitamin solution and Solution C is ferrous sulfide sludge.
- The reviewed root ingredient list is unsupported because it flattens stock-solution recipes into final medium amounts. For example, 123 g/L Na2S x 9H2O is the ferrous sulfide sludge stock concentration, not the final medium concentration.
- Several root amounts are artifacts of duplicate flattening and summing. The target reports NaCl as 40.5216 g/L from 30.5216 plus 10.0, MgSO4 x 7 H2O as 37.52497 g/L from 7.52497 plus 30.0, CaCl2 x 2 H2O as 2.55383 g/L from 1.55383 plus 1.0, and FeSO4 x 7 H2O as 155.0 g/L from 1.0 plus 154.0. Those pairs are Solution A, Wolfe's mineral elixir, or FeS-sludge amounts at different preparation levels and should remain nested.
- The generated preparation prose retains real DSMZ 1267a instructions, but the `solutions` field is absent, so the prose no longer has resolvable `Solution A`, `Solution B`, `Solution C`, Wolfe's mineral elixir, Wolin's vitamin solution, or ferrous sulfide sludge objects.
- The generated synonym for `es_medium_marine` is over-scoped: DSMZ 1267 uses Modified Wolin's mineral solution from medium 141 and MES in Solution A, while DSMZ 1267a uses Wolfe's mineral elixir from medium 792 and no MES.

## Completeness

- A gitignore-independent exact field scan over the generated record and both normalized `merged_from` owners found `ph_range`, `preparation_steps`, `parent_media`, and `variant_relationship` in the direct MediaDive owner and generated target; `ph_value` and `variant_children` occur only in the KOMODO 1267 owner. It found no `sources`, `source_data`, `target_organisms`, `growth_metrics`, `references`, `sterilization`, or `solutions` in any of those exact files.
- Empty `target_organisms` and `growth_metrics` are acceptable; the DSMZ pages support recipe formulation and preparation, not a measured growth result.
- The absence of `solutions` is the main completeness failure. The source is mostly stock recipes and addition volumes, and a flat root list cannot represent the recipe without changing the final amounts.
- The legacy `mediaingredientmech_term` on the `Na2SeO4` ingredient remains while neighboring terms use `mediaingredientmech_chebi_term`, but that is secondary to the stock flattening and source-duplicate errors.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | DSMZ 1267a stock and nested solution recipes are flattened into final root ingredient amounts. | MediaDive 1267a assembles 901 ml Solution A, 1 ml Solution B, and 100 ml Solution C. The normalized and generated records instead list Wolfe's mineral elixir, Wolin's vitamin solution, and ferrous sulfide sludge components as root g/L ingredients and sum repeated salts across solution boundaries. | Rebuild `data/normalized_yaml/bacterial/mariprofundus_es_medium.yaml` with nested `solutions`; then regenerate the generated record. |
| Major | The source-duplicate edge conflates DSMZ 1267a with DSMZ 1267. | DSMZ 1267a is MARIPROFUNDUS (ES) MEDIUM; DSMZ 1267 is FERRIPHASELUS (ES) MEDIUM with a different Solution A, Modified Wolin's mineral solution, MES, top-layer gas handling, and inoculation steps. `es_medium_marine.yaml` claims KOMODO 1267 / DSMZ 1267 provenance but is merged into the DSMZ 1267a representative. | Remove or replace the `SOURCE_DUPLICATE` edge between `data/normalized_yaml/bacterial/es_medium_marine.yaml` and `data/normalized_yaml/bacterial/mariprofundus_es_medium.yaml`; if KOMODO 1267 should denote DSMZ 1267, re-curate it to the DSMZ 1267 formula instead. |

No blocker findings: the representative ID and `media_term` still identify DSMZ 1267a, and the YAML is valid.

Minor findings:

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Minor | The `Na2SeO4` ingredient still carries a legacy `mediaingredientmech_term`. | The reviewed file links most CHEBI-grounded ingredients through `mediaingredientmech_chebi_term`, but `Na2SeO4` retains `mediaingredientmech_term: MediaIngredientMech:000198`. | Normalize the slot in `data/normalized_yaml/bacterial/mariprofundus_es_medium.yaml` after the larger nested-solution repair. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/mariprofundus_es_medium.yaml` from MediaDive/DSMZ 1267a with explicit Solution A, Solution B, Solution C, Wolfe's mineral elixir, Wolin's vitamin solution, and ferrous sulfide sludge boundaries.
2. Remove root ingredient amounts that belong only to stock recipes unless a diluted final-medium amount is explicitly calculated and documented.
3. Drop the `SOURCE_DUPLICATE` relation from `data/normalized_yaml/bacterial/es_medium_marine.yaml` to `mariprofundus_es_medium.yaml`; separately decide whether the KOMODO 1267 import should become a DSMZ 1267 record.
4. Add DSMZ 1267a `references` and structured sterilization metadata where the schema can represent filter sterilization, autoclaving, and anoxic handling.
5. Regenerate `data/merge_yaml/merged/mariprofundus_es_medium.yaml`.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation on the corrected normalized owner and regenerated target.
- Run `just verify-merges` and confirm the regenerated DSMZ 1267a record is no longer merged with `es_medium_marine`.
- Compare the regenerated YAML against MediaDive 1267a and the DSMZ 1267a PDF, checking each stock addition volume and ensuring no stock-only concentration appears as a root final-medium amount.
- Compare `es_medium_marine.yaml` against MediaDive/DSMZ 1267 before preserving or changing that KOMODO record's source identity.

## Additional Notes

- The two DSMZ records intentionally share Wolin's vitamin solution and ferrous sulfide sludge definitions. Those shared subsolutions are not evidence that the top-level 1267 and 1267a media are duplicate recipes.
