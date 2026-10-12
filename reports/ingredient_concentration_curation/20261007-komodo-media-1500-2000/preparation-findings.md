# Fourth KOMODO source-pass findings

This batch covers frozen inventory offsets 1500-1999: 500 exact tracked paths,
86 base accessions and 414 strain/variant accessions. The [candidate context](inspected-candidate-context.json)
preserves all eight complete candidate records and complete API responses.
The [original-source cross-checks](original-source-crosschecks.json) preserve
the separately inspected page-1 text and PDF hashes for all eight candidates.
Six records have accepted evidence-only proposals; two whole-record decisions
veto fifteen preliminary ingredient endorsements. The remaining records are
unresolved under the guarded source-mapping review, not scientifically complete.

## Preparation Findings

| Medium | Evidence and decision | Required follow-up |
| --- | --- | --- |
| 469 | [API](https://mediadive.dsmz.de/rest/medium/469) preparation separates catalase and magnesium sulfate into filtered stocks using 10 ml water each and 980 ml base water. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium469.pdf) says "Catalase and MgSO4 are sterilized separately by filtration." Its table gives 1000 ml water without stock volumes. | Represent separate preparations and preserve the original/API water-input distinction. Do not infer final stock or receiving-medium volumes. |
| 489 | [API](https://mediadive.dsmz.de/rest/medium/489) and [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium489.pdf) add cysteine and sulfide after sterilization from anoxic stocks. Resazurin is supplied as a 0.1% w/v stock. The local record flattens those stages and retains an aerobic import annotation. | Recover preparation boundaries without inventing cysteine/sulfide stock strengths or volumes; reconcile final-volume scope and atmospheric annotations. |

The [machine-readable decisions](withholdings.json) pin exact source responses,
JSON pointers and literal preparation excerpts. They do not automatically
disprove every basal amount. The read-only [prior-cohort handoff](prior-cohort-handoff.json)
identifies two earlier DSMZ copies with fifteen same-source ingredient entries
requiring preparation-scope reassessment. Their YAML and historical plans remain
unchanged by this batch.

## Accepted Scope

The accepted ingredient counts are 460: six, 464: four, 467: six, 468: two,
472: three and 513: four. Their inspected original tables agree with the
accepted API amounts and forms. Evidence supports the provider-reported main
recipe rates, not independently measured final volume, downstream dilutions,
chemical ontology mappings, category assignments or growth claims.

Known unresolved fields remain visible. In 467, the 1000 ml tap-water input is
still encoded locally as 1000 g/L and is not endorsed. In 468, the Oxoid-qualified
commercial broth is not endorsed without product identity reconciliation.
In 472, desiccated ox-bile and technical-grade glycerol mono-oleate remain
outside accepted evidence; absence of pH in its original PDF does not prove the
API's extra pH instruction false. No water density or final-volume assumption
is used to make these unresolved fields pass.

## Exact Variant Source

The [KOMODO page for 457_7098](https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=457_7098)
was retrieved successfully after the web tool was unavailable and sandbox DNS
failed. Neither access failure was counted as HTTP 404. The [frozen finding](variant-457_7098-source-finding.json)
preserves its exact HTML, response hash and the complete local record.

Its table explicitly reports per-liter gram amounts for that variant and lists
pentachlorophenol and trace ingredients. The local record instead contains
base-recipe dibenzofuran/DMSO and commercial-medium expansions whose use in this
variant is not established by that page. Even phosphate values differ. Thus
variant-specific evidence is available, but it does not justify treating the
current local formulation as correct or blindly replacing it with rounded web
values. Exact variant reconstruction, original-recipe preparation review and
source-version reconciliation remain required. No amounts were added to this
variant and no evidence was propagated from the base recipe.

The separately inspected [original DSMZ 457 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium457.pdf)
(page 1) distinguishes reactivation in complex media 1, 220 or 535 from later
cultivation in mineral medium with an appropriate carbon source. It also
separately sterilizes phosphates and defines nested SL-4/SL-6 trace stocks.
Those reactivation media must not be flattened into mineral-medium ingredients.
The inspected page does not specify the DSM 7098 carbon additions; its generic
carbon-source instruction cannot establish them. Exact variant reconstruction
must reconcile these stages with the variant's own table, including its rounded
reported rates, rather than assuming the original water input is a measured
final volume.

The current [legacy resolver](../../../src/culturemech/enrich/dsmz_resolver.py)
contains a source-copying rule consistent with this record's historical
`dsmz-resolver-v1.0` event. `_build_dsmz_index` and `extract_dsmz_id` strip DSMZ
letter suffixes; `resolve_recipe` does not compare the full KOMODO accession
before `merge_composition` copies base ingredients and solutions. The maintained
[command](../../../scripts/resolve_komodo_compositions.py) still exposes that
resolver. This code inspection does not replay or prove the exact historical
execution, and filename changes may affect which inputs it reaches today.
Future importer repair needs accession-preserving lookup and explicit rejection
of unverified base-to-variant transfers, plus guarded evidence-bearing writes.
The importer was not run or changed during this cohort's data validation.

## Access Gaps

The [source inventory](source-captures.json) pins 88 mapped endpoints: 81
accessible API captures and seven actual HTTP 404 responses, affecting eight
selected paths. The unavailable identifiers are 476, 478, 485, 488, 490a, 495
and 510. They remain source-access gaps, not evidence of zero ingredients or
absent original recipes. Cached responses were hash-verified; they are not
misrepresented as fresh downloads.
