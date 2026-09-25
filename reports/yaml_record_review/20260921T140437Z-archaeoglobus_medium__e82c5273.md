# YAML Record Review: archaeoglobus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/archaeoglobus_medium__e82c5273.yaml`
- Started UTC: 2026-09-21T14:03:45Z
- Finished UTC: 2026-09-21T14:04:37Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| ID | `CultureMech:008192` |
| Name | `archaeoglobus_medium` |
| Original name | Archaeoglobus Medium |
| Category | `archaea` |
| Source identity | `TOGO:M1637`, Archaeoglobus Medium |
| Upstream source | NBRC Medium 840 |
| Source URL | `https://togomedium.org/medium/M1637` |
| Upstream URL | `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=840` |
| Merge fingerprint | `e82c527304258e1bcc4c0a921a7fbdfbf7b664c9338ad67b36e58ab41581652b` |
| Merged from | `TOGO_M1637_Archaeoglobus_Medium` |

The reviewed YAML is a generated merge artifact. The maintained input that owns
content fixes is `data/normalized_yaml/archaea/TOGO_M1637_Archaeoglobus_Medium.yaml`,
with source-shape defects likely owned by the TOGO importer and its stock
solution parser.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_medium__e82c5273.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_medium__e82c5273.yaml --out /private/tmp/archaeoglobus_medium__e82c5273.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_medium__e82c5273.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_medium__e82c5273.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: the repository does not document a focused history validator for one generated merge record. |

## Identity and Grounding

The record's TOGO identity is coherent: the TOGO M1637 API names Archaeoglobus
Medium and points to the NBRC Medium 840 page; the generated record stores the
same TOGO accession, original NBRC provenance, and Archaeoglobus Medium label.

An ignored-inclusive exact search over `data/normalized_yaml`,
`data/merge_yaml`, `data/culturemech_id_registry.tsv`,
`data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`, and the import-tracking duplicate
and plausibility reports found one normalized owner for `CultureMech:008192`,
this generated merge, the expected registry/catalog/manifest rows, two
summed-duplicate diagnostics for NaCl and CaCl2 x 2 H2O, and plausibility
diagnostics for the flattened indicator, trace, and vitamin quantities.

Two stock references denote the wrong MediaDive stocks:

- NBRC M840 and TOGO M1637 define a local `Trace elements solution**` with
  NTA, FeCl3 x 6 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2,
  CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NaCl, NiCl2 x 6 H2O, Na2SeO4,
  Na2WO4, KAl(SO4)2 x 12 H2O, and water. The record instead references
  `mediadive.solution:6129`, whose local composition is a different
  ZnSO4/MnCl2/MoO3/CuSO4/cobalt nitrate stock.
- NBRC M840 and TOGO M1637 define a local `Vitamin solution***` with nine
  vitamin solutes plus water. The record instead references
  `mediadive.solution:6241`, a 100 ml stock with cyanocobalamin, thiamine HCl,
  biotin, and water.

Several ingredient groundings also need review. The main `Na2S2O3` row is
grounded to sodium thiosulfate pentahydrate even though the source names
anhydrous `Na2S2O3`; `Fe(NH4)2SO4 x 6H2O` lacks a ChEBI grounding; and the
hydrate labels for `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are broader generic
chloride terms.

## Evidence

The NBRC M840 page and the TOGO M1637 API agree on the top-level formulation:
1 L distilled water; 5 ml KP buffer; 2 ml trace elements solution; 2 ml vitamin
solution; gram quantities for MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, NaCl,
Na2S2O3, sodium acetate, coenzyme M, Na2CO3, and Na2S x 9H2O; milligram
quantities for Fe(NH4)2SO4 x 6H2O and resazurin; and H2/CO2 plus N2 gas
handling steps.

The generated record validates but misplaces stock composition:

- The 5 ml KP buffer, 2 ml trace stock, and 2 ml vitamin stock are represented
  as empty solution rows with `G_PER_L` units.
- KP buffer ingredients `KH2PO4` and `K2HPO4` are top-level final-medium
  ingredients at `119 G_PER_L` and `21 G_PER_L` even though they are per-liter
  stock ingredients.
- Trace stock ingredients are top-level final-medium ingredients. This creates
  summed duplicates for NaCl (`30 g` final plus `1 g` stock) and CaCl2 x 2 H2O
  (`0.15 g` final plus `0.1 g` stock), and it leaves the other trace salts at
  stock concentration in the final ingredient list.
- Vitamin stock milligram values are top-level `G_PER_L` rows, for example
  biotin is `2 G_PER_L` instead of 2 mg per liter of vitamin stock.
- Final-medium resazurin and Fe(NH4)2SO4 x 6H2O are also milligram quantities
  from the source but were imported as `1 G_PER_L` and `2 G_PER_L`.

Preparation evidence is missing. NBRC instructs curators to mix the main
ingredients except KP buffer, vitamin solution, Na2CO3, and Na2S x 9H2O;
dispense under 80/20 H2/CO2 and seal with butyl rubber stoppers; autoclave KP
buffer and a 5% Na2S x 9H2O solution separately under N2; filter-sterilize the
vitamin and 10% Na2CO3 solutions; add these solutions aseptically and
anaerobically before inoculation; and pressurize inoculated vessels to 150 kPa
with 80/20 H2/CO2. The generated record keeps only unscoped variable gas rows
and has no preparation notes.

## Completeness

The record is materially incomplete for a recipe that someone could
reconstruct:

- Three named stocks lack their own nested compositions, water rows, and
  preparation conditions.
- Stock additions have amount units that do not match the source milliliter
  additions.
- NBRC's pH note, anaerobic dispense and addition steps, and separate
  sterilization boundaries are absent.
- Unit conversion is wrong for the final milligram additives and for vitamin
  stock milligrams.
- The maintained owner repaired the four identical flattened water rows to a
  single `1.0 G_PER_L` distilled-water row on 2026-09-02, but `1 L` is still a
  volume and the generated merge still has the stale four-row sum.

Empty target-organism and growth-evidence fields are acceptable for this source
record; the inspected NBRC page and TOGO medium record are formula sources, not
strain-specific growth studies.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale for the 2026-09-02 water repair. | `data/merge_yaml/merged/archaeoglobus_medium__e82c5273.yaml` still has `4.0 G_PER_L` distilled water from four flattened 1 L rows; the normalized owner has collapsed that to `1.0 G_PER_L` and records the `repair_merged_duplicates.py` event. | Regenerate this merge from `data/normalized_yaml/archaea/TOGO_M1637_Archaeoglobus_Medium.yaml`. |
| Major | Top-level water remains dimensionally wrong after the normalized repair. | NBRC and TOGO state 1 L distilled water for the final medium; the normalized row is a volume imported as `1.0 G_PER_L`. | Fix the TOGO unit mapping for liter water volumes and repair `data/normalized_yaml/archaea/TOGO_M1637_Archaeoglobus_Medium.yaml`. |
| Major | KP buffer, trace elements, and vitamin stocks are flattened into the final ingredient list. | The source adds 5 ml KP buffer, 2 ml trace elements, and 2 ml vitamins. Their internal solutes are top-level ingredients in the normalized and generated record, with stock grams and milligrams treated as final-medium `G_PER_L`. | Fix the TOGO subcomponent parser and repair the normalized owner through a guarded YAML mutator. |
| Major | Local NBRC stock solutions are linked to wrong MediaDive identities. | `mediadive.solution:6129` and `mediadive.solution:6241` have different compositions from the M1637 trace and vitamin solutions. | Remove or replace those cross-links while modeling the local NBRC stocks. |
| Major | Multiple source milligram rows became gram-per-liter rows. | NBRC and TOGO give Fe(NH4)2SO4 x 6H2O as 2 mg, resazurin as 1 mg, and vitamin stock rows as 0.01 to 10 mg per liter; the generated record stores these values as `G_PER_L`. | Preserve milligram units in the TOGO importer and repair the affected normalized ingredients. |
| Major | NBRC preparation instructions were dropped. | The generated recipe omits pH-unadjusted status, H2/CO2 vessel setup, separate N2 autoclaving, filter sterilization of vitamin and carbonate stocks, aseptic anaerobic addition before inoculation, and the 150 kPa H2/CO2 pressurization. | Add source-supported preparation notes or structured condition fields to the normalized owner. |
| Major | At least one source ingredient is grounded to a chemically different ChEBI term. | The source names `Na2S2O3`; the record grounds it to sodium thiosulfate pentahydrate. | Re-run exact MIM/OAK resolution for `Na2S2O3` and update the normalized owner if an exact term is available. |
| Minor | Several hydrate labels have incomplete or missing ontology links. | `Fe(NH4)2SO4 x 6H2O` is ungrounded, `CoCl2 x 6H2O` and `NiCl2 x 6H2O` are grounded to broader generic salts, and `MnCl2 x 4H2O` lacks `mediaingredientmech_chebi_term`. | Check exact term availability before adding or changing ChEBI links. |

## Recommended Edits

1. Teach the TOGO importer to retain NBRC footnoted stocks as nested stocks
   with milliliter addition amounts, instead of flattening stock solutes into
   the final medium.
2. Repair `data/normalized_yaml/archaea/TOGO_M1637_Archaeoglobus_Medium.yaml`
   so KP buffer, Trace elements solution, and Vitamin solution have their own
   water rows, solute rows, and preparation notes.
3. Remove the unsupported `mediadive.solution:6129` and
   `mediadive.solution:6241` references unless a curator verifies exact local
   stock identities.
4. Restore milligram units for Fe(NH4)2SO4 x 6H2O, resazurin, and vitamin
   stock solutes.
5. Preserve the NBRC anaerobic setup, sterilization, pH, and pressurization
   instructions in preparation notes or structured condition slots.
6. Recheck exact ChEBI grounding for Na2S2O3 and the hydrate salts without
   inventing unavailable hydrate terms.
7. Regenerate the merge artifacts after the normalized repair.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/archaea/TOGO_M1637_Archaeoglobus_Medium.yaml`
  and `just validate-strict data/normalized_yaml/archaea/TOGO_M1637_Archaeoglobus_Medium.yaml`
  after the normalized edit.
- Rerun `just validate-terms data/normalized_yaml/archaea/TOGO_M1637_Archaeoglobus_Medium.yaml`
  after ontology changes.
- Rerun `just verify-merges` and `just audit-merge-freshness` after
  regenerating `data/merge_yaml/merged/`.
- Rerun the duplicate-merge and concentration-plausibility tracking jobs; the
  repaired record should no longer report NaCl/CaCl2 stock sums or gram-scale
  vitamin and indicator slips for `CultureMech:008192`.
- Manually compare the regenerated record against the NBRC 840 page and TOGO
  M1637 JSON so KP buffer, trace elements, and vitamin stock boundaries remain
  intact.

## Additional Notes

The noisy broad `CultureMech:` search output was discarded. The completeness
claim above relies on the later ignored-inclusive exact search for
`CultureMech:008192`, `TOGO:M1637`, the normalized file stem, and the merge
fingerprint.
