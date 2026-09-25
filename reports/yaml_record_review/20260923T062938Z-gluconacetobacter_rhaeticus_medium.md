# YAML Record Review: gluconacetobacter_rhaeticus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gluconacetobacter_rhaeticus_medium.yaml
- Started UTC: 2026-09-23T06:27:31Z
- Finished UTC: 2026-09-23T06:29:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:003603` |
| Name | `gluconacetobacter_rhaeticus_medium` |
| Original name | `GLUCONACETOBACTER RHAETICUS medium` |
| Category | `bacterial` |
| Canonical media term | `komodo.medium:1044` |
| Merged source count | 7 |
| Merged sources | `KOMODO_1044_GLUCONACETOBACTER_RHAETICUS_medium`, `KOMODO_850_ALTERNATIVE_ACETOBACTER_INTERMEDIUS_medium`, `acetobacter_musti_medium`, `alternative_acetobacter_intermedius_medium`, `gluconacetobacter_rhaeticus_medium`, `gy_medium`, `yed_acetobacter_medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gluconacetobacter_rhaeticus_medium.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/gluconacetobacter_rhaeticus_medium.yaml --out /private/tmp/gluconacetobacter_rhaeticus_medium.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/gluconacetobacter_rhaeticus_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/gluconacetobacter_rhaeticus_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

The canonical identity of this generated record is DSMZ Medium 1044 / KOMODO Medium 1044, but the generated merge also claims five additional MediaDive/DSMZ source accessions and one additional KOMODO accession as source duplicates.

A gitignore-independent exact search for `komodo.medium:1044`, `komodo.medium:850`, and `mediadive.medium:1044`, `mediadive.medium:850`, `mediadive.medium:1603`, `mediadive.medium:1543`, and `mediadive.medium:1424` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected seven maintained parents, their generated index references, and this generated merge.

Ingredient groundings are narrow for the three compounds the generated record retained. `CHEBI:17234` denotes glucose and `CHEBI:2509` denotes agar; yeast extract is ungrounded, which is safer than assigning a narrow chemical term to a complex extract.

## Evidence

The live MediaDive REST payloads show that only two of the seven maintained parents use DSMZ 1044's glucose / yeast / agar signature:

| Source | Medium label | Glucose | Yeast extract | Agar | pH |
|---|---|---:|---:|---:|---|
| `mediadive.medium:1044` | GLUCONACETOBACTER RHAETICUS MEDIUM | 50 g/l | 5 g/l | 15 g/l | 6.5 |
| `komodo.medium:1044` | GLUCONACETOBACTER RHAETICUS medium | 50 g/l | 5 g/l | 15 g/l | 6.5 |
| `mediadive.medium:1543` | GY - MEDIUM | 50 g/l | 10 g/l | 15 g/l | 7.0 |
| `mediadive.medium:1603` | ACETOBACTER MUSTI MEDIUM | 10 g/l | 10 g/l | 20 g/l | absent |
| `mediadive.medium:1424` | YED ACETOBACTER MEDIUM | 7 g/l | 4 g/l | 20 g/l | 7.0 |
| `mediadive.medium:850` | ALTERNATIVE ACETOBACTER INTERMEDIUS MEDIUM | 5 g/l | 3 g/l | 12 g/l | absent |
| `komodo.medium:850` | ALTERNATIVE ACETOBACTER INTERMEDIUS medium | 5 g/l | 3 g/l | 12 g/l | absent |

The generated ingredient list is evidence-backed only for DSMZ/KOMODO 1044. It is incompatible with the direct DSMZ 850, 1424, 1543, and 1603 payloads and the KOMODO 850 parent.

Every inspected MediaDive source lists a 1000 ml distilled-water row that is absent from its normalized parent and therefore absent from this generated merge.

Three direct MediaDive parents have source preparation steps that were dropped during merge:

- DSMZ 1044: `adjust pH 6.5`
- DSMZ 1603: `For solid media 20 g/l agar may be added.`
- DSMZ 1424: `Adjust to pH 7.0. The medium may be solidified by adding 20.0 g/l agar.`

## Completeness

This generated record is not complete enough to use as a canonical merge because it conjoins formulas that differ in both concentration and condition fields. The `merged_from` list and synonym set make distinct DSMZ recipes appear to be aliases of DSMZ 1044.

Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects on their own.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Five of the seven merged parents are not duplicates of DSMZ 1044. The merge has erased DSMZ 850, 1424, 1543, and 1603's source concentrations while preserving their accessions as synonyms. | MediaDive payloads for 850, 1424, 1543, and 1603 have distinct glucose, yeast-extract, and agar concentrations; KOMODO 850 matches DSMZ 850, not DSMZ 1044. | Duplicate relationships in `data/normalized_yaml/bacterial/` or the fingerprinting logic in `scripts/merge_recipes.py`. |
| Major | Source-specific pH and agar preparation context were dropped or contradicted by the canonical record. | The generated record keeps pH 6.5 from DSMZ 1044 even though DSMZ 1424 and 1543 have pH 7.0; DSMZ 1424 and 1603 describe agar as a solid-medium addition, but the generated record has unconditional `physical_state: SOLID_AGAR`. | `scripts/merge_recipes.py` and the normalized direct DSMZ parents. |
| Minor | Source water rows are missing for every parent in the duplicate cluster. | MediaDive 850, 1044, 1424, 1543, and 1603 all list 1000 ml distilled water in the main solution; no maintained parent represents it. | MediaDive and KOMODO importers or the maintained parent files under `data/normalized_yaml/bacterial/`. |
| Minor | The two KOMODO parents have malformed original import timestamps. | `KOMODO_1044_GLUCONACETOBACTER_RHAETICUS_medium.yaml` has `2026-01-27T01:15:01.fZ`; `KOMODO_850_ALTERNATIVE_ACETOBACTER_INTERMEDIUS_medium.yaml` has `2026-01-27T01:15:03.fZ`. | The two KOMODO normalized parents. |

## Recommended Edits

1. Split the generated cluster so DSMZ 1044, DSMZ 850, DSMZ 1424, DSMZ 1543, and DSMZ 1603 remain distinct unless a curator records source-backed equivalence among the actual formulas.
2. Limit the KOMODO 1044 source duplicate relationship to DSMZ 1044, and limit the KOMODO 850 source duplicate relationship to DSMZ 850.
3. Harden `scripts/merge_recipes.py` or the merge input overlay so records with different same-name ingredient concentrations cannot share a `merge_fingerprint`.
4. Preserve source-specific preparation steps and pH values only on the recipes they came from after the split.
5. Decide whether 1000 ml distilled-water rows from MediaDive should be represented and, if so, add them in the import or normalized layer.
6. Repair the two malformed KOMODO import timestamps.

## Follow-up Checks

- Re-run `scripts/merge_recipes.py` and verify the regenerated `merged_from` sets for `gluconacetobacter_rhaeticus_medium`, `alternative_acetobacter_intermedius_medium`, `acetobacter_musti_medium`, `gy_medium`, and `yed_acetobacter_medium`.
- Re-run open LinkML, strict, reference, and term validation on each regenerated merged record in the former cluster.
- Compare every split record against the corresponding live MediaDive REST payload and verify that glucose, yeast extract, agar, pH, and preparation steps match by DSMZ number.
- Repeat the gitignore-independent exact source-accession search to confirm `komodo.medium:1044` appears only with `mediadive.medium:1044`, and `komodo.medium:850` appears only with `mediadive.medium:850`.

## Additional Notes

The exact source-accession search included ignored files. It did not show stray generated YAML records for the five MediaDive accessions outside this collapsed merge; after curation, the split records should be regenerated rather than hand-authored under `data/merge_yaml/merged/`.
