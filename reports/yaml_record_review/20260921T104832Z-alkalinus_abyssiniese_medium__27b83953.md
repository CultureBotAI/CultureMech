# YAML Record Review: Alkalinus Abyssiniese Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml
- Started UTC: 2026-09-21T10:47:18Z
- Finished UTC: 2026-09-21T10:48:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007540` |
| Name | `alkalinus_abyssiniese_medium` |
| Original name | `Alkalinus Abyssiniese Medium` |
| Category | `bacterial` |
| Generated status | Generated merge from one maintained normalized source |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml` |
| Upstream source | TOGO `M1026`, imported from JCM `JCM_M974-2` |
| Merge fingerprint | `27b8395356cd5b00a6470efaa82f630b1bf446acc46a55a11b9a4ece99c7a17f` |

This generated record is the TOGO M1026 solid-agar variant of the JCM 974 /
TOGO M1025 alkaline medium family. Fix the normalized M1026 source and
regenerate; do not patch this derived merge directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml --out /private/tmp/alkalinus_abyssiniese_medium__27b83953.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning |
| Embedded curation history | Not checked | No focused validator is documented for embedded `MediaRecipe.curation_history`; `just validate-history` validates standalone files under `history/` |

The usual `just` wrappers were not rerun here because target-specific `just
validate-schema`, `just validate-strict`, and `just validate-terms` currently
fail before target validation while the project `uv` environment attempts to
build `llvmlite==0.46.0` under Python 3.13. The no-project validator commands
above use Python 3.11 and the cached validator packages instead.

## Identity and Grounding

The record is internally coherent for TOGO M1026: `media_term` uses
`TOGO:M1026`, `notes` identify TOGO M1026 and JCM `JCM_M974-2`, `physical_state`
is `SOLID_AGAR`, and the record includes the agar row that distinguishes this
variant from liquid TOGO M1025. The live JCM GRMD 974 page was checked while
reviewing this family and returns `Nothing found`, so the inspected recoverable
formulation is TOGO M1026.

The exact ignored-files-including search:

```bash
rg -n "M1026|JCM_M974-2|27b839536841b54cfe263e1e7600ed0a|alkalinus_abyssiniese_medium__27b83953|GRMD=974" data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml --glob '*.yaml' --no-ignore --hidden
```

found this generated M1026 record, its maintained normalized parent, and the
M1025 source URL that M1026 relies on for its trace-mineral solution. The target
is not conflated with M1025: it has TOGO M1026, stable ID `CultureMech:007540`,
`SOLID_AGAR`, and agar at 20 g/L.

Ingredient grounding for MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, KH2PO4, and agar
matches the source. Supplier-specific yeast extract and peptone are correctly
left ungrounded.

## Evidence

The fetched TOGO M1026 record has two top-level ingredient scopes:

| Source scope | Source content |
|---|---|
| Main 900 ml agar base | 900 ml water, MgSO4 x 7H2O 0.2 g, NaCl 117 g, CaCl2 x 2H2O 0.2 g, KH2PO4 0.1 g, agar 20 g/L, yeast extract 5 g, peptone 5 g, and 10 ml trace mineral solution from Medium M1025 |
| Post-autoclave stocks | 100 ml 10% (w/v) Na2CO3 solution and 5 ml 10% (w/v) glucose solution, both separately autoclaved and added aseptically after cooling |

The generated record preserves the agar variant and the main base ingredient
amounts, but it changes 900 ml water into `900 G_PER_L`, changes the 10 ml
M1025 trace-mineral stock addition into an empty `10 G_PER_L` solution, and
does the same volume-to-`G_PER_L` flattening for 100 ml Na2CO3 stock and 5 ml
glucose stock.

The TOGO M1026 preparation comment says to add the base components to distilled
water, bring the volume to 900 ml, add 20 g/L agar for solid medium, autoclave
and cool to 50 to 60 C for agar medium, then aseptically add the separately
autoclaved stock solutions. The generated record has no preparation steps and
does not preserve separate autoclaving or aseptic post-autoclave addition.

No claim-level `evidence` objects or structured `references` are present. The
TOGO/JCM provenance is retained only as free text in `notes`.

## Completeness

Consequential gaps:

- 900 ml source water is represented as mass-per-liter.
- The 10 ml cross-reference to M1025 trace-mineral solution is an empty
  solution placeholder and does not resolve to the maintained M1025 stock.
- The 100 ml 10% Na2CO3 and 5 ml 10% glucose post-autoclave additions are
  empty solution placeholders with addition volume conflated into `G_PER_L`.
- Base autoclaving, cooling to 50 to 60 C for agar, separate stock autoclaving,
  and aseptic addition are missing.
- TOGO M1026, the now-unavailable JCM GRMD 974 page, and the M1025
  trace-mineral cross-reference are not structured.

Empty optional slots that are not automatic defects:

- `target_organisms` and `growth_metrics` can remain empty because TOGO M1026
  is a formulation/protocol source, not a strain-specific growth record.
- Undefined supplier-specific yeast extract and peptone do not need ChEBI
  terms.

The prior-report search:

```bash
find reports/yaml_record_review -name '*alkalinus_abyssiniese_medium__27b83953*' -print
```

included ignored report files and found no existing report for this exact
generated record before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Water is dimensionally wrong: 900 ml source water is stored as `900 G_PER_L`. | TOGO M1026 lists 900 ml distilled water in the main agar base. | `data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml`, or the TOGO importer |
| Major | The 10 ml M1025 trace-mineral addition, 100 ml 10% Na2CO3 addition, and 5 ml 10% glucose addition lost their volumes and stock boundaries. | TOGO M1026 serializes each as a volume addition and names M1025 as the source for the trace stock. | `data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml`, or the TOGO importer |
| Major | Preparation context is missing. The solid medium must be autoclaved, cooled to 50 to 60 C, and amended aseptically with separately autoclaved stocks. | TOGO M1026 contains that preparation comment. | `data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml` |
| Minor | The trace-mineral stock cross-reference is free text only. `Trace mineral solution (see Medium [M1025])` should resolve to the M1025 stock owned by TOGO M1025. | TOGO M1026 has `reference_media_id: "M1025"` for the trace solution; the generated record only preserves that as text in `preferred_term`/`notes`. | `data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml` plus the repaired M1025 stock |
| Minor | TOGO/JCM provenance is free-text only and JCM GRMD 974 now has no live formulation table. | The source URLs are in `notes`; fetching JCM GRMD 974 returned `Nothing found`. | `data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml` |

No blocker findings were found.

## Recommended Edits

1. Change the 900 ml water entry to a volume-preserving representation for the
   agar base.
2. Represent the 10 ml trace-mineral solution addition as a reference to the
   repaired TOGO M1025 stock instead of an empty `10 G_PER_L` solution.
3. Replace the empty 10% Na2CO3 and 10% glucose solution placeholders with
   stock additions that preserve 100 ml and 5 ml respectively.
4. Add preparation steps for base mixing to 900 ml, agar autoclaving, cooling
   to 50 to 60 C, and aseptic addition of separately autoclaved stock
   solutions.
5. Add structured TOGO/JCM provenance and an explicit M1025 stock
   cross-reference.
6. Regenerate `data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml`
   and generated pages from the maintained source.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml` after rebuilding solution references.
- Run `just validate-references data/normalized_yaml/bacterial/TOGO_M1026_Alkalinus_Abyssiniese_Medium.yaml` after adding structured TOGO/JCM/M1025 references.
- Run `just validate-media-variant-links` if M1025 and M1026 are linked as liquid/solid variants.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merge.
- Manually compare the regenerated record with TOGO M1026 for 900 ml base
  water, 20 g/L agar, 10 ml/100 ml/5 ml stock additions, and the 50 to 60 C
  agar cooling instruction.

## Additional Notes

- M1026 reuses the M1025 trace-mineral stock; full curation of that stock
  belongs with `TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml`.
- `high_metal: true` should be recomputed after the 10 ml trace-stock addition
  is represented as a stock dose rather than a final `10 G_PER_L` placeholder.
