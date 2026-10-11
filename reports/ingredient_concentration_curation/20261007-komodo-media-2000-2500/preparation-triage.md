# Preliminary Preparation Triage

All 69 initial candidate preparation contexts and qualified/liquid/optional
source rows have been inspected, with local pH context and proposed ingredient
lists. The first 12 also included the fuller local context and proposed amounts.
This is not complete record/source inspection or approval of the 375 proposed
claims. No normalized record was edited. Source identities, response hashes and
retrieval metadata are pinned in [source-captures.json](source-captures.json).

## Priority Scope Checks

| Medium | Inspected source excerpt or conflict | Required next decision |
| --- | --- | --- |
| [530](https://mediadive.dsmz.de/rest/medium/530) | `Sterilize Na-Thioglycolate separately by filtration.` | Separate thioglycolate input/preparation from any claim about a stock strength. |
| [546](https://mediadive.dsmz.de/rest/medium/546) | `add 5 ml 1 M CaCl2 x 2 H2O and 5 ml 1 M MgSO4 x 7 H2O as sterile solutions.` | Reconcile both post-autoclave stocks and the basal-volume basis before approving amounts. |
| [588](https://mediadive.dsmz.de/rest/medium/588) | `glucose (50 ml of a 10% solution), and PIPES (100 ml of 400 mM solution, 12.096 g/100 ml)` | Reconcile the separately prepared glucose/PIPES additions and 850 ml basal water. Do not flatten stock compositions. |
| [623](https://mediadive.dsmz.de/rest/medium/623) | `Reduce the medium with a sterile Na2S stock solution to give a final concentration of 0.5 g/l.` | Verify representation of the late sulfide addition; do not invent its stock strength or dose. |
| [648](https://mediadive.dsmz.de/rest/medium/648) | `Complete the medium by adding glucose, cysteine, and sulfide from sterile anoxic stock solutions` | Resolve glucose, reducers and carbonate as separately prepared additions, not a single autoclaved mixture. |
| [650](https://mediadive.dsmz.de/rest/medium/650) | `Add 20 mM pyruvate after autoclaving.` | Check the complete record for this addition and its exact chemical form before accepting a complete-formulation claim. |
| [659](https://mediadive.dsmz.de/rest/medium/659) | `After autoclaving add a lactose solution (sterilized by filtration) up to a concentration of 8.0 g/l, and 1.2 ml 1M CaCl2` | Distinguish lactose final concentration, unknown lactose stock dose and the explicit calcium-stock dose. |
| [673](https://mediadive.dsmz.de/rest/medium/673) | Recipe sulfur row: `amount: 5`, `unit: g`; preparation says `sulfur (10 g)` | Resolve the table/preparation conflict using the original recipe; also inspect separately prepared yeast extract and sulfide. |
| [696](https://mediadive.dsmz.de/rest/medium/696) | `After sterilization add 5% bovine serum.` | Establish the percentage basis and representation of the serum before accepting final-medium scope. |
| [752](https://mediadive.dsmz.de/rest/medium/752) | `Add 20-30 ml of a sterile 10% Na2CO3 solution` | Distinguish liquid and agar formulations, the stated dose range and pH endpoint. |
| [762](https://mediadive.dsmz.de/rest/medium/762) | `Prepare the Na2CO3 and NaHCO3 in 100 ml water, sterilise separately and add to the cooled medium.` | Reconcile the carbonate stock and 900 ml basal water; do not infer an unstated final volume. |

The excerpts are short substrings for triage, not replacements for the full
preparation paragraphs. Consult the exact captured JSON paths under
`data.solutions[].steps[]` and the complete target before a guarded change.

## Additional Context

- Stock/preparation boundaries also require attention in 582, 587, 593, 615,
  620, 631, 670, 677, 694, 695, 729, 750 and 785. Medium 615 declares a
  provider volume of 1004 ml while including multiple liquid inputs; this is
  not a measured final volume. Medium 631 uses two agar layers with different
  strengths. Medium 694 supplies carbon by evaporation, not a fixed liquid dose.
- Medium 675 prepares a soil extract; 781 prepares an extract separately before
  adding a specified portion. Extraction input masses/volumes must not become
  final-medium concentrations. Unknown extraction yield stays unknown.
- Optional or state-dependent agar in 593, 595, 627, 654, 669, 699, 729, 752,
  782 and 785 requires exact physical-state/variant review. The 669 API row
  contains a 15 g amount and 3 g/L rate; do not choose one automatically.
- Agar rows in 656 and 658 have the previously identified 20 g / 15 g/L API
  conflict. The [original-recipe investigation](../20261007-solutions-water-ph-adjustments/agar-original-source-handoff.md)
  supports 15 g batch inputs, not a proof of final-volume concentrations.
- Medium 782 describes a preparation pH followed by a post-autoclave pH shift;
  those stages are not necessarily a source/local pH conflict. Its optional
  agar range must not be replaced by a single default.
- Branded nutrients, chemical mappings, legacy oxygen annotations and duplicate
  links remain unreviewed by this context screen. A simple preparation does not
  by itself approve any proposed concentration.

Next: read all complete candidate records and source recipes; decide which
claims can retain exact provider-declared scope and which need explicit
withholdings or structural follow-up. Preserve these initial findings rather
than treating a green schema result as scientific acceptance.
