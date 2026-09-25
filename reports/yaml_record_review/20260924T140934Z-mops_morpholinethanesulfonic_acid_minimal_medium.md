# YAML Record Review: mops_morpholinethanesulfonic_acid_minimal_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mops_morpholinethanesulfonic_acid_minimal_medium.yaml
- Started UTC: 2026-09-24T14:08:23Z
- Finished UTC: 2026-09-24T14:09:34Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mops_morpholinethanesulfonic_acid_minimal_medium.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:009501`
- Label: `mops_morpholinethanesulfonic_acid_minimal_medium`
- Original label: `MOPS (morpholinethanesulfonic acid) minimal medium`
- Category: `bacterial`
- Media source: `TOGO:M2978`
- Generated status: generated merge output
- Maintained owner: `data/normalized_yaml/bacterial/mops_morpholinethanesulfonic_acid_minimal_medium.yaml`

The generated record and maintained normalized record are identical except for the generated merge history appended to `curation_history`.

## Validation

Validation was run on the generated merged YAML.

- Open LinkML schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mops_morpholinethanesulfonic_acid_minimal_medium.yaml`
  - Result: passed with `No issues found`.
- Strict validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mops_morpholinethanesulfonic_acid_minimal_medium.yaml --out /private/tmp/mops_morpholinethanesulfonic_acid_minimal_medium.strict.tsv --workers 1 --quiet`
  - Result: passed; the TSV contained only the header, so 0 strict errors were reported.
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mops_morpholinethanesulfonic_acid_minimal_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 0 reference checks were evaluated.
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mops_morpholinethanesulfonic_acid_minimal_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed after the known `eutils` / `pkg_resources` warning.
- Embedded merge history:
  - Result: not checked. The repository history validator targets standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record identity is correctly scoped to TOGO Medium `M2978`, `MOPS (morpholinethanesulfonic acid) minimal medium`.

The TOGO API for `M2978` returns the same medium name and a two-part ingredient payload:

- The unnamed main component lists quantified `NaCl`, `NH4Cl`, `K2HPO4`, `MOPS`, `MgCl2`, `K2SO4`, `FeSO4`, and `Tricine`, plus unquantified `CaCl2` and a `Micronutrients` stock reference.
- The `Micronutrients` component lists `H3BO3`, `CuSO4`, `CoCl2`, `MnCl2`, `ZnSO4`, and `(NH4)6(MO7)24` without per-ingredient amounts.

The eight quantified main-medium rows in CultureMech match TOGO's millimolar concentrations exactly:

| Ingredient | TOGO M2978 amount | CultureMech amount | Status |
| --- | ---: | ---: | --- |
| `NaCl` | 50 mM | 50 mM | supported |
| `NH4Cl` | 9.52 mM | 9.52 mM | supported |
| `K2HPO4` | 1.32 mM | 1.32 mM | supported |
| `MOPS` | 40 mM | 40 mM | supported |
| `MgCl2` | 0.523 mM | 0.523 mM | supported |
| `K2SO4` | 0.276 mM | 0.276 mM | supported |
| `FeSO4` | 0.01 mM | 0.01 mM | supported |
| `Tricine` | 4 mM | 4 mM | supported |

Grounding is mostly narrow for the grounded salts and buffer rows. The source gaps are retained as `VARIABLE`, so the importer did not invent unsupported amounts for `CaCl2`, the `Micronutrients` stock, or the six micronutrient members.

## Evidence

Supported by TOGO `M2978`:

- `media_term.term.id` and label match the TOGO medium.
- The eight quantified main-medium molarities are imported faithfully.
- `CaCl2`, `Micronutrients`, `H3BO3`, `CuSO4`, `CoCl2`, `MnCl2`, `ZnSO4`, and `(NH4)6(MO7)24` are present in TOGO but have no recoverable amount in the TOGO payload that was inspected.

Unsupported or unresolved:

- The CultureMech recipe still has no numeric amount for `CaCl2` or any micronutrient row.
- `(NH4)6(MO7)24` has no `term` or `mediaingredientmech_chebi_term`. The 2026-02-06 import history says one invalid CHEBI ID from MicrobeMediaParam was removed, which is consistent with this row having no valid local grounding after cleanup.
- TOGO `M2978` does not expose a nonempty upstream `src_url`; the record therefore has no inspectable primary provider or publication URL beyond the TOGO medium page.

## Completeness

The formula is not complete enough for unambiguous use: calcium chloride and the micronutrient stock are mandatory-looking formula rows, but TOGO does not provide their amounts.

An exact gitignore-independent search with `rg --no-ignore --hidden` covered `data/normalized_yaml` and `data/merge_yaml` for the slug, the exact source label, `TOGO:M2978`, and `M2978` as a bounded identifier. It found only the maintained normalized record, this generated record, and generated index projections; no duplicate recipe record for `TOGO:M2978` was found in those data directories.

Empty optional fields are not defects in this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The MOPS minimal formula is incomplete because `CaCl2`, `Micronutrients`, and all six micronutrient members have schema-defaulted `VARIABLE` concentrations. | TOGO `M2978` exposes those rows without amounts; `schema-defaulter-v1.0` then defaulted all eight missing concentrations in this record. | `data/normalized_yaml/bacterial/mops_morpholinethanesulfonic_acid_minimal_medium.yaml` |
| Minor | The ammonium molybdate-like `(NH4)6(MO7)24` row is not grounded to CHEBI or MediaIngredientMech. | The source string is chemically ambiguous and no valid CHEBI remained after `invalid-chebi-removal`. | `data/normalized_yaml/bacterial/mops_morpholinethanesulfonic_acid_minimal_medium.yaml` |
| Minor | The record lacks exact upstream source provenance beyond TOGO. | The TOGO `M2978` `src_url` value is empty, so only TOGO could be inspected for this review. | `data/normalized_yaml/bacterial/mops_morpholinethanesulfonic_acid_minimal_medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/mops_morpholinethanesulfonic_acid_minimal_medium.yaml`, inspect upstream MOPS minimal-medium literature or provider records and add supported concentrations for `CaCl2`, the `Micronutrients` stock, and each micronutrient member if a source can be identified.
2. If no source supports the unquantified micronutrient members, keep the stock unresolved or remove unsupported decomposed stock members instead of preserving individual variable rows that look like a complete defined solution.
3. Resolve `(NH4)6(MO7)24` against the upstream source before adding a CHEBI term; if the upstream source cannot disambiguate the formula, leave it ungrounded and add a note that the imported TOGO formula string is ambiguous.
4. Preserve the TOGO `M2978` media term but add any exact publication, protocol, or provider source found during follow-up curation.
5. Regenerate `data/merge_yaml/merged/mops_morpholinethanesulfonic_acid_minimal_medium.yaml` from the maintained normalized record rather than editing the generated file directly.

## Follow-up Checks

- Re-run open schema validation on the regenerated merged YAML.
- Re-run `scripts/validate_strict.py` on the regenerated merged YAML and confirm the TSV remains header-only.
- Re-run `linkml-reference-validator` and `linkml-term-validator` to confirm any new ingredient groundings resolve.
- Manually compare every curated `CaCl2` and micronutrient amount against the exact upstream source text, because TOGO `M2978` currently omits those amounts.
- Repeat the bounded ignored-inclusive duplicate search for `TOGO:M2978` and `M2978` if follow-up curation adds or merges any adjacent record.

## Additional Notes

- The generated `medium_type: COMPLEX` and `composition_type: UNDEFINED` values follow from the retained open-ended micronutrient rows. They should become `DEFINED` only if every retained micronutrient component is assigned a supported quantity.
- `Tricine` has a CHEBI `term` but lacks a `mediaingredientmech_chebi_term`, and `MnCl2` has the same mirror gap. That is an enrichment gap, not an identity problem for this review.
