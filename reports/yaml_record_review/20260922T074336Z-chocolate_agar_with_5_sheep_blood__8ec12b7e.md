# YAML Record Review: CHOCOLATE AGAR WITH 5% SHEEP BLOOD

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chocolate_agar_with_5_sheep_blood__8ec12b7e.yaml
- Started UTC: 2026-09-22T07:42:34Z
- Finished UTC: 2026-09-22T07:44:07Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:002436 |
| Label | CHOCOLATE AGAR WITH 5% SHEEP BLOOD |
| Generated record | data/merge_yaml/merged/chocolate_agar_with_5_sheep_blood__8ec12b7e.yaml |
| Maintained owners | data/normalized_yaml/bacterial/chocolate_agar_with_5_sheep_blood.yaml; data/normalized_yaml/bacterial/brucella_agar.yaml |
| Sources | JCM Medium 1270; DSMZ Medium 584 |

The reviewed file is a generated false merge of two distinct direct
MediaDive-derived normalized records. Future fixes belong in merge fingerprint
logic that split `data/normalized_yaml/bacterial/chocolate_agar_with_5_sheep_blood.yaml`
from `data/normalized_yaml/bacterial/brucella_agar.yaml`; both owners have
already received September 2026 source repairs.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chocolate_agar_with_5_sheep_blood__8ec12b7e.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

This generated record is identity-conflicted. Its primary ID
`CultureMech:002436`, `mediadive.medium:J1270` media term, and original label
refer to JCM Medium 1270, CHOCOLATE AGAR WITH 5% SHEEP BLOOD. Its ingredients,
`brucella_agar` synonym, and `mediadive.medium:584` synonym source refer to DSMZ
Medium 584, BRUCELLA AGAR.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
`mediadive.medium:J1270`, `mediadive.medium:584`, JCM GRMD 1270 URL, and the
merge fingerprint found this generated false merge, its direct JCM owner, the
separate Brucella agar owner, the parallel TOGO/JCM M1366 record for GRMD 1270,
and normalized index entries.

## Evidence

The JCM GRMD 1270 page supports a three-component Chocolate Agar With 5% Sheep
Blood recipe: 44.0 g Columbia blood agar base (BD-Difco), 50.0 mL sheep blood,
and 950.0 mL distilled water, with sheep blood added after autoclaving and
cooling.

The DSMZ Medium 584 PDF supports a different recipe: prepare Brucella agar,
cool it to 50 C after autoclaving, and add 100 mL/L sheep blood. DSMZ 584 does
not mention Columbia blood agar base or JCM Medium 1270; JCM 1270 does not
mention Brucella agar.

The generated merge combines the two records into an invalid hybrid. It keeps
the JCM 1270 identity, uses the Brucella agar parent and 100 mL/L sheep blood
from the DSMZ 584 side at stale `G_PER_L` units, and keeps the old JCM
preparation text that incorrectly says to add horse blood.

## Completeness

The empty `target_organisms` and growth-observation fields are not the issue in
this record.

The generated record is unusable until the two owners are emitted as separate
records. The current normalized JCM and DSMZ owners each already carry
source-faithful ingredients, structured preparation steps, sterilization,
references, and data-quality flags.

## Findings

| Severity | Finding |
| --- | --- |
| Blocker | `chocolate_agar_with_5_sheep_blood__8ec12b7e.yaml` falsely merges JCM Medium 1270 with DSMZ Medium 584, so the generated record denotes two different media at once. **Owner:** merge fingerprint logic and any alias/KG-Microbe matching overlay that equates these records. |
| Major | The generated record also predates September repairs to both normalized owners, leaving stale g/L blood units and an unsupported horse-blood preparation sentence. **Owner:** generated merge output after the false merge is split. |

## Recommended Edits

1. Prevent `data/normalized_yaml/bacterial/chocolate_agar_with_5_sheep_blood.yaml`
   and `data/normalized_yaml/bacterial/brucella_agar.yaml` from merging.
2. Regenerate merged YAML so JCM Medium 1270 and DSMZ Medium 584 produce
   separate records from their current repaired owners.
3. Drop `brucella_agar`, `mediadive.medium:584`, and
   `kg_microbe_match: mediadive.medium:12` from the JCM 1270 generated record.
4. Recompare the regenerated JCM record against GRMD 1270 and the regenerated
   Brucella record against DSMZ Medium 584.

## Follow-up Checks

Run the narrow generated-record validators on both regenerated records:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py`.
3. `linkml-reference-validator validate data`.
4. `linkml-term-validator validate-data`.

Then manually confirm that JCM 1270 contains Columbia blood agar base with
50 mL sheep blood, and DSMZ 584 contains Brucella agar with 100 mL/L sheep
blood.

## Additional Notes

The exact search above used ignored files. It found many unrelated
`kg_microbe_match: mediadive.medium:12` rows when checking this record's
auxiliary KG-Microbe match, so that match should be treated as a noisy overlay
rather than evidence that the Brucella and Chocolate Agar records are the same.
