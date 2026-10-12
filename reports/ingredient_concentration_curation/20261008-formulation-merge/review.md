# Adversarial Self-Review

Scope: formulation grouping and preservation of existing source-backed claims.
This is a local self-review, not an independent reviewer or a GitHub PR review.

## Fixed Findings

1. Ingredient-set equality allowed incompatible quantities and reference-only
   stocks to collapse into one recipe. Four failing baseline cases reproduce
   this with and without a supplied fingerprint. The CLI now groups formulation
   assertions, and the direct merger rejects incompatible inputs. The actual
   M1038/M781/M3009 collision is a corpus regression.
2. Canonical selection discarded other sources' root evidence, references,
   history and ingredient/stock evidence. Corresponding nodes now union complete
   evidence entries, not just reference identifiers. Distinct snippets from the
   same URL survive. Stock composition is not flattened into medium quantities.
3. Shallow copies allowed merge metadata/history writes to mutate loaded inputs.
   Deep copies and a dedicated regression establish input isolation.
4. A supplied fingerprint was trusted without checking current contents. It is
   now checked, and cannot bypass formulation compatibility.
5. The inherited file fingerprint reader rewrote literal escape sequences before
   comparison. Exact formulation grouping reads source YAML without that repair
   heuristic. A literal `\x41` regression checks file/in-memory consistency.
6. Unordered iteration of newly added provenance fields could change emitted
   key order across processes. Union fields are processed in sorted order.
7. Candidate matching's permissive error handling could silently skip malformed
   formulation input and still produce a successful CLI result. Formulation
   grouping now aborts before output for malformed data or read errors. A typed
   unidentifiable-medium exception preserves the documented empty-composition
   routing without classifying errors by message text. Five CLI failure probes
   cover malformed provenance/stocks/YAML, missing files and absent ingredients.

## Challenges Checked

- Amount, unit, volume basis, missing/zero, nested stock stage, reference identity,
  hydrate labels, preparation, physical state and unknown fields affect grouping.
- List ordering remains significant to preserve preparation and index-referenced
  evidence. No reordering or unsupported conversion is performed.
- Malformed provenance and cyclic inputs fail; shared aliases are not themselves
  cycles. The existing standalone-solution exclusion is preserved.
- Same-name distinct formulations get separate CLI outputs with disambiguated
  filenames. The legacy ingredient-set fingerprint is not used as a unique
  formulation identifier.
- The independent retention comparator has mutation tests for changed values,
  dropped or altered evidence, stock/direct-stage moves and added assertions.

## Unresolved Outside This Repair

- Automatic consolidation is conservative, not a chemical equivalence engine.
  Different free-text notes or scalar provenance keep candidates separate even
  when a later source review might establish equivalence. No new variant
  relationships or source-equivalence claims are inferred.
- The prior routing omissions remain: empty/unfingerprintable media require
  further work, while standalone solutions belong to the separate stock scope.
- Historical merge outputs remain stale. The legacy merge verifier checks
  readability and ingredient fingerprints, not full formulation identity or
  closed-schema validity; duplicate names can denote distinct formulations.
- `merged_from` retains its legacy filename-stem representation. Identical
  basenames in different categories are not disambiguated by that field alone;
  the audit reports exact paths. This repair does not migrate that schema contract.
- Earlier cohort retention scripts that call the merger on ingredient-only
  groups require the formulation API on rerun. Their historical JSON results
  must not be silently rewritten. The helper covered by the regression suite
  was updated.
- Full-corpus concentration review, citation-validator limitations, publication,
  and GitHub PR/issue lifecycle work remain unfinished. No green publication
  claim follows from this repair's focused tests or retention audit.
