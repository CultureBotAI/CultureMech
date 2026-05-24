# Media Ingredient And Variant State Assessment

Date: 2026-05-13

## Objective

Assess the current state of CultureMech media YAML records for ingredient
validity, concentration coverage, and media variation modeling. The requested
target model is that media variations should be represented as child YAML
records, while parent media YAML records contain links to those child records,
across the full `data/normalized_yaml/**/*.yaml` corpus.

## Generated Assessment Artifacts

- `reports/media_content_review_manifest.tsv`
- `reports/media_content_review_manifest.json`
- `reports/media_content_review_manifest_summary.md`
- `reports/media_variation_candidate_groups.tsv`
- `reports/media_variation_candidate_groups.json`
- `scripts/build_media_content_review_manifest.py`
- `scripts/validate_media_variant_links.py`
- `reports/media_variant_link_validation.tsv`
- `reports/media_variant_link_validation.md`
- `scripts/propose_media_variant_links.py`
- `scripts/apply_media_variant_links.py`
- `reports/media_variant_link_proposals.tsv`
- `reports/media_variant_link_proposals.json`
- `reports/media_variant_parent_group_proposals.tsv`
- `reports/media_variant_parent_group_proposals.json`
- `reports/media_variant_link_proposal_summary.md`
- `reports/media_variant_link_apply_plan.tsv`
- `reports/media_variant_link_apply_plan.json`
- `reports/media_variant_algae_source_duplicate_review.md`
- `reports/media_variant_zahorchak_grid_review.md`
- `reports/media_variant_m63_salinity_grid_review.md`
- `reports/media_variant_802_salinity_grid_review.md`
- `reports/media_variant_rdm_salinity_grid_review.md`
- `reports/media_variant_defined_freshwater_cobalt_grid_review.md`
- `reports/media_variant_potato_carrot_agar_review.md`
- `reports/media_variant_btt_medium_review.md`
- `reports/media_variant_xed_agar_review.md`
- `reports/media_variant_tcg_medium_review.md`
- `reports/media_variant_ypg_medium_review.md`
- `reports/media_variant_dsmz_komodo_source_duplicate_review.md`
- `reports/media_variant_asw_barley_salinity_grid_review.md`
- `reports/media_variant_m9_kazan_glucose_grid_review.md`
- `reports/media_variant_m9_park_zinc_grid_review.md`
- `reports/media_variant_mrs_fructose_grid_review.md`
- `reports/media_variant_hassan_limiting_grid_review.md`
- `reports/media_variant_m40y_sucrose_grid_review.md`
- `reports/media_variant_802_glucose_grid_review.md`
- `reports/media_variant_desulfovibrio_brackish_salinity_review.md`
- `reports/media_variant_fungal_mcafes_glucose_grid_review.md`
- `reports/media_variant_mrs_nacl_salinity_review.md`
- `reports/media_variant_hmm_junlon_grid_review.md`
- `reports/media_variant_reinforced_clostridial_sea_salt_review.md`
- `reports/media_variant_small_axis_batch_review.md`
- `reports/media_variant_inorganic_defined_freshwater_review.md`
- `reports/media_variant_isolated_one_axis_review.md`
- `reports/media_variant_lb_salinity_review.md`
- `reports/media_variant_horikoshi_salinity_review.md`
- `reports/media_variant_source_local_salinity_review.md`
- `reports/media_variant_halobacteria_review.md`
- `reports/media_variant_salinity_ph_review.md`
- `reports/media_variant_strength_buffer_review.md`
- `reports/media_variant_mixed_one_axis_review.md`
- `reports/media_variant_isp_cys_pfennig_methylobacterium_review.md`
- `reports/media_variant_mmys_lb_nitrifier_salinispira_review.md`
- `reports/media_variant_togo_nbrc_agar_strength_review.md`
- `reports/media_variant_togo_nbrc_strength_review.md`
- `reports/media_variant_togo_sw_cmye_gym_r2a_review.md`
- `reports/media_variant_specialized_strength_review.md`
- `reports/media_variant_dilution_named_strength_review.md`
- `reports/media_variant_r2a_nutrient_agar_dilution_review.md`
- `reports/media_variant_misc_strength_salinity_review.md`
- `reports/media_variant_tsb_gym_salinity_review.md`
- `reports/media_variant_lb_r2a_cys_review.md`
- `reports/media_variant_same_name_duplicate_agar_review.md`
- `reports/media_variant_togo_tsb_nacl_ph_review.md`
- `reports/media_variant_same_name_concentration_source_review.md`
- `reports/media_variant_defined_strength_concentration_review.md`
- `reports/media_variant_ym_sw_k_concentration_review.md`
- `reports/media_variant_rhodobacter_halosimplex_acetobacter_review.md`
- `reports/media_variant_haloalkaliphile_alkaliphilus_chitin_review.md`
- `reports/media_variant_anaerobe_ml_concentration_review.md`
- `reports/media_variant_nam_tsby_gauze_573c_review.md`
- `reports/media_variant_rhodobium_mj_asw_acetobacter_dc8a_review.md`
- `reports/media_variant_acid_hypho_manning_marinitoga_review.md`
- `reports/media_variant_anaerobe_halobacteria_l21_review.md`
- `reports/media_variant_nutrient_agar_source_duplicate_review.md`
- `reports/media_variant_gyp_source_duplicate_review.md`
- `reports/media_variant_medium_88_source_duplicate_review.md`
- `reports/media_variant_phototrophic_source_duplicate_review.md`
- `reports/media_variant_sulfurimonas_source_duplicate_review.md`
- `reports/media_variant_yps_source_duplicate_review.md`

These were generated by:

```bash
just review-media-content
just propose-media-variant-links
just apply-media-variant-links
just apply-media-variant-links --signature 2c595e09214e74c8 --apply
just validate-media-variant-links
```

## Current Corpus State

The assessment script scanned all 15,827 normalized YAML records and loaded all
of them successfully.

Key counts:

- Records scanned: 15,827
- Direct ingredient entries: 170,691
- Solution composition entries: 24
- Total ingredient/component entries: 170,715
- Records with complete concentration object/value/unit coverage: 15,453
  (97.6%)
- Records where every component has a CHEBI `term.id`: 1,822 (11.5%)
- Records with embedded `variants`: 25
- Embedded variant entries: 36
- Records using `culturemech_term` component links: 0
- Candidate ingredient-identity variation groups: 1,451

Directory distribution:

| Directory | Records | Components | Missing concentration objects | Embedded variants |
|---|---:|---:|---:|---:|
| `algae` | 248 | 1,331 | 0 | 14 |
| `archaea` | 63 | 1,297 | 0 | 0 |
| `bacterial` | 14,937 | 157,789 | 2 | 20 |
| `fungal` | 124 | 999 | 0 | 0 |
| `specialized` | 455 | 9,299 | 0 | 2 |

## Ingredient State

The corpus has broad ingredient coverage, but it is not yet clean enough for a
safe automated parent/child variant migration.

Observed issues:

- Only 145,355 of 170,715 component entries have CHEBI `term.id` values.
- 1,872 component entries use non-CHEBI `term.id` values where the current
  schema expects CHEBI for ingredients.
- 121,711 component entries have MediaIngredientMech terms.
- No component entries currently use `parent_ingredient` or `variant_type`,
  despite the schema having slots for chemical parent/variant relationships.
- Common unexpected ingredient keys remain in the normalized YAML, especially
  `synonyms`, `source`, `curation_metadata`, and ingredient-level
  `data_quality_flags`.

Interpretation:

- Ingredient identity is partially normalized, but many records still mix
  CHEBI-compatible ingredients with FOODON/UBERON/other terms or local
  unstructured fields.
- Chemical variant modeling at the ingredient level is not populated yet.
  Hydrate/salt/anhydrous relationships cannot be relied on for parent/child
  media grouping until `parent_ingredient` and `variant_type` are enriched.

## Concentration State

The corpus mostly has syntactic concentration fields, but many concentrations
are semantically weak.

Observed issues:

- Missing concentration object: 2 component entries.
- Malformed concentration object: 0.
- Missing concentration value: 0.
- Missing concentration unit: 0.
- Non-schema concentration units: 533.
- `VARIABLE` is common: 6,649 records use it as a concentration unit.

Interpretation:

- The current YAML usually has a `concentration` block, but `VARIABLE` should
  be treated as unresolved concentration data, not a validated numeric
  formulation.
- Parent/child grouping must distinguish exact quantitative variants from
  records that only share a vague or placeholder composition.
- Candidate groups based on identical ingredient identities should be reviewed
  with concentration signatures and source provenance before any migration.

## Variation Modeling State

Current state:

- The schema supports embedded `variants` on a `MediaRecipe`.
- The corpus has only 25 records with embedded variants, totaling 36 variant
  entries.
- At the time of the scan, the YAML corpus did not use a first-class
  parent-media link on child records or a first-class child-record link list on
  parent records. A first pilot migration has now added those links for the
  MRS medium duplicate-source family.
- Existing `merge_fingerprint`, `chemical_fingerprint`, and
  `variant_fingerprint` slots are useful for grouping and deduplication, but
  they are not parent/child links.
- Existing `culturemech_term` slots are available for component references, but
  no records currently use them in this corpus-level scan, and they are not a
  complete parent/child media-variant model.

Candidate variation groups:

- The script identified 1,451 ingredient-identity groups with two or more
  records.
- Large groups include known medium families such as Marine Broth/Agar 2216,
  Mineral Medium Brunner, Nutrient Agar, CASO/Tryptic Soy groups, SP4, R2A,
  BHI, MRS, and many DSMZ "modified for strain" records.
- Some very large groups are low-information groups driven by shared placeholder
  ingredient identities and `VARIABLE` concentrations. These are triage leads,
  not validated parent/child relationships.

## Parent/Child Variant Model Needed

The requested target model requires explicit links in both directions. This
pass added schema support for those links and applied one curated pilot group,
but it did not migrate the full 15k YAML corpus into parent/child structure.

Recommended model:

- Parent `MediaRecipe`
  - canonical/base formulation
  - authoritative source identifiers
  - child links to variant YAML records
  - optional summary of variant dimensions, such as salt level, agar/liquid
    state, added blood, modified carbon source, antibiotics, or strain-specific
    supplementation

- Child `MediaRecipe`
  - full formulation for the variant
  - explicit parent link
  - variant relationship type
  - modification summary
  - source/provenance evidence
  - concentration deltas from the parent where computable

Recommended schema additions:

- `MediaRecipe.parent_media`
  - range: a media record reference with `id`, `name`, and path or CURIE
  - present only on child/variant records

- `MediaRecipe.variant_children`
  - range: list of media record references
  - present on canonical parent records

- `MediaRecipe.variant_relationship`
  - child-side controlled value such as `CONCENTRATION_VARIANT`,
    `PHYSICAL_STATE_VARIANT`, `SUPPLEMENTED_VARIANT`,
    `OMITTED_COMPONENT_VARIANT`, `STRAIN_SPECIFIC_VARIANT`, or
    `SOURCE_DUPLICATE`

- `MediaRecipe.variant_modifications`
  - child-side structured or free-text delta summary

The current embedded `variants` list can remain as a lightweight descriptive
summary, but it should not be the only representation once child YAML variant
records are created.

Implemented schema support in this pass:

- Added optional `MediaRecipe.parent_media`
- Added optional multivalued `MediaRecipe.variant_children`
- Added optional `MediaRecipe.variant_relationship`
- Added optional multivalued `MediaRecipe.variant_modifications`
- Added `MediaRecipeReference`
- Added `MediaVariantRelationshipEnum`
- Regenerated `src/culturemech/schema/culturemech_dataclasses.py`
- Added focused tests in `tests/test_media_variant_links.py`
- Added `scripts/validate_media_variant_links.py` to check future
  bidirectional parent/child link consistency

Baseline link validation:

- YAML records scanned: 15,827
- Parent-to-child links: 0
- Child-to-parent links: 0
- Link validation errors: 0
- Link validation warnings: 0

Post-pilot link validation:

- Applied signatures:
  - `2c595e09214e74c8`: MRS duplicate-source family, parent
    `data/normalized_yaml/bacterial/KOMODO_11_MRS_medium.yaml`
  - `6e3ee1a3c9c695bc`: PYX duplicate-source family, parent
    `data/normalized_yaml/bacterial/KOMODO_104b_PYX-MEDIUM.yaml`
  - `f9b40d25dd7564ea`: chopped-meat duplicate-source family, parent
    `data/normalized_yaml/bacterial/KOMODO_78_CHOPPED_MEAT_medium.yaml`
  - `79ce8735eae36f63`: SP4 duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_1076_SP4_MEDIUM.yaml`
  - `98284f238a8e6332`: R2A duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_830_R2A_medium.yaml`
  - `ff55a1b939c8b1e1`: alkaline nutrient agar duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml`
  - `245cf5c381131f84`: Pfennig's medium I duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_28_PFENNIG_S_MEDIUM_I.yaml`
  - `02ea91fe96a22310`: bifidobacterium medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml`
  - `074ae88d45668dd9`: Anaerolinea medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/JCM_J434_ANAEROLINEA_MEDIUM.yaml`
  - `aaa3bc5a2be98c8d`: Methanobacterium medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_119_METHANOBACTERIUM_medium.yaml`
  - `3e6e9392a006590f`: tryptone soya broth TSB duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_545_TRYPTONE_SOYA_BROTH_TSB.yaml`
  - `99a32ee516c9b597`: Ekho Lake strains medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_621a_EKHO_LAKE_STRAINS_medium.yaml`
  - `836f8f3eb7c08f75`: Caldicellulosiruptor medium duplicate-source links,
    parent `data/normalized_yaml/bacterial/KOMODO_640_CALDICELLULOSIRUPTOR_medium.yaml`
  - `a2760304f5488baa`: Methanosarcina medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_120_METHANOSARCINA_medium.yaml`
  - `8d1e18cb925b86bf`: Carboxydothermus medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml`
  - `429e541b82e37824`: ISP2 medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/isp2_medium.yaml`
  - `691ae1d8357dcea5`: Desulfobulbus medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_194_DESULFOBULBUS_MEDIUM.yaml`
  - `908203dd3e59b567`: hemin medium for Mycobacterium duplicate-source links,
    parent `data/normalized_yaml/bacterial/KOMODO_645a_HEMIN_medium_FOR_MYCOBACTERIUM.yaml`
  - `db070afd4a7b01d5`: MV medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/mv_medium.yaml`
  - `068a4df9ff5a55fb`: ASO4 medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/aso4_medium.yaml`
  - `4a2c10c522657329`: TTD medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_480b_TTD-MEDIUM.yaml`
  - `3363ee98aec71d0e`: MPOB medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_684_MPOB_medium.yaml`
  - `6f18efb68d3bf244`: Desulfohalobium utahense medium duplicate-source links,
    parent `data/normalized_yaml/bacterial/KOMODO_1055_DESULFOHALOBIUM_UTAHENSE_medium.yaml`
  - `5e2bc1483373ce88`: Desulfurococcus amylolyticus medium duplicate-source
    links, parent
    `data/normalized_yaml/bacterial/KOMODO_395_DESULFUROCOCCUS_AMYLOLYTICUS_medium.yaml`
  - `54668fe15dec2610`: CM3 medium duplicate-source links, parent
    `data/normalized_yaml/bacterial/KOMODO_520_CM3_medium.yaml`
  - `a01bef0e80c56c1d`: Thermoterrabacterium medium duplicate-source links,
    parent `data/normalized_yaml/bacterial/KOMODO_778_THERMOTERRABACTERIUM_medium.yaml`
  - Larger duplicate-source subset batch:
    `dd384074d2b0bde0`, `5675990270cf94e0`, `920f712dea14424c`,
    `cc5006aebfad0bc2`, `1e4db38724cd4f23`, `751bb2a86fe38a0e`,
    `cdf0873113fda87a`, `227894e5344764b2`, `1ea44e55c82b47bb`,
    `5bff58d5ec311815`, `8033e24331b94f5f`, `e1f0adc4316abec1`,
    `9d044d5c68f340a1`, and `7a93f587b0b1e1da`.
  - Ten-family duplicate-source subset batch:
    `ce6a03cf61c7a96d`, `422a3c1aee912239`, `38bb3d284c5621b1`,
    `fd3120537e12043d`, `f8af438ad36881b4`, `fd59bc76ae9dda0e`,
    `657f937087c05ed1`, `513d4b3dd331afc0`, `6def50c5dc1fd032`,
    and `1e64414ed9f3977b`.
  - Sixteen-family duplicate-source subset batch:
    `31e933071d552d59`, `667de0785e206661`, `c0d715c6fb4a5f6b`,
    `edcccd5702e79d91`, `2254d458684f0f0d`, `c293726997ee0ac7`,
    `2cbc082fe006510b`, `ae0830d754c976de`, `bebf3402f1550c81`,
    `9756552866477dab`, `897c9a9fc47b990b`, `54b8783e81c1d2d4`,
    `f083dc47fedc76c7`, `157db6b52d73edbb`, `b95b3612b88ffef0`,
    and `273307435e947fac`.
  - Fifteen-family duplicate-source subset batch:
    `be44f95fa76676c4`, `37a401be8f6e26a3`, `7a1ae900f6c215cd`,
    `ccc08ecdb83c664d`, `4c13eb6947114a82`, `d9585236171dacf8`,
    `ea84b45bcfe399ce`, `ef45ad2d7b354687`, `9b5f074a733d9bed`,
    `1dc62e76c4439ef5`, `8de38f70c4479db8`, `fd58e248175f9989`,
    `57a33c1c95e969ac`, `2a0a4aa2908e9c70`, and `84d88efc2fc73f15`.
  - Nineteen-family duplicate-source subset batch:
    `6783d5e08d454706`, `3c78ec9ee067ea2a`, `b8c9e0f673112c61`,
    `3bb6aaa1572fa621`, `c50c4ae8cb0a7b6b`, `2acc4afa1af41340`,
    `6842233c8e895f42`, `fadbd1e98fa049eb`, `6a7a6de7222a2119`,
    `ab7a2097c8873a7f`, `6f5c6f5d1b5eff32`, `df25543bd2a7cb88`,
    `6e393e0d347a6134`, `1a4bf0f907552826`, `a9d3165abeb945cd`,
    `03e437acafb07831`, `2d255b097110e715`, `87eeaffada6da354`,
    and `93a63df61531f8af`.
- Remaining non-algae high-confidence duplicate-source batch:
    439 additional child links from `reports/media_variant_link_proposals.tsv`,
    excluding broad algae-family rows for separate review.
- Algae exact-signature duplicate-source candidates were downgraded to
  `REVIEW_REQUIRED` instead of applied, because the remaining groups have
  semantically broad medium names despite identical parsed ingredients.
  See `reports/media_variant_algae_source_duplicate_review.md`.
- Zahorchak et al. ATP/Mg2+ concentration-grid batch:
  `a451d0b41bb50a0d` and `812c7a4f12d1fe82`, adding 28
  `CONCENTRATION_VARIANT` child links under two MediaDB-backed parent records.
  See `reports/media_variant_zahorchak_grid_review.md`.
- Modified M63 salinity-grid batch: `42d068b346bbb298`,
  `abfd3d312a99ff4e`, and `0db83e9ece8944f6`, adding 9
  `SALINITY_VARIANT` child links under three MediaDB-backed parent records.
  See `reports/media_variant_m63_salinity_grid_review.md`.
- 802 NaCl salinity-grid batch: `cf7e86da02e4150a`, adding 3
  `SALINITY_VARIANT` child links under one TOGO/NBRC-backed parent record.
  See `reports/media_variant_802_salinity_grid_review.md`.
- RDM NaCl salinity-grid batch: `4dec2a88209ec06e`, adding 2
  `SALINITY_VARIANT` child links under one MediaDB-backed parent record.
  See `reports/media_variant_rdm_salinity_grid_review.md`.
- Defined freshwater cobalt-grid batch: `d886f172259919ee` and
  `5a3514d1623cfe0a`, adding 6 `CONCENTRATION_VARIANT` child links under two
  MediaDB-backed parent records. See
  `reports/media_variant_defined_freshwater_cobalt_grid_review.md`.
- Potato-Carrot Agar concentration batch: `80268265dbacd17d`, adding 2
  `CONCENTRATION_VARIANT` child links under one JCM-backed parent record. See
  `reports/media_variant_potato_carrot_agar_review.md`.
- BTT medium concentration batch: `f16eefbb7fe8c11d`, adding 2
  `CONCENTRATION_VARIANT` child links under one JCM-backed parent record. See
  `reports/media_variant_btt_medium_review.md`.
- XED Agar concentration batch: `2b26a51f391142ee`, adding 2
  `CONCENTRATION_VARIANT` child links under one JCM-backed parent record. See
  `reports/media_variant_xed_agar_review.md`.
- TCG medium concentration batch: `3ce61b2bc10aaf9a`, adding 2
  `CONCENTRATION_VARIANT` child links under one JCM-backed parent record. See
  `reports/media_variant_tcg_medium_review.md`.
- YPG medium source-duplicate batch: adding 2 `SOURCE_DUPLICATE` child links
  under two DSMZ-backed parent records. See
  `reports/media_variant_ypg_medium_review.md`.
- DSMZ/KOMODO source-duplicate batch: adding 652 `SOURCE_DUPLICATE` child links
  under six hundred fifty-two DSMZ-backed parent records. See
  `reports/media_variant_dsmz_komodo_source_duplicate_review.md`.
- ASW barley salinity-grid batch: `20de1cbb500637ad`, adding 2
  `SALINITY_VARIANT` child links under one CCAP-backed parent record. See
  `reports/media_variant_asw_barley_salinity_grid_review.md`.
- M9 Kazan glucose-grid batch: `9c2bddbdb1331396`, adding 4
  `CONCENTRATION_VARIANT` child links under one MediaDB-backed parent record.
  See `reports/media_variant_m9_kazan_glucose_grid_review.md`.
- M9 Park zinc-grid batch: `1a914136a7c31a86`, `fde0496d256fac66`,
  `48c2f351a8d85ea1`, and `628cfa650804fefc`, adding 8
  `CONCENTRATION_VARIANT` child links under four MediaDB-backed parent records.
  See `reports/media_variant_m9_park_zinc_grid_review.md`.
- MRS fructose-grid batch: `9dafec1eb2e39af1`, adding 2
  `CONCENTRATION_VARIANT` child links under one TOGO/NBRC-backed parent record.
  See `reports/media_variant_mrs_fructose_grid_review.md`.
- Hassan limiting-nutrient grid batch: `ce304eb8af6f0d55`, adding 3
  `CONCENTRATION_VARIANT` child links under one MediaDB-backed parent record.
  See `reports/media_variant_hassan_limiting_grid_review.md`.
- M40Y sucrose-grid batch: `0b07617b84b13a36`, adding 1
  `SOURCE_DUPLICATE` child link and 3 `CONCENTRATION_VARIANT` child links under
  one TOGO/JCM-backed parent record. See
  `reports/media_variant_m40y_sucrose_grid_review.md`.
- 802 glucose-grid batch: `ce327350c07f8fa5`, adding 2
  `CONCENTRATION_VARIANT` child links under one TOGO/NBRC-backed parent record.
  See `reports/media_variant_802_glucose_grid_review.md`.
- Desulfovibrio marine/brackish salinity batch: `f71bde4d8f58f666`, adding 2
  `SALINITY_VARIANT` child links under one KOMODO/DSMZ-backed parent record.
  See `reports/media_variant_desulfovibrio_brackish_salinity_review.md`.
- Fungal mCAFEs glucose-grid batch: `04147af3e8e81666`, adding 2
  `CONCENTRATION_VARIANT` child links under one CultureBotHT-backed parent
  record. See `reports/media_variant_fungal_mcafes_glucose_grid_review.md`.
- MRS NaCl salinity batch: `41f79e981fafed0e` and `a39871bf4874f93a`,
  adding 4 `SALINITY_VARIANT` child links under two source-specific parent
  records. See `reports/media_variant_mrs_nacl_salinity_review.md`.
- HMM Junlon PW 110 concentration-grid batch: `71b880daeb7183f1`, adding 3
  `CONCENTRATION_VARIANT` child links under one MediaDB-backed parent record.
  See `reports/media_variant_hmm_junlon_grid_review.md`.
- Reinforced Clostridial Medium sea-salt batch: adding 2 `SALINITY_VARIANT`
  child links under two source-specific 3% sea-salt parent records. See
  `reports/media_variant_reinforced_clostridial_sea_salt_review.md`.
- Small-axis concentration/salinity batch: adding 9 child links across
  modified M1 lactate, RDM ammonium chloride, P2 butanol challenge, nutrient
  broth NaCl, Marine 2216 NaCl, R2A NaCl, 1/2 ISP 2 NaCl, and MRS NaCl pairs.
  See `reports/media_variant_small_axis_batch_review.md`.
- Inorganic and defined freshwater concentration batch: adding 5 child links
  across ferrous sulfate, toluene, and nitrate concentration axes. See
  `reports/media_variant_inorganic_defined_freshwater_review.md`.
- Isolated one-axis batch: adding 6 child links across malt-extract, glycerol,
  ethanol, Marine AOB NaCl, and Varel Bryant low-cysteine variants. See
  `reports/media_variant_isolated_one_axis_review.md`.
- LB salinity batch: adding 3 child links across FEBA LB salt variants and the
  TOGO Lennox/Luria broth salt pair. See
  `reports/media_variant_lb_salinity_review.md`.
- Horikoshi-I salinity batch: adding 3 child links under the JCM/MediaDive 2%
  NaCl Horikoshi-I parent record. See
  `reports/media_variant_horikoshi_salinity_review.md`.
- Source-local salinity batch: adding 4 child links across JCM/MediaDive TSB
  agar, fungal ISP-2 agar, and JCM/TOGO CM+YE salinity variants. See
  `reports/media_variant_source_local_salinity_review.md`.
- Halobacteria medium batch: adding 3 `SALINITY_VARIANT` links and 1
  `CONCENTRATION_VARIANT` link across source-local JCM/MediaDive and TOGO
  Halobacteria-style formulations. See
  `reports/media_variant_halobacteria_review.md`.
- Salinity plus pH batch: adding 2 child links to existing TSB agar and fungal
  ISP-2 salinity parent groups, with pH captured in the modification notes. See
  `reports/media_variant_salinity_ph_review.md`.
- Strength and buffer concentration batch: adding 3 child links across Marine
  Broth 2216 strength, TOGO YM agar concentration, and BL low-MOPS variants.
  See `reports/media_variant_strength_buffer_review.md`.
- Mixed one-axis batch: adding 6 child links across sucrose, phosphate, NaCl,
  and yeast-extract concentration axes. See
  `reports/media_variant_mixed_one_axis_review.md`.
- ISP/CYS/Pfennig/Methylobacterium batch: adding 5 child links across ISP-4
  NaCl, CYS NaCl, Pfennig's medium I NaCl, and Methylobacterium MgSO4 axes. See
  `reports/media_variant_isp_cys_pfennig_methylobacterium_review.md`.
- MMYS/LB/nitrifier/Salinispira batch: adding 4 child links across TOGO MMYS
  and LB salt variants plus DSMZ nitrite and Salinispira salt variants. See
  `reports/media_variant_mmys_lb_nitrifier_salinispira_review.md`.
- TOGO/NBRC agar strength batch: adding 2 concentration-variant child links
  across Enriched Cytophaga Agar and BN agar source-local records. See
  `reports/media_variant_togo_nbrc_agar_strength_review.md`.
- TOGO/NBRC strength batch: adding 4 concentration-variant child links across
  artificial seawater, Potato-Carrot Agar, R2A Agar, and Nutrient Agar No. 2
  source-local records. See
  `reports/media_variant_togo_nbrc_strength_review.md`.
- TOGO SW/CM+YE/GYM/R2A batch: adding 6 concentration-variant child links
  across SW-20/SW-10, CM+YE modified-B, GYM agar, and diluted R2A agar source-
  local records. See `reports/media_variant_togo_sw_cmye_gym_r2a_review.md`.
- Specialized strength batch: adding 4 concentration-variant child links
  across MS Basal Salts Robin and SGW Northen Exometabolite mix records. See
  `reports/media_variant_specialized_strength_review.md`.
- Dilution and named-strength batch: adding 7 concentration-variant child links
  across Marine Broth/Agar, LB, TSB, f/2, Hyphomicrobium, and ISP-5 records.
  See `reports/media_variant_dilution_named_strength_review.md`.
- R2A and Nutrient Agar dilution batch: adding 3 concentration-variant child
  links across R3 A/R2A and Nutrient Agar No. 2 records. See
  `reports/media_variant_r2a_nutrient_agar_dilution_review.md`.
- Miscellaneous strength and salinity batch: adding 5 child links across
  Mycorrhiza, KB, R2A Agar, salt-water growth, and Halobacteria records. See
  `reports/media_variant_misc_strength_salinity_review.md`.
- TSB and GYM salinity batch: adding 3 salinity-variant child links across
  TOGO TSB and MediaDive GYM Streptomyces records. See
  `reports/media_variant_tsb_gym_salinity_review.md`.
- LB/R2A/CYS batch: adding 3 child links across LB 0.1x, R2A .1x, and CYS
  modified-NaCl records. See `reports/media_variant_lb_r2a_cys_review.md`.
- Same-name duplicate and agar batch: adding 2 source-duplicate links and 1
  agar concentration-variant link across Dubos Salts, TUA Acetobacter, and
  Sucrose-Bennett records. See
  `reports/media_variant_same_name_duplicate_agar_review.md`.
- TOGO Trypticase Soy Broth Agar NaCl/pH batch: adding 2 salinity-variant
  child links and 1 pH-variant child link under the TOGO 5% NaCl parent record.
  See `reports/media_variant_togo_tsb_nacl_ph_review.md`.
- Same-name concentration and source batch: adding 1 source-duplicate link and
  2 concentration-variant links across Nutrient Agar, Mixotrophic Nitrobacter,
  and Acidimicrobium records. See
  `reports/media_variant_same_name_concentration_source_review.md`.
- Defined and source-local strength concentration batch: adding 3
  concentration-variant links across CDM, 3N-BBM+V, and Enriched Cytophaga Agar
  records. See `reports/media_variant_defined_strength_concentration_review.md`.
- YM, SW-20, and K Medium concentration batch: adding 4 concentration-variant
  links across TOGO SW-20, YM Agar, and JCM K Medium records. See
  `reports/media_variant_ym_sw_k_concentration_review.md`.
- Rhodobacter, Halosimplex, and Acetobacter concentration batch: adding 4
  concentration-variant links across TOGO Rhodobium/Rhodobacter, TOGO
  Halosimplex, and JCM Acetobacter/Gluconacetobacter records. See
  `reports/media_variant_rhodobacter_halosimplex_acetobacter_review.md`.
- Haloalkaliphile, Alkaliphilus, and Chitin medium concentration batch: adding
  4 concentration-variant links across carbonate, thiosulfate, salt, and yeast-
  extract axes. See
  `reports/media_variant_haloalkaliphile_alkaliphilus_chitin_review.md`.
- Anaerobe and ML medium concentration batch: adding 4 concentration-variant
  links across Acetobacterium/Moorella, sulfate-reducer, and ML/ML-15 records.
  See `reports/media_variant_anaerobe_ml_concentration_review.md`.
- NAM, TSBY, Gauze, and 573C batch: adding 1 source-duplicate link and 3
  concentration-variant links across blood agar, TSBY Salt, Gauze synthetic
  medium, and Alicyclobacillus/573C records. See
  `reports/media_variant_nam_tsby_gauze_573c_review.md`.
- Rhodobium, MJ, ASW, Acetobacter, and DC-8A concentration batch: adding 5
  concentration-variant links across bacterial and algae records. See
  `reports/media_variant_rhodobium_mj_asw_acetobacter_dc8a_review.md`.
- Acidimicrobium, Hyphomicrobium, Manning, and Marinitoga batch: adding 4
  concentration-variant links across JCM, KOMODO, and normalized bacterial
  media records. See
  `reports/media_variant_acid_hypho_manning_marinitoga_review.md`.
- Anaerobe, Halobacteria, and L21 concentration batch: adding 4
  concentration-variant links across sulfate-reducer, methanogen,
  halobacteria, and L21-style records. See
  `reports/media_variant_anaerobe_halobacteria_l21_review.md`.
- Nutrient Agar source-duplicate batch: adding 151 source-duplicate links from
  KOMODO/DSMZ Medium 1 to strain-specific copied Medium 1 records. See
  `reports/media_variant_nutrient_agar_source_duplicate_review.md`.
- GYP source-duplicate batch: adding 8 source-duplicate links from GYP glucose
  yeast peptone medium to strain-specific copied DSMZ Medium 852 records. See
  `reports/media_variant_gyp_source_duplicate_review.md`.
- Medium 88 source-duplicate batch: adding 7 source-duplicate links from
  `KOMODO_88-2_For_DSM_18786` to DSM strain-specific and specialized
  Sulfolobus copies. See
  `reports/media_variant_medium_88_source_duplicate_review.md`.
- Phototrophic medium source-duplicate batch: adding 6 source-duplicate links
  from `for_dsm_17935` to DSM strain-specific and named phototrophic copies.
  See `reports/media_variant_phototrophic_source_duplicate_review.md`.
- Sulfurimonas medium source-duplicate batch: adding 1 source-duplicate link
  from `KOMODO_1053_SULFURIMONAS_PARALVINELLA_MEDIUM` to the DSM 19353 source
  copy. See `reports/media_variant_sulfurimonas_source_duplicate_review.md`.
- YPS source-duplicate batch: adding 2 source-duplicate links from
  `yeast_peptone_succinate_medium` to DSM 15761 and DSM 15867 source copies.
  See `reports/media_variant_yps_source_duplicate_review.md`.
- Applied relationships currently include curated `SOURCE_DUPLICATE` families
  plus `CONCENTRATION_VARIANT`, `SALINITY_VARIANT`, and `PH_VARIANT` grids.
- Parent-to-child links: 2,546
- Child-to-parent links: 2,546
- Link validation errors: 0
- Link validation warnings: 0

Targeted schema validation passed for all applied duplicate-source pilot
records, for 30/30 touched Zahorchak concentration-grid records, and for 12/12
touched modified M63 salinity-grid records, and for 4/4 touched 802 salinity
grid records, for 3/3 touched RDM salinity-grid records, for 8/8 touched
defined freshwater cobalt-grid records, for 3/3 touched Potato-Carrot Agar
records, for 3/3 touched BTT medium records, for 3/3 touched XED Agar records,
for 3/3 touched TCG medium records, for 4/4 touched YPG medium records, and
for 1304/1304 touched DSMZ/KOMODO source-duplicate records, for 3/3 touched
ASW barley salinity-grid records, for 5/5 touched M9 Kazan glucose-grid
records, for 12/12 touched M9 Park zinc-grid records, and for 3/3 touched MRS
fructose-grid records, for 4/4 touched Hassan limiting-nutrient records, and
for 5/5 touched M40Y sucrose-grid records, and for 3/3 touched 802 glucose-grid
records, and for 3/3 touched Desulfovibrio marine/brackish records.
Targeted schema validation also passed for 3/3 touched fungal mCAFEs glucose-grid
records and for 6/6 touched MRS NaCl salinity-grid records.
Targeted schema validation also passed for 4/4 touched HMM Junlon records.
Targeted schema validation also passed for 4/4 touched Reinforced Clostridial
Medium sea-salt records.
Targeted schema validation also passed for 18/18 touched small-axis
concentration/salinity records.
Targeted schema validation also passed for 10/10 touched inorganic and defined
freshwater concentration records.
Targeted schema validation also passed for 12/12 touched isolated one-axis
variant records.
Targeted schema validation also passed for 5/5 touched LB salinity records.
Targeted schema validation also passed for 4/4 touched Horikoshi-I salinity
records.
Targeted schema validation also passed for 8/8 touched source-local salinity
records.
Targeted schema validation also passed for 7/7 touched Halobacteria medium
variant records.
Targeted schema validation also passed for 4/4 touched salinity plus pH
variant records.
Targeted schema validation also passed for 6/6 touched strength and buffer
concentration variant records.
Targeted schema validation also passed for 12/12 touched mixed one-axis variant
records.
Targeted schema validation also passed for 9/9 touched ISP/CYS/Pfennig/
Methylobacterium variant records.
Targeted schema validation also passed for 8/8 touched MMYS/LB/nitrifier/
Salinispira variant records.
Targeted schema validation also passed for 4/4 touched TOGO/NBRC agar strength
variant records after normalizing pre-existing invalid `bn_agar.yaml` solution
metadata.
Targeted schema validation also passed for 8/8 touched TOGO/NBRC strength
variant records.
Targeted schema validation also passed for 12/12 touched TOGO SW/CM+YE/GYM/R2A
variant records.
Targeted schema validation also passed for 6/6 touched specialized strength
variant records.
Targeted schema validation also passed for 13/13 touched dilution and
named-strength variant records.
Targeted schema validation also passed for 5/5 touched R2A and Nutrient Agar
dilution variant records.
Targeted schema validation also passed for 10/10 touched miscellaneous strength
and salinity variant records.
Targeted schema validation also passed for 5/5 touched TSB and GYM salinity
variant records.
Targeted schema validation also passed for 6/6 touched LB/R2A/CYS variant
records.
Targeted schema validation also passed for 6/6 touched same-name duplicate and
agar variant records.
Targeted schema validation also passed for 4/4 touched TOGO Trypticase Soy
Broth Agar NaCl/pH variant records.
Targeted schema validation also passed for 6/6 touched same-name concentration
and source variant records.
Targeted schema validation also passed for 6/6 touched defined and source-local
strength concentration variant records.
Targeted schema validation also passed for 7/7 touched YM, SW-20, and K Medium
concentration variant records.
Targeted schema validation also passed for 7/7 touched Rhodobacter,
Halosimplex, and Acetobacter concentration variant records.
Targeted schema validation also passed for 8/8 touched Haloalkaliphile,
Alkaliphilus, and Chitin medium concentration variant records.
Targeted schema validation also passed for 8/8 touched anaerobe and ML medium
concentration variant records.
Targeted schema validation also passed for 8/8 touched NAM, TSBY, Gauze, and
573C variant records.
Targeted schema validation also passed for 10/10 touched Rhodobium, MJ, ASW,
Acetobacter, and DC-8A concentration variant records.
Targeted schema validation also passed for 8/8 touched Acidimicrobium,
Hyphomicrobium, Manning, and Marinitoga concentration variant records.
Targeted schema validation also passed for 8/8 touched anaerobe, Halobacteria,
and L21 concentration variant records.
Targeted schema validation also passed for nine 6/6 touched Nutrient Agar
source-duplicate subsets, ten 11/11 touched Nutrient Agar source-duplicate
subsets, and one 7/7 final Nutrient Agar source-duplicate subset.
Targeted schema validation also passed for 9/9 touched GYP source-duplicate
records.
Targeted schema validation also passed for 8/8 touched Medium 88
source-duplicate records.
Targeted schema validation also passed for 7/7 touched phototrophic
source-duplicate records.
Targeted schema validation also passed for 2/2 touched Sulfurimonas
source-duplicate records.
Targeted schema validation also passed for 3/3 touched YPS source-duplicate
records.
Validated
duplicate-source examples include:

- `data/normalized_yaml/bacterial/KOMODO_11_MRS_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_11a_MODIFIED_medium_11.yaml`
- `data/normalized_yaml/bacterial/modified_medium_11.yaml`
- `data/normalized_yaml/bacterial/KOMODO_104b_PYX-MEDIUM.yaml`
- `data/normalized_yaml/bacterial/anaerobaculum_medium.yaml`
- `data/normalized_yaml/bacterial/medium_104_modified_for_dsm_15597.yaml`
- `data/normalized_yaml/bacterial/KOMODO_78_CHOPPED_MEAT_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_78a_CHOPPED_MEAT_medium_FOR_TREPONEMA_SP.yaml`
- `data/normalized_yaml/bacterial/medium_78_modified_for_dsm_1396.yaml`
- `data/normalized_yaml/bacterial/KOMODO_1076_SP4_MEDIUM.yaml`
- `data/normalized_yaml/bacterial/KOMODO_830_R2A_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml`
- `data/normalized_yaml/bacterial/KOMODO_28_PFENNIG_S_MEDIUM_I.yaml`
- `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml`
- `data/normalized_yaml/bacterial/JCM_J434_ANAEROLINEA_MEDIUM.yaml`
- `data/normalized_yaml/bacterial/KOMODO_119_METHANOBACTERIUM_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_545_TRYPTONE_SOYA_BROTH_TSB.yaml`
- `data/normalized_yaml/bacterial/KOMODO_621a_EKHO_LAKE_STRAINS_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_640_CALDICELLULOSIRUPTOR_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_120_METHANOSARCINA_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml`
- `data/normalized_yaml/bacterial/isp2_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_194_DESULFOBULBUS_MEDIUM.yaml`
- `data/normalized_yaml/bacterial/KOMODO_645a_HEMIN_medium_FOR_MYCOBACTERIUM.yaml`
- `data/normalized_yaml/bacterial/mv_medium.yaml`
- `data/normalized_yaml/bacterial/aso4_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_480b_TTD-MEDIUM.yaml`
- `data/normalized_yaml/bacterial/KOMODO_684_MPOB_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_1055_DESULFOHALOBIUM_UTAHENSE_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_395_DESULFUROCOCCUS_AMYLOLYTICUS_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_520_CM3_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_778_THERMOTERRABACTERIUM_medium.yaml`

Most recent apply plan:

- Manual curated batch: Nutrient Agar source duplicates
- Mode: apply
- Planned/applied actions: 40
- `add_parent_media`: 10
- `add_variant_child`: 10
- `set_variant_relationship`: 10
- `add_variant_modification`: 10

## Migration Plan For The 15k YAML Corpus

1. Stabilize validation inputs.
   - Normalize or quarantine unexpected ingredient keys.
   - Resolve non-CHEBI ingredient `term.id` values where the schema requires
     CHEBI, preserving FOODON/UBERON provenance in notes or cross-reference
     slots.
   - Treat `VARIABLE` concentrations as unresolved until source formulation
     review confirms values.

2. Add parent/child schema slots.
   - Add explicit parent and child link slots to `MediaRecipe`.
   - Regenerate dataclasses and docs.
   - Add validator checks for bidirectional consistency.

3. Build candidate parent groups.
   - Start from `reports/media_variation_candidate_groups.tsv`.
   - Prioritize groups with high counts and clear source families:
     DSMZ/KOMODO modified medium families, TOGO/NBRC duplicates, MRS, BHI,
     R2A, marine 2216, tryptic soy/CASO, BG11, M9, LB, artificial seawater,
     F/2, and Zahorchak ATP/Mg2+ grids.
   - Exclude low-information placeholder groups until ingredients and
     concentrations are resolved.

4. Choose canonical parent records.
   - Prefer authoritative base formulations with complete ingredient and
     concentration coverage.
   - Prefer stable CultureMech IDs and source-backed formulations.
   - Avoid selecting strain-specific or modified records as parents unless no
     base formulation exists.

5. Convert variants to child YAML records.
   - Keep one full YAML record per actual child formulation.
   - Add child-to-parent link and parent-to-child link.
   - Preserve the child formulation rather than collapsing it into embedded
     free text.
   - Record concentration and component differences from the parent.

6. Validate each migration batch.
   - Schema validation for parent and child records.
   - Parent/child bidirectional link validation.
   - Ingredient/concentration signature checks before and after migration.
   - Report unresolved or ambiguous groups instead of forcing parentage.

## Immediate Next Work

Focused pilot migrations have been applied to MRS, PYX, chopped-meat, SP4, R2A,
alkaline nutrient agar, Pfennig's medium I, bifidobacterium medium, Anaerolinea
medium, Methanobacterium medium, tryptone soya broth TSB, Ekho Lake strains
medium, Caldicellulosiruptor medium, and additional smaller named bacterial
duplicate-source families. The next productive implementation step is to review
and apply another well-bounded family using the generated proposal manifests,
rather than rewriting the full corpus blindly.

The proposal pass identified:

- Candidate parent groups: 1,451
- Candidate parent-child links: 9,145
- Proposed links ready for curated migration: 3,251
- Links requiring review before migration: 5,894
- High-confidence links: 2,878
- Medium-confidence links: 983
- Low-confidence links: 5,284

The best pilot candidates from the generated grouping are:

- BHI family: clear broth/agar and supplement distinctions.
- Marine 2216 family: many source-derived modified records.
- Zahorchak ATP/Mg2+ grid: explicit concentration-grid variants.

A full 15k-record migration should not be attempted until more families have
been reviewed for canonical parent choice and source/formulation equivalence.
