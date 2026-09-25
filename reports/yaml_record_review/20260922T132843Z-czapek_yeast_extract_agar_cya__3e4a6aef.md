# YAML Record Review: czapek_yeast_extract_agar_cya__3e4a6aef

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/czapek_yeast_extract_agar_cya__3e4a6aef.yaml`
- Started UTC: 2026-09-22T13:27:00Z
- Finished UTC: 2026-09-22T13:28:43Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated ID | `CultureMech:010511` |
| Name | `czapek_yeast_extract_agar_cya` |
| Original name | `CZAPEK YEAST EXTRACT AGAR (CYA)` |
| Source term | `mediadive.medium:J226` / JCM Medium J226 |
| Original source | JCM Medium 226 |
| Generated from | `czapek_yeast_extract_agar_cya` |
| Merge fingerprint | `3e4a6aef1a9e53c6a2c365355f2c669d06a2a4f75f63651cb55126fa23e1f438` |

The generated record is a one-source projection of
`data/normalized_yaml/fungal/czapek_yeast_extract_agar_cya.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/czapek_yeast_extract_agar_cya__3e4a6aef.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/czapek_yeast_extract_agar_cya__3e4a6aef.yaml --out /private/tmp/czapek_yeast_extract_agar_cya__3e4a6aef.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/czapek_yeast_extract_agar_cya__3e4a6aef.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/czapek_yeast_extract_agar_cya__3e4a6aef.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with no diagnostics. |
| Embedded history | `just validate-history` equivalent for `curation_history` | Not checked: the repository history validator targets standalone `history/*.yaml` records, not embedded generated `MediaRecipe.curation_history` events. |

## Identity and Grounding

- The record identifies JCM Medium 226, `CZAPEK YEAST EXTRACT AGAR (CYA)`.
  The JCM 226 page resolves and supports that identity.
- JCM 226 has two scopes: the final medium contains 10 ml/L Czapek concentrate,
  and the concentrate itself contains six salts in 100 ml distilled water.
- The generated record is not a faithful representation of either scope. It
  divides K2HPO4, yeast extract, sucrose, and agar by an apparent 1.01 L total,
  omits the final 1 L water row and the 10 ml Czapek concentrate addition, and
  leaves the Czapek concentrate solutes as top-level stock concentrations.
- The exact same JCM 226 source is also present through TOGO M219 and generated
  separately as `data/merge_yaml/merged/czapek_yeast_extract_agar_cya.yaml`.
- A gitignore-independent search with `rg --no-ignore --hidden` over `data/raw`,
  `data/normalized_yaml`, and `data/merge_yaml/merged` found no raw capture for
  `mediadive.medium:J226`; it found the maintained fungal source, generated
  sibling, and source indexes for `CultureMech:010511`.

## Evidence

- Supported as final-medium source rows: K2HPO4 1 g, Czapek concentrate 10 ml,
  yeast extract 5 g, sucrose 30 g, agar 15 g, and distilled water 1 L.
- Supported as Czapek concentrate source rows: NaNO3 30 g, KCl 5 g,
  MgSO4 x 7 H2O 5 g, FeSO4 x 7 H2O 0.1 g, ZnSO4 x 7 H2O 0.1 g,
  CuSO4 x 5 H2O 0.05 g, and distilled water 100 ml.
- Unsupported by JCM 226: K2HPO4 0.990099 g/L, yeast extract 4.9505 g/L,
  sucrose 29.703 g/L, and agar 14.8515 g/L. Those appear to be artifacts of
  dividing source grams by 1.01 L rather than preserving the source amounts.
- Unsupported as final-medium rows: NaNO3 300 g/L, KCl 50 g/L, MgSO4 x 7 H2O
  50 g/L, FeSO4 x 7 H2O 1 g/L, ZnSO4 x 7 H2O 1 g/L, and CuSO4 x 5 H2O
  0.5 g/L. Those are Czapek-concentrate stock concentrations, not final-medium
  concentrations.

## Completeness

- Missing solution boundary: the generated record needs an explicit Czapek
  concentrate stock or nested solution.
- Missing final-medium rows: `Czapek concentrate (see below)` 10 ml and
  distilled water 1 L are absent.
- Missing stock row: the Czapek concentrate's own 100 ml distilled water row is
  absent.
- Correctly empty: JCM 226 does not state a pH, target organism, growth metric,
  or special preparation beyond the default 121 deg C for 15 minutes note.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Final-medium ingredient masses were diluted by an inferred 1.01 L volume. | JCM 226 lists K2HPO4 1 g, yeast extract 5 g, sucrose 30 g, and agar 15 g; the generated values are 0.990099, 4.9505, 29.703, and 14.8515 g/L. | Re-curate `data/normalized_yaml/fungal/czapek_yeast_extract_agar_cya.yaml` to preserve the final recipe and the separate Czapek concentrate scope. |
| Major | Czapek concentrate stock solutes are flattened as final-medium ingredients. | JCM 226 puts NaNO3, KCl, MgSO4 x 7 H2O, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, and CuSO4 x 5 H2O inside the `Czapek concentrate` table; the generated record stores them as top-level rows. | Model Czapek concentrate as a stock solution in the maintained fungal source and regenerate. |
| Major | The generated record drops both water rows and the 10 ml stock addition. | JCM 226 lists 1 L final distilled water, 10 ml Czapek concentrate, and 100 ml concentrate water; none survive in the generated record. | Add the missing final and stock water/addition rows in the maintained fungal source. |
| Minor | NaNO3 still carries a deprecated legacy MIM secondary grounding. | The primary NaNO3 `term` is exact `CHEBI:63005`, but `mediaingredientmech_term` remains `MediaIngredientMech:000171`. | Refresh the NaNO3 secondary term to `mediaingredientmech_chebi_term: CHEBI:63005`. |

## Recommended Edits

1. Represent JCM 226 as a final recipe that adds 10 ml/L Czapek concentrate.
2. Move NaNO3, KCl, MgSO4 x 7 H2O, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, and
   CuSO4 x 5 H2O into that Czapek concentrate stock with 100 ml distilled water.
3. Restore final K2HPO4, yeast extract, sucrose, agar, and water to the exact
   JCM table values.
4. Regenerate and ensure this direct JCM/MediaDive import merges with repaired
   TOGO M219.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the edited
  fungal source and regenerated merged record.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare both CYA imports against JCM 226 to ensure only one CYA
  generated record remains and the stock boundary is intact.

## Additional Notes

- JCM's global header says to autoclave media at 121 deg C for 15 minutes
  unless otherwise stated. The current record does not encode that default.
