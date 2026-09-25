# YAML Record Review: glycerol_fermentation_medium_for_diet_coculture

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_fermentation_medium_for_diet_coculture.yaml
- Started UTC: 2026-09-23T07:09:16Z
- Finished UTC: 2026-09-23T07:14:02Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:015432` |
| Name | `glycerol_fermentation_medium_for_diet_coculture` |
| Original name | `Glycerol Fermentation Medium for DIET Coculture` |
| Category | `specialized` |
| Canonical source | `CommunityMech:000031` |
| Merged sources | `Glycerol_Fermentation_Medium_for_DIET_Coculture` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_fermentation_medium_for_diet_coculture.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_fermentation_medium_for_diet_coculture.yaml --out /private/tmp/glycerol_fermentation_medium_for_diet_coculture.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_fermentation_medium_for_diet_coculture.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_fermentation_medium_for_diet_coculture.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This is a generated single-source merge of a CommunityMech-derived specialized medium for the Geobacter sulfurreducens and Clostridium pasteurianum glycerol-fermentation coculture in PMID:28287150.

A gitignore-independent exact search for `CultureMech:015432`, `CommunityMech:000031`, `PMID:28287150`, `Glycerol_Fermentation_Medium_for_DIET_Coculture`, and `glycerol_fermentation_medium_for_diet_coculture` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the maintained parent, this generated record, and the expected source indexes.

Grounding for glycerol, sodium acetate, ammonium chloride, sodium dihydrogen phosphate, disodium hydrogen phosphate, sodium sulfate, magnesium chloride hexahydrate, calcium chloride dihydrate, and L-cysteine is narrow and matches the named chemicals in the paper.

## Evidence

The paper's `Fermentation medium and set-up` method lists the coculture medium per liter of water as 10 g glycerol, 0.82 g Na-acetate, 2.00 g NH4Cl, 0.75 g KCl, 2.45 g NaH2PO4, 4.58 g Na2HPO4, 0.28 g Na2SO4, 0.26 g MgCl2 x 6H2O, 2.90 mg CaCl2 x 2H2O, 0.50 g L-cysteine, 10 ml vitamin solution from DSMZ medium 141, 10 ml trace element solution from DSMZ medium 141, and 0.5 ml trace element solution SL-10 from DSMZ medium 320, then pH 6.9.

The generated record keeps the glycerol, acetate, ammonium, phosphate, sulfate, magnesium, calcium, cysteine, pH, 35 C temperature, and anaerobic headspace context. It does not include the 0.75 g/l KCl row, any explicit water row, the 10 ml/l DSMZ 141 vitamin row, the 10 ml/l DSMZ 141 trace row, or the 0.5 ml/l DSMZ 320 SL-10 row. The omitted DSMZ stock rows are only mentioned in free-text `notes`.

DSMZ medium 141 exposes `Wolin's vitamin solution` and `Modified Wolin's mineral solution`; DSMZ medium 320 exposes `Trace element solution SL-10`. Those are the three named stocks referenced by the PMID:28287150 method.

## Completeness

The record is a useful partial reconstruction of the paper medium, but it is not complete enough for mechanistic use until KCl and the three stock-solution additions are structured and the two coculture organisms are captured as target organisms. Empty optional fields such as `references` and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | KCl is missing from the structured ingredient list. | PMID:28287150 lists 0.75 g KCl per liter in the coculture fermentation medium; the generated YAML has no potassium chloride ingredient. | `data/normalized_yaml/specialized/Glycerol_Fermentation_Medium_for_DIET_Coculture.yaml`. |
| Major | The three required DSMZ stock additions are prose-only. | The paper adds 10 ml/l DSMZ 141 vitamin solution, 10 ml/l DSMZ 141 trace element solution, and 0.5 ml/l DSMZ 320 SL-10; the YAML only mentions those additions in `notes`, so none participate in the structured formula. | CommunityMech importer or manual specialized-medium curation. |
| Major | The coculture target organisms are not structured. | The source medium is explicitly for Geobacter sulfurreducens DSM 12127 plus Clostridium pasteurianum DSM 525, but the record has no `target_organisms` rows. | CommunityMech-to-CultureMech organism mapping. |
| Minor | The generated record is stale relative to the maintained parent. | The normalized parent added a structured `sources` entry for `CommunityMech:000031` on September 13, 2026; the generated August 6 merge still lacks that `sources` entry. | Merge regeneration after CommunityMech source repair. |

## Recommended Edits

1. Add the missing 0.75 g/l KCl row from PMID:28287150.
2. Structure the 10 ml/l DSMZ 141 vitamin stock, 10 ml/l DSMZ 141 trace stock, and 0.5 ml/l DSMZ 320 SL-10 stock instead of leaving those formula components in notes only.
3. Add target-organism rows for Geobacter sulfurreducens DSM 12127 and Clostridium pasteurianum DSM 525.
4. Regenerate the merged record so the September 2026 `sources` repair is preserved under `data/merge_yaml/merged/`.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation after adding KCl, the DSMZ stock rows, and target-organism rows.
- Compare the regenerated formula against the PMID:28287150 `Fermentation medium and set-up` paragraph.
- Compare the stock names against MediaDive/DSMZ medium 141 and medium 320 to confirm the DSMZ stock aliases resolve to the intended vitamin, modified Wolin mineral, and SL-10 recipes.
- Re-run the exact gitignore-independent search for `CultureMech:015432`, `CommunityMech:000031`, `PMID:28287150`, `Glycerol_Fermentation_Medium_for_DIET_Coculture`, and `glycerol_fermentation_medium_for_diet_coculture` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the generated record is current.

## Additional Notes

The reference validator initially failed under sandboxed DNS when trying to fetch `PMID:28287150`; rerunning the same validator with network access returned no validation issues.
