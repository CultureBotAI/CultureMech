# YAML Record Review: Chopped meat medium with 1% glucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium_with_1_glucose.yaml
- Started UTC: 2026-09-22T08:21:30Z
- Finished UTC: 2026-09-22T08:23:19Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009305 |
| Label | Chopped meat medium with 1% glucose |
| Generated record | data/merge_yaml/merged/chopped_meat_medium_with_1_glucose.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_medium_with_1_glucose.yaml |
| Source | TOGO Medium M2754, ATCC Medium 735 |

The reviewed file is a generated one-source merge of the TOGO M2754 / ATCC
Medium 735 normalized owner. Future source corrections belong in
`data/normalized_yaml/bacterial/chopped_meat_medium_with_1_glucose.yaml` or
the TOGO importer; this generated merge needs regeneration after the
September 2026 normalized repair.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium_with_1_glucose.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is coherent: `CultureMech:009305`, `TOGO:M2754`, the ATCC
PDF fingerprint `0AB039CD914D4A9BAC9CAB709196F694`, the maintained owner stem,
and the generated merge fingerprint all denote ATCC Medium 735, Chopped meat
medium with 1% glucose.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml`, `data/merge_yaml/merged`, the registry and catalog
TSVs, and `data/import_tracking/reports` for the CultureMech ID, TOGO ID,
ATCC PDF fingerprint, maintained owner stem, and merge fingerprint found this
generated record, its maintained owner, normalized indexes, the linked ATCC
Medium 593 parent, and diagnostic registry or import-tracking rows for this
record.

The generated record no longer agrees with its maintained owner. The owner was
repaired on 2026-09-11, grounds ATCC Medium 735 as ATCC Medium 593 plus
10 g/L glucose, fixes the N NaOH and resazurin volumes to `ML_PER_L`, adds
pH 7.0, adds ATCC preparation steps, and links the recipe as a supplemented
variant of `TOGO_M2710_Chopped_meat_medium`.

## Evidence

The inspected TOGO M2754 JSON and ATCC Medium 735 PDF support a 1 L recipe
starting with 500 g fat-free ground beef, 1.0 L distilled water, and 25 mL
N NaOH. The boiled meat extract is cooled, skimmed, and filtered while
retaining both meat particles and filtrate, then the filtrate is restored to
1 L with distilled water.

ATCC then adds 30 g peptone, 5 g yeast extract, 5 g `K2HPO4`, 10 g glucose,
and 4 mL 0.025% resazurin solution to the filtrate. The medium is boiled,
cooled, supplemented with 0.5 g L-cysteine HCl, adjusted to pH 7.0, dispensed
as 7 mL over one part meat particles to four to five parts fluid under 97% N2 /
3% H2, capped under N2/H2 with butyl rubber stoppers, and autoclaved for 15
minutes under fast exhaust.

The generated record still carries stale pre-repair modeling: 1 L water is
1 g/L, 25 mL N NaOH is a direct 25 g/L ingredient, and 4 mL 0.025% resazurin
solution is an empty `G_PER_L` solution shell. It also lacks the ATCC
preparation workflow, pH 7.0, source references, and the parent/variant link
that are now present in the maintained owner.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO/ATCC source record.

The generated record is incomplete until it reflects the repaired maintained
owner: `ML_PER_L` solution entries for N NaOH and 0.025% resazurin solution,
explicit pH and preparation steps, references, quality flags, and the ATCC
Medium 593 supplemented-variant relationship.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The generated record is stale relative to the maintained owner repaired on 2026-09-11: 1 L water, 25 mL N NaOH, and 4 mL 0.025% resazurin solution are still mis-modeled as `G_PER_L` quantities. **Owner:** regenerate `data/merge_yaml/merged/chopped_meat_medium_with_1_glucose.yaml` from `data/normalized_yaml/bacterial/chopped_meat_medium_with_1_glucose.yaml`. |
| Major | The generated record omits owner-only curation added in the 2026-09-11 repair, including pH 7.0, five ATCC preparation steps, source references, data-quality flags, and the ATCC Medium 593 supplemented-variant link. **Owner:** regenerated merge output. |
| Major | The generated `0.025% Resazurin solution` remains an empty solution shell instead of the repaired `4.0 ML_PER_L` solution entry with source notes and term grounding. **Owner:** already fixed in the maintained owner; rerun the merge. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/chopped_meat_medium_with_1_glucose.yaml`
   from the current maintained owner.
2. Preserve the repaired `ML_PER_L` amounts for 1 L water, 25 mL N NaOH, and
   4 mL 0.025% resazurin solution.
3. Preserve pH 7.0, the five ATCC preparation steps, the source references,
   quality flags, and the `SUPPLEMENTED_VARIANT` link to
   `TOGO_M2710_Chopped_meat_medium`.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then diff the regenerated record against the repaired maintained owner to
confirm that water, N NaOH, resazurin, pH, ATCC preparation steps, and the
parent/variant relationship reflect the 2026-09-11 repair.

## Additional Notes

None found.
