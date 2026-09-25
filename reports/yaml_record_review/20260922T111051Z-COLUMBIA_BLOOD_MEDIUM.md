# YAML Record Review: COLUMBIA BLOOD MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/COLUMBIA_BLOOD_MEDIUM.yaml`
- Started UTC: 2026-09-22T11:07:00Z
- Finished UTC: 2026-09-22T11:10:51Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:006311`
- Canonical source: `data/normalized_yaml/bacterial/columbia_blood_medium.yaml`
- Canonical source identity: DSMZ Medium 693, `COLUMBIA BLOOD MEDIUM`
- Merged inputs: DSMZ Medium 693, KOMODO Medium 693, and 13 KOMODO strain-specific Medium 693 records

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- DSMZ Medium 693 is Columbia agar base supplemented with 5% defibrinated sheep blood.
- The DSMZ source explicitly says media 545, 215, and 1 listed on the same PDF are for rehydrating freeze-dried pellets, not for cultivation of organisms whose catalogue entry only names M 693.
- TOGO M2582 resolves to the same DSMZ Medium 693 URL and the same two ingredients: Columbia agar base and 5% defibrinated sheep blood.
- The generated record is stale relative to the normalized source graph: `TOGO_M2582_Columbia_Blood_Medium.yaml` is already linked as a `SOURCE_DUPLICATE`, but still appears separately as `data/merge_yaml/merged/columbia_blood_medium__c25575e2.yaml`.

## Evidence

- Source PDF checked: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium693.pdf`.
- TOGO API checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2582`.
- Local DSMZ owner checked: `data/normalized_yaml/bacterial/columbia_blood_medium.yaml`.
- Local KOMODO duplicate checked: `data/normalized_yaml/bacterial/KOMODO_693_COLUMBIA_BLOOD_medium.yaml`.
- Local TOGO duplicate checked: `data/normalized_yaml/bacterial/TOGO_M2582_Columbia_Blood_Medium.yaml`.

## Completeness

- Medium category, type, composition type, and solid agar physical state are appropriate for DSMZ 693.
- The recipe should preserve an opaque Columbia agar base plus a 5% sheep-blood supplement.
- The TSB, BHI, and nutrient-broth sections from the DSMZ PDF are rehydration alternatives and are not part of DSMZ 693's cultivation medium.

## Findings

1. The canonical DSMZ/KOMODO merge imports unrelated rehydration-media ingredients into the cultivation recipe. `Casein peptone`, `Soy peptone`, `D(+)-Glucose`, `NaCl`, `K2HPO4`, `Peptone`, and `Meat extract` come from DSMZ 545 or DSMZ 1, while `Calf brains`, `Beef heart`, `Proteose peptone`, `Dextrose`, `Sodium chloride`, and `Disodium phosphate` are an unsupported expansion of the DSMZ 215 BHI rehydration option.
2. `Columbia agar base` is recorded as `1000 G_PER_L`, which turns a one-liter base volume into one kilogram of dry base. `Defibrinated sheep blood` is likewise converted from the supported 5% supplement to `50 G_PER_L`.
3. Preparation steps for the DSMZ 545 and DSMZ 1 rehydration media were copied into DSMZ 693, including pH 7.3, pH 7.0, and the Caso Bouillon note.
4. The generated merge is missing the already curated TOGO M2582 source duplicate, so a future regenerated record should absorb `data/merge_yaml/merged/columbia_blood_medium__c25575e2.yaml`.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/columbia_blood_medium.yaml` by keeping only Columbia agar base and defibrinated sheep blood.
2. Represent the Columbia agar base as an opaque commercial/base ingredient, with the sheep blood as `5 PERCENT_V_V`.
3. Remove all TSB, BHI, nutrient-broth, MicrobeNotes, and pH entries copied from the rehydration media.
4. Regenerate the merge so the DSMZ, KOMODO, strain-specific KOMODO, and TOGO M2582 source duplicates collapse into one canonical generated record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the repaired generated record.
- Confirm that `columbia_blood_medium__c25575e2.yaml` disappears after merge regeneration.
- Re-check the regenerated ingredient list against DSMZ Medium 693 and TOGO M2582.

## Additional Notes

- No schema-level defects were found; all issues are evidence and generated-merge defects.
- The direct TOGO normalized owner is already closer to the primary evidence than the current generated canonical record.
