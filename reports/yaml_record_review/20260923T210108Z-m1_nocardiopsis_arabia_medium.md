# YAML Record Review: M1-NOCARDIOPSIS ARABIA medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m1_nocardiopsis_arabia_medium.yaml`
- Started UTC: 2026-09-23T20:59:07Z
- Finished UTC: 2026-09-23T21:01:08Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m1_nocardiopsis_arabia_medium.yaml`
- Canonical maintained owner: `data/normalized_yaml/bacterial/KOMODO_1065_M1-NOCARDIOPSIS_ARABIA_medium.yaml`
- Duplicate maintained owner: `data/normalized_yaml/bacterial/m1_nocardiopsis_arabia_medium.yaml`
- CultureMech ID: `CultureMech:003648`
- Media term: `komodo.medium:1065`
- DSMZ source duplicate: `mediadive.medium:1065`
- Merge fingerprint: `569d53df5fea0b83540df3cdbb4f1f49ca90c3411f9abf622e1be5f6d797a20d`
- Merge sources: `KOMODO_1065_M1-NOCARDIOPSIS_ARABIA_medium`, `m1_nocardiopsis_arabia_medium`
- Ignored-inclusive exact searches over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the KOMODO 1065 owner, the DSMZ 1065 owner, the generated two-source merge, generated indexes, and archived source-duplicate and validation rows.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m1_nocardiopsis_arabia_medium.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The generated record represents KOMODO Medium 1065 and its DSMZ source duplicate, DSMZ Medium 1065, `M1-NOCARDIOPSIS ARABIA MEDIUM`. The source-duplicate relationship is sound: the inspected MediaDive REST record for `1065` and the linked DSMZ Medium 1065 PDF both support the recipe's starch, yeast extract, peptone, NaCl, agar, sea-water, and pH values.

The `kg_microbe_match` grounding is wrong. Both maintained owners and the generated record set `kg_microbe_match: mediadive.medium:687`, but inspected MediaDive record `687` is `COLUMBIA BLOOD AGAR`, a separate blood agar formula unrelated to DSMZ 1065.

## Evidence

- The DSMZ 1065 PDF supports the exact source title, 10 g starch, 4 g yeast extract, 2 g peptone, 20 g NaCl, 18 g agar, 1000 ml sea water, and the instruction to adjust pH to 7.2.
- MediaDive REST for `1065` agrees with the DSMZ PDF and reports one 1000 ml `Main sol. 1065` with the same six components and an `Adjust pH to 7.2` step.
- `reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md` already classified the DSMZ 1065 and KOMODO 1065 maintained records as `SOURCE_DUPLICATE`.
- MediaDive REST for `687` identifies that target as `COLUMBIA BLOOD AGAR`, confirming that the `kg_microbe_match` is not a correct crosswalk for M1-Nocardiopsis arabia medium.

## Completeness

The generated record is complete enough for the DSMZ 1065 ingredient list, pH scalar, physical state, and KOMODO/DSMZ duplicate identity. It is incomplete for source preparation because the direct DSMZ owner has an `Adjust pH to 7.2` preparation step, while the generated record inherits the KOMODO owner and drops that step.

The sea-water amount is also carried as `1000 G_PER_L` even though DSMZ encodes `1000.0 ml` as the final solvent volume. That captures the liter-scale amount but loses the source's volume semantics and should not be treated as a weighed 1000 g/L solute.

## Findings

1. **Major - the KG Microbe cross-reference points to an unrelated medium.** `kg_microbe_match: mediadive.medium:687` resolves to DSMZ 687, `COLUMBIA BLOOD AGAR`, not DSMZ 1065. This bad crosswalk appears in both maintained owners and is propagated into the generated merge.

2. **Major - the generated merge drops the DSMZ pH-adjustment step.** The direct DSMZ owner has `preparation_steps` with `Adjust pH to 7.2`, and DSMZ/MediaDive both support that instruction. The generated canonical inherited the KOMODO copy, which has only a `ph_value` scalar and no preparation step.

3. **Minor - the sea-water volume is represented as a mass concentration.** DSMZ specifies 1000 ml sea water, but the YAML flattens it to `1000 G_PER_L`. That is a common import shorthand for waterlike solvents, but sea water is source-specified by volume and should retain volume/final-solution semantics where the schema permits it.

4. **Minor - source references are not structured.** KOMODO 1065 and DSMZ 1065 are recoverable from `media_term`, `notes`, and merge metadata, but neither maintained owner exposes the DSMZ PDF or MediaDive source as a structured `references` entry.

## Recommended Edits

- Remove `kg_microbe_match: mediadive.medium:687` from `data/normalized_yaml/bacterial/KOMODO_1065_M1-NOCARDIOPSIS_ARABIA_medium.yaml` and `data/normalized_yaml/bacterial/m1_nocardiopsis_arabia_medium.yaml`, or replace it with a verified M1/DSMZ 1065 match if one exists in the KG Microbe identifier space.
- Preserve the DSMZ `Adjust pH to 7.2` preparation step when KOMODO 1065 and DSMZ 1065 merge.
- Represent the 1000 ml sea-water solvent in a way that keeps the source volume rather than a weighed `G_PER_L` concentration.
- Add structured source references for KOMODO 1065, MediaDive medium 1065, and the DSMZ Medium 1065 PDF.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- After curation and regeneration, re-run an ignored-inclusive exact search for `CultureMech:003648`, `CultureMech:000498`, `komodo.medium:1065`, `mediadive.medium:1065`, and `mediadive.medium:687` to confirm the Columbia Blood Agar crosswalk no longer appears in the M1 owners or merge.
- Reinspect the DSMZ 1065 PDF and MediaDive 1065 REST record to verify the merged record still has the six supported source components and pH 7.2.
- Rerun open schema, strict, term, and reference validation on the regenerated `m1_nocardiopsis_arabia_medium.yaml`.

## Additional Notes

The exact search included ignored files. It found unrelated records for `mediadive.medium:687`, and those records are legitimate Columbia Blood Agar owners or variants; the defect is only the reuse of that crosswalk on the two M1-Nocardiopsis arabia owners.
