# YAML Record Review: bhi_agar_with_5_bovine_blood

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bhi_agar_with_5_bovine_blood.yaml
- Started UTC: 2026-09-21T21:05:05Z
- Finished UTC: 2026-09-21T21:06:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008835 |
| Name | bhi_agar_with_5_bovine_blood |
| Original name | BHI agar with 5% bovine blood |
| Category | bacterial |
| Source identity | TOGO Medium M2247, `TOGO:M2247` |
| Reviewed artifact | `data/merge_yaml/merged/bhi_agar_with_5_bovine_blood.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/bhi_agar_with_5_bovine_blood.yaml` |
| Generated state | Derived single-source merge from `merged_from: [bhi_agar_with_5_bovine_blood]`, `merge_fingerprint: d4ab3e23782cae2622d391a8297bac6c39524d7d519dd5d2ea8edc177e7a0a5c` |

`data/culturemech_id_registry.tsv` maps `CultureMech:008835` to
`data/normalized_yaml/bacterial/bhi_agar_with_5_bovine_blood.yaml`.

The inspected TOGO M2247 API payload identifies "BHI agar with 5% bovine blood"
and has two component rows: Bovine blood at 5% and BHI agar (Difco) at 1 L. Its
`src_url` is empty, so TOGO is the narrowest inspected source available in this
review.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bhi_agar_with_5_bovine_blood.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bhi_agar_with_5_bovine_blood.yaml --out /private/tmp/bhi_agar_with_5_bovine_blood.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 ERROR rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bhi_agar_with_5_bovine_blood.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bhi_agar_with_5_bovine_blood.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded-`MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/` |

The direct `just validate-*` wrappers were not rerun for this record because
this checkout currently fails before target-specific validation while building
`llvmlite==0.46.0` under Python 3.13. The no-project commands above exercise
the same narrow validators under Python 3.11 from a cache outside the project
environment.

## Identity and Grounding

- **Record identity is coherent.** `TOGO:M2247`, the TOGO API payload, and the
  record label all identify BHI agar with 5% bovine blood.
- **Bovine blood is present but underresolved.** TOGO lists Bovine blood at
  5%. The record keeps the ingredient ungrounded, matching local import
  tracking's `UNRESOLVED_CHEMICAL` flag.
- **The percentage axis is over-specified.** TOGO reports unit `%` for Bovine
  blood and does not state weight/volume. The YAML converts it to
  `PERCENT_W_V`, which should be treated as unresolved until an original source
  or TOGO convention confirms the intended fraction.
- **The source BHI agar aggregate is missing.** TOGO lists `BHI agar (Difco)`
  at 1 L. The record omits that solid aggregate and instead expands a BHI
  broth-like formula from MicrobeNotes, with no agar-bearing row.

## Evidence

| Claim | Review |
|---|---|
| `TOGO:M2247` / BHI agar with 5% bovine blood | Supported by the inspected TOGO M2247 payload. |
| 5% Bovine blood | Supported as 5%; the w/v interpretation is not supported. |
| `physical_state: SOLID_AGAR` | Supported by TOGO's `BHI agar (Difco)` component, but not by the current ingredient list after that component was removed. |
| Six expanded BHI constituents | Unsupported. TOGO lists a 1 L commercial `BHI agar (Difco)` aggregate, not calf brain, beef heart, proteose peptone, dextrose, sodium chloride, or disodium phosphate rows. |
| MicrobeNotes `supplier_catalog` evidence | Unsupported product evidence. The source is a secondary BHI Agar article and not an official Difco catalog page for TOGO M2247's BHI agar ingredient. |

## Completeness

- The bovine blood component is present.
- The source `BHI agar (Difco)` component is absent.
- The TOGO payload has no upstream `src_url`; no original source was identified
  in this review beyond TOGO M2247.
- Empty pH, preparation, organism, and growth slots are acceptable because the
  inspected TOGO record does not assert those claims.
- The TOGO source and BHI catalog claims live in free-text `notes` and
  `supplier_catalog` fields rather than structured `references`, so reference
  validation performed zero checks.
- A gitignore-independent search with `rg --no-ignore --hidden` over `data`
  and `reports/yaml_record_review` for `CultureMech:008835`, `TOGO:M2247`,
  `bhi_agar_with_5_bovine_blood`, and the merge fingerprint found the expected
  normalized owner, generated merge, generated indexes, import-tracking
  references, and a local ungrounded-ingredient report row for Bovine blood. A
  `find` search over the ignored `reports/yaml_record_review` directory found
  no pre-existing `*-bhi_agar_with_5_bovine_blood.md` report before this one
  was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source `BHI agar (Difco)` aggregate was replaced by unsupported BHI broth constituents. | TOGO M2247 lists only 5% Bovine blood and 1 L `BHI agar (Difco)`. The YAML omits the BHI agar row and carries six MicrobeNotes BHI subcomponents with no source agar component. | `data/normalized_yaml/bacterial/bhi_agar_with_5_bovine_blood.yaml`; the BHI premix enrichment source. |
| minor | The 5% bovine blood unit is over-specified as w/v. | TOGO provides `%` with no mass/volume axis; the YAML uses `PERCENT_W_V`. | `data/normalized_yaml/bacterial/bhi_agar_with_5_bovine_blood.yaml`; the TOGO unit normalizer if it maps bare `%` to w/v. |
| minor | Structured references are absent. | The YAML has no `references` block; source URLs are free-text, and BHI subcomponent catalog URLs point to MicrobeNotes. | `data/normalized_yaml/bacterial/bhi_agar_with_5_bovine_blood.yaml`. |

## Recommended Edits

1. Restore a 1 L `BHI agar (Difco)` aggregate row and remove the unsupported
   Calf brains, Beef heart, Proteose peptone, Dextrose, Sodium chloride, and
   Disodium phosphate subcomponent rows.
2. Leave Bovine blood at 5% but use a percent unit that does not assert w/v
   unless an original source or TOGO convention proves the intended axis.
3. Add TOGO M2247 as a structured reference and record that no upstream
   `src_url` was present in the inspected TOGO payload.
4. Add an append-only curation event to the normalized owner and regenerate
   `data/merge_yaml/merged/bhi_agar_with_5_bovine_blood.yaml`.

## Follow-up Checks

- Rerun schema, strict, term, and reference validation on the normalized TOGO
  owner.
- Manually inspect the regenerated merge and confirm it contains only Bovine
  blood plus the BHI agar aggregate at the source-supported amounts.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.

## Additional Notes

None found.
