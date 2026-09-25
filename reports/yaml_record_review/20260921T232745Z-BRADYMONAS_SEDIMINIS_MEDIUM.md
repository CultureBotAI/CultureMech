# YAML Record Review: BRADYMONAS SEDIMINIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml
- Started UTC: 2026-09-21T23:27:45Z
- Finished UTC: 2026-09-21T23:29:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001064 |
| Label | BRADYMONAS SEDIMINIS MEDIUM |
| Merge source | data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml |
| Source accession | mediadive.medium:1588 |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | fde855917236472e9be7eb6d60e78de8e87cec132bba5dcca87be217212f5f79 |

The reviewed file is a derived merge record. The authoritative owned record is
`data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml`; future
scientific fixes should be made there or in the MediaDive importer path that
owns the flattening behavior, then `data/merge_yaml/merged/` should be
regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml --out /private/tmp/BRADYMONAS_SEDIMINIS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `CultureMech:001064`, `name: bradymonas_sediminis_medium`,
  `media_term: mediadive.medium:1588`, and the source PDF
  `DSMZ_Medium1588.pdf` all identify DSMZ Medium 1588, BRADYMONAS SEDIMINIS
  MEDIUM.
- A gitignore-independent search for `mediadive.medium:1588`,
  `CultureMech:001064`, the merge fingerprint, the normalized slug, and the
  uppercase DSMZ label across `data`, `src`, `scripts`, `docs`, `.claude`, and
  `justfile` found one authoritative normalized record plus the derived merge
  and generated indexes; it did not find a second maintained sibling recipe for
  DSMZ 1588.
- The ingredient groundings that are present preserve exact hydrates for
  `CaCl2 x 2 H2O`, `MgCl2 x 6 H2O`, and `MgSO4 x 7 H2O`. `Natural sea water`
  is intentionally unresolved in the current record.

## Evidence

The DSMZ 1588 PDF supports the top-level identity, final-medium table, pH
adjustment sequence, agar autoclaving step, post-autoclave sea-water addition,
and aged-natural-seawater note. The record, however, blends the substitute
artificial sea water recipe into the final medium instead of keeping it as an
alternative solution recipe.

DSMZ lists the final formulation as peptone 10.0 g, meat extract 3.0 g, NaCl
5.0 g, D(+)-trehalose 1.0 g, agar 19.0 g if appropriate, tap water 250.0 ml,
and sea water 750.0 ml. It then states that aged natural sea water can be
replaced by an artificial sea water recipe made separately from NaCl 28.13 g,
KCl 0.77 g, CaCl2 x 2 H2O 1.60 g, MgCl2 x 6 H2O 4.80 g, NaHCO3 0.11 g,
MgSO4 x 7 H2O 3.50 g, and distilled water 1000.0 ml.

## Completeness

- Consequential gap: no `SolutionRecipe` represents the artificial sea water
  fallback, so its salts are indistinguishable from final-medium components.
- Consequential gap: the 1000.0 ml distilled water in the artificial sea water
  fallback is absent.
- Consequential gap: the two source volumes, 250.0 ml tap water and 750.0 ml
  sea water, are represented as gram-per-liter masses.
- Empty optional organism and growth slots are acceptable for a source-only
  DSMZ formulation; no inspected growth paper was attached to this record.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `BRADYMONAS_SEDIMINIS_MEDIUM` report, so this report did not overwrite an
  earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The final medium is polluted with artificial sea water stock ingredients. `KCl`, `CaCl2 x 2 H2O`, `MgCl2 x 6 H2O`, `NaHCO3`, and `MgSO4 x 7 H2O` are listed as direct final-medium ingredients even though DSMZ puts them only under the substitute artificial sea water recipe. | DSMZ Medium 1588 lists aged natural sea water at 750.0 ml in Solution A, then introduces a separate artificial sea water recipe to use only if natural sea water is unavailable. | `data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml`; likely also the MediaDive import normalization rule for nested fallback formulations |
| Major | The NaCl concentration is arithmetically unsupported. The record's `33.129999999999995 G_PER_L` is the sum of the final-medium NaCl `5.0 g` and the artificial sea water NaCl `28.13 g`, but DSMZ does not add a full liter of artificial sea water on top of Solution A. | DSMZ separates `NaCl 5.0 g` in Solution A from `NaCl 28.13 g` in the 1000.0 ml artificial sea water recipe that can replace the 750.0 ml sea-water aliquot. | `data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml`; likely also the MediaDive import normalization rule for nested fallback formulations |
| Major | Water volumes are converted to gram-per-liter ingredient concentrations. The record encodes `Tap water` as `250 G_PER_L` and `Natural sea water` as `750 G_PER_L`; DSMZ gives `250.0 ml` tap water and `750.0 ml` sea water. | The source units are explicit volume units, not masses. | `data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml` |
| Minor | The recipe provenance is only a free-text `notes` string imported from MediaDive. The record has no structured `sources`, `source_data`, or `references` entry for the DSMZ Medium 1588 PDF. | The only source pointer is `notes: 'Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1588.pdf'`, and the reference validator had 0 checks. | `data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml` or the MediaDive importer |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml`, restore
   the final Solution A formulation as peptone 10 g, meat extract 3 g, NaCl
   5 g, D(+)-trehalose 1 g, optional agar 19 g, tap water 250 ml, and sea water
   750 ml.
2. Represent artificial sea water as a separate fallback `SolutionRecipe` or
   an explicitly scoped alternate solution under the normalized owner, with
   NaCl 28.13 g, KCl 0.77 g, CaCl2 x 2 H2O 1.60 g, MgCl2 x 6 H2O 4.80 g,
   NaHCO3 0.11 g, MgSO4 x 7 H2O 3.50 g, and distilled water 1000.0 ml per
   liter of stock.
3. Change tap-water, sea-water, and fallback artificial-seawater additions from
   `G_PER_L` masses to volume-aware quantities.
4. Add structured DSMZ Medium 1588 source provenance so the PDF URL and source
   accession are machine-checkable instead of only present in `notes`.
5. Regenerate merged records and media pages after the maintained normalized
   input, or the importer that populates it, is corrected.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/bradymonas_sediminis_medium.yaml`
  after curation.
- Rerun the narrow LinkML, strict, term, and reference validators on the
  normalized owner and regenerated `data/merge_yaml/merged/BRADYMONAS_SEDIMINIS_MEDIUM.yaml`.
- Rerun `just verify-merges` to prove the generated merge is fresh.
- Manually compare the regenerated ingredient tree against DSMZ Medium 1588 to
  confirm artificial sea water is an alternative nested recipe, not a final
  direct ingredient group.

## Additional Notes

- The generated merge and its single normalized owner currently carry the same
  scientific representation, so the issue is not a stale merge.
- Optional empty slots were not treated as defects.
