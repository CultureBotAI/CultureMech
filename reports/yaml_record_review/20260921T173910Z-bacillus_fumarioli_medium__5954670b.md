# YAML Record Review: bacillus_fumarioli_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacillus_fumarioli_medium__5954670b.yaml
- Started UTC: 2026-09-21T17:38:17Z
- Finished UTC: 2026-09-21T17:39:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002961 |
| Generated record | data/merge_yaml/merged/bacillus_fumarioli_medium__5954670b.yaml |
| Maintained owner | data/normalized_yaml/bacterial/bacillus_fumarioli_medium.yaml |
| Label | BACILLUS FUMARIOLI MEDIUM |
| Source identity | MediaDive import of JCM J614 |
| Merge state | Single-source merge from `bacillus_fumarioli_medium` |

The generated target and normalized owner are identical in their scientific
content, so future formulation fixes belong in
`data/normalized_yaml/bacterial/bacillus_fumarioli_medium.yaml` or the
MediaDive/JCM import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacillus_fumarioli_medium__5954670b.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/bacillus_fumarioli_medium__5954670b.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, import
  history, and JCM GRMD=614 URL all point to BACILLUS FUMARIOLI MEDIUM.
- **The pH, agar state, and concentration arithmetic are source-faithful.** JCM
  614 lists a 1 L solid medium with pH 5.5; the record retains pH 5.5, 18 g/L
  agar, all gram-scale rows, and the 5 mg MnSO4.xH2O row as `0.005 G_PER_L`.
- **MnSO4.xH2O is too specifically grounded.** The source intentionally leaves
  hydration variable, while the record grounds the row to `CHEBI:86360` /
  manganese(II) sulfate.

## Evidence

- The record cites JCM GRMD=614, whose page is BACILLUS FUMARIOLI MEDIUM.
- JCM 614 lists 1 L distilled water, yeast extract 4 g, ammonium sulfate 2.5 g,
  KH2PO4 3 g, MgSO4.7H2O 0.2 g, CaCl2.2H2O 0.25 g, MnSO4.xH2O 5 mg, agar
  18 g, and pH adjustment to 5.5.
- The generated record matches the pH, agar, MgSO4.7H2O, CaCl2.2H2O, KH2PO4,
  ammonium sulfate, yeast extract, and MnSO4.xH2O source amounts after
  expressing them per liter.
- The source 1 L distilled-water row is absent from `ingredients`.

## Completeness

- The final-medium 1 L distilled-water row is missing.
- The variable-hydrate MnSO4.xH2O row needs exact grounding or an explicit
  unresolved term rather than an anhydrous manganese sulfate term.
- `target_organisms`, growth metrics, incubation temperature, salinity, and
  light are empty. The inspected JCM page does not supply those claims, so I
  did not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for the exact
  stem `bacillus_fumarioli_medium__5954670b` found no prior report before this
  file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The 1 L distilled-water row is absent. | JCM GRMD=614 contains `Distilled water 1.0 L`; the record has no water ingredient. | `data/normalized_yaml/bacterial/bacillus_fumarioli_medium.yaml`. |
| Minor | MnSO4.xH2O is grounded as anhydrous manganese(II) sulfate. | The source leaves hydration variable as `xH2O`, while the record uses `CHEBI:86360` / manganese(II) sulfate. | `data/normalized_yaml/bacterial/bacillus_fumarioli_medium.yaml`; MIM/CHEBI grounding. |
| Minor | Source evidence is encoded only as a note. | The JCM URL appears in free text, but there is no structured reference or evidence tying ingredient rows to JCM GRMD=614. | `data/normalized_yaml/bacterial/bacillus_fumarioli_medium.yaml` or the MediaDive/JCM importer. |

## Recommended Edits

1. Add the final 1 L distilled-water row from JCM GRMD=614.
2. Re-ground `MnSO4 x n H2O` to an exact verified variable-hydrate term if one
   is available, or remove the anhydrous CHEBI term until hydration can be
   represented.
3. Add structured source provenance for JCM GRMD=614.
4. Regenerate merged products after the normalized owner is repaired.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained JCM
  owner after water, term, and provenance edits.
- Regenerate merges and verify `bacillus_fumarioli_medium__5954670b.yaml`
  retains pH 5.5 and `MnSO4 x n H2O 0.005 G_PER_L` while adding 1 L water.
- Compare the regenerated record manually against JCM GRMD=614, focusing on
  the water row and the manganese `mg` unit.

## Additional Notes

- This sibling does not have the manganese unit defect seen in the TOGO M622
  import of the same source medium.
- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
