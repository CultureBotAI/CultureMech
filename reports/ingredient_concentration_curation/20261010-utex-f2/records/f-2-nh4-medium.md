# UTEX F/2 Ingredient And Stock Review

- Record: data/normalized_yaml/algae/f_2_nh4_medium.yaml
- ID: CultureMech:000169
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: 9dc2cba1b150bce303b6d1b8d889115d903051c659079bf776a886958aaf91da
- Result SHA256: 6a54f03bf7609d29e344454d31f73943c892a9d6a11ffea0d15c536ad70218fc

## Source And Scope

The [pinned source ledger](../source-review.json) contains the inspected exact UTEX HTML recipe, linked stock tables, PDF hashes and identity sources. Five formulation PDF page images were visually inspected. Chemical database and supplier sources support identities only, not doses. The supplier page was inspected with the web tool after direct HTTP capture timed out; no successful full HTTP capture is claimed. Authors/publication years were not established. Each enriched bibliography records source type, discovery mode and access date.

All structured ingredient, inline-stock and stock-addition concentration fields are listed below. Removed water/makeup quantities and the pinch remain as evidenced preparation notes. The supplied chemical names resolve through the packaged MIM index; the old phosphate formula alias in that immutable index still points at a different, non-hydrated term and is not repaired here.

| Field / ingredient | Before | Applied | Status | Identity correction | PURL / exact snippet / locator / reasoning |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NH4MgPO4 | {"unit": "VARIABLE", "value": "pinch per 175 mL flask"} | omitted; nonnumeric preparation note retained | correct | unchanged; not separately recertified | {"explanation": "Claim: ingredients[0].concentration. Source-explicit nonnumeric dose; no mass or final concentration is supplied. Remove the pseudo-concentration and preserve the pinch as a preparation note. Locator: Directions step 3, interpreted with step 2; source version is the hash-pinned HTML capture. Evidence supports removing the numeric/pseudo-concentration and retaining the preparation note, not a replacement numeric amount. ", "locator": "Directions step 3, interpreted with step 2", "reference": "https://utex.org/products/f-2-nh4-medium", "snippet": "add a pinch of NH 4 MgPO 4 to each flask."} |
| solutions[0].concentration / F/2 Medium | {"unit": "ML_PER_L", "value": "1000"} | {"unit": "L", "value": "0.175"} | correct | unchanged; not separately recertified | {"explanation": "Claim: solutions[0].concentration. Absolute F/2 input per flask: 175 mL / 1000 = 0.175 L. Neither 250 mL vessel capacity nor the table preparation amount of 1 L is a final-volume denominator. Locator: Directions step 2; source version is the hash-pinned HTML capture. ", "locator": "Directions step 2", "reference": "https://utex.org/products/f-2-nh4-medium", "snippet": "Dispense 175 mL into 250 mL flasks."} |

## Other Evidenced Changes

All exact field operations, identity evidence, source links and merged root-level stock-dose evidence are recorded in [the plan](../plan.json). Existing history, organism claims and unrelated fields remain unchanged. The parent child-link note distinguishes a 175 mL aliquot from its 250 mL vessel; 8 ppt filtration is removed; the NH4 variant no longer asserts dissolution.

## Narrative Variants

No inline literature variants occur in this record; parent/child formulations are not interchangeable.

## Remaining Issues

- Trace-metal source mass/molarity discrepancy remains unresolved; only mass-column stock amounts are supported.
- The parent and 1% HTML/PDF seawater salinity versions differ; neither is silently substituted for the other.
- The 5% source lists vitamin doses but omits a later vitamin-addition step; no missing procedure is invented.
- Narrative literature variants and existing organism/growth claims are unchanged and not certified by UTEX sources.
- No numeric amount is invented for makeup/carrier water, seawater or the NH4MgPO4 pinch.

## Validation

[Preview](../preview.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json), [retention](../reconcile-retention.json) and [checkpoint](../validation.json) record outcomes. Pending and failed checks are not passes. No taxa-media associations are added.

## Applied F/2 Evidence Successor

This section supersedes only the claim wording/evidence listed here. The preceding rows document the earlier UTEX batch, including its original snippet typography; all structured parent ingredient and stock quantities remain unchanged. The original report is preserved as a non-canonical text snapshot in the successor directory.

Previous result SHA256: `f49cc0b2c4b6d97f51c48229ac615a0cd9f285b80f0c3007210c80632ea502c8`.
Current result SHA256: `6a54f03bf7609d29e344454d31f73943c892a9d6a11ffea0d15c536ad70218fc`.

The [successor source ledger](../../20261010-utex-f2-followup/source-review-v2.json) pins the metadata, exact excerpts, unit-heading typography and old/new operations. The [guarded plan](../../20261010-utex-f2-followup/plan-v2.json) preserves prior history and unrelated organism/growth evidence. No taxa-media associations are added.

| Field / component | Existing | Disposition | Source / snippet / locator / calculation / action |
| --- | --- | --- | --- |
| ingredients[0].concentration | unknown / not asserted | not_quantified | {"action": "Correct evidence typography only; quantity remains omitted.", "calculation": "No numeric amount is stated.", "locator": "Directions step 3", "new": null, "reference": "https://utex.org/products/f-2-nh4-medium", "snippet": "add a pinch of NH4MgPO4 to each flask."} |
| solutions[0].concentration | {"unit": "L", "value": "0.175"} | evidence_only | {"action": "Retain aliquot; correct two relationship descriptions and scope existing root evidence.", "calculation": "175 mL / 1000 = 0.175 L; flask capacity is not a concentration denominator.", "locator": "Directions steps 2-3", "new": {"unit": "L", "value": "0.175"}, "reference": "https://utex.org/products/f-2-nh4-medium", "snippet": "Dispense 175 mL into 250 mL flasks."} |

The seven successor rows across the two records are additional claim-level follow-up, not two newly reviewed corpus paths. Unchanged variant condition/growth assertions are not blanket-certified by this ingredient review.

### Remaining Source Limits

- The selenite correction reports Table S1 only: 0.001 micromolar = 1 nanomolar. Main methods remain inaccessible, so possible main-text/table disagreement and the existing UTEX LB2658 strain claim are not resolved.
- The Table S1 recipe and Matsui artificial-seawater variant are not equivalent to canonical UTEX natural-seawater F/2; no parent ingredient or stock concentration changes.
- The Tetraselmis evidence is abstract-level only. Phosphorus repletion is a separate experimental condition, not an added ingredient in the nitrogen-replete variant.
- The NH4MgPO4 pinch remains unquantified; 250 mL is flask capacity, not final medium volume.
- Earlier UTEX stock molarity, salinity-version, chemical catalog and missing vitamin-step issues remain open. Existing organism/growth claims and earlier curation history are unchanged.
- Matsui methods were manually inspected, not captured as a complete HTTP download; current browser-check failures and production reference outcomes are reported separately.

### Successor Validation

[Preview](../../20261010-utex-f2-followup/preview.json), [application](../../20261010-utex-f2-followup/apply.json), [post-edit](../../20261010-utex-f2-followup/post.json), [references](../../20261010-utex-f2-followup/references.json), [corpus](../../20261010-utex-f2-followup/corpus.json) and [terminal checkpoint](../../20261010-utex-f2-followup/validation.json) record actual results. Pending or failed gates are not passes.
