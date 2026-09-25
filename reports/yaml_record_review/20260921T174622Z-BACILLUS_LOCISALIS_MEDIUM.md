# YAML Record Review: BACILLUS LOCISALIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_LOCISALIS_MEDIUM.yaml
- Started UTC: 2026-09-21T17:44:30Z
- Finished UTC: 2026-09-21T17:46:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:004064 |
| Generated record | data/merge_yaml/merged/BACILLUS_LOCISALIS_MEDIUM.yaml |
| Bacillus owners | `data/normalized_yaml/bacterial/bacillus_locisalis_medium.yaml`; `data/normalized_yaml/bacterial/KOMODO_1309_BACILLUS_LOCISALIS_medium.yaml` |
| Aquisalimonas owners | `data/normalized_yaml/bacterial/aquisalimonas_medium.yaml`; `data/normalized_yaml/bacterial/KOMODO_1182_AQUISALIMONAS_medium.yaml` |
| Label | BACILLUS LOCISALIS medium |
| Source identity | KOMODO 1309 / DSMZ Medium 1309 |
| Merge state | Four-source merge from DSMZ/KOMODO 1309 and DSMZ/KOMODO 1182 records |

The generated target crosses two source media and does not faithfully reproduce
either. Bacillus-specific fixes belong in the DSMZ/KOMODO 1309 normalized
owners, Aquisalimonas-specific fixes belong in the DSMZ/KOMODO 1182 owners, and
the cross-medium merge overlay should be removed before regenerating merged
products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_LOCISALIS_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_LOCISALIS_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **The generated record has crossed identities.** It keeps KOMODO 1309 and the
  Bacillus locisalis label, but it merged in Aquisalimonas DSMZ 1182 / KOMODO
  1182 synonyms and carries the doubled Aquisalimonas ingredient values.
- **DSMZ 1309 and DSMZ 1182 are distinct source accessions.** DSMZ 1309 is
  titled BACILLUS LOCISALIS MEDIUM; DSMZ 1182 is titled AQUISALIMONAS MEDIUM.
- **Ingredient groundings are mostly plausible but attached to the wrong
  merged formulation.** The K2HPO4, MgSO4 x 7 H2O, glucose, NaCl, Na2CO3, and
  agar terms agree with their displayed ingredient strings; the primary problem
  is source and concentration scope.

## Evidence

- DSMZ 1309 lists BACILLUS LOCISALIS MEDIUM with peptone 5.0 g, yeast extract
  5.0 g, glucose 10.0 g, K2HPO4 1.0 g, MgSO4 x 7 H2O 0.2 g, agar 20.0 g,
  NaCl 80.0 g, Na2CO3 20.0 g, and distilled water 1000.0 ml.
- DSMZ 1309 instructs that NaCl and Na2CO3 are dissolved and autoclaved
  separately before addition to the organic components at 60 C before pouring
  the agar medium.
- DSMZ 1182 lists AQUISALIMONAS MEDIUM as Solution A with glucose 10.0 g,
  peptone 5.0 g, yeast extract 5.0 g, K2HPO4 1.0 g, MgSO4 x 7 H2O 0.2 g, and
  500 ml water plus Solution B with Na2CO3 20.0 g, NaCl 80.0 g, and 500 ml
  water. The two solutions are mixed, and the final pH is 9.5.
- The generated Bacillus-labeled record instead has glucose 20, peptone 10,
  yeast extract 10, K2HPO4 2, MgSO4 x 7 H2O 0.4, Na2CO3 40, and NaCl
  160 `G_PER_L`. Those are the DSMZ 1182 per-500-ml solution concentrations,
  not the DSMZ 1309 Bacillus recipe and not the final Aquisalimonas recipe.
- The generated record has no water rows, no preparation steps, and no pH even
  though the inspected normalized Bacillus DSMZ owner has the NaCl/Na2CO3
  separate-autoclave step and the inspected Aquisalimonas DSMZ owner has
  Solution A/B mixing plus pH 9.5.

## Completeness

- The generated record must be split back into Bacillus 1309 and Aquisalimonas
  1182 records.
- The Aquisalimonas owners need Solution A and Solution B boundaries or a final
  1 L recalculation; the current half-volume rows double every solute.
- The Bacillus owners are missing the final distilled-water row.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected DSMZ 1309 and DSMZ 1182 PDFs do not supply those claims,
  so I did not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_LOCISALIS_MEDIUM` found no prior report before this file was
  written. A separate ignored-inclusive label search for `BACILLUS LOCISALIS
  MEDIUM` found only a mention in a `3_8m_characterization_medium_no_1` review,
  not a prior review of this record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Blocker | DSMZ/KOMODO 1309 Bacillus and DSMZ/KOMODO 1182 Aquisalimonas were falsely merged. | The generated record identifies KOMODO 1309 / BACILLUS LOCISALIS medium but includes Aquisalimonas 1182 synonyms and doubled Aquisalimonas ingredient values. DSMZ 1309 and DSMZ 1182 are different source media with different titles and preparation protocols. | Merge overlay plus all four normalized owners listed under Target. |
| Major | Aquisalimonas Solution A and Solution B were flattened at half-volume concentration. | DSMZ 1182 defines 10 g glucose and 20 g Na2CO3 in 500 ml stocks that are mixed to 1 L final medium. The Aquisalimonas owners and generated record store those as `20 G_PER_L` glucose and `40 G_PER_L` Na2CO3. | `data/normalized_yaml/bacterial/aquisalimonas_medium.yaml`; `data/normalized_yaml/bacterial/KOMODO_1182_AQUISALIMONAS_medium.yaml`. |
| Major | The generated Bacillus record is 2x too concentrated for the Bacillus source. | DSMZ 1309 has 10 g glucose, 5 g peptone, 5 g yeast extract, 80 g NaCl, and 20 g Na2CO3 per liter; the generated Bacillus-labeled record has 20, 10, 10, 160, and 40 g/L respectively. | Regenerate after removing the false cross-source merge. |
| Major | Source water and preparation details are missing. | DSMZ 1309 has 1000 ml water and a NaCl/Na2CO3 separate-autoclave instruction; DSMZ 1182 has 500 ml water in each of two solutions, Solution A/B mixing instructions, and pH 9.5. The generated record has none of those fields. | All four normalized owners plus merge regeneration. |
| Minor | Source evidence is encoded only as notes and generated synonyms. | DSMZ and KOMODO source IDs appear in free text, curation history, and `synonyms`, but there is no structured evidence tying ingredients to DSMZ 1309, DSMZ 1182, KOMODO 1309, or KOMODO 1182. | MediaDive/KOMODO importers or all four normalized owners. |

## Recommended Edits

1. Remove the SOURCE_DUPLICATE relationship between the Bacillus 1309 and
   Aquisalimonas 1182 record families.
2. Recalculate DSMZ 1182 Aquisalimonas against the final 1 L mixed medium, or
   represent Solution A and Solution B explicitly with their 500 ml water rows.
3. Keep DSMZ/KOMODO 1309 Bacillus at peptone 5, yeast extract 5, glucose 10,
   K2HPO4 1, MgSO4 x 7 H2O 0.2, agar 20, NaCl 80, and Na2CO3 20 g/L.
4. Restore the DSMZ 1309 and DSMZ 1182 preparation steps to their respective
   generated records after the split.
5. Add structured source provenance for DSMZ 1309, KOMODO 1309, DSMZ 1182, and
   KOMODO 1182.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on all four normalized
  owners after splitting the merge and repairing Aquisalimonas solution scope.
- Regenerate merges and verify Bacillus 1309 no longer contains Aquisalimonas
  synonyms or doubled concentrations.
- Compare the regenerated Bacillus record manually against DSMZ Medium 1309 and
  the regenerated Aquisalimonas record manually against DSMZ Medium 1182.

## Additional Notes

- The exact prior-report searches used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
