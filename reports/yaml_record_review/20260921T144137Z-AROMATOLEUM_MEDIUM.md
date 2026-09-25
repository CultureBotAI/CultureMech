# YAML Record Review: AROMATOLEUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AROMATOLEUM_MEDIUM.yaml
- Started UTC: 2026-09-21T14:40:00Z
- Finished UTC: 2026-09-21T14:41:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001192` |
| Generated record | `data/merge_yaml/merged/AROMATOLEUM_MEDIUM.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/aromatoleum_medium.yaml` |
| Merge input | `aromatoleum_medium` |
| Name | `aromatoleum_medium` |
| Original/source label | `AROMATOLEUM MEDIUM` |
| Source grounding | DSMZ / MediaDive medium `1712`, `mediadive.medium:1712` |

The generated merge has one normalized source recipe, so future corrections
belong in `data/normalized_yaml/bacterial/aromatoleum_medium.yaml` followed by
merge regeneration.

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AROMATOLEUM_MEDIUM.yaml` returned `No issues found`. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AROMATOLEUM_MEDIUM.yaml --out /private/tmp/aromatoleum_medium.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| Reference validation | Pass with no reference checks. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AROMATOLEUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported one file validated, zero checks, and all validations passed. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AROMATOLEUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported `Validation passed` after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/*.yaml` records, not a focused validator for `MediaRecipe.curation_history` arrays embedded in one generated merge. |
| DSMZ source retrieval | Pass. The cited DSMZ Medium 1712 PDF was fetched and extracted locally for source comparison. The extractor emitted CFF Type1 font warnings, but the formulation text was readable. |

The documented `just` entrypoints are currently blocked by the project
environment's Python 3.13 / `llvmlite==0.46.0` build failure, so the review used
the same focused validators through the Python 3.11 no-project workaround.

## Identity and Grounding

The record denotes the intended DSMZ medium. The YAML declares
`CultureMech:001192`, `mediadive.medium:1712`, and
`AROMATOLEUM MEDIUM`; the inspected DSMZ PDF is titled
`1712. AROMATOLEUM MEDIUM`. An ignored-inclusive exact search found the same
stable ID and source accession in the ID registry, active recipe catalog,
global normalized index, MediaDive index, bacterial index, and target-specific
concentration-plausibility report rows.

The top-level medium identity is correct, but two hydrated or vitamer-specific
ingredient identities are wrong or under-specified:

- DSMZ lists `NiCl2 x 6H2O`; the YAML row is labeled `NiCl2 x 6 H2O` but both
  the primary term and the MIM link point to `CHEBI:34887`, nickel dichloride,
  instead of the hexahydrate-specific identity. The packaged MIM label index
  has a `NiCl2 x 6 H2O` mapping to `CHEBI:53542`.
- DSMZ lists `Pyridoxolhydrochloride`; the YAML uses
  `Pyridoxal hydrochloride` grounded to `CHEBI:131529`. Pyridoxol and
  pyridoxal are different vitamin B6 forms, so the source string must be
  re-grounded instead of treated as pyridoxal.

## Evidence

Supported by the inspected DSMZ PDF:

- DSMZ Medium 1712 is based on Rabus and Widdel 1995 and is named
  `AROMATOLEUM MEDIUM`.
- The anoxic base medium consists of `KH2PO4`, `NH4CL`, `MgSO4 x 7H2O`,
  `CaCl2 x 2H2O`, `NaNO3`, and `distilled water 950 mL`.
- After autoclaving and cooling to 85 C under `N2`, DSMZ adds six stocks to
  the base: Trace element solution at `1.0 mL/L`, Vitamin mixture at
  `1.0 mL/L`, Vitamin B12 solution at `1.0 mL/L`, `1 M NaHCO3` at
  `40.0 mL/L`, `1 M Ascorbate` at `4.0 mL/L`, and `1 M Benzoate` at
  `4.0 mL/L`.
- DSMZ gives separate stock recipes and preparation instructions for the Trace
  element solution, Vitamin mixture, Vitamin B12 solution, Bicarbonate
  solution, Ascorbate solution, and Benzoate solution.

Unsupported in the YAML:

- The base salts are scaled by `1 / 0.95` from the 950 mL water volume even
  though DSMZ subsequently brings the formulation close to 1 L with stock
  additions.
- All Trace element solution components are stored as direct final ingredients
  at their 1 L stock-recipe quantities.
- All Vitamin mixture components are stored as direct final ingredients at
  their 100 mL stock-recipe quantities converted to g/L.
- Cyanocobalamine is stored as the 50 mL Vitamin B12 stock concentration
  instead of as a `1.0 mL/L` Vitamin B12 solution addition.
- `NaHCO3`, `Ascorbic acid`, and `Sodiumbenzoate` are stored at the 1 M stock
  strengths instead of at 40, 4, and 4 mL/L stock additions.
- The four water rows from the distinct base and stock recipes were summed into
  one `Double distilled water` row at `1250.0 G_PER_L`.

## Completeness

The record is structurally valid but it is not complete enough to reproduce
DSMZ Medium 1712 because stock-solution boundaries were flattened. A user
would prepare the trace element, vitamin, bicarbonate, ascorbate, and benzoate
stock recipes as if they were direct final-medium rows.

The existing preparation steps partly preserve the stock-solution protocols,
but they are detached from represented `solutions`: steps 3-4 describe the
trace element stock, step 5 the Vitamin mixture, step 6 the Vitamin B12
solution, step 7 the bicarbonate solution, step 8 the ascorbate solution, and
step 9 the benzoate solution. The YAML does not name those stock recipes as
the scope of each step.

An ignored-inclusive exact search of the report directory found no prior
`*AROMATOLEUM_MEDIUM.md` report before this one was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DSMZ stock solutions were flattened into final-medium ingredients with stock concentrations. | DSMZ lists Trace element, Vitamin mixture, Vitamin B12, Bicarbonate, Ascorbate, and Benzoate as separate stock additions at `1`, `1`, `1`, `40`, `4`, and `4 mL/L`; the YAML stores their internal stock compositions as direct `G_PER_L` rows. | `data/normalized_yaml/bacterial/aromatoleum_medium.yaml` |
| Major | The base medium amounts were normalized against the 950 mL water addition instead of the final stock-complemented medium. | DSMZ lists `0.5 g` `KH2PO4`, `0.3 g` `NH4CL`, `0.5 g` `MgSO4 x 7H2O`, `0.1 g` `CaCl2 x 2H2O`, and `0.6 g` `NaNO3` before the 950 mL water and stock additions; the YAML stores them as `0.526316`, `0.315789`, `0.526316`, `0.105263`, and `0.631579 G_PER_L`. | `data/normalized_yaml/bacterial/aromatoleum_medium.yaml` |
| Major | Two ingredient identities do not preserve the source chemical forms. | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride, and `Pyridoxolhydrochloride` is represented as pyridoxal hydrochloride. | `data/normalized_yaml/bacterial/aromatoleum_medium.yaml` |

No blockers: the YAML is syntactically valid and points to the intended DSMZ
medium.

No minor findings beyond the material stock-boundary, arithmetic, and chemical
identity issues above.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/aromatoleum_medium.yaml`, split DSMZ
   Medium 1712 into the anoxic base medium plus named Trace element, Vitamin
   mixture, Vitamin B12, Bicarbonate, Ascorbate, and Benzoate stock additions
   using the source-stated `mL/L` addition volumes.
2. Move the trace element, vitamin, Vitamin B12, bicarbonate, ascorbate, and
   benzoate component rows into their owning stock solution records or nested
   solution descriptors; do not leave stock concentrations as direct final
   `ingredients`.
3. Restore the source-stated base-medium gram amounts and water volume without
   summing water from unrelated stock recipes.
4. Re-ground `NiCl2 x 6 H2O` to the hydrate-specific CHEBI identity and
   re-check the pyridoxol hydrochloride row against an exact vitamin B6
   hydrochloride identifier before writing a replacement.
5. Attach each stock-preparation step to its stock solution, append a curation
   event, and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Re-run the focused schema, strict, term, and reference validators on the
  normalized owner and regenerated merged record.
- Run `just verify-merges` after regenerating merge outputs.
- Re-run the concentration-plausibility report or an exact ignored-inclusive
  `rg` over `data/import_tracking/reports/concentration_plausibility.tsv` to
  confirm `CultureMech:001192` no longer appears for stock concentration or
  water-as-mass rows.
- Inspect the regenerated record manually to ensure each DSMZ stock component
  is scoped to its own stock and each final anoxic-medium stock addition
  retains the correct `mL/L` value.

## Additional Notes

The generated record is number 518 of 6286 in the case-folded
`data/merge_yaml/merged/*.yaml` review order used by this bulk pass.
