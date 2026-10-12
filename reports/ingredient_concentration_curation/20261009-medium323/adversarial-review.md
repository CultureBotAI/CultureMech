# Medium323 Adversarial Review

## Findings

1. **Open: sodium-resazurin publication identity.** The production MIM resolver
   still maps the sodium label to sodium-free CHEBI:8806. The local ChEBI
   snapshot reports formula C12H7NO4. Local withdrawal in DSMZ323 and solution599
   does not fix the immutable upstream index or certify publication readiness.
   The index remains unchanged. No GitHub write was attempted.

2. **Open: source limitations.** The required KOMODO physical-state field remains
   unverified; its compound table has no agar. The DSMZ table and procedure have
   different conditional agar rates, which remain explicitly distinguished.
   Solution599's generic glucose secondary mapping is retained, not newly
   certified as an exact D-glucose identity. These are not silently resolved
   through guessed values, averaging or a schema default.

3. **Resolved before application: cysteine review omitted source context.** The
   first draft treated the absence of L in the compound label as grounds for
   withdrawing its existing L-specific links. Full-page inspection finds that
   this very compound row includes `SEED-cpd00084`, and the same page's SEED table
   identifies cpd00084 as L-Cysteine. The successor [plan](plan-v2.json) retains
   both original links and supplies the additional exact excerpt. Its 1.13 g/L
   amount still comes only from the compound table. No aggregate SEED molarity
   is converted into a supplied-salt rate. The concentration parser deliberately
   excludes the SEED aggregate table; the independent auditor checks that table
   separately for identity. This supersedes the older cysteine withdrawal and
   uncertainty statements in the preserved draft artifacts.

4. **Resolved before application: late parent-directory symlink.** A temporary
   fixture replaced the parent directory after the first audit. The original
   writer did not reject the change; the regression test failed with
   `DID NOT RAISE`. The writer now rechecks resolved scope and symlink ancestors
   during full-batch preflight and immediately before each write. The regression
   remains in `tests/test_medium323_ingredients.py`. This is not a claim of
   transactional multi-file writes or elimination of all filesystem race windows.

5. **Resolved in the reviewed proposal: copied formulations and stock stages.**
   KOMODO's exact compound table replaces copied DSMZ rates, carbonate and agar;
   null amounts remain unquantified. The two media lose unrelated LB additions.
   DSMZ fatty-acid stock composition, missing component and addition dose are
   restored; solution percentages and water units are corrected with evidence.
   All 62 old quantity fields are accounted for, including removed placeholders.

6. **Resolved in the proposal: unsupported equivalence.** The KOMODO page links
   to DSMZ323, but their formulations differ. Reciprocal links are `UNCERTAIN`,
   not `SOURCE_DUPLICATE`, and do not assert a historical derivation direction.

7. **Resolved after application: stale historical-hash test assumptions.** Two
   batch tests compared current bytes directly with an earlier applied result,
   rejecting later registered evidence-backed changes. The tests now audit and
   invert the complete successor chain, then independently count the original
   batch. Mutation checks remain active. The original QA result (202 passed,
   two failed) and interrupted fast run are preserved. The final QA-v2 result
   is 204 passed; fast-v2 is 13,064 passed, sixteen skipped, 3,498 deselected.

8. **Open: global merge artifacts.** Strict/ID/product checks pass, but merge
   verification and freshness fail. The corpus receipt's aggregate `passed`
   means required checks passed; the two failing diagnostic commands are
   explicitly non-required and are not a clean publication gate.

## Receipts

The initial checkpoint failed before any recipe write because a generated test
cache lacked a version field. Its [failed receipt](preview.json) is retained.
The succeeding preview receipts and original plan remain historical, not
application authority after the later write-guard and cysteine corrections.
The latest gate is [preview-final.json](preview-final.json), which must be
terminal and passing, match current code/plan hashes, and match the unchanged
full-corpus inventory before application.

The current DSMZ PDF was re-opened through the web tool and its page image
inspected. MediaDive's API and KOMODO did not open through that tool in this
turn; their hash-pinned official captures are used, not claimed as fresh live
responses. The source snippets, headers, rows and locators are rechecked locally.
