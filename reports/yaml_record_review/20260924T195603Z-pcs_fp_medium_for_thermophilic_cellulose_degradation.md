# YAML Record Review: pcs_fp_medium_for_thermophilic_cellulose_degradation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pcs_fp_medium_for_thermophilic_cellulose_degradation.yaml
- Started UTC: 2026-09-24T19:56:03Z
- Finished UTC: 2026-09-24T19:56:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:015439 |
| Name | pcs_fp_medium_for_thermophilic_cellulose_degradation |
| Original name | PCS-FP medium for thermophilic cellulose degradation |
| Source identity | CommunityMech:000061 |
| Source path | data/normalized_yaml/bacterial/PCS_FP_medium_for_thermophilic_cellulose_degradation.yaml |
| Generated path | data/merge_yaml/merged/pcs_fp_medium_for_thermophilic_cellulose_degradation.yaml |
| Merge fingerprint | f1904e52b4c4664ca0a949dd9e149090b9e1a5893f065a4227a4669951511a1f |

The target is a generated merged record. Future edits should be made in the
maintained CommunityMech-derived input and by regenerating merged YAML, not
directly in
`data/merge_yaml/merged/pcs_fp_medium_for_thermophilic_cellulose_degradation.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pcs_fp_medium_for_thermophilic_cellulose_degradation.yaml` exited 0 and reported no issues. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/pcs_fp_medium_for_thermophilic_cellulose_degradation.yaml --out /private/tmp/pcs_fp_medium_for_thermophilic_cellulose_degradation.strict.tsv --workers 1 --quiet` exited 0 and wrote only the TSV header. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/pcs_fp_medium_for_thermophilic_cellulose_degradation.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/pcs_fp_medium_for_thermophilic_cellulose_degradation.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The record identity matches the CommunityMech-imported PCS-FP medium used for
thermophilic cellulose degradation by the defined SF356 bacterial community.

PMID 16269746 resolves to the Kato et al. 2005 Applied and Environmental
Microbiology paper on a stable five-strain cellulose-degrading community. Its
open PMC full text supports the PCS-FP pH 8.0 condition, loose-capped static
incubation at 50 C, 40 microliter inoculum into 4 ml medium, 6-day subculture
cadence, 1% wt/vol filter paper, and 2 g/L CaCO3. It also defines PCS basal
medium as 1 g/L yeast extract, 5 g/L peptone, and 5 g/L NaCl in 1 liter of
water.

PMID 15545431 resolves to the Kato et al. 2004 Clostridium straminisolvens
species paper. Its PubMed abstract supports the CommunityMech note that the
CSK1 member is a moderately thermophilic cellulolytic bacterium, with optimum
growth and cellulose degradation at 50 to 55 C and pH 7.5.

The represented ingredient groundings for filter paper/cellulose, calcium
carbonate, and sodium chloride are syntactically valid and agree with the
source ingredient identities.

## Evidence

The maintained ingredient list matches the paper-supported PCS-FP formula for
the five explicit solutes and substrates:

| PCS-FP component | Generated representation |
| --- | --- |
| 1% wt/vol filter paper | `Filter paper (cellulose substrate)`, 10 `G_PER_L` |
| 2 g/L CaCO3 | `Calcium carbonate`, 2 `G_PER_L` |
| 1 g/L yeast extract | `Yeast extract`, 1 `G_PER_L` |
| 5 g/L peptone | `Peptone`, 5 `G_PER_L` |
| 5 g/L NaCl | `Sodium chloride`, 5 `G_PER_L` |

The paper also states that the PCS basal components are dissolved in 1 liter of
water. That final water volume is not represented in the generated record or in
the maintained normalized input.

An ignored-inclusive search for `CultureMech:015439`, `CommunityMech:000061`,
`PMID:16269746`, `PMID:15545431`,
`PCS_FP_medium_for_thermophilic_cellulose_degradation`, and
`pcs_fp_medium_for_thermophilic_cellulose_degradation` found exactly one
maintained normalized input and this generated record. The same search found
import logs and a repair script reference, but no duplicate PCS-FP recipe.

## Completeness

The generated target is materially incomplete because it omits the 1 L water
row for PCS basal medium.

The maintained normalized input has a structured `sources` entry for
`CommunityMech:000061` added after the generated file was last built. The
generated target is stale and lacks that `sources` array.

No provider source duplicate is expected for this CommunityMech import. Empty
provider `media_term` and `target_organisms` slots are acceptable for the
current import shape.

## Findings

### Major

- `data/normalized_yaml/bacterial/PCS_FP_medium_for_thermophilic_cellulose_degradation.yaml`
  and the generated target omit the 1 L water row from PCS basal medium.

### Minor

- The generated record is stale relative to the maintained input's
  `sources: CommunityMech:000061` provenance repair.

## Recommended Edits

- Add the missing 1 L water ingredient to the maintained PCS-FP input.
- Regenerate the merged YAML so the generated PCS-FP record includes both the
  water row and the repaired structured `sources` entry.

## Follow-up Checks

- Rerun the open schema, strict, reference, and term validators on the
  regenerated PCS-FP record.
- Compare the regenerated ingredient list against PMID 16269746 and confirm it
  contains filter paper, calcium carbonate, yeast extract, peptone, sodium
  chloride, and water at source-supported amounts.
- Re-run an ignored-inclusive exact search for `CultureMech:015439`,
  `CommunityMech:000061`, and
  `PCS_FP_medium_for_thermophilic_cellulose_degradation` to confirm no duplicate
  PCS-FP recipe was introduced.

## Additional Notes

None found.
