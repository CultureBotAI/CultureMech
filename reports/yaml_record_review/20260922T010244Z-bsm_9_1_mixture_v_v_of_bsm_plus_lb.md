# YAML Record Review: BSM+ (9:1 mixture v/v of BSM plus LB)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml
- Started UTC: 2026-09-22T01:02:44Z
- Finished UTC: 2026-09-22T01:02:44Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:008988 |
| Label | bsm_9_1_mixture_v_v_of_bsm_plus_lb |
| Original label | BSM+ (9:1 mixture v/v of BSM plus LB) |
| Category | bacterial |
| Source accession | TOGO:M2405 |
| Generated path | data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml |
| Maintained owner | data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml |
| Merge fingerprint | 07b944ab84da5bb9fd3509cc804edfb9d840b2b5159a52a9d8cfabf3bde540ed |

The reviewed target is a generated merge under `data/merge_yaml/merged`,
derived from the single normalized owner `bsm_9_1_mixture_v_v_of_bsm_plus_lb`.
Future fixes belong in that normalized file, the TOGO import path, or the
LB-commercial-product enrichment path that expanded LB as unsupported full-
strength rows.

## Validation

| Check | Result |
| --- | --- |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml --out /private/tmp/bsm_9_1_mixture_v_v_of_bsm_plus_lb.strict.tsv --workers 1 --quiet` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 structured URL checks |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| `just validate-history data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml` | Not checked: `validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |

Direct `just validate-schema`, `just validate-strict`, `just validate-terms`,
and `just validate-references` were not rerun because the project uv environment
tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with
`TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The
equivalent no-project Python 3.11 validators above passed.

## Identity and Grounding

The TOGO identity is coherent: the live TOGO M2405 payload resolves to
`BSM+ (9:1 mixture v/v of BSM plus LB)`, and the generated record uses
`TOGO:M2405` with the same label.

The record does not preserve the source hierarchy. TOGO defines the top-level
medium as 10% v/v LB medium plus 90% v/v Basal salts medium, then defines BSM as
a separate one-liter recipe. The generated YAML flattens LB and the BSM
subrecipe into one top-level ingredient list, stores `Basal salts medium (BSM)`
as a `90 G_PER_L` ingredient, and loses the required 10% LB / 90% BSM volume
relationship.

The CHEBI mappings for water, magnesium sulfate heptahydrate, sodium chloride,
potassium dihydrogen phosphate, disodium hydrogenphosphate, and agar are
plausible. `FeSO4 . 7H2O` is plausibly the ferrous sulfate heptahydrate
specified by TOGO; `(NH4)SO4` remains unresolved. `CaCl2 . 7H2O` must remain
unresolved until the source conflict is handled because the literal source
formula says 7 waters while TOGO's GMO label says calcium chloride hexahydrate;
the current anhydrous `CHEBI:3312` grounding does not preserve either hydrate
claim.

## Evidence

Supported:

| Claim | Source support |
| --- | --- |
| TOGO M2405 denotes BSM+ | The live TOGO M2405 payload has `name: BSM+ (9:1 mixture v/v of BSM plus LB)`. |
| The top-level medium is 10% v/v LB medium plus 90% v/v BSM | TOGO M2405 lists `LB medium`, `10 % (v/v)`, and `Basal salts medium (BSM)`, `90 % (v/v)`, as the two top-level components. |
| The BSM subrecipe contains distilled water, MgSO4 . 7H2O, NaCl, KH2PO4, FeSO4 . 7H2O, (NH4)SO4, Na2HPO4, CaCl2 . 7H2O, and agar | TOGO M2405 lists those labels under the `Basal salts medium (BSM)` subcomponent. |
| Agar concentration and solid physical state | TOGO M2405 specifies 1.5% agar in the BSM recipe. |

Unsupported or incomplete:

| Generated claim | Problem |
| --- | --- |
| Full-strength top-level `Tryptone 10.0 G_PER_L`, `Yeast extract 5.0 G_PER_L`, and `Sodium chloride 10.0 G_PER_L` | TOGO M2405 only says the final BSM+ medium receives 10% v/v LB medium; it does not expand LB into these components, and these rows are not diluted to 10% final strength. |
| `Basal salts medium (BSM)`, `90 G_PER_L` | TOGO M2405 uses 90% v/v BSM, not 90 g/L BSM. |
| BSM subrecipe rows as top-level final ingredients | The source labels these rows as the composition of the BSM subcomponent, not as direct top-level additions. |
| `FeSO4 . 7H2O`, `0.28 G_PER_L` and `CaCl2 . 7H2O`, `10.69 G_PER_L` | TOGO M2405 gives those two quantities in milligrams, not grams. |
| `CaCl2 . 7H2O` grounded to anhydrous calcium dichloride | The source formula and TOGO GMO label already conflict on hydration state; the anhydrous CHEBI term drops both possible hydrated identities. |
| Top-level LB Miller notes and supplier catalog metadata | TOGO M2405 does not cite laboratorynotes.com, Sigma L3522, BD 244520, or the LB Miller enrichment source. |
| No structured TOGO reference | The only source support is free text in `notes`; there is no `source_data` or reference object for TOGO M2405. |

## Completeness

The maintained owner is not complete enough to reconstruct TOGO M2405. It lacks
a structured top-level 10% LB / 90% BSM mixture, lacks a structured BSM
subrecipe boundary, changes the BSM reference and the water volume into `G_PER_L`
quantities, imports two milligram salts as grams, and leaves the chemically
significant calcium hydrate conflict unresolved.

A gitignore-independent `rg --no-ignore --hidden` search of
`data/normalized_yaml`, `data/merge_yaml/merged`, the ID registry, the recipe
catalog, `reports/yaml_record_review`, `reports/media_content_review_manifest`,
and `data/import_tracking/reports` for `CultureMech:008988`, `TOGO:M2405`,
`M2405`, `bsm_9_1_mixture_v_v_of_bsm_plus_lb`, and merge fingerprint
`07b944ab...` found the active TOGO M2405 owner, this generated merge, and
expected generated indexes and reports. `find reports/yaml_record_review
-maxdepth 1 -type f -name '*bsm_9_1_mixture_v_v_of_bsm_plus_lb.md'` found no
pre-existing report, including ignored files in the report directory.

The live TOGO M2405 payload has an empty upstream `src_url`. Empty preparation,
target-organism, and growth-evidence slots are not defects for this source-only
TOGO recipe.

## Findings

| Severity | Finding | Maintained owner for a future fix |
| --- | --- | --- |
| Major | The required 10% v/v LB medium plus 90% v/v BSM mixture is lost. LB medium was expanded to full-strength top-level LB Miller ingredients, and BSM was stored as `90 G_PER_L` instead of 90% v/v. | `data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml` and the TOGO import path |
| Major | The BSM subrecipe is flattened into final top-level ingredients. This loses the source boundary between a final mixture and the BSM base recipe. | `data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml` |
| Major | FeSO4 . 7H2O and CaCl2 . 7H2O milligram amounts were imported as grams, inflating them by 1000-fold. | `data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml` and the TOGO import path |
| Major | `CaCl2 . 7H2O` is grounded to anhydrous `CHEBI:3312` even though hydration is explicitly part of the source formula and conflicts with TOGO's hexahydrate GMO label. | `data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml` |
| Minor | The record has no structured TOGO M2405 source reference, so the reference validator had no source URL to check. | `data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml` |

No blocker findings found.

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml`
   as 10% v/v LB medium plus 90% v/v BSM instead of full-strength LB rows and a
   `90 G_PER_L` BSM row.
2. Model Basal salts medium as a nested or referenced subrecipe with its own
   one-liter BSM component amounts.
3. Convert FeSO4 . 7H2O 0.28 and CaCl2 . 7H2O 10.69 back to milligram-scale
   source amounts.
4. De-ground `CaCl2 . 7H2O` from anhydrous `CHEBI:3312` unless a source-faithful
   hydrated identity can be resolved.
5. Remove unsupported LB Miller supplier metadata and avoid expanding LB unless
   the curated LB stock itself is represented as a 10% volume addition.
6. Add structured TOGO M2405 provenance.
7. Regenerate `data/merge_yaml/merged/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml`.

## Follow-up Checks

- Rerun focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/bsm_9_1_mixture_v_v_of_bsm_plus_lb.yaml`.
- Rerun `just verify-merges` after regeneration and inspect the generated BSM+
  diff to confirm the 10%/90% mixture, BSM boundary, milligram units, calcium
  grounding, and LB metadata are fixed.
- Manually compare the regenerated owner against live TOGO M2405 because the
  payload has no upstream `src_url`.

## Additional Notes

- `data/import_tracking/reports/ungrounded_ingredients.tsv` already flags
  `Basal salts medium (BSM)` and `(NH4)SO4` as unresolved in this record.
