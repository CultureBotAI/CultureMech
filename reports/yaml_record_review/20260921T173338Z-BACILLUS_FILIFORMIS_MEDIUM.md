# YAML Record Review: BACILLUS FILIFORMIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
- Started UTC: 2026-09-21T17:32:44Z
- Finished UTC: 2026-09-21T17:33:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002880 |
| Generated record | data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml |
| Label | BACILLUS FILIFORMIS MEDIUM |
| Source identity | JCM GRMD=531 |
| Merge state | Single-source merge from `JCM_J531_BACILLUS_FILIFORMIS_MEDIUM` |

The generated target and normalized owner are identical in their scientific
content, so every future formulation fix belongs in
`data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml` or
the JCM import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record name, `media_term`, notes, and JCM
  GRMD=531 all point to BACILLUS FILIFORMIS MEDIUM.
- **Most direct salts have plausible groundings.** Sodium citrate, KCl,
  Na2CO3, NaCl, MnCl2 x 4 H2O, and FeSO4 x H2O have groundings that preserve
  the displayed chemical identities.
- **MgSO4 x H2O is too broadly grounded.** The JCM source specifies the
  monohydrate, while the record uses `CHEBI:32599` / magnesium sulfate.
  Hydration is identity-significant and should not be silently broadened.

## Evidence

- JCM 531 lists a 1 L main solution with yeast extract 10 g, sodium citrate
  3 g, KCl 2 g, MgSO4 x H2O 1 g, Na2CO3 3 g, NaCl 100 g, 1 ml MnCl2 solution,
  and 1 ml FeSO4 solution, followed by pH about 9.0.
- The generated main-solution rows match the source after the importer divided
  by the 1002 ml combined volume: yeast extract 9.98004 g/L, sodium citrate
  2.99401 g/L, KCl 1.99601 g/L, MgSO4 x H2O 0.998004 g/L, Na2CO3
  2.99401 g/L, and NaCl 99.8004 g/L.
- The MnCl2 and FeSO4 stock rows do **not** match the final medium. JCM 531
  defines the MnCl2 stock as 0.36 g/L and the FeSO4 stock as 50 g/L, each added
  at 1 ml/L. The record stores `MnCl2 x 4 H2O 0.36 G_PER_L` and
  `FeSO4 x H2O 50 G_PER_L` directly at top level.
- The JCM page includes three water rows: 1 L in the main solution, 1 L in the
  MnCl2 stock, and 1 L in the FeSO4 stock. None are represented in the record.
- The preparation note to separately autoclave Na2CO3 and NaCl and check final
  pH around 9.0 is retained.

## Completeness

- The two metal stock solutions are missing as solutions at 1 ml/L each.
- The final and stock water rows are missing.
- The MgSO4 monohydrate row needs exact grounding or an explicit unresolved
  term rather than the broad magnesium sulfate term.
- `target_organisms`, growth metrics, incubation temperature, salinity, and
  light are empty. The inspected JCM page does not supply those claims, so I
  did not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_FILIFORMIS_MEDIUM`, `Bacillus Filiformis Medium`, and
  `BACILLUS FILIFORMIS` found no prior report before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | MnCl2 solution is flattened into the final medium at 1000x the intended final addition. | JCM 531 adds 1 ml of a 0.36 g/L MnCl2 x 4 H2O stock. The record stores the stock concentration as a top-level `0.36 G_PER_L` row. | `data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml`; JCM stock import. |
| Major | FeSO4 solution is flattened into the final medium at 1000x the intended final addition. | JCM 531 adds 1 ml of a 50 g/L FeSO4 x H2O stock. The record stores the stock concentration as a top-level `50 G_PER_L` row. | `data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml`; JCM stock import. |
| Major | The 1 L stock waters and 1 L main water are absent. | JCM 531 has separate `Distilled water` rows in the main solution, MnCl2 stock, and FeSO4 stock; the record has no water ingredient and no `solutions` entries to own stock water. | `data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml`. |
| Major | MgSO4 x H2O is grounded too broadly. | The source specifies magnesium sulfate monohydrate, while the record uses an unhydrated/generic magnesium sulfate CHEBI term. | `data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml`; MIM/CHEBI grounding. |
| Minor | Source evidence is encoded only as a note. | The JCM URL and `J531` accession appear in free text, but there is no structured reference or evidence tying the ingredient rows and preparation text to JCM GRMD=531. | `data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml` or the JCM importer. |

## Recommended Edits

1. Move `MnCl2 x 4 H2O` into a local MnCl2 stock with 0.36 g/L, 1 L water, and
   a 1 ml/L addition to the final medium.
2. Move `FeSO4 x H2O` into a local FeSO4 stock with 50 g/L, 1 L water, and a
   1 ml/L addition to the final medium.
3. Add the 1 L final-medium water row from JCM 531.
4. Re-ground `MgSO4 x H2O` to an exact verified magnesium sulfate monohydrate
   term, or remove the broad CHEBI term until that exact hydrate can be
   verified.
5. Add structured source provenance for JCM GRMD=531 and regenerate the merge.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the normalized JCM
  owner after stock and term edits.
- Regenerate merges and verify `BACILLUS_FILIFORMIS_MEDIUM.yaml` has local
  MnCl2 and FeSO4 stocks, no stock-strength top-level metal rows, and a
  source-faithful final pH/preparation note.
- Compare the regenerated recipe manually against JCM GRMD=531, focusing on
  the two 1 ml metal additions and all three water rows.

## Additional Notes

- This is not a generated-staleness issue: `JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml`
  currently has the same flattened stock rows as the generated merge.
- The exact prior-report search used `--no-ignore --hidden`, so ignored review
  reports were included.
