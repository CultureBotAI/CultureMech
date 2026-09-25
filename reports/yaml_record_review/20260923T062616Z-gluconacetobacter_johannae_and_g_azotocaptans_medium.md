# YAML Record Review: gluconacetobacter_johannae_and_g_azotocaptans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml
- Started UTC: 2026-09-23T06:23:31Z
- Finished UTC: 2026-09-23T06:26:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:006825` |
| Name | `gluconacetobacter_johannae_and_g_azotocaptans_medium` |
| Original name | `GLUCONACETOBACTER JOHANNAE AND G. AZOTOCAPTANS medium` |
| Category | `bacterial` |
| Canonical media term | `komodo.medium:920` |
| Direct source duplicate | `data/normalized_yaml/bacterial/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml`, `mediadive.medium:920` |
| KOMODO source duplicates | `data/normalized_yaml/bacterial/KOMODO_920_GLUCONACETOBACTER_JOHANNAE_AND_G._AZOTOCAPTANS_medium.yaml`, `data/normalized_yaml/bacterial/dsm_13594_and_dsm_13595.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml --out /private/tmp/gluconacetobacter_johannae_and_g_azotocaptans_medium.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

The generated recipe is the merged DSMZ 920 family. A gitignore-independent exact search for `komodo\.medium:920`, `mediadive\.medium:920`, `DSMZ Medium: 920`, `DSMZ_Medium920`, and `dsm_13594_and_dsm_13595` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the three maintained parents, their normalized index references, and this generated merge.

The source identity is materially recoverable, but the merge chooses the KOMODO derivative as canonical:

- `KOMODO_920_GLUCONACETOBACTER_JOHANNAE_AND_G._AZOTOCAPTANS_medium.yaml` and `dsm_13594_and_dsm_13595.yaml` both state `DSMZ Medium: 920 (mediadive.medium:920)` and contain identical DSMZ 920 ingredient signatures.
- `gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml` is the direct MediaDive/DSMZ import for `mediadive.medium:920`.
- DSMZ 920 names this formula `GLUCONACETOBACTER JOHANNAE AND G. AZOTOCAPTANS MEDIUM`, so the generated `dsm_13594_and_dsm_13595` synonym is only a KOMODO alias, not a separate medium formula.

Ingredient groundings are generally consistent with the source compounds. Glucose, mannitol, dipotassium hydrogen phosphate, potassium dihydrogen phosphate, and agar resolve to matching CHEBI entries; yeast extract and MES buffer correctly remain ungrounded rather than receiving over-broad atomic or class terms.

## Evidence

The direct MediaDive 920 REST payload and the DSMZ 920 PDF support the six non-water ingredient concentrations in the generated recipe:

| Ingredient | Generated value | Source support |
|---|---:|---|
| Yeast extract | 2.7 g/l | DSMZ and MediaDive list 2.70 g in a 1000 ml main solution. |
| Glucose | 2.7 g/l | DSMZ and MediaDive list 2.70 g in a 1000 ml main solution. |
| Mannitol | 1.8 g/l | DSMZ and MediaDive list 1.80 g in a 1000 ml main solution. |
| MES buffer | 4.4 g/l | DSMZ and MediaDive list 4.40 g in a 1000 ml main solution, with the Sigma attribute retained in MediaDive but not represented in CultureMech. |
| K2HPO4 | 4.81 g/l | DSMZ and MediaDive list 4.81 g in a 1000 ml main solution. |
| KH2PO4 | 0.65 g/l | DSMZ and MediaDive list 0.65 g in a 1000 ml main solution. |

The source includes 1000 ml distilled water. That carrier row is absent from all three normalized parents and therefore from the generated merge.

The DSMZ PDF adds two preparation qualifications after the table: agar may be added at 15.0-18.0 g/l to prepare solid media, and DSM 13594 / DSM 13595 revive better in liquid media than on plates. MediaDive exposes the shorter preparation step "Agar may be added (15.0-18.0 g/l) to prepare solid media. Final pH 6.7."; the direct MediaDive parent keeps that text, but the generated merge drops `preparation_steps`.

No inspected DSMZ or MediaDive source supports the KOMODO note fragment `Aerobic: No`; it appears only in the KOMODO-derived normalized rows.

## Completeness

The major formula identity is complete enough to merge: all three maintained parents point to DSMZ 920 and carry the same non-water formula at the same concentrations.

The generated record is not yet complete enough for preparation-level reuse:

- `physical_state: SOLID_AGAR` makes the agar formulation look mandatory, while DSMZ describes agar as a 15.0-18.0 g/l optional addition for preparing solid medium.
- The generated file lost the direct DSMZ / MediaDive `preparation_steps` row that scopes agar and pH.
- The source's 1000 ml distilled water row is absent.

Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects for this generated duplicate merge.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated physical state and agar row over-specialize DSMZ 920 as `SOLID_AGAR` at 18 g/l. DSMZ makes agar a 15.0-18.0 g/l optional addition and explicitly notes that the two named DSM strains revive better in liquid medium than on plates. | The DSMZ 920 PDF and MediaDive 920 step both scope agar as "may be added"; the generated merge has `physical_state: SOLID_AGAR` and only an agar ingredient note of `(for solid medium)`. | `data/normalized_yaml/bacterial/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml`, both KOMODO normalized parents, or the DSMZ/KOMODO importers. |
| Major | `preparation_steps` from the direct DSMZ/MediaDive parent were dropped during merge, losing the only generated evidence that final pH is a preparation property and that agar is optional. | `data/normalized_yaml/bacterial/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml` contains the MediaDive step; `data/merge_yaml/merged/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml` has no `preparation_steps`. | `scripts/merge_recipes.py` or the merge overlay logic that owns parent field preservation. |
| Minor | The generated canonical `media_term` is the KOMODO copy even though the canonical formulation is DSMZ Medium 920 and the KOMODO rows state that DSMZ 920 was their source. | The generated file uses `komodo.medium:920`; the direct normalized DSMZ parent uses `mediadive.medium:920`. | Merge selection policy in `scripts/merge_recipes.py` or a normalized merge overlay for this duplicate family. |
| Minor | The source's 1000 ml distilled water row is absent. | DSMZ 920 and MediaDive 920 list distilled water at 1000 ml; no normalized parent has a water ingredient. | The DSMZ/KOMODO importers or the three normalized parents under `data/normalized_yaml/bacterial/`. |
| Minor | The two KOMODO parents have malformed original import timestamps. | Both rows contain `timestamp: 2026-01-27T01:15:03.fZ`. | KOMODO importer repair in `data/normalized_yaml/bacterial/KOMODO_920_GLUCONACETOBACTER_JOHANNAE_AND_G._AZOTOCAPTANS_medium.yaml` and `data/normalized_yaml/bacterial/dsm_13594_and_dsm_13595.yaml`. |

## Recommended Edits

1. In the maintained DSMZ 920 family under `data/normalized_yaml/bacterial/`, recode DSMZ 920 as a liquid basal recipe with agar represented as an optional solidifying addition or a solid-agar variant, preserving DSMZ's 15.0-18.0 g/l range and the revival note for DSM 13594 / DSM 13595.
2. Update the merge logic so `preparation_steps` from a source-duplicate parent survive into the generated record when they are not contradicted by sibling parents, then regenerate `data/merge_yaml/merged/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml`.
3. Prefer the direct DSMZ/MediaDive accession as the generated canonical `media_term`, and retain the two KOMODO accessions as aliases or source duplicates.
4. Decide whether source water rows should be retained for direct MediaDive/DSMZ 1000 ml recipes; if so, add the 1000 ml distilled water row upstream and regenerate.
5. Normalize `2026-01-27T01:15:03.fZ` in the two KOMODO parent histories to a valid UTC timestamp.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated merged record.
- Re-run the exact gitignore-independent search for `komodo\.medium:920`, `mediadive\.medium:920`, `DSMZ Medium: 920`, `DSMZ_Medium920`, and `dsm_13594_and_dsm_13595` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to ensure the duplicate cluster remains limited to the expected three parents and one generated merge.
- Compare the regenerated record against the DSMZ 920 PDF or MediaDive 920 REST payload and verify that optional agar, pH 6.7, water, and the DSM 13594 / DSM 13595 liquid-revival note are either represented or explicitly tracked as unresolved.
- Confirm the generated canonical `media_term` is `mediadive.medium:920` and the two `komodo.medium:920` accessions remain discoverable after merge.

## Additional Notes

The DSMZ 920 formula in the live MediaDive REST endpoint still matches the maintained direct MediaDive parent for all six non-water ingredient masses and the 18 g/l solid-medium agar value.
