# Adversarial Review

## Corrected Findings

1. **Stock dose mistaken for concentration.** DSMZ 1157's 5 ml riboflavin stock
   addition had become 5 g/L or 5% v/v. All three linked records now separate
   the 0.005 L batch dose from its explicit 0.2 mg/ml stock strength. Primary
   PDF and exact API snippets support the correction.
2. **Ambiguous percentage bases.** Flattened glucose/MgSO4/CaCl2 rates were not
   stock strengths. Their source percentages remain in notes without invented
   w/v, w/w or v/v units. Batch volumes remain explicit and supported.
3. **Drops interpreted as mass.** DSMZ 1164's seven drops of 0.5% iron stock
   do not establish 7 g/L, a fixed drop volume or an unambiguous stock strength.
   Numeric fields were withdrawn at those unsupported stages; the original
   source dose and percentage label remain quoted.
4. **Water percentage error and omission.** Two standalone solutions encoded
   1000 ml as 1000% v/v; four medium records omitted the source water input.
   All six now distinguish 1 L batch water from measured final volume.
5. **Stale exact relationship paths.** The 1164 parent and child IDs resolve
   to tracked archaea paths, not the bacterial paths in the old links. Only
   the paths changed; relationship semantics and permanent IDs were retained.
6. **Bibliographic and presentation problems in the first preview.** New API
   titles now use the actual dataset names. Repeated excerpts within one
   evidence explanation are deduplicated. The rejected preview was not applied.
7. **Historical regression test lacked the new successor.** The medium-batch
   test now follows the explicit hash-linked plan, as its established pattern
   requires. It still validates record hashes and literal historical evidence.

## Deliberately Unresolved

- No source-explicit final medium volume, percentage basis or drop volume was
  found in these inspected recipes. No derived final-medium concentrations are
  asserted from stock inputs.
- Existing high_metal flags, secondary chemical mappings and placeholder
  quality flags are not independently validated by these amount sources.
- Older API bibliography titles are preserved as historical metadata, not
  silently rewritten by this stock repair. Automated citation validation and
  actual merge-retention results must be reported separately from scientific
  source inspection and schema checks.

## Publication Findings

1. **Merge provenance loss remains open.** The actual two fingerprint groups
   preserve stock structures, quantities and literal ingredient quotations.
   They do not preserve twelve full ingredient evidence entries, two new events
   or all source-specific root metadata. `RecipeMerger.merge_group` copies one
   canonical recipe; `_merge_ingredients` takes one recipe's entire ingredient
   list instead of reconciling evidence. This is not a reason to remove evidence
   from normalized records or declare the strict retention check passed.
   See `merge-retention.json` and `merge-evidence-details.json`. A general fix
   must preserve claim/quantity scope when equal ingredient sets have different
   formulations; blindly pooling concentration evidence would be unsafe.
2. **Reference-validator format limitations remain open.** The network retry
   eliminates DNS failures and verifies 65 snippets, but six exact PDF snippets
   fail its matcher and twelve API/PDF titles fail when retrieved titles are
   URLs. Primary PDF bytes, extracted text and page images support those quoted
   claims. No cache injection, manufactured title or rewritten quote was used
   to manufacture a green validation result.

## Verification Scope

The independent auditor does not import the mutator. It checks source
arithmetic and claim coverage, preserves exact historical quotations, verifies
new provenance, and reconstructs every original record after reversing only
the reviewed changes. Regression mutations test guessed doses, strengths,
percentage bases, solvents, lost history/quotes, wrong links, changed flags,
unrelated amounts, missing claim rows and concurrent edits.

Historical source readback passes across all three affected cohorts: 500
medium records, 500 standalone solutions and 633 KOMODO records. Six shifted
historical ingredient claims have explicit relocation evidence. Wider test and
publication gate outcomes are tracked in the validation journal, not inferred
from the narrow tests.
