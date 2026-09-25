# YAML Record Review: mjytfsh_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml
- Started UTC: 2026-09-24T08:01:38Z
- Finished UTC: 2026-09-24T08:01:38Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml`
- Class: `MediaRecipe`
- Record ID: `CultureMech:002771`
- Label: `mjytfsh_medium`
- Original label: `MJYTFSH MEDIUM`
- Source grounding: `mediadive.medium:J417`, labelled `MJYTFSH MEDIUM`
- Category: `bacterial`
- Generated status: generated merged record with `merge_fingerprint: abab98ba39b1f949aba1f9ae6e4e7ec9a714da262371f8c0ad118ed3afc6665d`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/mjytfsh_medium.yaml`

## Validation

- Open schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml`
  - Result: passed with `No issues found`.
- Strict schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml --out /private/tmp/mjytfsh_medium__abab98ba.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mjytfsh_medium__abab98ba.strict.tsv` has 1 line, the header only.
- LinkML reference validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 reference checks, all validations passed.
- Term validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed.
- Embedded history validation:
  - Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated merged YAML.

## Identity and Grounding

- The generated record identity matches MediaDive `J417`: the source payload names `id: J417`, `name: MJYTFSH MEDIUM`, `source: JCM`, and fixed pH 5.5.
- The inspected JCM medium 417 table supports the main salts, yeast extract, tryptone, sodium formate, 10 ml Trace mineral solution, 1 ml Trace vitamins, 2 g NaHCO3, 10 g sulfur powder, 0.5 g Na2S x 9 H2O, and 1 L distilled water.
- The generated direct rows for NaCl through sodium formate match MediaDive main solution 4151 after its 1011 ml volume normalization.
- JCM and MediaDive both represent Trace mineral solution and Trace vitamins as stock additions. The generated record has no `solutions` key and represents the Trace vitamins stock compounds as final-medium `ingredients`.
- An exact gitignore-independent search with `rg --no-ignore --hidden` over `data/normalized_yaml` and this generated target found the maintained MediaDive source at `data/normalized_yaml/bacterial/mjytfsh_medium.yaml`; the same label also occurs in `data/normalized_yaml/bacterial/TOGO_M415_MJYTFSH_Medium.yaml`.

## Evidence

- The source identity, fixed pH, JCM provenance, main J417 formulation, and preparation prose are supported by the inspected MediaDive REST payload for `rest/medium/J417` and the inspected JCM medium 417 page.
- MediaDive main solution 4151 includes `solution_id: 4092`, Trace mineral solution, at 10 ml. The generated record has only a free-text preparation step saying to use Trace mineral solution of Medium No. 324 supplemented with SrCl2 x H2O, NaBr, and KI.
- JCM medium 417 and MediaDive main solution 4151 include `Trace vitamins` as a 1 ml addition. MediaDive `solution_id: 3861` is a 1000 ml stock containing biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-Aminobenzoic acid, and lipoic acid.
- The generated record flattens the one-liter stock concentrations from `solution_id: 3861` directly into J417. For example, the source stock contains 2 mg biotin per 1000 ml, but the medium uses only 1 ml of that stock; the generated final-medium row says `0.002 G_PER_L`, which is the stock strength before the 1:1011 dilution.
- An exact `rg --no-ignore --hidden` search for `^solutions:`, `solution_id: 4092`, and `solution_id: 3861` across `data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml` and `data/normalized_yaml/bacterial/mjytfsh_medium.yaml` returned no matches, with ignored files included by the search.
- The source explicitly supplies `NiCl2 x 6 H2O` and `Sulfur (powder)`, but the generated rows ground those ingredients to `CHEBI:34887` labelled `nickel dichloride` and `CHEBI:26833` labelled `sulfur atom`.

## Completeness

- The record captures the direct J417 salts, yeast extract, tryptone, sodium formate, NaHCO3, sulfur, and Na2S x 9 H2O quantities exposed in the MediaDive main recipe.
- The record is materially incomplete for stock-solution structure: it does not represent the 10 ml Trace mineral solution addition or the 1 ml Trace vitamins addition as solution rows.
- The record is materially incomplete for vitamin quantities because it stores Trace vitamins stock concentrations as if they were final J417 concentrations.
- The preparation prose preserves the JCM instructions for pH adjustment, filter sterilization, sulfur steaming, N2 autoclaving for the sulfide solution, H2-CO2 sparging, and 200 kPa H2-CO2 pressurization.
- Empty optional organism, source-data, and discussion fields are not defects for this generated import. The inspected JCM and MediaDive entries support the recipe but do not attach a specific growth observation that should have produced a `target_organisms` claim here.

## Findings

1. **major - Trace mineral solution is not machine-readable**
   - Evidence: JCM 417 lists 10 ml Trace mineral solution, and MediaDive encodes this as `solution_id: 4092` in main solution 4151. The generated record lacks a solution row for 4092 and retains its Medium 324 plus Sr/Br/I supplementation only as a standalone preparation sentence.
   - Maintained owner: `data/normalized_yaml/bacterial/mjytfsh_medium.yaml`, via the MediaDive solution importer that flattens or drops stock additions.
2. **major - Trace vitamins were flattened without applying the 1 ml stock dilution**
   - Evidence: MediaDive main solution 4151 uses only 1 ml of stock solution 3861, but the generated record copies the one-liter stock formula into final-medium ingredient rows, yielding final concentrations equal to the stock concentrations rather than stock concentrations multiplied by 1 ml in 1011 ml.
   - Maintained owner: `data/normalized_yaml/bacterial/mjytfsh_medium.yaml`, via the MediaDive solution importer.
3. **major - two source-specified ingredients are grounded to broader or wrong CHEBI terms**
   - Evidence: `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`, `nickel dichloride`, and sulfur powder is grounded to `CHEBI:26833`, `sulfur atom`. The first loses the hydrate form, and the second grounds a bulk elemental ingredient to an atom-level term.
   - Maintained owner: `data/normalized_yaml/bacterial/mjytfsh_medium.yaml` and the MediaDive chemical mapping used by enrichment.

## Recommended Edits

1. Rework the MediaDive import or post-import normalization for `data/normalized_yaml/bacterial/mjytfsh_medium.yaml` so main solution 4151 retains explicit stock rows for the 10 ml Trace mineral solution and the 1 ml Trace vitamins additions.
2. Preserve Trace mineral solution 4092, including its dependency on Medium 324 and the SrCl2 x H2O, NaBr, and KI supplementation instruction, as structured solution data or as a resolvable stock reference instead of preparation-only prose.
3. Replace the flattened Trace vitamins ingredient rows with a structured 1 ml stock addition to MediaDive solution 3861, or scale each vitamin by the 1 ml in 1011 ml dilution if the importer intentionally materializes nested stocks.
4. Re-enrich `NiCl2 x 6 H2O` and sulfur powder against source-scoped chemical terms, or leave those terms unresolved until exact ingredient-level mappings are available.
5. Regenerate `data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml` after the normalized source and any importer fixes land; do not patch the generated merged file directly.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/mjytfsh_medium__abab98ba.yaml`.
- Inspect the regenerated YAML for explicit `solution_id: 4092` and `solution_id: 3861` equivalents rather than vitamin rows copied at stock strength.
- Compare regenerated J417 quantities against the MediaDive main solution volume of 1011 ml and the JCM 417 table.
- Re-run exact ignored-inclusive `rg --no-ignore --hidden` checks for `Trace mineral solution`, `Trace vitamins`, `solution_id: 4092`, and `solution_id: 3861` against the maintained normalized owner and regenerated merge output.

## Additional Notes

- The sibling TOGO-derived `data/normalized_yaml/bacterial/TOGO_M415_MJYTFSH_Medium.yaml` uses the same normalized label. After the J417 stock-solution hierarchy is preserved, compare that TOGO source with this MediaDive source to decide whether the two generated records should merge or remain source-distinct.
