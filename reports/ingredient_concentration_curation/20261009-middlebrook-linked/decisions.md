# Linked Middlebrook Curation Decisions

Historical pre-apply checkpoint. The subsequent application and validation are
documented in [README.md](README.md); the decisions below preserve their original scope.

Status: source-reviewed decisions for eleven unchanged records, not an applied
repair or a completed per-record review. `context.json` freezes their exact
baselines and fourteen sources; `source-rows.json` contains each inspected
table row with its source URL, literal excerpt and locator. The previous
thirteen-record batch is explicitly excluded. These decisions do not increase
curation or follow-up coverage counts.

The [source refresh](source-refresh.json) downloaded all fourteen public
sources with HTTP 200 and found byte-identical captures; all parsed with the
requested identities. The three original PDF page images were inspected,
including the conditional route and hemin wording. This explicit urllib
retrieval does not change the validator's network transport or cache.

## Representation

1. KOMODO 645, its five strain entries, 645a, 911 and 911_44536 must follow
   their own ingredient tables, not the DSMZ compositions copied into their
   histories. Preserve displayed Gram Amount precision as provider-reported
   g/L. Leave null water/glycerol/NaOH amounts unquantified. Do not turn the
   rounded Mol Amount column into new molar assertions. Preserve source
   conflicts and do not claim a dilution mechanism explains the differences.
2. All nine KOMODO records need source-listed bovine albumin restored and the
   supplier-tagged false LB expansion removed. Preserve the distinct genuine
   NaCl and, for both 911 records, pancreatic digest of casein. Retain chemical
   annotations only for unchanged chemical identities, without claiming their
   groundings have been recertified. Source secondary-name inconsistencies
   such as Na2HPO4/monobasic phosphate and pyridoxine/HCl remain explicit.
3. KOMODO 645a additionally needs hemin and unquantified NAOH. Its table's
   hemin 0.04 g/L is a provider assertion. DSMZ 645a specifies 60 micromoles
   without a denominator and dissolution using 1N NAOH without a dose; this
   cannot independently establish 60 uM or a mass conversion. Withdraw the
   copied glycerol amount and commercial powder node, neither of which occurs
   as an ingredient row in this table. Do not assert experimentally glycerol-
   free medium merely because the table omits glycerol.
4. For DSMZ 645, use the explicit commercial route as the main preparation:
   19 g commercial 7H10, 5 ml glycerol, 900 ml water, then 100 ml OADC after
   sterilization/cooling. Preserve 19 g in a source-backed batch-mass note;
   the API's 20.9945 g/L uses a 905 ml encoding and is not a verified final
   concentration. Withdraw the commercial mixture's pure-agar grounding.
   Store OADC composition separately, retaining literal stock masses and
   explicitly attributed API stock rates, never finished-medium rates.
5. Preserve DSMZ 645's conditional from-scratch alternative separately in
   `variants[].modifications`, with one source-backed entry per table input.
   Its 1,000 ml water is not the commercial route's 900 ml water, and they
   must not be summed. The schema's `MediaVariant` has no typed ingredient
   list: do not invent one or place the alternative as simultaneous root
   inputs. Preserve displaced chemical annotations in the immutable before
   snapshot and append-only change history, not as false canonical ingredients.
   The source does not give a measured final volume for this alternative.
6. For DSMZ 911, keep the 21 g commercial-base input separate from its detailed
   basal table and the later 100 ml OADC dose. The basal detail belongs under
   the base descriptor and is not an additional set of simultaneous inputs.
   Preserve its 900 ml water as table context, not another receiving-medium
   water addition. Do not use the API's 11.0236 g/L powder field as a verified
   final rate. Keep glycerol/water as 0.005/0.9 L inputs and OADC as a 0.1 L
   dose; these do not establish a measured final volume.
7. DSMZ's pH statements are not heating operations. Preserve the literal pH
   and temperature at the correct recipe/alternative scope, with evidence;
   remove the spurious `HEAT` representation. Do not infer a titration step or
   reagent. All nine KOMODO PH Info cells are null, so do not copy a numeric
   pH assertion into those records.

All numerical assertions require an attached exact snippet in the eventual
YAML. The source-row inventory alone is not sufficient authorization for a
bulk numerical replacement; the guarded builder must encode these scopes.

## Relationship Decisions

The nine existing family edges must be reconciled on both ends, with source-
linked evidence and exact path/ID/name checks. No record is deleted or merged.

| Child | Proposed parent | Relationship | Evidence and limit |
| --- | --- | --- | --- |
| KOMODO 645 | DSMZ 645 | DERIVED_FROM | KOMODO's Instructions explicitly link DSMZ 645; different source quantity encodings are not an exact-duplicate proof. |
| KOMODO 645_44338/44339/44482/44483/44680 | KOMODO 645 | STRAIN_SPECIFIC_VARIANT | Each provider title explicitly says medium 645 modified for its DSM strain. Displayed ingredient tables match the KOMODO base; do not invent an unreported numerical modification or a new growth claim. |
| KOMODO 645a | DSMZ 645 | UNCERTAIN | Recognizable 7H10/OADC family with hemin, but historical product numbers and preparation details differ. This is a candidate family link, not a verified parent-plus-only-hemin formulation. |
| KOMODO 911 | DSMZ 911 | DERIVED_FROM | Explicit DSMZ 911 Instructions link, with unresolved rate normalization differences. |
| KOMODO 911_44536 | KOMODO 911 | STRAIN_SPECIFIC_VARIANT | Explicit strain-modified title; the displayed table matches the KOMODO base and does not identify the modification. |

DSMZ 645 and DSMZ 911 become family roots. KOMODO 645a must no longer be an
exact-duplicate parent of the seven plain/strain-specific 645 records. Remove
the old reciprocal edges before adding the proposed ones, and check cycles,
reciprocity and all links into the cohort across the corpus. The UNCERTAIN
645a relationship remains open for scientific review rather than claiming an
exact or fully characterized variant.

The [current-neighbor inventory](linked-neighbors.json) parsed all 15,910
tracked normalized YAMLs and compared that set with an ignored-inclusive
filesystem inventory. It found nine parent edges with eighteen reciprocal
references, no ID/name/path mismatches, no missing reciprocal entries, and
no external neighbors. This is a structural preflight, not validation of the
old duplicate assertions or the proposed new forest. The first read-only
helper attempt stopped on a stock record's optional name; the corrected
inventory handles that schema difference without changing any YAML.

## Before Applying

Build the scoped mutator and an independent source-derived audit. Account for
every old quantity node, every source row, both recipe alternatives and every
link change. Add mutation tests for water/dose scope, stock/final quantities,
genuine versus false casein/NaCl, hemin denominators, chemical-form ambiguity,
reciprocal edges, concurrent changes and no-op behavior. Refresh the sources,
run baseline checks, inspect the complete preview and attach evidence in YAML
before any write. Then run per-record schema/strict/reference checks, corpus
checks, runtime merge retention, metadata regeneration and the fast tier.
