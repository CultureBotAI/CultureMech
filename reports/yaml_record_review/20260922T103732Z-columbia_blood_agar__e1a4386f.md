# YAML Record Review: Columbia Blood Agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar__e1a4386f.yaml`
- Started UTC: `2026-09-22T10:33:45Z`
- Finished UTC: `2026-09-22T10:37:32Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:005268` for KOMODO Medium 429, `COLUMBIA BLOOD AGAR`, generated as the canonical `columbia_blood_agar` merge on fingerprint `e1a4386f6227b9fea3bc3e226ee3271fcfd3bcce9786cffbc4b1b8085952be27`.

The generated record merged 24 source records, headed by `data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml` and the direct DSMZ branch `data/normalized_yaml/bacterial/columbia_blood_agar.yaml`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar__e1a4386f.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The parent KOMODO identity is coherent: KOMODO `429` maps to DSMZ / MediaDive Medium 429, `COLUMBIA BLOOD AGAR`.

The biological formulation is not coherent. DSMZ 429 defines the medium as Columbia agar base supplemented with 4% horse blood. The local KOMODO and direct DSMZ normalized inputs instead import the separate DSMZ 545, 215, and 1 liquid rehydration-media blocks that follow the Columbia Blood Agar note in the DSMZ PDF.

The generated merge is also too broad. It aliases and merges the parent `429` record with KOMODO `429a` charcoal agar, `429b` chocolate agar, `429c` Columbia-glucose-cysteine agar, `429d` Francisella halioticida medium, MediaDive `429e` Columbia Blood Agar 10%, blood-source replacements, and multiple DSM-specific variants. Those sibling media are related DSMZ 429 variants, but they are not exact aliases of the parent formulation.

## Evidence

The inspected DSMZ 429 PDF text supports exactly one top-level recipe statement for this medium: Columbia agar base plus 4% horse blood. The later 545 Tryptone Soya Broth, 215 BHI Medium, and 1 Nutrient Broth blocks are optional liquid rehydration media for freeze-dried ampoules, not Columbia Blood Agar components.

The formula is therefore source-inflated in both normalized owners: casein peptone, soy peptone, D(+)-glucose, NaCl, K2HPO4, Brain Heart Infusion-derived calf brain, beef heart, Proteose peptone, dextrose, disodium phosphate, Peptone, and Meat extract are all copied from downstream rehydration media or from a secondary commercial-product expansion.

The Staphylococcus saccharolyticus growth evidence is supported at the general Columbia blood agar level. The cached PMID:7077295 abstract states that the highest counts for Peptococcus saccharolyticus strains were obtained on Columbia blood agar under anaerobic incubation, and the inspected BacDive page for strain 14567 identifies Staphylococcus saccharolyticus S1 as a type strain with DSM 20359 / ATCC 14953 / JCM 1768 / NCTC 11807 aliases, NCBI taxon 33028, and a `GCA_003968885` Staphylococcus saccharolyticus NCTC 11807 genome assembly.

The variant-level note correctly records that BacDive DSMZ Medium 693 is sheep-blood Columbia Blood Medium while this parent branch is horse-blood DSMZ Medium 429. `SAMN05977977` was not found in the inspected BacDive HTML in an ignored-inclusive search and is a BioSample-style accession stored in a `genome_assembly_id` list beside a true GCA assembly accession.

## Completeness

The canonical formula needs to be reduced to the source-supported Columbia agar base plus 4% horse blood. Empty explicit solution fields are not defects because DSMZ 429 has no separate stock solutions.

The record needs variant separation. Charcoal, chocolate, glucose-cysteine, Francisella, 10% blood, sheep-blood replacement, and strain-specific DSMZ 429 branches should remain separate `MediaRecipe` records or variant links, not exact synonyms on the parent formula.

The target-organism and growth evidence should be preserved when the parent is repaired. The unresolved piece is the non-assembly `SAMN05977977` value in `genome_assembly_id`; the inspected BacDive page supported `GCA_003968885` but not the `SAMN` string.

## Findings

- Major: DSMZ Medium 429's optional rehydration-media blocks were flattened into the Columbia Blood Agar recipe in both `data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml` and `data/normalized_yaml/bacterial/columbia_blood_agar.yaml`.
- Major: the generated canonical merge treats DSMZ 429 variants and sibling formulae as source duplicates and exact synonyms of the parent Columbia Blood Agar formula.
- Major: the external Brain Heart Infusion commercial-product expansion is unsupported in this medium because Brain Heart Infusion appears only in DSMZ Medium 215, an optional rehydration medium.
- Minor: `SAMN05977977` is stored under `genome_assembly_id` even though it was not found on the inspected BacDive page and has a BioSample-style accession prefix, not a GCA assembly prefix.

## Recommended Edits

- In `data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml` and `data/normalized_yaml/bacterial/columbia_blood_agar.yaml`, remove the DSMZ 545, 215, and 1 ingredients plus the secondary BHI commercial-product expansion.
- Represent DSMZ 429 as Columbia agar base supplemented with horse blood at `4 PERCENT_V_V`, preserving the DSMZ note about media 545, 215, and 1 as a rehydration instruction rather than ingredient rows.
- Repair `merge_recipes.py` input metadata or duplicate-detection guards so KOMODO 429a, 429b, 429c, 429d, MediaDive 429e, blood-replacement variants, and DSM-specific variants do not collapse into the parent 429 source duplicate.
- Keep the Staphylococcus saccharolyticus target-organism and anaerobic-growth evidence on the repaired Columbia blood agar record, but remove `SAMN05977977` from `genome_assembly_id` or move it to an accession field with BioSample semantics.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/` and validate the regenerated canonical record with open schema, strict, reference, and term validators.
- Confirm no casein peptone, soy peptone, D(+)-glucose, NaCl, K2HPO4, Brain Heart Infusion, calf brain, beef heart, Proteose peptone, dextrose, disodium phosphate, Peptone, or Meat extract rows remain on the parent Columbia Blood Agar formula.
- Confirm charcoal agar, chocolate agar, glucose-cysteine agar, Francisella halioticida medium, and Columbia Blood Agar 10% are no longer `synonyms` or `merged_from` aliases of the parent.
- Recheck the Staphylococcus saccharolyticus growth evidence after regeneration so the supported BacDive and PMID evidence are retained while `SAMN05977977` is corrected.

## Additional Notes

The search for `SAMN05977977` covered the target record, the cached PMID, and the locally fetched BacDive HTML with `rg --no-ignore --hidden`, so ignored files in those paths were included.
