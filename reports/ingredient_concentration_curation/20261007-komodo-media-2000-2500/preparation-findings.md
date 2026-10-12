# Candidate Formulation Review

Complete source data and local candidate records were inspected for the 69
initially proposed records. The frozen [context](inspected-candidate-context.json)
contains every original field, original text, source response, source metadata,
and preliminary claim. Shared ingredient/history templates were inspected using
a lossless representation that reconstructs every full local object exactly;
all differing amounts, root metadata, variant links and preparation contexts
were retained. This does not claim manual review of all 500 records or validation
of the historical ontology mappings and duplicate links.

The [source-pinned withholdings](withholdings.json) remove 155 initially proposed
concentration claims across 23 records. They cannot authorize a new amount.
The resulting preview proposes 220 evidence-only claims on 46 records, with
no quantity, unit, ingredient, stock, variant or growth-association changes.
Application and validation status are recorded separately in the batch README.

## Withheld Formulations

Each entry below has its exact source excerpt, JSON locator, source URL and hash
in `withholdings.json`. The complete context preserves the other relevant rows
and preparation paragraphs. These are unresolved formulation tasks, not a claim
that every individual basal amount is false.

| Medium | Required follow-up |
| --- | --- |
| 546 | Reconstruct the 990 ml base and two 5 ml, 1 M salt additions; do not accept imported mass conversions as stock evidence. |
| 582 | Represent the post-sterilization bicarbonate addition; its stock strength and dose are unspecified. The local medium is liquid. |
| 588 | Separate 850 ml basal water, 50 ml glucose solution and 100 ml PIPES preparation; resolve the glucose percentage basis. |
| 593 | Represent the late bicarbonate stock. The 15 g/l agar instruction matches the solid state but does not resolve this stock. |
| 615 | Reconcile acidified iron and indicator stocks, and the provider's 1004 ml denominator versus the listed liquid inputs. |
| 620 | Resolve unqualified 2% methanol and separately filtered supplements; 20 G_PER_L is not established by a bare percent sign. |
| 623 | Add the required late sulfide reduction stage from exact evidence. It is absent from the local ingredient list. |
| 631 | Repair acetic acid/ethanol volume inputs currently encoded as mass concentrations. Do not impose the separate two-layer agar procedure on the liquid record. |
| 648 | Separate glucose, cysteine, sulfide and carbonate additions and their specified anoxic preparation atmospheres. |
| 650 | Pyruvate is present, not missing. Reconcile 1.741 G_PER_L with the source's post-autoclave 20 mM instruction and exact chemical form. |
| 659 | Represent the 1.2 ml, 1 M calcium stock rather than 1.2 G_PER_L; retain the explicit lactose final concentration without inventing a stock dose. |
| 670 | Reconstruct the acidified 40% w/v ferrous-sulfate stock and its 50 ml addition to the autoclaved base. |
| 673 | Reconcile sulfur (table 5 g, preparation 10 g), yeast extract (table 1 g, preparation 20 ml of 10% w/v) and the omitted sulfide stock. |
| 675 | Represent prepared soil-extract addition in volume units and its separate extraction; do not infer retained soil mass or extraction yield. |
| 677 | Restore separately prepared anoxic glucose, cysteine and sulfide additions. |
| 694 | Resolve the magnesium stock, unqualified thiamine percent and carbon supplied by evaporation; no fixed carbon dose is specified. |
| 695 | Resolve unqualified iron-stock percent and the artificial-seawater volume input; do not equate it to a mass concentration. |
| 696 | Serum is present, not missing. Resolve its unqualified post-sterilization 5% addition versus the imported 50 G_PER_L. |
| 750 | Represent the late 10 ml methanol input without assuming density or measured final volume. |
| 752 | The record is liquid, so the agar-specific carbonate replacement is not itself a conflict. Both 1 ml metal-stock doses are nevertheless misencoded as 1 G_PER_L. |
| 762 | Represent the separately sterilized carbonate/bicarbonate preparation in 100 ml water and the 900 ml base. |
| 781 | Separate extraction from the 100 ml prepared-extract receiving dose; 150 ml extraction water does not establish final-medium concentration. |
| 785 | Represent separately dissolved/sterilized carbonate and chloride, preserving unknown volume allocation and optional agar scope. |

## Retained Claim Boundaries

- Claims are exact, provider-declared main-recipe `g_l` values, not independently
  measured final concentrations or authorization to convert an input mass using
  water alone as the denominator. The evidence states this limitation explicitly.
- 530: separate filtration of thioglycolate does not specify a different stock
  strength. Only its declared main-recipe amount is supported.
- 587: the preparation explicitly specifies ferric ammonium citrate at 0.25 g/l.
  Its stock strength and dose remain unknown; they are not inferred.
- 729: separately autoclaving glucose does not supply a stock strength or dose.
  The evidence supports only the declared main-recipe amount, not a stock recipe.
- 581 and 736: glycerol is actually specified in grams; 736 also gives Tween 80
  in grams. These are not density-based conversions from liquid volume.
- 627: pH 7.8 before boiling and pH 7.3 after readjustment are distinct stages.
  The local solid formulation agrees with the explicit agar instruction. The
  seawater mass encoding is not supported by this pass.
- 782: pH 6.8-7.0 before autoclaving and 8.5-9.0 after it are distinct stages.
  The conditional 1.5-2.0% w/v agar range is not endorsed as one fixed value.
- 775: the stated liquid base is cheese whey, not distilled water. Neither the
  whey nor Tween volume input is endorsed as a mass concentration.
- 555, 656, 658 and 669: inconsistent agar rows remain conflicted, while only
  other unambiguous source rows receive evidence. The earlier original-recipe
  investigation for 656/658 supports 15 g input, not proof of 15 g/l final volume.
- Qualified/branded ingredients, optional rows and unsupported water quantities
  remain explicit gaps. Source-dose support does not validate secondary ChEBI,
  MIM, KG-Microbe, historical oxygen, or duplicate/variant annotations.

All 23 withholdings and other unresolved rows require follow-up; this cohort
does not complete the all-record objective.
