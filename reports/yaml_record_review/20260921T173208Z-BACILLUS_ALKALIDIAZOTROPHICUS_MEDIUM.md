# YAML Record Review: BACILLUS ALKALIDIAZOTROPHICUS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_ALKALIDIAZOTROPHICUS_MEDIUM.yaml
- Started UTC: 2026-09-21T17:30:30Z
- Finished UTC: 2026-09-21T17:32:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:003956 |
| Generated record | data/merge_yaml/merged/BACILLUS_ALKALIDIAZOTROPHICUS_MEDIUM.yaml |
| Canonical normalized owner | data/normalized_yaml/bacterial/KOMODO_1208_BACILLUS_ALKALIDIAZOTROPHICUS_medium.yaml |
| Duplicate normalized owner | data/normalized_yaml/bacterial/bacillus_alkalidiazotrophicus_medium.yaml |
| Label | BACILLUS ALKALIDIAZOTROPHICUS medium |
| Source identity | KOMODO Medium 1208 / DSMZ Medium 1208 |
| Merge state | Two-source merge from KOMODO 1208 and DSMZ Medium 1208 |

The generated record is owned by normalized inputs. The KOMODO owner is
canonical in the generated merge, but the DSMZ owner preserves source
preparation text that the KOMODO owner lacks.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_ALKALIDIAZOTROPHICUS_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_ALKALIDIAZOTROPHICUS_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

I ran the focused checks through the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails while
building `llvmlite==0.46.0` under Python 3.13.

## Identity and Grounding

- **Source identity is coherent.** KOMODO Medium 1208 explicitly points at DSMZ
  Medium 1208, and the DSMZ duplicate owner carries the same medium number and
  formula.
- **The source formula is liquid at pH 10.0.** The `physical_state: LIQUID` and
  `ph_value: 10.0` slots agree with DSMZ 1208.
- **Hydrate and salt groundings are mostly plausible.** NaHCO3, Na2CO3, NaCl,
  K2HPO4, NH4Cl, MgCl2 x 6 H2O, Na2SO4, glucose, Na2-EDTA x 2 H2O,
  FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, boric acid, CoCl2 x 6 H2O,
  CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and the
  vitamins are all grounded to matching or near-matching chemical entities.
- **One hydrate-sensitive grounding is wrong.** The source row
  `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / nickel dichloride, losing the
  hexahydrate form.

## Evidence

- DSMZ Medium 1208's direct final-medium salts are represented with the same
  gram-per-liter values in the generated record: NaHCO3 8, Na2CO3 22, NaCl 6,
  K2HPO4 1, NH4Cl 0.2, MgCl2 x 6 H2O 0.2, yeast extract 0.05, Na2SO4 2.8, and
  glucose 2.
- DSMZ Medium 1208 adds three stocks that are absent as stocks in the generated
  YAML: 1 ml/L Trace element solution SL-11 from DSMZ 722, 1 ml/L
  Selenite-tungstate solution from DSMZ 385, and 10 ml/L Wolin's vitamin
  solution from DSMZ 141.
- The SL-11 metal stock rows were imported at full stock concentration rather
  than as the 1 ml/L final contribution. For example, Na2-EDTA x 2 H2O is
  `5.2 G_PER_L` in the record but is 5.2 g/L in the DSMZ 722 stock that DSMZ
  1208 adds at 1 ml/L.
- The same stock-flattening error affects the selenite-tungstate and vitamin
  stocks: `NaOH 0.5 G_PER_L`, `Na2SeO3 x 5 H2O 0.003 G_PER_L`, and
  `Na2WO4 x 2 H2O 0.004 G_PER_L` are full DSMZ 385 stock values, while the
  vitamin rows from DSMZ 141 are full Wolin's stock values added at 10 ml/L.
- The DSMZ duplicate owner retains preparation text for boiling/cooling under
  N2, dispensing under N2, autoclaving, adding sterile anoxic NH4Cl, MgCl2,
  yeast extract, trace elements, and vitamins after sterilization, filter
  sterilizing the vitamin stock, and adjusting final pH to 10. The canonical
  KOMODO owner and generated merge omit all `preparation_steps`.

## Completeness

- The generated record does not distinguish final-medium ingredients from three
  referenced stock solutions, so the trace metals, selenite-tungstate, and
  vitamin amounts are all overstated in the final medium.
- The final 1000 ml distilled water row from DSMZ 1208 is absent.
- DSMZ source preparation is missing from the canonical generated record even
  though it exists in the duplicate DSMZ normalized owner.
- `target_organisms`, growth metrics, incubation temperature, salinity, and
  light are empty. I did not count those as defects because the inspected DSMZ
  source specifies a formulation and preparation protocol, not a growth assay.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_ALKALIDIAZOTROPHICUS_MEDIUM`, `Bacillus Alkalidiazotrophicus
  Medium`, and `BACILLUS ALKALIDIAZOTROPHICUS` found no prior report before
  this one was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Trace element solution SL-11 is flattened into direct final ingredients at 1000x its intended final addition. | DSMZ 1208 adds 1 ml/L SL-11. DSMZ 722 defines the stock with 5.2 g/L Na2-EDTA x 2 H2O, 1.5 g/L FeCl2 x 4 H2O, 70 mg/L ZnCl2, 100 mg/L MnCl2 x 4 H2O, 6 mg/L H3BO3, 190 mg/L CoCl2 x 6 H2O, 2 mg/L CuCl2 x 2 H2O, 24 mg/L NiCl2 x 6 H2O, and 36 mg/L Na2MoO4 x 2 H2O. Those values are all present as top-level `G_PER_L` rows. | `data/normalized_yaml/bacterial/KOMODO_1208_BACILLUS_ALKALIDIAZOTROPHICUS_medium.yaml` and `data/normalized_yaml/bacterial/bacillus_alkalidiazotrophicus_medium.yaml`; DSMZ/KOMODO stock import. |
| Major | Selenite-tungstate solution is flattened into direct final ingredients at 1000x its intended final addition. | DSMZ 1208 adds 1 ml/L of the DSMZ 385 selenite-tungstate stock. The generated record stores the stock's NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O rows as top-level final-medium ingredients. | Same normalized owners; DSMZ/KOMODO stock import. |
| Major | Wolin's vitamin solution is flattened into direct final ingredients at 100x its intended final addition. | DSMZ 1208 adds 10 ml/L of the DSMZ 141 Wolin's vitamin stock. The generated record stores the stock's biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid as top-level final-medium rows at full stock strength. | Same normalized owners; DSMZ/KOMODO stock import. |
| Major | DSMZ preparation steps were dropped in the canonical merge. | `data/normalized_yaml/bacterial/bacillus_alkalidiazotrophicus_medium.yaml` retains the DSMZ instructions for N2 cooling/dispensing, autoclaving, post-sterilization anoxic additions, vitamin filtration, and final pH adjustment; the generated canonical record has no `preparation_steps`. | Merge conflict selection or `KOMODO_1208_BACILLUS_ALKALIDIAZOTROPHICUS_medium.yaml`. |
| Major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | The source stock is the hexahydrate; the generated row has `CHEBI:34887` / nickel dichloride. Exact hydration is identity-significant for this corpus. | Both normalized owners; MIM/CHEBI grounding. |
| Minor | Source evidence is not structured. | The record carries source IDs in notes and merge history but has no structured references or evidence snippets tying the direct ingredients and stock solution claims to DSMZ 1208, 722, 385, and 141. | Both normalized owners or the DSMZ/KOMODO importer. |

## Recommended Edits

1. Move the SL-11 component rows into a stock solution added to the final medium
   at 1 ml/L, sourced from DSMZ 722.
2. Move NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O into a
   selenite-tungstate stock added at 1 ml/L, sourced from DSMZ 385.
3. Move the ten Wolin vitamin rows into a vitamin stock added at 10 ml/L,
   sourced from DSMZ 141 and sterilized by filtration.
4. Add the DSMZ 1208 preparation sequence from the DSMZ owner to the canonical
   KOMODO owner or adjust merge conflict resolution so the generated recipe
   retains it.
5. Add the source 1000 ml distilled water row from DSMZ 1208.
6. Replace the `NiCl2 x 6 H2O` grounding with a verified nickel dichloride
   hexahydrate term, or leave the row ungrounded until an exact hydrate term is
   verified.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on both normalized
  Bacillus Alkalidiazotrophicus owners after stock and term edits.
- Regenerate merged records and verify this generated record has only direct
  DSMZ 1208 final ingredients at top level plus three stock additions:
  SL-11 at 1 ml/L, Selenite-tungstate solution at 1 ml/L, and Wolin's vitamin
  solution at 10 ml/L.
- Compare the stock recipes against DSMZ 722, DSMZ 385, and DSMZ 141, then
  compare the final medium and post-autoclave workflow against DSMZ 1208.

## Additional Notes

- This record passes schema and term validators because stock components are
  legal `IngredientDescriptor` rows and the mistaken nickel chloride grounding
  still uses an existing CHEBI term.
- The KOMODO and DSMZ owners agree on the flattened ingredient list, so the
  generated record is not stale; the defect is upstream in normalized curation
  and canonical merge selection.
