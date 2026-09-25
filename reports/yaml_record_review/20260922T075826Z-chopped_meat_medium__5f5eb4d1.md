# YAML Record Review: Chopped meat medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium__5f5eb4d1.yaml
- Started UTC: 2026-09-22T07:57:39Z
- Finished UTC: 2026-09-22T07:58:28Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009262 |
| Label | Chopped meat medium |
| Generated record | data/merge_yaml/merged/chopped_meat_medium__5f5eb4d1.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2710_Chopped_meat_medium.yaml |
| Source | TOGO Medium M2710, ATCC Medium 593 |

The reviewed file is a generated one-source merge of ATCC Medium 593 through
TOGO M2710. The generated record is stale: its maintained owner was repaired on
2026-09-11, after this 2026-08-06 merge artifact was produced.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium__5f5eb4d1.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009262`, `TOGO:M2710`, the ATCC
PDF token in the source URL, the maintained owner stem, and the generated merge
fingerprint all denote ATCC Medium 593 Chopped meat medium.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2710 source ID, ATCC source URL token, maintained owner stem, and merge
fingerprint found this generated record, its maintained owner, its normalized
index entries, and the expected child-variant backreference from the repaired
ATCC Medium 735 owner.

## Evidence

ATCC Medium 593 and TOGO M2710 support a medium that first extracts 500.0 g
fat-free ground beef with 1.0 L distilled water and 25.0 mL N NaOH, filters the
meat while retaining both particles and filtrate, and restores the filtrate to
1 L. The source then adds 30.0 g peptone, 5.0 g yeast extract, 5.0 g `K2HPO4`,
and 4.0 mL 0.025% resazurin solution, followed by boiling, cooling, adding
0.5 g L-cysteine HCl, adjusting pH to 7.0, dispensing 7 mL over one part meat
particles to 4-5 parts fluid per tube under 97% nitrogen / 3% hydrogen, capping
with butyl rubber stoppers under N2/H2, and autoclaving for 15 minutes under
fast exhaust.

The generated record is the old TOGO import. It stores the 1 L water, 25 mL
N NaOH, and 4 mL 0.025% resazurin solution as `G_PER_L`; moves resazurin into
an empty `solutions` entry; omits pH 7.0; reduces the 97% nitrogen / 3% hydrogen
condition to two variable gas ingredients; and has no preparation steps or
references.

The maintained owner has already repaired these issues. Its 2026-09-11
curation event converted water, N NaOH, and 0.025% resazurin to volume units,
added pH 7.0 and ordered preparation steps, grounded the mappable ingredients,
and retained ATCC M593 source references.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this ATCC source record.

The generated record is incomplete until it is regenerated from the repaired
maintained owner.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The generated record predates the maintained owner's 2026-09-11 TOGO M2710/ATCC 593 repair, so it still has gram-per-litre liquid volumes, an empty resazurin solution shell, missing pH, missing preparation steps, and default gas ingredients. **Owner:** regenerate from `data/normalized_yaml/bacterial/TOGO_M2710_Chopped_meat_medium.yaml`. |

## Recommended Edits

1. Rerun the merge generator so `data/merge_yaml/merged/chopped_meat_medium__5f5eb4d1.yaml`
   is rebuilt from the repaired TOGO M2710 owner.
2. Confirm that the regenerated record preserves the maintained owner's
   `ML_PER_L` water, N NaOH, and resazurin quantities, pH 7.0, references, and
   ATCC 593 preparation steps.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2710, the ATCC
Medium 593 PDF, and the repaired maintained owner to confirm no repaired
ATCC 593 fields were dropped during merge.

## Additional Notes

None found.
