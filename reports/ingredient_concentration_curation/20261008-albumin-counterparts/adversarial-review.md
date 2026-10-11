# Adversarial Review

## Findings Addressed

1. False LB supplier nodes replaced albumin in all four records. The repair
   uses source-specific albumin amounts and stock stages. J252 has a genuine
   yeast-extract node with the same label as a false LB constituent: explicit
   paths and supplier provenance prevent deleting the genuine ingredient.
2. Batch masses, liquid doses, percentage labels and final concentrations were
   conflated. The audit reconstructs every source row and every old quantity;
   it rejects source milligrams restored as same-number g/L, water interpreted
   as final volume, or fixed values hidden behind VARIABLE placeholders.
3. M244/J252 explicitly specify albumin 10% w/v. Treating all percentage bases
   as unknown would discard supported data. The repair preserves this stock
   strength and derives its 10 ml batch dose from the separately evidenced 1 g
   contribution. Tests reject a changed basis, wrong factor, missing strength,
   fabricated per-liter dose, or missing calculation explanation.
4. Unspecified gelatin, serum, glucose, cysteine, yeast and sulfide percentage
   bases do not inherit albumin's w/v basis. Hemin's normality-labeled solvent
   also does not establish molarity or a fixed solvent dose.
5. Filtration, autoclaving, anaerobic additions and pH temperature are distinct
   preparation scopes. Tests reject albumin autoclaving, hemin receiving another
   stock's filtration instruction, pore-size guesses, and room-temperature pH.
6. M244's `high_metal` flag requires a verified total molar concentration under
   its schema definition. Corrected milligram batch inputs and an unknown final
   volume do not support that flag. It is removed explicitly, not set false;
   the independent audit and history verify this withdrawal.
7. JCM201's HTTP 200 response contains no recipe. M194's access gap is disclosed
   and no SUPPORT claim or bibliography entry cites that unavailable original.
8. Two existing resolver tests mutated the live normalized corpus. Their
   temporary-file race caused the corpus ID scanner to exit 2 despite all
   15,910 actual records having IDs. Both tests now use a monkeypatched temporary
   corpus, and all 11 direct resolver tests pass. The original failure is retained
   alongside a successful serial ID recheck, not erased. The resolver-only
   fast selection also passes six tests with one skip, not a full fast-tier
   rerun. See the local
   [issue draft](issue-live-corpus-test-mutation.md).

The 155 dedicated tests and 498-test focused selection pass. The broad fast tier
passed 9,173 tests before the test-only corpus-isolation fix. Tests cover source
amount disagreement, unsupported numbers, missing identity/annotation/history,
fabricated quotations, duplicate evidence, incomplete claims or lineage, and
concurrent edits, forged plans and symlinks before any target write.

This is local adversarial self-review with an independent reconstruction and
mutation tests, not external PR approval or independent human review. No GitHub
issue, comment or PR was submitted in this batch.

## Remaining Findings

- The identity queue contains 111 unchanged candidates: 76 acid-name and 35
  albumin-name substitutions. Existing review reports did not prevent these errors.
- The next DSMZ/KOMODO 403/751 records remain unedited. Their original recipes
  have distinct stock stages, product alternatives and a liquid SC variant;
  do not copy the JCM201/JCM220 repair or mix these formulations.
- Existing chemical mappings are preserved, not automatically recertified.
  Unknown final volumes and unspecified percentage bases remain explicit.
- Global merge/freshness failures, remaining corpus reviews and publication
  remain separate unfinished work.
