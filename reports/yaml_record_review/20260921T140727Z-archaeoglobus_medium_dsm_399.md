# YAML Record Review: archaeoglobus_medium_dsm_399

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/archaeoglobus_medium_dsm_399.yaml`
- Started UTC: 2026-09-21T14:05:41Z
- Finished UTC: 2026-09-21T14:07:27Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| ID | `CultureMech:009220` |
| Name | `archaeoglobus_medium_dsm_399` |
| Original name | Archaeoglobus medium (DSM 399) |
| Category | `archaea` |
| Source identity | `TOGO:M2665`, Archaeoglobus medium (DSM 399) |
| Primary source | ATCC Medium 1775, Archaeoglobus medium (DSM 399) |
| Source URL | `https://togomedium.org/medium/M2665` |
| Primary source URL | `https://www.atcc.org/~/media/385F0331DBAE42A3B87040A1D040AC39.ashx` |
| Merge fingerprint | `6573f7ee767003b08e1e2cfab5785f795bcb68099443f56c7ce260eab16a5dfb` |
| Merged from | `archaeoglobus_medium_dsm_399` |

This is a generated merge record. The maintained recipe owner is
`data/normalized_yaml/archaea/archaeoglobus_medium_dsm_399.yaml`; importer-level
failures should be repaired in the TOGO/ATCC import path and regenerated into
`data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_medium_dsm_399.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_medium_dsm_399.yaml --out /private/tmp/archaeoglobus_medium_dsm_399.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_medium_dsm_399.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Failed with 3 errors after a network-enabled rerun: the Tarui target-organism snippet and Reed variant snippet were not found as substrings; the Hartzell Methods in Enzymology DOI had no fetched content. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_medium_dsm_399.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: no focused history validator for one generated merge record is documented. |

## Identity and Grounding

The source identity is correct. The generated record points to `TOGO:M2665`;
the TOGO M2665 API calls the source Archaeoglobus medium (DSM 399) and links
to the ATCC Medium 1775 PDF with the same title.

An ignored-inclusive exact search across `data/normalized_yaml`,
`data/merge_yaml`, `data/culturemech_id_registry.tsv`,
`data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`, and the import-tracking
plausibility and duplicate reports found one normalized owner for
`CultureMech:009220` / `TOGO:M2665`, the reviewed generated merge, the expected
catalog/index rows, two summed-duplicate rows for MgSO4 x 7H2O and NaCl, and
one plausibility row for the resazurin unit slip.

The embedded Trace Elements Solution is not the same as
`mediadive.solution:6129`, despite sharing a generic label. ATCC lists a local
solution with NTA, MgSO4 x 7H2O, MnSO4 x 2H2O, NaCl, FeSO4 x 7H2O,
CoSO4 x 7H2O, CaCl2 x 2H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O,
KAl(SO4)2 x 12H2O, H3BO3, Na2MoO4 x 2H2O, NiCl2 x 6H2O,
Na2SeO3 x 5H2O, and water. The referenced `mediadive.solution:6129` is a
different ZnSO4/MnCl2/MoO3/CuSO4/cobalt nitrate solution and should not be
used for this stock.

Several exact ingredient identities still need resolver review:

- `Na2SeO3 x 5H2O` is grounded to `CHEBI:48843` disodium selenite, broader than
  the pentahydrate named by ATCC and TOGO.
- `NiCl2 x 6H2O` is grounded to generic nickel dichloride.
- The rows imported only inside the flattened trace stock are missing
  `mediaingredientmech_chebi_term` links.

## Evidence

The ATCC source and TOGO API agree that the final medium uses 1 L distilled
water, 10 ml Trace Elements Solution, 1 mg resazurin, 2 mg
Fe(NH4)2(SO4)2 x 7H2O, and gram quantities for the salts, sodium bicarbonate,
sodium lactate, yeast extract, and sodium sulfide. The generated record
misrepresents several of those values:

- The generated merge is stale for water. It still has a flattened
  `2.0 G_PER_L` distilled-water row; the normalized owner was repaired on
  2026-09-02 to collapse the two identical 1 L rows, although that owner still
  stores the remaining source volume as `1.0 G_PER_L`.
- The 10 ml Trace Elements Solution is stored as an empty `G_PER_L` solution
  and its internal solutes were moved into the final `ingredients` list.
- Flattening summed stock rows into final rows: MgSO4 x 7H2O is
  `6.45 G_PER_L` from 3.45 g final plus 3.0 g stock, NaCl is `19.0 G_PER_L`
  from 18.0 g final plus 1.0 g stock, and CaCl2 x 2H2O is
  `0.24000000000000002 G_PER_L` from 0.14 g final plus 0.1 g stock.
- `Na2SeO3 x 5H2O` is 0.3 mg in the trace stock, but the record stores
  `0.3 G_PER_L`.
- Resazurin and Fe(NH4)2(SO4)2 x 7H2O are 1 mg and 2 mg in the source, but the
  generated record stores them as `1 G_PER_L` and `2 G_PER_L`.
- `KOH solusion` is a misspelled, variable final solution row. In the ATCC
  source KOH is used only to dissolve nitrilotriacetic acid at pH 6.5 and
  adjust the trace stock to pH 7.0.

The preparation notes are absent. ATCC instructs readers to dissolve all
ingredients except sodium bicarbonate and sodium sulfide, boil for 3 minutes,
cool while gassing with 80% N2 and 20% CO2, add bicarbonate and adjust to
pH 6.9, dispense anaerobically under the same gas phase, pressurize sealed
containers up to 2 bar, autoclave, and add sodium sulfide from an anaerobic
neutral stock before inoculation. The Trace Elements Solution also has a
separate pH-adjusted preparation. None of that survives in the generated
record beyond variable gas rows and `KOH solusion`.

The manually added organism and STL variant evidence needs source-level
reinspection. The DOI reference validator could not verify any of the three
supporting snippets: it reported exact-text failures for the Tarui and Reed
snippets and no available content for the Hartzell DOI.

## Completeness

The main formula is not complete enough to reconstruct ATCC Medium 1775 because
the trace stock is absent, top-level concentrations blend final and stock
recipes, source milligrams became grams per liter, final-volume water remains
a concentration row, and all preparation text is missing.

The target-organism and variant slots are populated but not fully verified.
They should remain review candidates until the DOI snippets are replaced with
exact excerpts from inspected source text or until a curator narrows the claims
to text the fetched references actually support.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge lags the normalized 2026-09-02 water repair. | The merge has `2.0 G_PER_L` distilled water from two identical source volume rows; the normalized owner has already collapsed that to `1.0 G_PER_L`. | Regenerate `data/merge_yaml/merged/archaeoglobus_medium_dsm_399.yaml`. |
| Major | Final and stock waters are dimensionally wrong. | ATCC and TOGO store both water rows as 1 L volumes, while the normalized owner stores one remaining row as `1.0 G_PER_L`; the generated merge stores the stale sum as `2.0 G_PER_L`. | Fix TOGO liter-water unit conversion and repair `data/normalized_yaml/archaea/archaeoglobus_medium_dsm_399.yaml`. |
| Major | Trace Elements Solution is flattened and linked to the wrong external solution. | The source adds 10 ml of a local trace stock; the record moves its internal solutes into the final medium and points to unrelated `mediadive.solution:6129`. | Model the local ATCC stock in the normalized owner and remove the incorrect MediaDive link. |
| Major | Stock and final ingredient amounts are arithmetically conflated. | MgSO4 x 7H2O, NaCl, and CaCl2 x 2H2O are sums of final-medium and trace-stock rows. | Fix the source importer or repair the normalized owner so final ingredients and trace-stock ingredients are distinct. |
| Major | Milligram rows are encoded as grams per liter. | ATCC specifies 1 mg resazurin, 2 mg Fe(NH4)2(SO4)2 x 7H2O, and 0.3 mg Na2SeO3 x 5H2O; the record stores the same numeric values with `G_PER_L`. | Preserve milligram units in the TOGO import and repair affected rows. |
| Major | Preparation semantics were dropped. | Boiling, 80/20 N2/CO2 gassing, pH 6.9 adjustment, anaerobic dispensing, 2 bar pressurization, autoclaving, sulfide addition, and trace-stock pH adjustment are absent. | Add ATCC-supported preparation notes or structured preparation fields to the normalized owner. |
| Major | DOI-backed organism and variant snippets fail reference validation. | The network-enabled reference validator found 3 errors across `doi:10.7888/juoeh.29.131`, `doi:10.1016/s0076-6879(99)10027-2`, and `doi:10.1128/jb.183.24.7007-7016.2001`. | Reinspect the cited papers and replace snippets with exact, supported excerpts or narrow the claims. |
| Minor | Several exact chemical groundings are incomplete. | Hydrate-specific trace-stock labels either have broader ChEBI terms or no `mediaingredientmech_chebi_term` after the June grounding migrations. | Re-run exact resolver checks for the affected hydrate labels. |

## Recommended Edits

1. Repair the TOGO/ATCC importer so local Trace Elements Solution is nested as
   its own stock and 10 ml remains a stock addition amount.
2. Repair `data/normalized_yaml/archaea/archaeoglobus_medium_dsm_399.yaml`:
   separate final MgSO4, NaCl, and CaCl2 rows from trace-stock rows; restore
   milligram units for resazurin, Fe(NH4)2(SO4)2 x 7H2O, and Na2SeO3 x 5H2O;
   model the trace stock water and pH adjustment; and remove the wrong
   `mediadive.solution:6129` reference.
3. Add the ATCC preparation instructions to the normalized owner, including
   the source gas ratio, pH 6.9 target, 2 bar pressurization, and neutral
   anaerobic sodium sulfide stock addition.
4. Reinspect the Tarui, Hartzell, and Reed DOI full texts and replace the
   generated snippets with exact excerpts that the reference validator can
   verify.
5. Resolve exact ChEBI and MIM links for the remaining hydrate rows without
   inventing unavailable terms.
6. Regenerate `data/merge_yaml/merged/` so this generated record picks up the
   2026-09-02 water repair and the future source-shape fixes.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/archaea/archaeoglobus_medium_dsm_399.yaml`
  and `just validate-strict data/normalized_yaml/archaea/archaeoglobus_medium_dsm_399.yaml`
  after the repair.
- Rerun `just validate-references data/normalized_yaml/archaea/archaeoglobus_medium_dsm_399.yaml`
  after replacing the DOI snippets.
- Rerun `just validate-terms data/normalized_yaml/archaea/archaeoglobus_medium_dsm_399.yaml`
  after grounding fixes.
- Rerun `just verify-merges` and `just audit-merge-freshness` after
  regenerating the merge layer.
- Recheck `data/import_tracking/reports/merged_duplicates.tsv` and
  `data/import_tracking/reports/concentration_plausibility.tsv`; this record
  should no longer appear for summed MgSO4/NaCl/CaCl2 rows or gram-scale
  resazurin.

## Additional Notes

- The ATCC M2665 formula differs legitimately from DSMZ Medium 399 in details
  such as NaHCO3 amount, nickel amount, and MnSO4 hydration; those source
  differences are not defects by themselves.
- Empty optional slots not implicated in the flattened stock issue were left
  unflagged.
