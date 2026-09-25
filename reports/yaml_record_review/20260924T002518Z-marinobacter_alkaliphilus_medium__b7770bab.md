# YAML Record Review: marinobacter_alkaliphilus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/marinobacter_alkaliphilus_medium__b7770bab.yaml`
- Started UTC: 2026-09-24T00:24:42Z
- Finished UTC: 2026-09-24T00:25:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002748` |
| Name | `marinobacter_alkaliphilus_medium` |
| Original name | `MARINOBACTER ALKALIPHILUS MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:J392` |
| Generated status | Generated merge output from 2026-08-06 |
| Merge fingerprint | `b7770bab4ffb3421201d5f0fce9595b22938015b8aa3415cf078bb58cb7ebbd8` |
| Maintained owner | `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml` |

The reviewed record is a generated single-source merge from the JCM/MediaDive normalized owner. The formulation was repaired after the reviewed merge was generated, while one bad `kg_microbe_match` remains in the maintained source.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinobacter_alkaliphilus_medium__b7770bab.yaml` | Passed with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinobacter_alkaliphilus_medium__b7770bab.yaml --out /private/tmp/marinobacter_alkaliphilus_medium__b7770bab.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinobacter_alkaliphilus_medium__b7770bab.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinobacter_alkaliphilus_medium__b7770bab.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` validators were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The primary identity is correct: `CultureMech:002748`, `mediadive.medium:J392`, the JCM Medium 392 URL, and the `MARINOBACTER ALKALIPHILUS MEDIUM` label all identify the same JCM recipe.
- The inspected MediaDive `J392` REST payload and the live JCM `GRMD=392` page agree on 37.4 g Marine broth 2216, 0.05 g Na2SiO3, 1.0 g Na2CO3, and 1 L distilled water for the JCM 392 medium.
- The `kg_microbe_match` field is wrong. `mediadive.medium:634c` resolves to DSMZ RCM Medium (N2/CO2), which is chemically and taxonomically unrelated to Marinobacter alkaliphilus Medium J392.
- An exact gitignore-independent scan found `CultureMech:002748` and `mediadive.medium:J392` only in the reviewed generated file, `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml`, and MediaDive source indexes. A separate exact scan for `mediadive.medium:634c` found the bad `kg_microbe_match` in the reviewed target and its normalized owner alongside the real RCM 634c records.

## Evidence

- The reviewed generated target is partly stale. It omits the explicit 1 L distilled-water component and leaves `Na2SiO3` ungrounded, both of which are already fixed in `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml` by the 2026-09-12 `repair_jcm_j392_marinobacter_score15.py` event.
- The generated preparation step is source-supported but less structured than the maintained repair. JCM Medium 392 dissolves Marine broth 2216 in 900 ml water, autoclaves it, separately dissolves Na2SiO3 and Na2CO3 in 100 ml water, autoclaves that supplement, and adds it to the base.
- The generated target lacks the maintained `references` block for the JCM source.
- The `kg_microbe_match: mediadive.medium:634c` assertion is unsupported by JCM 392 and contradicted by inspected MediaDive 634c source data, which describes a different RCM medium made from dehydrated RCM medium, sodium resazurin, sodium carbonate, and water.

## Completeness

- A gitignore-independent exact field scan over the reviewed generated file and `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml` found `preparation_steps` and `kg_microbe_match` in both files, while `sterilization`, `data_quality_flags`, and `references` exist only in the normalized owner. It found no `sources`, `source_data`, `target_organisms`, or `growth_metrics` in either exact file.
- Missing `target_organisms` and `growth_metrics` are acceptable: the JCM/MediaDive medium source defines a formulation and does not report a growth assay result.
- The missing water, sodium silicate grounding, structured two-part autoclaving, and reference are not harmless generated blanks because the normalized owner already contains the repaired representation.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated merge is stale relative to the repaired JCM J392 normalized owner. | The generated file omits 1 L distilled water, keeps `Na2SiO3` ungrounded, flattens the two-part autoclave procedure, and has no JCM `references`; the maintained owner fixed those fields on 2026-09-12. | Regenerate `data/merge_yaml/merged/marinobacter_alkaliphilus_medium__b7770bab.yaml` from `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml`; if any repaired field is dropped, fix the merge path. |
| Major | The maintained owner and generated target carry an unrelated `kg_microbe_match`. | `mediadive.medium:634c` resolves to RCM Medium (N2/CO2), not Marinobacter alkaliphilus Medium J392. The exact source scan found this incorrect CURIE in `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml` and the generated target. | Remove or replace `kg_microbe_match` in `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml`, then regenerate the merged YAML. |

No blocker findings: the `media_term` identity and ingredient recipe still denote the intended JCM medium, and the YAML is valid.

No minor findings found.

## Recommended Edits

1. Delete `kg_microbe_match: mediadive.medium:634c` from `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml` unless a source-backed correct match for JCM Medium 392 is identified.
2. Regenerate the merged record so the reviewed YAML gains distilled water, the `CHEBI:60720` sodium silicate grounding, structured preparation steps, `sterilization`, `data_quality_flags`, and the JCM `references` block.
3. Confirm the regeneration does not reintroduce the stale `kg_microbe_match`.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation on the corrected normalized owner and the regenerated generated record.
- Run `just verify-merges` to prove the generated record is synchronized with `data/normalized_yaml/bacterial/marinobacter_alkaliphilus_medium.yaml`.
- Recompare the regenerated record against MediaDive J392 and JCM Medium 392, paying specific attention to the 900 ml / 100 ml split and separate autoclave operations.
- If a replacement `kg_microbe_match` is proposed, fetch and inspect that target before assigning it.

## Additional Notes

- This review inspected `mediadive.medium:634c` only to identify the bad `kg_microbe_match`; it is otherwise outside the maintained provenance of JCM Medium 392.
