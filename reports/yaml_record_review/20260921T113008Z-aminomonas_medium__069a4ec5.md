# YAML Record Review: aminomonas_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/aminomonas_medium__069a4ec5.yaml`
- Started UTC: 2026-09-21T11:27:17Z
- Finished UTC: 2026-09-21T11:30:08Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002002` |
| Name | `aminomonas_medium` |
| Original name | `AMINOMONAS MEDIUM` |
| Source identity | DSMZ Medium 846, `mediadive.medium:846` |
| Generated status | Generated five-source merge |
| Generated path | `data/merge_yaml/merged/aminomonas_medium__069a4ec5.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/aminomonas_medium.yaml` plus related normalized DSMZ/KOMODO records |

The generated record merges `aminomonas_medium`, `aminobacterium_medium`, `anaerobic_serine_arginine_medium`, `for_dsm_12260`, and `for_dsm_12261_and_dsm_12262` on `merge_fingerprint: 069a4ec5285e6fb261cd87ee4a2105ccb7c18c6741e1cb59e0e4f1279ec2c06b`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/aminomonas_medium__069a4ec5.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/aminomonas_medium__069a4ec5.yaml --out /private/tmp/aminomonas_medium__069a4ec5.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/aminomonas_medium__069a4ec5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/aminomonas_medium__069a4ec5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The top-level record identity is DSMZ Medium 846 / AMINOMONAS MEDIUM:

- `id: CultureMech:002002`
- `name: aminomonas_medium`
- `media_term.preferred_term: DSMZ Medium 846`
- `media_term.term.id: mediadive.medium:846`
- source URL in `notes`: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf`

That identity is internally contradicted by two fields copied from the sibling `data/normalized_yaml/bacterial/aminobacterium_medium.yaml` / DSMZ Medium 846a owner:

- `NaCl: 19.9402 G_PER_L` matches DSMZ 846a's 20 g NaCl input, not DSMZ 846's 1 g NaCl input.
- `MgCl2 x 6 H2O: 2.99103 G_PER_L` matches DSMZ 846a's 3 g MgCl2 input, not DSMZ 846's 0.40 g MgCl2 input.

The normalized DSMZ 846 and KOMODO 846 owners carry the low-salt `NaCl: 0.997009 G_PER_L` and `MgCl2 x 6 H2O: 0.398804 G_PER_L` values. The generated merge should not group DSMZ Medium 846a with DSMZ Medium 846 solely because their ingredient-name sets are the same.

Most small-molecule groundings match the preferred material as written, but `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` / nickel dichloride. The local ChEBI snapshot has exact nickel chloride hexahydrate as `CHEBI:53542`, and `src/culturemech/data/mediaingredientmech/label_index.csv` lists that exact label as a rejected candidate.

## Evidence

Inspected source documents:

- DSMZ Medium 846 PDF from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf`
- DSMZ Medium 846a PDF from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846a.pdf`

Supported by DSMZ Medium 846:

- AMINOMONAS MEDIUM identity, pH 7.2, complex liquid formulation, and anaerobic 80% N2 / 20% CO2 preparation.
- The low-salt base formula: 0.30 g NH4Cl, 0.20 g K2HPO4, 0.30 g KH2PO4, 0.40 g MgCl2 x 6 H2O, 0.15 g CaCl2 x 2 H2O, 0.50 g KCl, 1.00 g NaCl, 2.00 g yeast extract, 1.50 g Na2CO3, 1.05 g L-serine, 0.50 g L-cysteine HCl x H2O, and 0.50 g Na2S x 9 H2O.
- Addition of 1.00 ml Trace element solution SL-10, 1.00 ml Selenite-tungstate solution, 1.00 ml Wolin's vitamin solution (10x), and 0.50 ml 0.1% sodium resazurin.
- The two DSMZ-published strain modifications: DSM 12260 replaces L-serine with 1.74 g/L L-arginine x HCl; DSM 27871 adjusts the final medium to pH 7.8.

Supported by DSMZ Medium 846a:

- AMINOBACTERIUM MEDIUM is a distinct DSMZ accession whose basal formula contains 20.00 g NaCl and 3.00 g MgCl2 x 6 H2O in the same water volume.
- Its preparation omits magnesium chloride before autoclaving and adds magnesium chloride afterward from a sterile anoxic stock solution, unlike DSMZ 846's preparation.

Unsupported or mismatched claims:

- The generated `aminomonas_medium__069a4ec5` formulation combines DSMZ 846 identity with DSMZ 846a NaCl and MgCl2 amounts.
- The generated `synonyms` list treats DSMZ 846a / `mediadive.medium:846a` as a source duplicate of DSMZ 846 even though DSMZ publishes separate salt concentrations and a different magnesium-addition step.
- Root ingredients flatten the SL-10, selenite-tungstate, and Wolin's vitamin stock formulas into final-medium grams per liter. For example, SL-10 has 1.5 g/L FeCl2 x 4 H2O and 24 mg/L NiCl2 x 6 H2O as stock concentrations; DSMZ 846 adds only 1 ml of that stock to the main liter.
- `preparation_steps` carries the SL-10 stock preparation as a second unnamed top-level step, but does not preserve Selenite-tungstate solution or Wolin's vitamin solution as solution recipes with their own preparation boundary.
- The generated `parent_media` says DSMZ Medium 846 is a child of `for_dsm_12260`; the normalized owner has the intended direction, with `for_dsm_12260` listed under `aminomonas_medium.variant_children`.

## Completeness

Consequential gaps:

- The generated merge lacks explicit stock-solution boundaries for Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x).
- The DSMZ 12260 arginine replacement and DSMZ 27871 pH 7.8 variants are not represented in the normalized Aminomonas topology; the KOMODO 846.2 wrapper for DSM 12260 still carries the unmodified 35-ingredient serine signature.
- No inspected source supports the high-NaCl/high-Mg formulation for DSMZ Medium 846.
- No exact target-organism or growth-evidence claim is present; that is an empty optional field, not a defect by itself.
- `Yeast extract` remains ungrounded; no exact small-molecule term should be forced for this undefined component.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*aminomonas_medium__069a4ec5.md'` found no prior report for this generated target.
- `rg --no-ignore --hidden` over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the target label, source labels, and fingerprint found the generated target, maintained DSMZ and KOMODO inputs, the repair script that linked the normalized KOMODO 846 records under DSMZ 846, the independent TOGO M2549 Aminomonas owner, and no existing `aminomonas_medium__069a4ec5` review report.
- `rg --no-ignore --hidden` for `nickel chloride hexahydrate` found exact `CHEBI:53542` in `src/culturemech/data/chebi/structure_index.csv` and a rejected exact candidate row in `src/culturemech/data/mediaingredientmech/label_index.csv`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated merge conflates DSMZ Medium 846 and DSMZ Medium 846a. | The target says `mediadive.medium:846` but carries DSMZ 846a-only `NaCl: 19.9402 G_PER_L` and `MgCl2 x 6 H2O: 2.99103 G_PER_L`; DSMZ 846 lists 1.00 g NaCl and 0.40 g MgCl2 x 6 H2O, while DSMZ 846a lists 20.00 g and 3.00 g. | `src/culturemech/merge/fingerprint.py`, `src/culturemech/merge/merge_recipes.py`, and the normalized records under `data/normalized_yaml/bacterial/` |
| Major | Three named stock additions are flattened into root ingredients at stock strength. | DSMZ 846 adds 1 ml each of SL-10, Selenite-tungstate, and Wolin's vitamin solution, but the target records their internal salts/vitamins as final `G_PER_L`; the SL-10 and vitamin rows are therefore about 1000x above final-medium scale. | `data/normalized_yaml/bacterial/aminomonas_medium.yaml` and the MediaDive/KOMODO import or stock-normalization path that produced the flattened rows |
| Major | The generated record inverts the normalized variant topology. | `data/normalized_yaml/bacterial/aminomonas_medium.yaml` lists `for_dsm_12260` as a `STRAIN_SPECIFIC_VARIANT` child, but the merged output lists `for_dsm_12260` as the parent of canonical DSMZ Medium 846. | `src/culturemech/merge/merger.py` |
| Major | DSMZ-published strain variants are absent or misrepresented. | DSMZ Medium 846 specifies an L-arginine x HCl replacement for DSM 12260 and pH 7.8 for DSM 27871; the normalized KOMODO `for_dsm_12260` child keeps L-serine and the generated record has no DSM 27871 child. | `data/normalized_yaml/bacterial/aminomonas_medium.yaml`, `data/normalized_yaml/bacterial/for_dsm_12260.yaml`, and any source-specific KOMODO repair |
| Major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | The preferred term and DSMZ stock formula are hexahydrate; the record uses `CHEBI:34887`, whereas the local ChEBI snapshot has exact `CHEBI:53542` / nickel chloride hexahydrate. | MediaIngredientMech label index or post-import ingredient grounding |

## Recommended Edits

1. Tighten duplicate grouping so records whose ingredient names match but concentrations differ are not merged, then regenerate `data/merge_yaml/merged/`. DSMZ 846 and DSMZ 846a should remain separate canonical merged recipes.
2. Preserve the DSMZ 846 top-level recipe as a main solution plus Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) stock additions; either keep those stocks as explicit nested `SolutionRecipe` references or rescale every stock component to its final-medium amount with notes that document the dilution.
3. Update the merge process to drop or remap `parent_media` links when a normalized parent and its child appear in the same generated group so a canonical parent cannot become a child of one of its source variants.
4. Re-review the DSMZ 846 strain variants: represent DSM 12260 as an arginine replacement, add a DSM 27871 pH 7.8 variant if it belongs in this corpus, and do not keep the KOMODO 846.2 wrapper as an exact duplicate while the DSMZ primary source says DSM 12260 changes the amino acid.
5. Ground `NiCl2 x 6 H2O` to exact nickel chloride hexahydrate (`CHEBI:53542`) or leave it ungrounded if the packaged MIM label index intentionally rejects that term.

## Follow-up Checks

- Rerun `just verify-merges` and `just audit-merge-freshness` after tightening the merge fingerprint so `aminomonas_medium` and `aminobacterium_medium` no longer share one generated merge record.
- Rerun `just validate data/normalized_yaml/bacterial/aminomonas_medium.yaml`, `just validate-media-variant-links`, and the no-project single-record schema/strict/term/reference checks after the maintained DSMZ/KOMODO records are corrected and generated outputs are refreshed.
- Manually compare the regenerated Aminomonas page with DSMZ Medium 846 to confirm the final displayed NaCl/Mg amounts, SL-10/wolins/selenite stock handling, pH, gas mix, and post-autoclave additions match the source.
- Recheck `src/culturemech/data/mediaingredientmech/label_index.csv` after any MIM refresh to confirm exact hydrate labels do not regress to anhydrous `CHEBI:34887`.

## Additional Notes

- `data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml` is an independent Aminomonas owner imported from TOGO, but it was not part of this generated merge group.
- The open, strict, reference, and term validators check structural validity and resolvable IDs; they did not catch the scientifically wrong DSMZ 846 / 846a merge because source identity and amount equality are outside those record-level gates.
