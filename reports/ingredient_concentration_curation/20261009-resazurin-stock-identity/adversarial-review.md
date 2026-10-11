# Resazurin Identity Review

## Findings

1. **Open: publication identity remains wrong.** The packaged MIM label index
   resolves `Sodium resazurin (0.1% w/v)` to `CHEBI:8806` with `mim_exact`, both
   with and without the local primary term. This was verified with the production
   resolver, not inferred from label similarity. The index SHA256 is
   `a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262` at MIM commit
   `9f09e4fb97fb0e6cbbd6f25baca40b36512adb88`. Local withdrawal does not repair
   that upstream mapping. The immutable snapshot and resolver are unchanged.
   No GitHub issue was created because the earlier GitHub-write denial remains
   unresolved. This local finding remains a publication blocker.

2. **Resolved locally: unsupported exact primary identity.** The inspected
   DSMZ161 page 1, DSMZ212 pages 1-2 and DSMZ212a pages 1-2 specify sodium
   resazurin, 0.1% w/v, 0.50 ml. The same input is in Solution A for 212/212a.
   The local ChEBI snapshot labels CHEBI:8806 `Resazurin` with formula C12H7NO4
   and charge 0. It is not an exact identity for the named sodium-salt stock.
   The applied change withdraws that primary mapping, without inventing a replacement
   or asserting that a suitable salt term does not exist. The live ChEBI URL
   was inaccessible through the web tool; no service-wide outage is claimed.

3. **Resolved locally: evidence preservation and dose scope.** All three
   existing PDF snippets and earlier explanations are preserved; the identity
   disposition extends each existing evidence entry rather than adding a
   duplicate reference. The 0.0005 L preparation inputs are not converted into
   final-medium concentrations. Entire-record inversion checks all other fields
   and earlier history, including nested stock topology.

4. **Resolved before application: write protection.** The mutator checks exact
   git-tracked paths, pinned starting bytes, stable IDs, expected node labels,
   source/PDF hashes, schema, full-batch drift and symlink ancestors. It defaults
   to preview and refuses to overwrite a plan. Repeat application must be a
   no-op. Forty-four focused tests exercise these controls and forged data.

## Validation Scope

The [preview diff](preview.diff) changes only the three terms, the three evidence
explanations and three appended events. The first checkpoint harness failed
before any recipe write because it unpacked the claim API incorrectly; its
failed receipt is preserved. The corrected `preview-validation-v2.json` records
the actual subsequent baseline and safety checks. A terminal passing preview
does not imply application or all-record completion. Actual application and
post-write outcomes are recorded separately in [apply.json](apply.json) and
[post-validation.json](post-validation.json). Readback and repeat no-op pass;
the nine per-record commands, 158 reference checks and 943 focused tests pass.

No concentration value, unit, taxon association, chemical resolver rule, or
test allowlist is changed by this follow-up. It does not certify unrelated
groundings or close the remaining medium323 work or the all-record objective.
