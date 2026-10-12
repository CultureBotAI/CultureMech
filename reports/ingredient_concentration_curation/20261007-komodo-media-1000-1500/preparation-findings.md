# Source and preparation findings

These findings apply to the exact paths and source captures in [plan.json](plan.json).
The [pinned vetoes](withholdings.json) contain the source URL, hash, JSON pointer,
literal preparation snippet and reason. They can withhold support, not authorize
a replacement amount. The 46 accepted records receive only scoped evidence for
264 already-present ingredient amounts. No numeric or formulation edits occur.

## Whole-record withholdings

| Medium | Unresolved scope and decision |
| --- | --- |
| 226 | A required 1 ml/L addition of 10% acetylacetone in ethanol is absent locally. Stock and percentage bases need representation. The API supports the finding; the original PDF could not be retrieved through the web tool in this review. |
| 232 | The required 0.05% cysteine-HCl addition is missing. Its unqualified percentage does not establish a mass/volume basis. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium232.pdf) corroborates the addition. |
| 232b | Resazurin stock and cysteine additions are missing. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium232b.pdf) describes supplements and gas handling; the legacy duplicate link to 232 does not prove the same formulation. |
| 239 | The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium239.pdf) specifies alternative 100 ml additions of 1 mM diethylphosphonate or 20 mM phosphate buffer. Local stock boundaries and alternatives are absent; a liquid dose is encoded as mass. No branch is selected. |
| 255 | The API uses 1002 ml, but the table lists 1000 ml water, 1.25 ml iron stock and 0.5 ml resazurin stock, plus separately prepared cellobiose. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium255.pdf) also describes strain-specific substitutions/additions. Rounded volume and unknown cellobiose-stock volume do not establish a final denominator. |
| 262 | The API dissolves glucose separately in 10 ml water but uses a 1000 ml main denominator. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium262.pdf) requires separate glucose sterilization without that volume. Stock, basal and complete-medium stages need reconciliation. |
| 265 | API yeast extract is 20 mg/L, whereas preparation specifies 20 ml of 10% w/v solution and the [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium265.pdf) lists 2 g. Separate supplements and a variable 6-12 ml lipid dose are flattened. Preserve the conflict; do not infer a final concentration from the input mass alone. |
| 266 | Both the API and [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium266.pdf) contain a 5 g sulfur table entry but a 10 g preparation instruction. An added sulfide stock is absent locally. Neither sulfur statement is silently preferred. |
| 268 | Tea and sucrose are extraction inputs, followed by filtration and a separately acidified starter. Input loading, recovered tea and starter dilution must be distinguished; no extraction yield or retained-solute concentration is inferred. |
| 303 | The table lists 1000 ml water plus 100 ml serum; the [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium303.pdf) adds serum after autoclaving at 100 ml/L. The API denominator is still 1000 ml. Base and supplemented-medium bases remain unresolved. |
| 338 | The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium338.pdf) prepares haemin in NaOH and dilutes it to 10 ml; formate and fumarate are also sterilized separately. The local flat recipe lacks these preparations and an established final-volume basis. |
| 368 | Required post-sterilization 10% v/v ethanol is absent from the local recipe/table. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium368.pdf) corroborates the addition. The basal and supplemented formulations are not interchangeable. |
| 393 | API preparation says pH 5.6, whereas API/local metadata and the [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium393.pdf) specify 6.5. This is a source/version conflict, not permission to overwrite either value. |
| 394 | The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf) defines separately sterilized molar/percentage stocks. API base rates use 1070 ml while several stock-derived rates use another basis; local Tris-HCl is a volume encoded as mass. Reconcile stages and denominators. |
| 435 | The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium435.pdf) doses charcoal per liter of agar base before serum addition, not per unqualified complete medium. Resolve the 800 ml base/200 ml serum boundary. Its calf-serum label does not independently establish the local fetal-bovine identity. |

These 15 records are unchanged. The [prior-cohort handoff](prior-cohort-handoff.json)
pins their exact DSMZ counterparts, current records/hashes, earlier plan results
and 97 existing same-source ingredient entries. All 15 hashes still match the
historical results. These new findings reopen preparation scope; they do not
automatically disprove every basal amount or justify deleting historical quotes.
Any corrective follow-up must link its predecessor and preserve the source
disagreement and history.

## Accepted scope and remaining gaps

- 221 supports ten basal table amounts on the provider-declared basis; its two
  20% substrate stocks and conditional agar are not newly quantified. 222, 223,
  227, 229, 256, 281 and 352 retain unsupported product, substrate-form, liquid,
  stock-strength or unquantified-material attributes where applicable.
- 231's unqualified cysteine percentage, 240's blood percentage, and 242's
  methanol dose/conditional agar remain unsupported. Liquid doses encoded as
  mass in 250, 254, 264 and 267 are not endorsed or repaired by basal evidence.
- 251's soil-extract dose remains unsupported as a mass rate. Extraction input
  loading does not establish yield or recovered concentration. Its four accepted
  main-table claims are not evidence for the raw soil input. 249's exact accession
  mapping was checked despite the updated dataset name; its legacy oxygen note
  is not supported by this concentration review.
- 237, 340, 344, 376 and 449 retain separate-sterilization follow-ups. Stock
  strengths are not invented; 344 evidence is not propagated to medium 729.
  Optional manganese additions for 238, 306 and 362 are not universal doses.
  Legacy external-match numbers are not recipe-identity evidence.
- 310 explicitly makes up to 1000 ml, supporting its basal calcium-carbonate
  and agar scope; the V8 liquid dose remains unsupported as mass. For 354,
  six claims use the provider's declared 1612 ml basis, not a measured final
  volume. Liquid egg/glycerol encodings are not endorsed. The
  [original 354 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium354.pdf)
  does not authorize inventing an additional preparation step.
- 360 explicitly permits agar for the local solid recipe. 365's liquid
  reactivation and solid cultivation steps are not interchangeable growth
  claims. 370 explicitly specifies sequential pH adjustments, unlike the
  unresolved 393 disagreement. 372 gives a final 1000 ml basis; product-label
  attributes are not established by the amount alone.
- The original recipes for [425](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium425.pdf)
  and [426](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium426.pdf) list
  15 g agar. Their API tables contain a 20 g amount with a 15 g/L rate. The
  arithmetic guard withholds agar despite the local 15 g/L value; other
  unambiguous rows receive evidence. Resolving this conflict requires separately
  scoped original-source evidence, not treating an inconsistent API as verified.

Ontology mappings, legacy oxygen annotations and duplicate/variant links are
unchanged and not verified by concentration snippets. Complete records and
source payloads were preserved and checked programmatically; the scientific
candidate contexts were inspected. This is not a claim of manual review of
every historical curation event or every ontology/variant relationship.

## Unavailable sources

The [capture inventory](source-captures.json) records actual HTTP 404 responses
for 34 endpoints affecting 40 selected paths: 272, 273, 279, 285, 290, 293a,
296, 297, 298c, 298d, 298e, 298f, 298g, 298h, 298i, 299, 304, 307, 313, 324,
327, 334b, 345, 349, 355, 383c, 383d, 384, 386a, 387, 400, 406, 409 and 418.
These are endpoint-specific failures, not evidence that no original or archived
recipe exists. No source DOI, author, publication year, quantity or variant
equivalence was manufactured. The dataset identity mapping and amount source
have separate provenance and roles.
