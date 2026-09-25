# YAML Record Review: chocolate agar plates (supplemented with 1% isovitalex)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chocolate_agar_plates_supplemented_with_1_isovitalex.yaml
- Started UTC: 2026-09-22T07:35:14Z
- Finished UTC: 2026-09-22T07:37:15Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009498 |
| Label | chocolate agar plates (supplemented with 1% isovitalex) |
| Generated record | data/merge_yaml/merged/chocolate_agar_plates_supplemented_with_1_isovitalex.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chocolate_agar_plates_supplemented_with_1_isovitalex.yaml |
| Source | TOGO Medium M2975 |

The reviewed file is a generated one-source merge of TOGO M2975. Source-level
repairs already belong to the maintained owner
`data/normalized_yaml/bacterial/chocolate_agar_plates_supplemented_with_1_isovitalex.yaml`;
the generated record needs regeneration from that current owner.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chocolate_agar_plates_supplemented_with_1_isovitalex.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO API request failed on DNS resolution inside the sandbox and then
passed when retried directly. The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The record identity is coherent: `CultureMech:009498`, `TOGO:M2975`, the
normalized owner, and the generated fingerprint all denote TOGO
`chocolate agar plates (supplemented with 1% isovitalex)`.

An exact ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2975 source ID, normalized owner stem, and merge fingerprint found this
generated record, its TOGO owner, and normalized index entries.

## Evidence

TOGO M2975 supports growth of `H. influenzae` strains at 37 C in room air or
5% CO2, where indicated, on chocolate agar plates supplemented with 1%
IsoVitaleX from BD Biosciences. It does not disclose the chocolate agar plate
formulation or amount.

The generated record is stale relative to its maintained owner. The current
normalized owner records 1.0% v/v IsoVitaleX, keeps chocolate agar plates at a
deliberately variable concentration, removes the default CO2 ingredient,
records `temperature_value: 37.0`, adds the TOGO URL reference, and documents
the sparse source limitation. The August generated record still has 1% w/v
`isovitalex (BD Biosciences)`, a default variable CO2 ingredient, and lacks the
September 2026 repair event and source-limitation fields.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO source record.

The source is sparse but the current maintained owner captures that limitation.
The generated record is incomplete until it is regenerated from the repaired
normalized YAML.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The generated record is stale and lacks the corrected IsoVitaleX unit, removal of the default CO2 ingredient, 37 C temperature, reference, data-quality flags, source notes, and September 2026 repair event already present in the maintained M2975 owner. **Owner:** generated merge output; regenerate after verifying the maintained owner. |

## Recommended Edits

1. Regenerate the generated M2975 YAML from the current
   `data/normalized_yaml/bacterial/chocolate_agar_plates_supplemented_with_1_isovitalex.yaml`
   owner.
2. Preserve the owner-level note that TOGO M2975 does not state the chocolate
   agar plate amount or formulation.
3. After regeneration, compare the generated output against TOGO M2975 and the
   September `RESOLVED_TOGO_M2975_CHOCOLATE_ISOVITALEX_SCORE15` repair event.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually confirm that the generated record includes Chocolate agar plates,
1.0% v/v IsoVitaleX, 37 C, the TOGO URL reference, and the explicit note that
the plate formulation is not stated.

## Additional Notes

None found.
