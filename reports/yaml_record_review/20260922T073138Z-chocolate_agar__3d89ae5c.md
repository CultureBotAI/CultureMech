# YAML Record Review: chocolate agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chocolate_agar__3d89ae5c.yaml
- Started UTC: 2026-09-22T07:29:25Z
- Finished UTC: 2026-09-22T07:31:48Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009500 |
| Label | chocolate agar |
| Generated record | data/merge_yaml/merged/chocolate_agar__3d89ae5c.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2977_chocolate_agar.yaml |
| Source | TOGO Medium M2977 |

The reviewed file is a generated one-source merge of TOGO M2977. Most source
repairs already belong to the maintained owner
`data/normalized_yaml/bacterial/TOGO_M2977_chocolate_agar.yaml`; the generated
record needs regeneration from that current owner.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chocolate_agar__3d89ae5c.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO API request failed on DNS resolution inside the sandbox and then
passed when retried directly. The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The record identity is coherent: `CultureMech:009500`, `TOGO:M2977`, the
generated merge fingerprint, and the maintained owner all denote TOGO
`chocolate agar`.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2977 source ID, normalized owner stem, and merge fingerprint found this
generated record, its TOGO owner, and normalized index entries.

## Evidence

TOGO M2977 supports one liter of chocolate agar with bacitracin and an
incubation temperature of 37 C. It does not state the bacitracin amount.

The generated record is stale relative to its maintained owner. The current
normalized owner has repaired the source import by representing Chocolate agar
as 1000 mL/L, adding bacitracin with a variable concentration, adding
`temperature_value: 37.0`, adding `references`, and documenting the source
limitations in notes and `data_quality_flags`. The August generated record
still has only a lower-case `chocolate agar` ingredient at `1 G_PER_L` and has
none of those September 2026 owner repairs.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO source record.

The source itself is coarse: it names chocolate agar with bacitracin but does
not provide a full chocolate agar formulation or a bacitracin amount. The
current maintained owner captures that limitation better than the generated
record.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The generated record is stale and lacks the repaired 1000 mL/L Chocolate agar amount, bacitracin inhibitor, 37 C temperature, reference, data-quality flags, and source-limitation notes already present in `data/normalized_yaml/bacterial/TOGO_M2977_chocolate_agar.yaml`. **Owner:** generated merge output; regenerate after verifying the maintained owner. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/chocolate_agar__3d89ae5c.yaml` from the
   current TOGO M2977 normalized owner.
2. Preserve the current owner-level caution that TOGO M2977 names chocolate
   agar with bacitracin but does not state the bacitracin amount.
3. After regeneration, compare the generated output against TOGO M2977 and the
   September repair event.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually confirm that the regenerated record includes Chocolate agar,
bacitracin, the 37 C temperature, the TOGO URL reference, and the explicit note
that the bacitracin amount is not stated.

## Additional Notes

None found.
