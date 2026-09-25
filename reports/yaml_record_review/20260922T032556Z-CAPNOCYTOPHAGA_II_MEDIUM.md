# YAML Record Review: capnocytophaga_ii_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
- Started UTC: 2026-09-22T03:25:56Z
- Finished UTC: 2026-09-22T03:25:56Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:006440`, `capnocytophaga_ii_medium`, class `MediaRecipe`.
- Merge lineage: two source recipes, `KOMODO_779_CAPNOCYTOPHAGA_II_medium` and `capnocytophaga_ii_medium`, on fingerprint `99602cf539ace07b1078b3103ea19f78ab71c745c81ee45bfec4999b72ffa619`.
- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml` and `data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml`.
- Claimed source identities: KOMODO medium 779 mirrored from DSMZ/MediaDive medium 779, and direct DSMZ/MediaDive medium 779.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated record denotes DSMZ/MediaDive Medium 779, `CAPNOCYTOPHAGA II MEDIUM`. The DSMZ PDF and MediaDive JSON agree on the label, complex solid-agar classification, pH 7.6-7.8, nine non-water components, 1000 ml distilled water, and 1050 ml final source volume after 50 ml horse blood is added.
- The duplicate link between the KOMODO import and direct MediaDive/DSMZ import is valid: the active registry/catalog keeps both normalized owners as `ACTIVE`, a gitignore-independent exact search found only those two maintained owners plus the generated merge for `CultureMech:006440`, `CultureMech:001914`, `komodo.medium:779`, and `mediadive.medium:779`, and `find . -iname '*capnocytophaga*'` found this target among expected Capnocytophaga-family records but no hidden or ignored second Medium 779 owner.
- The generated merge chose the KOMODO mirror as the canonical body, so `media_term` is `komodo.medium:779` and `notes` only say `Aerobic: Yes` even though the direct DSMZ owner cites `mediadive.medium:779` and stores the horse-blood addition and incubation steps.
- Lab-Lemco beef extract, Proteose peptone no. 3, Yeast extract, and Horse blood are intentionally ungrounded complex ingredients. The other simple or polymer ingredients use source-compatible CHEBI groundings.

## Evidence

- DSMZ Medium 779 lists Lab-Lemco meat extract 2.4 g, Proteose peptone no. 3 10 g, Yeast extract 5 g, Na2HPO4 4 g, Glucose 1.5 g, soluble Starch 0.5 g, Cysteine-HCl x H2O 0.5 g, Agar if necessary 15 g, Horse blood 50 ml, and Distilled water 1000 ml.
- MediaDive's Medium 779 JSON preserves the same `Main sol. 779` recipe as `mediadive.solution:1584` with the same source attributes, an explicit 1050 ml solution volume, and the same two steps imported on the direct DSMZ medium owner.
- DSMZ and MediaDive both require pH adjustment to 7.6-7.8, addition of horse blood after heat sterilization and cooling to 50 deg C, and incubation either under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2.
- The active solution import `data/normalized_yaml/bacterial/mediadive_1584_Main_sol_779.yaml` represents the same `mediadive.solution:1584` main solution, but the generated medium does not link to it, and the solution stores Horse blood and Distilled water as `47.61904761904761 PERCENT_V_V` and `952.3809523809523 PERCENT_V_V` rather than preserving their 50 ml and 1000 ml source additions.

## Completeness

- The generated record is missing the source `Distilled water` row.
- The generated record stores `Horse blood` as `50 G_PER_L`, but DSMZ and MediaDive both give 50 ml; this loses the source volume unit and makes a blood ingredient look like a weighed solid.
- The generated record is missing the horse-blood post-sterilization step and the CO2/anaerobic incubation alternatives from the direct DSMZ owner.
- Target organisms, variants other than the source-duplicate relationship, and references are empty. DSMZ Medium 779 has enough source context for formula and preparation review, but this record has not tried to curate strain-specific growth claims.

## Findings

- Major: the source-duplicate merge discarded DSMZ/MediaDive preparation instructions. `data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml` stores the horse-blood addition and incubation text, but the generated `CultureMech:006440` body is inherited from the KOMODO mirror and has no `preparation_steps`.
- Major: the generated record omits the required 1000 ml distilled-water component. DSMZ, MediaDive Medium 779, and the active `mediadive.solution:1584` import all include it.
- Major: `Horse blood` has the wrong unit. The source gives 50 ml, while both normalized medium owners and the generated merge store `50 G_PER_L`.
- Minor: the KOMODO note `Aerobic: Yes` is too coarse for the inspected source. DSMZ supports a CO2-enriched aerobic incubation option but also lists a 95% N2 plus 5% CO2 anaerobic option.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml` and `data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml`, not the generated merge.
- Copy the DSMZ `preparation_steps` into the KOMODO mirror or make the merge prefer the direct DSMZ/MediaDive owner when an exact `SOURCE_DUPLICATE` exists, then regenerate the merged record.
- Add `Distilled water` at `1000 ML_PER_L` to both maintained medium owners.
- Change `Horse blood` from `50 G_PER_L` to a volume unit that preserves the source 50 ml addition, and reconcile `data/normalized_yaml/bacterial/mediadive_1584_Main_sol_779.yaml` so the standalone solution does not encode 50 ml and 1000 ml source rows as pseudo-percent values.
- Replace the KOMODO `Aerobic: Yes` note with source-backed incubation text or drop it once the structured preparation steps carry the atmosphere options.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both maintained medium owners and `data/normalized_yaml/bacterial/mediadive_1584_Main_sol_779.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml`.
- Inspect the regenerated merge to confirm it contains `Distilled water`, a volume-based `Horse blood` row, both DSMZ steps, and no unsupported standalone aerobic-only note.
- Re-check the MediaDive Medium 779 JSON export and DSMZ PDF to confirm the maintained medium and solution still match all source rows and instructions.

## Additional Notes

- Agar is legitimately conditional in the source text: DSMZ says `Agar, if necessary`, and the generated record keeps the condition as a note while classifying this record as `SOLID_AGAR`.
- `CAPNOCYTOPHAGA_MEDIUM.yaml` is nearby in casefold order but is DSMZ/MediaDive Medium 340, not a duplicate of Medium 779.
