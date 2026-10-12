# Local Adversarial Review

These findings are local; no GitHub issues or review comments were published.

1. **Nested stock evidence had no faithful container. Fixed in schema.** Root
   `SolutionRecipe.evidence` uses the existing evidence class and is optional.
   It avoids inventing import provenance or claiming that another ingredient's
   evidence supports a stock dose. Scientific claim-to-field linkage remains
   an explicit curation requirement, not something JSON Schema proves.
2. **An inserted dataclass field could shift positional arguments. Fixed.**
   The new attribute is appended after all existing attributes. A regression
   test checks the entire legacy constructor prefix and the new field position.
3. **Documentation generation reported success after generator failure. Fixed.**
   The obsolete `gen-markdown` entry point is replaced by the installed LinkML
   `gen-doc` interface, and the shell now fails on a failed generator. A fake
   generator exercises both exit paths without relying on a user's environment.
   The first failed generation receipt remains preserved.
4. **Schema acceptance could be mistaken for verified concentration evidence.
   Constrained, not solved globally.** Tests verify the reference walker visits
   root and composition evidence and rejects an altered source quote. The skill
   still requires an actual DOI/PURL, exact snippet, scoped explanation and
   supported arithmetic for every added or corrected concentration. Merely
   attaching a real quote cannot prove an unrelated numerical assertion.
5. **Flat documentation overwrote class pages with same-named slots. Fixed.**
   Thirteen pages contained fifteen wrong-case links. Enabling imported terms
   did not help; type-separated generation preserves both kinds of pages and
   passes all links. Staged output prevents failed generation from replacing
   previous documentation and successful generation removes stale output.
6. **Historical tests rejected independently audited later curation. Fixed.**
   Forty-one KOMODO and two stock states follow exact registered history chains.
   Tests independently audit the current changes before checking original claims
   at their historical scope; unknown hashes still fail. Old KOMODO829 repair
   tests now use their pinned baseline and explicitly reject current curated
   records instead of weakening the mutator's guards or restoring outdated data.
7. **Three sodium-resazurin stock inputs retain a sodium-free primary term.
   Open.** Structured traversal confirms the exact records and primary-source
   snippets. Preserve their supported doses and evidence while preparing a
   guarded identity correction; do not add a blanket test exemption. The local
   ontology snapshot is checked, but live entry access was unavailable and no
   replacement ID or ontology-wide absence claim is asserted.

All 830 final targeted tests and the 15,910-record closed-schema corpus check pass.
ID/product checks pass with the documented warning/unsupported-adapter limits.
The production-schema S599 smoke passes eleven source checks without writing
the recipe. The full regression run is terminal with 16,405 passes, 25 failures,
nineteen skips and two warnings. The passing targeted rerun covers 24 repaired
failures; the grounding failure remains open. This is not a green full-suite
rerun. No normalized record or in-record ingredient evidence was added in this
schema checkpoint. Source projections account for all 62 old medium323 quantity
fields but still require a guarded proposal and independent review before writes.
The all-record ingredient objective and global merge/freshness defects remain
open regardless of this optional-field change.
