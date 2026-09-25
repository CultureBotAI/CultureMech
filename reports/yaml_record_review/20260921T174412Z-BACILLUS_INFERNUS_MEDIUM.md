# YAML Record Review: BACILLUS INFERNUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_INFERNUS_MEDIUM.yaml
- Started UTC: 2026-09-21T17:39:33Z
- Finished UTC: 2026-09-21T17:44:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:001844 |
| Generated record | data/merge_yaml/merged/BACILLUS_INFERNUS_MEDIUM.yaml |
| Primary maintained owner | data/normalized_yaml/bacterial/bacillus_infernus_medium.yaml |
| Other merged owners | `data/normalized_yaml/bacterial/msa_fe_medium.yaml`; `data/normalized_yaml/bacterial/msa_fe_medium_replace_na_lactate_with_na_formate.yaml` |
| Label | BACILLUS INFERNUS MEDIUM |
| Source identity | DSMZ Medium 705 |
| Merge state | Three-source merge from `bacillus_infernus_medium`, `msa_fe_medium`, and `msa_fe_medium_replace_na_lactate_with_na_formate` |

The generated target is owned by three normalized records. Future DSMZ 705
stock-solution and water fixes belong in `bacillus_infernus_medium.yaml` and the
KOMODO DSMZ-705 copy owners before regenerating merge products; the
lactate-to-formate variant needs to be separated or repaired before it is
merged again.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_INFERNUS_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_INFERNUS_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Primary DSMZ identity is correct.** The label, `media_term`, notes, and
  normalized primary owner all identify DSMZ Medium 705, BACILLUS INFERNUS
  MEDIUM.
- **The KOMODO lactate-to-formate variant is not a source duplicate as
  represented.** Its source ID and label say `705_replace_Na-lactate_with_Na-formate`,
  but the normalized owner has the same `Na-lactate` row as DSMZ 705 and no
  formate row.
- **Two hydrate groundings are too broad.** DSMZ 705 specifies `K2HPO4 x 3 H2O`
  and `NiCl2 x 6 H2O`; the record uses dipotassium hydrogen phosphate and
  nickel dichloride groundings that do not preserve those hydrates.

## Evidence

- The DSMZ PDF title and rendered first page identify `705: BACILLUS INFERNUS
  MEDIUM`, with final pH 7.5 and final volume 1030 ml.
- DSMZ 705 lists ferric citrate 5.30 g, NaCl 5.80 g, NH4Cl 1.00 g,
  K2HPO4 x 3 H2O 0.40 g, MgCl2 x 6 H2O 1.00 g, yeast extract 2.00 g,
  Trypticase peptone 2.00 g, 10 ml trace element solution, Na-acetate 0.80 g,
  Na-lactate 1.20 g, 2-mercaptoethanesulfonate 0.50 g, and distilled water
  1000 ml in the final 1030 ml medium.
- The generated direct DSMZ rows are scaled by final volume; for example,
  5.30 g ferric citrate / 1.03 L gives `5.14563 G_PER_L` and 1.20 g
  Na-lactate / 1.03 L gives `1.16505 G_PER_L`.
- DSMZ 705 defines a 1 L trace element stock with Na2-EDTA x 2 H2O 0.50 g,
  CoCl2 x 6 H2O 0.15 g, MnCl2 x 4 H2O 0.10 g, FeSO4 x 7 H2O 0.10 g, ZnCl2
  0.10 g, AlCl3 x 6 H2O 40 mg, Na2WO4 x 2 H2O 40 mg, Na2SeO3 x 5 H2O 30 mg,
  NiCl2 x 6 H2O 20 mg, CuCl2 x 2 H2O 20 mg, H3BO3 10 mg, Na2MoO4 x 2 H2O
  10 mg, and 1000 ml distilled water. The final medium adds 10 ml of that
  trace stock.
- The generated record has no distilled-water rows and no `Trace element
  solution` addition; it places the stock ingredients directly at their 1 L
  stock concentrations.
- DSMZ 705 page 2 instructs the trace stock to dissolve EDTA in distilled water,
  adjust to pH 7 with 2 N NaOH, and then dissolve the remaining compounds. The
  generated `preparation_steps` retains that text but does not attach it to a
  trace-element solution.

## Completeness

- The 1000 ml final-medium water row and the 1000 ml trace-stock water row are
  missing.
- The trace-element solution is missing as a 10 ml final-medium addition.
- The formate variant owner was overwritten with the base DSMZ 705 lactate
  recipe and then merged as a source duplicate.
- `target_organisms`, growth metrics, incubation temperature, salinity, and
  explicit anaerobic gas fields are empty. DSMZ 705 supplies 80% N2 / 20% CO2
  preparation instructions but not target strain or growth metrics.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_INFERNUS_MEDIUM` and `BACILLUS INFERNUS MEDIUM` found no prior
  report before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The DSMZ 705 trace element solution is flattened into top-level ingredients at stock concentration. | DSMZ adds 10 ml of a 1 L trace stock to 1030 ml final medium. The record stores each stock component directly, such as `Na2-EDTA x 2 H2O 0.5 G_PER_L` and `CoCl2 x 6 H2O 0.15 G_PER_L`, with no solution addition. | `data/normalized_yaml/bacterial/bacillus_infernus_medium.yaml`, `msa_fe_medium.yaml`, `msa_fe_medium_replace_na_lactate_with_na_formate.yaml`; DSMZ/KOMODO solution import. |
| Major | Main and trace-stock water rows are absent. | DSMZ 705 has 1000 ml distilled water in the final medium and 1000 ml in the trace stock; the generated record has no `Distilled water` ingredient and no trace `solutions` block to own stock water. | All three normalized owners. |
| Major | The lactate-to-formate KOMODO variant was overwritten by base DSMZ 705 and falsely merged. | `msa_fe_medium_replace_na_lactate_with_na_formate.yaml` identifies KOMODO `705_replace_Na-lactate_with_Na-formate` but has `Na-lactate` and no formate row after `dsmz-resolver-v1.0` copied ingredients from DSMZ Medium 705. | `data/normalized_yaml/bacterial/msa_fe_medium_replace_na_lactate_with_na_formate.yaml`; KOMODO DSMZ resolver and merge overlay. |
| Major | Two hydrate-specific salts are grounded too broadly. | The source specifies K2HPO4 x 3 H2O and NiCl2 x 6 H2O; the record uses groundings labeled dipotassium hydrogen phosphate and nickel dichloride. | All three normalized owners; MIM/CHEBI grounding. |
| Minor | Source evidence is encoded only as notes. | The DSMZ and KOMODO source identifiers appear in free text, generated synonyms, or curation history, but there is no structured reference or evidence tying ingredient rows to DSMZ Medium 705 or KOMODO medium 705. | MediaDive/KOMODO importers or all three normalized owners. |

## Recommended Edits

1. Move DSMZ 705 trace elements into a local `Trace element solution` with the
   1 L water row, then add that stock at 10 ml per 1030 ml final medium.
2. Add the 1000 ml final-medium distilled-water row from DSMZ 705.
3. Restore the KOMODO `705_replace_Na-lactate_with_Na-formate` variant from its
   actual KOMODO composition or mark it unresolved; do not merge it as a
   source duplicate of DSMZ 705 while it claims a formate substitution.
4. Re-ground `K2HPO4 x 3 H2O` and `NiCl2 x 6 H2O` to exact verified hydrate
   terms, or remove the broad CHEBI terms until exact hydrate terms are
   verified.
5. Add structured source provenance for DSMZ Medium 705 and the two KOMODO
   source IDs, then regenerate merged products.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on all three normalized
  owners after solution, variant, water, grounding, and provenance edits.
- Regenerate merges and verify `BACILLUS_INFERNUS_MEDIUM.yaml` has a 10 ml
  trace stock addition, no top-level stock-strength trace rows, and no
  source-duplicate relationship to the formate variant unless the variant
  truly has the same composition.
- Compare the regenerated DSMZ owner manually against DSMZ Medium 705, focusing
  on the 1030 ml final volume, the two water rows, the trace stock, and the
  acetate/lactate/coenzyme M stock-addition instructions.

## Additional Notes

- The DSMZ PDF rendered visually through Quick Look. Its normal `pypdf`
  extraction returned empty strings, so I decoded the page content streams as
  UTF-16BE literal text to inspect page 2 and corroborate the rendered first
  page.
- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
