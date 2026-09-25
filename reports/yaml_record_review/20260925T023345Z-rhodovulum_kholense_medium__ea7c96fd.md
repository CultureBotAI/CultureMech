# YAML Record Review: rhodovulum_kholense_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rhodovulum_kholense_medium__ea7c96fd.yaml
- Started UTC: 2026-09-25T02:31:52Z
- Finished UTC: 2026-09-25T02:33:44Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record:

- Path: `data/merge_yaml/merged/rhodovulum_kholense_medium__ea7c96fd.yaml`
- ID: `CultureMech:010067`
- Label: `rhodovulum_kholense_medium`
- Source identity: TOGO Medium M664, original source JCM `JCM_M649`
- Source CURIE: `TOGO:M664`
- Generated from:
  - `data/normalized_yaml/bacterial/TOGO_M664_Rhodovulum_Kholense_Medium.yaml`

The target is a generated singleton merge. Future fixes belong in the
normalized TOGO owner or in TOGO cross-reference import logic, followed by
regeneration of `data/merge_yaml/merged/`.

## Validation

| Check | Result |
| --- | --- |
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rhodovulum_kholense_medium__ea7c96fd.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/rhodovulum_kholense_medium__ea7c96fd.yaml --out /private/tmp/rhodovulum_kholense_medium__ea7c96fd.strict.tsv --workers 1 --quiet` | Passed; 0 error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/rhodovulum_kholense_medium__ea7c96fd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/rhodovulum_kholense_medium__ea7c96fd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- The record ID, normalized label, bacterial category, liquid physical state,
  and TOGO M664 source identity are internally aligned.
- TOGO M664 resolves to `Rhodovulum Kholense Medium`, carries source pH 7.0,
  and records original source `JCM_M649` with the JCM `GRMD=649` URL.
- MediaDive's JCM J649 REST record also resolves `GRMD=649` as
  `RHODOVULUM KHOLENSE MEDIUM`, pH 7.0, and a recipe with the same seven
  base components plus 1000 ml distilled water and 1 ml of the SL12 stock
  from Medium 497. Its g/L values are 1000/1001 conversions of the source
  masses because it counted the 1 ml stock in the final volume.
- The live JCM `GRMD=649` page was inspected on 2026-09-25 and returned
  `Nothing found`; TOGO M664 and MediaDive J649 remained the usable secondary
  captures of the JCM formulation.
- The exact ignored-inclusive search covered `data` and `src` YAML and Python
  files for `TOGO:M664`, `mediadive.medium:J649`,
  `TOGO_M664_Rhodovulum_Kholense_Medium`,
  `JCM_J649_RHODOVULUM_KHOLENSE_MEDIUM`, and `JCM_M649`. It found the TOGO
  owner, the generated TOGO target, the JCM owner, the generated JCM sibling,
  and `data/metal_ree_analysis.yaml`.

## Evidence

- TOGO M664 supports the seven base medium components and masses represented
  by the target: distilled water 1 L, MgSO4 x 7 H2O 2 g, yeast extract 0.5 g,
  NaCl 20 g, CaCl2 x 2 H2O 0.12 g, KH2PO4 0.5 g, NH4Cl 0.64 g, and sodium
  pyruvate 3 g.
- TOGO M664 supports a stock addition named
  `Trace element solution SL--12 (see Medium [M497])` at 1 ml, not a stock
  entry at `1 G_PER_L`.
- TOGO M497, the stock cross-reference named by M664, contains a
  `Trace element solution SL--12` subcomponent with 1 L distilled water and
  the expected molybdate, borate, FeSO4, MnCl2, CoCl2, NiCl2, CuCl2, ZnCl2,
  and disodium EDTA salts. That inspected source supports resolving the empty
  `solutions` placeholder to a real stock record instead of leaving
  `composition: []`.
- The source pH 7.0 from TOGO M664 is not represented as `ph_value`.
- The source JCM page URL is correct historically in both TOGO and MediaDive
  captures, but the live page was unavailable at review time, so the record
  should retain the TOGO source URL and source metadata rather than cite a
  newly inspected live JCM formulation.

## Completeness

- The generated target has no final-medium volume semantics for distilled
  water; `1 L` was converted to `1 G_PER_L`.
- The generated target has an empty, unit-damaged SL-12 stock reference.
- The generated target has no `ph_value`, even though TOGO M664 declares
  pH 7.0.
- The generated target has no explicit `SOURCE_DUPLICATE` or variant relation
  to the MediaDive JCM J649 sibling, although both records are secondary
  captures of JCM `GRMD=649`.
- The generated target has no target-organism, growth-metric, reference, or
  evidence blocks. These are optional in the schema and TOGO M664 does not by
  itself establish a specific growth outcome.

## Findings

### Major

1. **Water and stock volumes were imported as grams per liter.**
   The TOGO source says final `Distilled water` is `1 L` and the SL-12 stock
   addition is `1 ml`. The target encodes both as `G_PER_L`, which is
   dimensionally wrong and hides the difference between a liter final volume
   and a milliliter stock addition. Future fixes belong in
   `data/normalized_yaml/bacterial/TOGO_M664_Rhodovulum_Kholense_Medium.yaml`
   or in `src/culturemech/import/togo_importer.py` volume handling.

2. **The M497 stock cross-reference was not resolved.**
   The source points to `Medium [M497]`, and the inspected TOGO M497 payload
   contains the `Trace element solution SL--12` composition. The target keeps
   an `Unknown solution` with `composition: []`, so a reader cannot reconstruct
   the required trace salts. Future fixes belong in the TOGO owner and the
   importer path that maps `reference_media_id` cross-references to reusable
   solution records.

3. **The source pH is missing.**
   TOGO M664 declares pH 7.0, and the MediaDive JCM J649 capture agrees. The
   target has no `ph_value`, so a required culture condition from the source
   was dropped by TOGO import or normalization.

4. **The JCM/TOGO duplicate set is split and chemically inconsistent.**
   TOGO M664 and MediaDive JCM J649 both capture the same JCM `GRMD=649`
   recipe, but they generate as separate records. The JCM sibling maps the
   free-text SL12 stock to `mediadive.solution:6236`, whose normalized
   composition is a different micronutrient solution, while the TOGO sibling
   leaves the JCM Medium 497 stock unresolved. Future curation should repair
   the two stock references and then add the appropriate `SOURCE_DUPLICATE`
   relationship between `TOGO_M664_Rhodovulum_Kholense_Medium.yaml` and
   `JCM_J649_RHODOVULUM_KHOLENSE_MEDIUM.yaml`.

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/TOGO_M664_Rhodovulum_Kholense_Medium.yaml`
   so `Distilled water` keeps source volume semantics and
   `Trace element solution SL--12 (see Medium [M497])` is represented as a
   1 ml/L stock addition, not as `G_PER_L`.
2. Teach `src/culturemech/import/togo_importer.py` to preserve or resolve
   `reference_media_id: M497` stock links so regenerated TOGO M664 records do
   not keep `composition: []` placeholders for resolvable stock solutions.
3. Add pH 7.0 from TOGO M664 to the normalized owner.
4. Review the MediaDive JCM J649 owner and `mediadive.solution:6236` mapping;
   its source string says SL12 / Medium 497, but the current linked solution
   is not the M497 SL-12 stock.
5. After the TOGO and JCM owners both represent JCM `GRMD=649` faithfully,
   add reciprocal `SOURCE_DUPLICATE` metadata and regenerate
   `data/merge_yaml/merged/`.

## Follow-up Checks

- `just validate data/normalized_yaml/bacterial/TOGO_M664_Rhodovulum_Kholense_Medium.yaml`
- `just validate data/normalized_yaml/bacterial/JCM_J649_RHODOVULUM_KHOLENSE_MEDIUM.yaml`
- The focused open-schema, strict, reference, and term validators used in this
  review against the regenerated generated targets.
- A manual comparison of the regenerated TOGO M664 owner against the inspected
  TOGO M664 and M497 JSON payloads, specifically checking pH 7.0, 1 L final
  distilled water, and the 1 ml SL-12 stock boundary.
- An exact ignored-inclusive search for `TOGO:M664`, `mediadive.medium:J649`,
  `JCM_M649`, and the owner stems before adding duplicate links, so any
  existing stale relation is found before curation.

## Additional Notes

- The sibling generated JCM and DSMZ/KOMODO `rhodovulum_kholense_medium`
  records were inspected only to bound identity and duplicate risk; their
  detailed defects belong in their own reports.
- The M497 normalized owner
  `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`
  is not a ready stock solution. It has the same TOGO volume/unit flattening
  pattern as this record and should not be copied wholesale to repair M664
  without preserving the stock subcomponent boundary from the TOGO M497
  payload.
