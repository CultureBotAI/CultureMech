# YAML Record Review: bhi_supplemented_with_0_1_tween_80_ph_8_0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml
- Started UTC: 2026-09-21T21:17:38Z
- Finished UTC: 2026-09-21T21:18:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009059 |
| Name | bhi_supplemented_with_0_1_tween_80_ph_8_0 |
| Original name | BHI supplemented with 0.1% Tween 80 (pH 8.0) |
| Category | bacterial |
| Source identity | TOGO Medium M2486 |
| Reviewed artifact | `data/merge_yaml/merged/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml` |
| Generated state | Derived single-source merge from `merged_from: [bhi_supplemented_with_0_1_tween_80_ph_8_0]`, `merge_fingerprint: 60ca4e37b0bc74ed9af3d800246b4a7762a24b5acc685db9c6ba1add82d38872` |

`data/culturemech_id_registry.tsv` maps `CultureMech:009059` to
`data/normalized_yaml/bacterial/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml`.

The inspected TOGO `M2486` API payload identifies a two-component record:
0.1% Tween 80 (pH 8.0) and BHI from Becton, Dickinson and Company, Baltimore,
MD. TOGO does not give a mass, volume, or stock concentration for the BHI
commercial product.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml --out /private/tmp/bhi_supplemented_with_0_1_tween_80_ph_8_0.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 ERROR rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded-`MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/` |

The direct `just validate-*` wrappers were not rerun for this record because
this checkout currently fails before target-specific validation while building
`llvmlite==0.46.0` under Python 3.13. The no-project commands above exercise
the same narrow validators under Python 3.11 from a cache outside the project
environment.

## Identity and Grounding

- **Record identity is coherent.** `TOGO:M2486`, the record label, and the TOGO
  API payload all identify BHI supplemented with 0.1% Tween 80 (pH 8.0).
- **The Tween 80 amount is source-supported but over-specified.** TOGO lists
  `Tween 80 (pH 8.0)` at 0.1% and labels it Polysorbate 80. The generated
  record keeps it ungrounded and asserts `PERCENT_W_V`; the source says `%`
  without a w/v or v/v basis.
- **The BHI row is unsupported.** TOGO lists a BHI commercial product but does
  not give an amount. The generated row therefore should remain variable; the
  current record has a 2026-02-03 defaulting event for that BHI component and
  now expands it into six full-strength Difco product constituents.
- **pH 8.0 is missing structurally.** The source title and growth comment both
  state pH 8.0, but the generated record has no `ph_value`.
- **Growth context is missing.** TOGO's retained source comment says
  Erysipelothrix rhusiopathiae strain Fujisawa was grown at 37 degrees C in
  BHI supplemented with 0.1% Tween 80 at pH 8.0; the generated record has no
  target organism, incubation temperature, or literature reference.

## Evidence

| Claim | Review |
|---|---|
| TOGO M2486 / BHI supplemented with 0.1% Tween 80 (pH 8.0) | Supported by the TOGO API payload. |
| 0.1% Tween 80 | Supported by TOGO. |
| pH 8.0 | Supported by the TOGO title and retained source comment. |
| Six expanded BHI constituents | Unsupported. TOGO lists `BHI (Becton, Dickinson and Company, Baltimore, MD)` with no quantity. |
| `Tween 80` as `PERCENT_W_V` | Unsupported over-specification; TOGO records a percent value without the percentage basis. |

## Completeness

- The BHI commercial product is exact enough to preserve as an unresolved
  source row with a variable amount; the current schema-defaulted expansion is
  not evidence-backed.
- Empty preparation fields are acceptable because the inspected TOGO payload
  does not describe sterilization or handling steps.
- The reviewed merge has only the public TOGO URL in `notes`; it has no
  structured `references` entry for the public TOGO page or TOGO API payload.
- A gitignore-independent search with `rg --no-ignore --hidden` over `data`
  and `reports/yaml_record_review` for `CultureMech:009059`, `TOGO:M2486`,
  `bhi_supplemented_with_0_1_tween_80_ph_8_0`, and the merge fingerprint found
  the expected normalized owner, generated merge, generated indexes,
  import-tracking reports, and no related prior review report. A `find` search
  over the ignored `reports/yaml_record_review` directory found no
  pre-existing `*-bhi_supplemented_with_0_1_tween_80_ph_8_0.md` report before
  this one was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source's quantity-free BHI commercial-product row was defaulted and replaced by six unsupported full-strength BHI constituents. | TOGO M2486 lists a Becton Dickinson BHI product without a quantity, and the normalized owner records a schema-defaulter event for that ingredient. | `data/normalized_yaml/bacterial/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml` |
| major | Source pH 8.0 is missing. | TOGO names the medium `BHI supplemented with 0.1% Tween 80 (pH 8.0)` and repeats pH 8.0 in the retained growth comment. | `data/normalized_yaml/bacterial/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml` |
| minor | The Tween 80 percentage basis is over-specified as w/v and remains ungrounded. | TOGO lists 0.1% Tween 80 and labels it Polysorbate 80, but does not specify w/v. | `data/normalized_yaml/bacterial/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml` |
| minor | Structured source references are absent. | The TOGO URL is present only in the free-text `notes`, and the TOGO API URL is not recorded. | `data/normalized_yaml/bacterial/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml` |

## Recommended Edits

1. In
   `data/normalized_yaml/bacterial/bhi_supplemented_with_0_1_tween_80_ph_8_0.yaml`,
   replace the six BHI decomposition rows with one explicit BHI commercial
   product row carrying a variable amount and the TOGO GMO provenance.
2. Add `ph_value: 8.0` from the TOGO title and source comment.
3. Change Tween 80 to a unit that preserves the source's unspecified `0.1%`
   basis, and ground or explicitly leave unresolved the Polysorbate 80
   identity.
4. Add structured references for the public TOGO `M2486` page and the TOGO API
   payload.
5. Record the E. rhusiopathiae strain Fujisawa growth context only after the
   source paper behind TOGO's retained paragraph has been recovered.
6. Regenerate this merge and generated media pages from the corrected
   normalized owner.

## Follow-up Checks

- Rerun schema, strict, term, and reference validation on the corrected
  normalized owner and on the regenerated merge.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare the regenerated merge against TOGO `M2486` and confirm the
  six unsupported BHI decomposition rows are gone, pH 8.0 is explicit, and no
  unsupported BHI amount was introduced.

## Additional Notes

None found.
