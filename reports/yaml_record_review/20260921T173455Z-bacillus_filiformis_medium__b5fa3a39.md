# YAML Record Review: bacillus_filiformis_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacillus_filiformis_medium__b5fa3a39.yaml
- Started UTC: 2026-09-21T17:34:55Z
- Finished UTC: 2026-09-21T17:36:11Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:009925 |
| Generated record | data/merge_yaml/merged/bacillus_filiformis_medium__b5fa3a39.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml |
| Label | Bacillus Filiformis Medium |
| Source identity | TOGO M533, imported from JCM_M531 |
| Merge state | Single-source merge from `TOGO_M533_Bacillus_Filiformis_Medium` |

The generated target is stale relative to its maintained normalized owner for
the water row: the owner was repaired to a single `1.0` row on 2026-09-02, but
this generated merge still has a summed `3.0` row. All remaining formulation
fixes belong in `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml`
or the TOGO import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacillus_filiformis_medium__b5fa3a39.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/bacillus_filiformis_medium__b5fa3a39.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, TOGO M533
  accession, original source note, and JCM GRMD=531 URL all point to the TOGO
  import of JCM 531 Bacillus Filiformis Medium.
- **The main direct ingredients match the TOGO/JCM source quantities.** TOGO
  M533 lists a 1 L main solution with NaCl 100 g, KCl 2 g, Na2CO3 3 g, sodium
  citrate 3 g, MgSO4.H2O 1 g, and yeast extract 10 g; those rows are present at
  the same numeric values in the generated record.
- **MgSO4.H2O is too broadly grounded.** The source and TOGO GMO identity are
  magnesium sulfate monohydrate, but the record grounds the row to
  `CHEBI:32599` / magnesium sulfate.

## Evidence

- The TOGO API for M533 resolves to `http://togomedium.org/medium/M533`, names
  the medium `Bacillus Filiformis Medium`, and records original media ID
  `JCM_M531` with pH `9.0`.
- TOGO M533 has three separate formulation scopes: a main 1 L medium, a local
  MnCl2 solution containing 0.36 g MnCl2.4H2O in 1 L distilled water, and a
  local FeSO4 solution containing 50 g FeSO4.H2O in 1 L distilled water.
- The final medium adds 1 ml of the local MnCl2 solution and 1 ml of the local
  FeSO4 solution. The generated record instead keeps both solution additions as
  empty `solutions` with `1 G_PER_L` and promotes the stock components as
  top-level `MnCl2.4H2O 0.36 G_PER_L` and `FeSO4.H2O 50 G_PER_L` rows.
- The generated `Distilled water 3.0 G_PER_L` row came from summing three 1 L
  waters from different scopes. The maintained owner has already collapsed
  that to `1.0`, but it still retains one top-level water row and no stock water
  rows because the MnCl2 and FeSO4 solutions remain empty.
- TOGO M533 carries the preparation comment to separately autoclave Na2CO3 and
  NaCl and to check final pH near 9.0. The generated record drops both pH and
  preparation.

## Completeness

- The final 1 ml/L additions of the two local metal stocks are missing.
- The MnCl2 and FeSO4 stock recipes are missing; their components are flattened
  into top-level final-medium ingredients.
- The generated merge still contains the stale summed water row from before the
  2026-09-02 owner repair.
- pH 9.0 and the Na2CO3/NaCl separate autoclave note are missing.
- `target_organisms`, growth metrics, incubation temperature, salinity, and
  light are empty. The inspected TOGO M533 payload does not supply those
  claims, so I did not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for the exact
  stem `bacillus_filiformis_medium__b5fa3a39` found no prior report before this
  file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated water row is stale and sums waters from the main medium and two stocks. | TOGO M533 has three independent 1 L water rows in three scopes. The maintained owner was repaired on 2026-09-02 to collapse the former `3.0` value, but this generated record still has `Distilled water 3.0 G_PER_L`. | Regenerate `data/merge_yaml/merged/bacillus_filiformis_medium__b5fa3a39.yaml` from `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml`. |
| Major | The MnCl2 local stock is flattened into the final medium at stock concentration. | TOGO M533 adds 1 ml of a 0.36 g/L MnCl2.4H2O stock to the main medium. The generated record stores the stock component as a top-level `0.36 G_PER_L` ingredient and leaves the MnCl2 solution with empty composition and a `1 G_PER_L` addition. | `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml`; TOGO solution import. |
| Major | The FeSO4 local stock is flattened into the final medium at stock concentration. | TOGO M533 adds 1 ml of a 50 g/L FeSO4.H2O stock to the main medium. The generated record stores the stock component as a top-level `50 G_PER_L` ingredient and leaves the FeSO4 solution with empty composition and a `1 G_PER_L` addition. | `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml`; TOGO solution import. |
| Major | Preparation and pH evidence were dropped. | TOGO M533 records pH 9.0 and the preparation comment to separately autoclave Na2CO3 and NaCl and check final pH near 9.0; the generated record has neither structured pH nor preparation text. | `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml`; TOGO comment/pH import. |
| Major | MgSO4.H2O is grounded too broadly. | TOGO's component and GMO label identify magnesium sulfate monohydrate, while the row uses generic magnesium sulfate. Hydration is identity-significant. | `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml`; MIM/CHEBI grounding. |
| Minor | Source evidence is encoded only as a note. | The TOGO and original JCM URLs appear in free text, but there is no structured reference or evidence tying the ingredient rows and preparation text to TOGO M533/JCM GRMD=531. | `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml` or the TOGO importer. |

## Recommended Edits

1. Regenerate the merged record so it picks up the owner-side 2026-09-02 water
   repair.
2. In `data/normalized_yaml/bacterial/TOGO_M533_Bacillus_Filiformis_Medium.yaml`,
   move the `MnCl2.4H2O` and `FeSO4.H2O` rows into local stock compositions with
   their 1 L water rows.
3. Encode the two stock additions to the main medium as 1 ml/L solution
   additions, not `1 G_PER_L`.
4. Preserve TOGO M533 pH 9.0 and the Na2CO3/NaCl separate autoclave comment.
5. Re-ground `MgSO4.H2O` to an exact verified magnesium sulfate monohydrate
   term, or remove the broad CHEBI term until that exact hydrate can be
   verified.
6. Add structured source provenance for TOGO M533 and original JCM GRMD=531.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained TOGO
  owner after stock, pH/preparation, provenance, and term edits.
- Regenerate merges and verify the generated
  `bacillus_filiformis_medium__b5fa3a39.yaml` water row is no longer `3.0`.
- Compare the regenerated record manually against TOGO M533, focusing on the
  main solution, the two local 1 L stock solutions, the two 1 ml additions, pH,
  and Na2CO3/NaCl autoclave instruction.

## Additional Notes

- Unlike the JCM-only sibling record, this generated TOGO record retains the
  main direct ingredient quantities as unscaled source amounts.
- The exact prior-report search used `find` under `reports/yaml_record_review`,
  so ignored review reports were included.
