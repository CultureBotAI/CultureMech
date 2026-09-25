# YAML Record Review: Columbia Blood Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_medium__c25575e2.yaml`
- Started UTC: 2026-09-22T11:11:00Z
- Finished UTC: 2026-09-22T11:12:31Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009150`
- Normalized source: `data/normalized_yaml/bacterial/TOGO_M2582_Columbia_Blood_Medium.yaml`
- Source identity: TOGO M2582, `Columbia Blood Medium`
- Current generated merge: one source recipe, `TOGO_M2582_Columbia_Blood_Medium`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- TOGO M2582 cites DSMZ Medium 693 and mirrors its Columbia agar base plus 5% defibrinated sheep blood recipe.
- DSMZ Medium 693 is already represented by `data/merge_yaml/merged/COLUMBIA_BLOOD_MEDIUM.yaml`.
- The normalized TOGO owner was repaired to link to `data/normalized_yaml/bacterial/columbia_blood_medium.yaml` as a `SOURCE_DUPLICATE`, but this generated record was produced before that September 2026 repair.
- This generated YAML should disappear after merge regeneration because it is a stale standalone rendering of a source-catalogue duplicate.

## Evidence

- TOGO API checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2582`.
- DSMZ source checked: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium693.pdf`.
- Repaired normalized owner checked: `data/normalized_yaml/bacterial/TOGO_M2582_Columbia_Blood_Medium.yaml`.
- DSMZ parent checked: `data/normalized_yaml/bacterial/columbia_blood_medium.yaml`.

## Completeness

- The generated record has the correct category, medium type, composition type, and solid agar state.
- It has the two expected high-level ingredients, but both concentrations preserve stale TOGO import units.
- It has no explicit `SOURCE_DUPLICATE` relationship because it predates the repaired normalized source graph.

## Findings

1. `Defibrinated sheep blood` is generated as `5 PERCENT_W_V`; TOGO and DSMZ support a 5% blood supplement, and the repaired normalized owner now records `5 PERCENT_V_V`.
2. `Columbia agar base` is generated as `1 G_PER_L`; TOGO encodes a 1 L base volume and the repaired owner now avoids treating one liter of opaque agar base as one gram per liter.
3. The generated merge omits the normalized `SOURCE_DUPLICATE` relationship to DSMZ Medium 693, leaving this TOGO source as a false standalone medium.

## Recommended Edits

1. Keep the repaired ingredient units in `data/normalized_yaml/bacterial/TOGO_M2582_Columbia_Blood_Medium.yaml`.
2. Regenerate merged records so `TOGO_M2582_Columbia_Blood_Medium.yaml` is folded into the canonical DSMZ 693 Columbia blood medium record.
3. Confirm that the regenerated canonical record keeps the TOGO and DSMZ URLs as evidence for the same recipe rather than treating M2582 as an independent variant.

## Follow-up Checks

- Confirm that `data/merge_yaml/merged/columbia_blood_medium__c25575e2.yaml` is absent after regeneration.
- Re-run the generated-record validators on the regenerated DSMZ 693 canonical YAML.
- Re-check that the TOGO M2582 source duplicate still points at `data/normalized_yaml/bacterial/columbia_blood_medium.yaml`.

## Additional Notes

- No schema-level defects were found.
- This record is stale generated output; the direct normalized owner already contains the intended evidence-backed repair.
