# YAML Record Review: Brain Heart Infusion Agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml
- Started UTC: 2026-09-21T23:32:28Z
- Finished UTC: 2026-09-21T23:33:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009008 |
| Label | Brain Heart Infusion Agar |
| Source accession | TOGO:M2425 |
| Merge source | data/normalized_yaml/bacterial/TOGO_M2425_Brain_Heart_Infusion_Agar.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 99bfa02e06ae120984400bdf18f7260d8f77e9e6fbd06b84b83891d830ad8caf |

The reviewed file is a stale derived merge. Its single normalized owner was
repaired on 2026-09-06 by `repair_atcc_score40.py`; future work should not edit
the generated merge directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml --out /private/tmp/Brain_Heart_Infusion_Agar.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- TOGO:M2425 resolves to Brain Heart Infusion Agar and cites the ATCC Medium 44
  PDF at the same ATCC URL retained in the record.
- ATCC Medium 44 supports the repaired normalized owner: 52 g Brain Heart
  Infusion Agar (BD 211065), 1000 ml DI water, pH 7.4 +/- 0.2, and autoclaving
  at 121 C.
- A gitignore-independent search for `TOGO:M2425`, `CultureMech:009008`, the
  merge fingerprint, `TOGO_M2425_Brain_Heart_Infusion_Agar`, and the ATCC URL
  token across `data`, `src`, `scripts`, `docs`, `.claude`, and `justfile`
  found one normalized owner plus the generated merge and generated indexes.
- The generated merge still has the stale label `Heart Infusion Agar (BD
  211065)`, whereas ATCC names the component `Brain Heart Infusion Agar (BD
  211065)` and TOGO assigns it the GMO label `BBL Brain heart infusion agar`.

## Evidence

The ATCC PDF supports the normalized post-repair formulation and contradicts
the generated stale water unit. It lists 52 g Brain Heart Infusion Agar (BD
211065) and 1000 ml DI water, then gives a 121 C autoclave instruction. The
TOGO API payload for M2425 carries the same 52 g Heart Infusion Agar
commercial-product row, the same 1000 ml DI Water row, `ph: 7.2 - 7.6`, and
the autoclave comment.

## Completeness

- Consequential gap in the generated merge: the repaired `ph_value`,
  `preparation_steps`, `sterilization`, `references`, `parent_media`,
  `variant_relationship`, and `variant_modifications` from the normalized owner
  are absent.
- The normalized owner already has structured TOGO and ATCC references; the
  generated stale record only has them as free text in `notes`.
- Empty target-organism and growth-evidence slots are acceptable for this
  source-only ATCC/TOGO formulation.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `Brain_Heart_Infusion_Agar` report, so this report did not overwrite an
  earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to its single maintained owner and ATCC Medium 44. It still has 1000 `G_PER_L` DI Water, the stale `Heart Infusion Agar (BD 211065)` label, no pH, no autoclave step, no references, and no source-duplicate link to TOGO M21. | `data/normalized_yaml/bacterial/TOGO_M2425_Brain_Heart_Infusion_Agar.yaml` was repaired on 2026-09-06 with 52 g Brain Heart Infusion Agar, 1000 `ML_PER_L` DI Water, pH 7.4, ATCC/TOGO references, and TOGO M21 duplicate metadata. ATCC Medium 44 lists the same 52 g commercial agar and 1000 ml water. | `data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml` should be regenerated from `data/normalized_yaml/bacterial/TOGO_M2425_Brain_Heart_Infusion_Agar.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml` from
   `data/normalized_yaml/bacterial/TOGO_M2425_Brain_Heart_Infusion_Agar.yaml`.
2. Regenerate the media page/browser products that derive from the merged
   record.
3. Do not hand-edit `data/merge_yaml/merged/Brain_Heart_Infusion_Agar.yaml`;
   the authoritative normalized owner already contains the ATCC-supported
   September repair.

## Follow-up Checks

- Rerun `just verify-merges` and confirm `Brain_Heart_Infusion_Agar.yaml` is no
  longer stale.
- Rerun `just gen-media-pages --force` or the project product-generation gate
  used for regenerated merge outputs.
- Rerun the focused LinkML, strict, term, and reference validators on the
  regenerated merge.

## Additional Notes

- Optional empty growth-evidence slots were not treated as defects.
- The only issue found in the reviewed record is freshness; the normalized
  owner was already corrected in the maintained layer.
