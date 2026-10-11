# Medium 265 preparation and concentration repair

This applied, source-backed follow-up repairs three existing normalized records:
[DSMZ medium](dsmz-followup.md), [exact KOMODO wrapper](komodo-followup.md), and
[standalone MediaDive solution 531](solution-followup.md). It adds no new ID,
growth association or unique reviewed path. The all-record objective and
publication workflow remain unfinished.

## Evidence and decisions

The [original DSMZ recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium265.pdf)
was retrieved and its complete page inspected visually alongside extracted
text. PDF SHA256: `904a0973cffadca97f2da8c6b8cd2a89f5f842d53bdb98212d27aa86741ab173`.
The [frozen plan](plan.json) preserves the inspected text and hash, the complete
hash-verified medium/solution API captures, the exact KOMODO identity mapping,
before/after records and claim-level source snippets. Cached API payloads were
used after their web-tool URLs could not be retrieved; that tool failure is not
treated as an HTTP 404. The PDF download succeeded through authorized network
access. The PDF's copyright and creation years are not invented publication
metadata; individual authors and publication year remain unestablished.

The original recipe specifies 20 ml of 10% w/v yeast-extract stock, consistent
with its 2 g table input. The API's 20 mg/l row and imported 0.02 g/L conflict
with that instruction and the API's own preparation. The repair represents the
explicit stock strength and batch addition, not an inferred 2 g/L final-medium
concentration. The API row remains quoted as evidence of the disagreement.

The source also prepares sucrose, sulfide, sulfur and lipid separately from the
autoclaved mineral salt base. Each corrected record now distinguishes:

- Twelve mineral ingredients and the 1000 ml distilled-water input in the base.
  Their existing g/L values remain explicitly scoped provider normalizations;
  neither water input nor the API denominator proves measured final volume.
- Yeast-extract and sucrose stocks at 10% w/v, with 20 ml batch additions each.
- Sodium sulfide nonahydrate stock at 3% w/v, with a 10 ml batch addition.
- Sulfur's 10 g batch input and separate steaming procedure in notes/evidence,
  without an unsupported final-medium g/L slot.
- The original aqueous polar-lipid suspension's 6-12 ml batch dose as a range,
  without the former mass/percentage encoding. The API's alternative 10 ml/l
  dose and modified extraction protocol remain explicit source-version gaps.

Stock solvents are represented without guessed amounts. Base autoclaving is
distinguished from separately treated supplements; yeast is not incorrectly
autoclaved. No detailed lipid extraction procedure is inferred from the unread
Zillig article cited within the recipe. Historical aerobic/import annotations
and secondary chemical mappings are not endorsed by concentration evidence.

## Verified changes

The [applied independent audit](diff-audit.json) verifies 50 new evidence entries
supporting 102 scoped claims, five references and three appended curation events.
It verifies full-record inversion, all historical snippets and all prior history.
Record-local change counts, not independent scientific confirmations, are:

| Category | Count |
| --- | ---: |
| Existing ingredient nodes moved to their preparation | 49 |
| New quantity slots, including stock batch doses | 14 |
| Unsupported sulfur/lipid quantity slots removed | 6 |
| Water input unit correction | 1 |
| Concentrations rebased from flattened rates to stock strengths | 9 |
| Copies of the yeast amount conflict repaired | 3 |
| Stock/preparation descriptors added | 15 |
| Unquantified stock-water carriers added | 9 |
| Existing evidence scopes updated with preserved historical explanations | 24 |

The yeast-conflict count overlaps the stock-rebasing count; these are not
interchangeable or additive units. The three records represent the same source
recipe, not three independent confirmations. Source batch additions use `L`,
not `ML_PER_L`, and no measured complete-medium concentrations are calculated.

The [presentation check](presentation-check.json) verifies unchanged top-level
text and the full prior history text. Only the reviewed scientific fields and
their provenance are changed. The [initial preview](initial-preview.json) is
preserved; the final plan adds explicit powder-form and pH excerpts to its
explanations. The [reconciled preflight counts](preflight-counts-reconciled.json)
split 63 ingredient-note edits into 54 additions and nine corrections; the
earlier preflight's combined note count is historical, not an additional change.

Six final [baseline checks](baseline.json) pass, including all 15,910 records
under strict validation, three target schemas, independent inversion and 24
pre-apply tests. The first test attempt had one wrong historical-cohort reference;
its failure log is preserved and the corrected rerun passes. Applied readback,
independent inversion and a zero-change second apply pass. All 26 post-apply
checks are terminal in [validation.json](validation.json): twenty pass, three
are unavailable and three merge gates fail. No unavailable or failed check is
claimed as passed.

The focused post-apply runs pass **359 tests on isolated Python 3.11** and
**235 tests on cached Python 3.13**, with no errors, failures or skips. Strict
validation passes all 15,910 normalized records, and all three target schemas,
the ID check and the variant-link check pass. These are local focused checks,
not a full project-environment, full-suite or CI pass.
The product check is unavailable because `oaklib` is missing, and both requested
reference-validator runs are unavailable because `linkml-reference-validator`
is missing. These three exit-2 results are not automated source-verification
passes. Applied readback, independent inversion, no-op application, prior
medium/solution/KOMODO readbacks, cumulative semantic diff and exact-path
coverage all pass.

The [actual-group retention check](merge-retention.json) fails. The two medium
records form one group, whose canonical KOMODO copy preserves all checked fields
and all 25 scoped snippets. The DSMZ copy retains 24 of 25 scoped snippets but
not its complete solution metadata, preparation, notes, record evidence,
references or history. This is distinct from the complete preservation in the
authoritative normalized records. Standalone solution 531 is correctly outside
medium matching. No generated merge is published to bypass that failure.

Global merge verification also fails, with 1,247 name conflicts and 3,287
fingerprint issues. The [freshness audit](merge-freshness.json) fails with
6,320 tracked and 6,493 temporary outputs: 3,719 only tracked, 3,892 only fresh,
1,665 changed and 936 unchanged. All 6,493 identified groups were written;
this does not mean every input participated in merging. The pipeline excludes
4,785 standalone solutions and skips 342 other inputs. No tracked merge output
changed. Ruff, Black and `git diff --check` pass.

## Remaining scope

Final mineral-base and receiving-medium volumes remain unverified, as do detailed
lipid composition/yield, the original/API lipid-protocol difference, and independent
chemical-identity grounding. Existing placeholder/quality metadata in the standalone
solution is preserved rather than silently repurposed. The historical concentration
reports and the third KOMODO pass's withholding remain unchanged; this explicit
hash-linked successor records the repair. No generated merged file is hand-edited
or published, and no commit, PR or merge is claimed.
