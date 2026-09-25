# YAML Record Review: Chocolate Agar With 5% Sheep Blood

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chocolate_agar_with_5_sheep_blood.yaml
- Started UTC: 2026-09-22T07:40:33Z
- Finished UTC: 2026-09-22T07:41:47Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007904 |
| Label | Chocolate Agar With 5% Sheep Blood |
| Generated record | data/merge_yaml/merged/chocolate_agar_with_5_sheep_blood.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1366_Chocolate_Agar_With_5_Sheep_Blood.yaml |
| Source | TOGO Medium M1366, JCM Medium 1270 |

The reviewed file is a generated one-source merge of JCM 1270 through TOGO
M1366. Source-level repairs already belong to the maintained owner
`data/normalized_yaml/bacterial/TOGO_M1366_Chocolate_Agar_With_5_Sheep_Blood.yaml`;
the generated record needs regeneration from that current owner.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chocolate_agar_with_5_sheep_blood.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO and JCM requests failed on DNS resolution inside the sandbox and
then passed when retried directly. The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The record identity is coherent: `CultureMech:007904`, `TOGO:M1366`, JCM Medium
1270, and the generated merge fingerprint all denote Chocolate Agar With 5%
Sheep Blood.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M1366 source ID, JCM 1270 identifiers, normalized owner stem, and merge
fingerprint found this generated record, its maintained owner, a separate
direct JCM sibling record for GRMD 1270, and normalized index entries.

## Evidence

TOGO M1366 and JCM 1270 both support the same formula: 44.0 g Columbia blood
agar base (BD-Difco), 50.0 mL sheep blood, and 950.0 mL distilled water. JCM
also supports the preparation workflow: mix everything except sheep blood,
autoclave, cool to about 70 C, aseptically add 5% final sterile defibrinated
sheep blood, keep at 70 C for 15 minutes, cool to about 50 C, mix, and quickly
dispense into sterile petri dishes.

The generated record is stale relative to its maintained owner. The current
normalized owner uses `ML_PER_L` for the water and sheep-blood volumes, keeps
Columbia blood agar base at 44.0 g/L, splits the JCM preparation into five
structured steps, adds the autoclave sterilization method, adds TOGO and JCM
references, and documents the September 2026 source repair. The generated
record still has water and sheep blood as `G_PER_L` masses and lacks the
preparation, sterilization, data-quality, and reference fields.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO/JCM source record.

The generated record is incomplete until regenerated from the repaired
normalized YAML.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The generated record is stale and lacks the corrected mL water and blood units, JCM preparation steps, autoclave sterilization, references, data-quality flags, and September 2026 repair event already present in the maintained M1366 owner. **Owner:** generated merge output; regenerate after verifying the maintained owner. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/chocolate_agar_with_5_sheep_blood.yaml`
   from the current TOGO M1366 normalized owner.
2. Preserve the owner-level 950 mL water, 50 mL sheep blood, 44 g Columbia
   blood agar base, and five JCM preparation steps.
3. After regeneration, compare the generated output against TOGO M1366, JCM
   Medium 1270, and the direct JCM sibling record for the same GRMD page.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually confirm that the generated record includes the three source
ingredients with source units, all JCM preparation steps, and both TOGO and JCM
references.

## Additional Notes

None found.
