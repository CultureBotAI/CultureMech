# YAML Record Review: anoxynatronum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ANOXYNATRONUM_MEDIUM.yaml
- Started UTC: 2026-09-21T13:20:30Z
- Finished UTC: 2026-09-21T13:21:06Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:000869 |
| Label | anoxynatronum_medium |
| Original label | ANOXYNATRONUM MEDIUM |
| Source term | mediadive.medium:1408 |
| Maintained owner | data/normalized_yaml/bacterial/anoxynatronum_medium.yaml |
| Generated record | data/merge_yaml/merged/ANOXYNATRONUM_MEDIUM.yaml |

This is a generated merge record derived from one normalized MediaDive/DSMZ
owner. Fixes should land in `data/normalized_yaml/bacterial/anoxynatronum_medium.yaml`
or the DSMZ import mapping that produced it, then the generated merge should be
rebuilt.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANOXYNATRONUM_MEDIUM.yaml` returned `No issues found`. |
| Strict schema | Passed: `scripts/validate_strict.py data/merge_yaml/merged/ANOXYNATRONUM_MEDIUM.yaml --workers 1 --quiet` scanned 1 file and emitted 0 error rows. |
| References | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/ANOXYNATRONUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` found 0 active checks and reported all validations passed. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/ANOXYNATRONUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone files under `history/`, not a focused validator for one embedded `MediaRecipe.curation_history` block in a generated merge. |

The repository's documented `just validate-schema`, `just validate-strict`,
`just validate-references`, and `just validate-terms` wrappers are currently
blocked before target-specific validation by the project `uv` environment
attempting to build `llvmlite==0.46.0` under Python 3.13 and failing inside
`setuptools` with `TypeError: Popen.__init__() got an unexpected keyword
argument 'dry_run'`. The equivalent validators above were run through
`uv --no-project` on Python 3.11 with the same schema and target file.

## Identity and Grounding

The record correctly identifies DSMZ Medium 1408, `ANOXYNATRONUM MEDIUM`, as
imported through MediaDive accession 1408. The cited DSMZ PDF is live and
contains the same title and medium number.

The represented solutes agree with the source: 15 g/L NaCl, 10 g/L Yeast
Extract, and 8 g/L NaCO3. The two grounded defined solutes use appropriate
ChEBI terms for sodium chloride and sodium carbonate. The unresolved Yeast
Extract term is acceptable for this complex undefined ingredient.

## Evidence

The inspected DSMZ PDF supports the record's DSMZ 1408 identity, complex
liquid classification, pH 10.0, NaCl at 15 g/L, Yeast Extract at 10 g/L, and
NaCO3 at 8 g/L. It also supports the preparation text captured in the record:
prepare the liquid medium, adjust to pH 10.0, dispense into serum bottles under
N2, and autoclave.

The record is not over-scoped to a target organism, strain, or growth result.
`Microbial cultivation` is a generic application consistent with a DSMZ
cultivation medium.

## Completeness

The DSMZ source includes distilled water at 1000 ml. That final-volume
component is absent from the generated record, so a curator reading only the
YAML sees normalized g/L solute concentrations but not the source's explicit
water row.

An ignored-inclusive exact search for
`CultureMech:000869|mediadive.medium:1408|ANOXYNATRONUM_MEDIUM|DSMZ_Medium1408|anoxynatronum_medium`
covered `data`, `src`, `reports`, `.claude`, `CLAUDE.md`, and `justfile`.
It found the normalized owner, generated merge, registry/catalog/index rows,
and archived validation output only; it found no second maintained owner for
DSMZ Medium 1408.

Empty optional `target_organisms`, `discussion`, and `quality_flags` fields
are not defects here because the source medium recipe does not assert a
strain-specific growth result or name a conflict requiring a flag.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| minor | The source water/final-volume row is omitted. | The DSMZ 1408 PDF lists `Distilled Water 1000.0 ml`; the record contains only NaCl, Yeast extract, and NaCO3. | `data/normalized_yaml/bacterial/anoxynatronum_medium.yaml`; DSMZ/MediaDive import mapping |
| minor | The preparation action enum contradicts the liquid serum-bottle protocol. | `physical_state` is `LIQUID`, the DSMZ PDF says to dispense the liquid medium into serum bottles under N2, and the free-text step preserves that; only the structured `action: POUR_PLATES` is plate-specific. | `data/normalized_yaml/bacterial/anoxynatronum_medium.yaml`; preparation-step action mapping |

## Recommended Edits

1. Preserve the DSMZ `Distilled Water 1000.0 ml` row, or otherwise store an
   explicit final-volume/water component through the normalized DSMZ owner if
   the schema has a preferred representation.
2. Change the structured preparation action from `POUR_PLATES` to a liquid
   medium action that matches the existing DSMZ text; preserve the pH 10.0, N2
   gassing, serum-bottle dispensing, and autoclaving details.

## Follow-up Checks

- Re-run `just validate data/normalized_yaml/bacterial/anoxynatronum_medium.yaml`,
  `just validate-strict data/normalized_yaml/bacterial/anoxynatronum_medium.yaml`,
  `just validate-terms data/normalized_yaml/bacterial/anoxynatronum_medium.yaml`,
  and `just validate-references data/normalized_yaml/bacterial/anoxynatronum_medium.yaml`
  after the normalized owner or importer is changed.
- Re-run `just verify-merges` after regenerating `data/merge_yaml/merged/`.
- Compare the regenerated merge against DSMZ Medium 1408 and confirm the three
  solute rows, pH 10.0, serum-bottle/N2/autoclave preparation text, and 1000 ml
  water/final-volume representation all remain source supported.

## Additional Notes

DSMZ prints the third solute as `NaCO3`. The current row preserves that source
label while grounding the material to sodium carbonate; I did not flag that as
a grounding defect because the human-readable DSMZ medium names sodium
carbonate by context, and there is no adjacent unsupported ingredient in this
record.
