# Vogel Medium N Source Follow-Up

This is a read-only handoff, not an applied correction or a canonical per-record
review. It adds zero recipe edits, evidence entries or review coverage.

Target: `data/normalized_yaml/bacterial/vogels_medium_n.yaml`,
`CultureMech:007187` / `MEDIADB:287`. All twelve existing ingredient rows were
read. The [earlier source ledger](source-review.json) is preserved unchanged.
The [supplement](source-review-supplement.json) adds the 2006 protocol, rechecks
the target and captures, and pins twelve amount holds and six exact-path
name/citation candidates. The stock-boundary hold is not a new finding.

The earlier ledger records original scan inspection of *Stanford Neurospora
Methods* by N. Murray and D. Perkins, including an explicit fiftyfold dilution
and a separate carbon-source statement. Those notebook methods are labeled
informational and not for citation in publication. Their issue year was not
established from the inspected pages. The HTML version is not a verbatim scan
transcription: it includes a citrate-hydrate alternative, and a separate crossing
medium has a phosphate-table discrepancy. Neither that crossing medium nor
its quantities should be substituted for Medium N.

The official [FGSC recipe](https://www.fgsc.net/methods/vogels.html) separates
a concentrated salt stock, nested trace/biotin stocks and the working-medium
addition. Its volume language and post-stock preservative addition need careful
handling; do not assume an exact final volume from the water input alone.

David D. Perkins's [FGSC protocol, revised 2006-04-18](https://www.fgsc.net/neurosporaprotocols/How%20to%20choose%20and%20prepare%20media.pdf)
independently labels the main recipe as a one-liter 50-fold stock. Page 2 was
rendered and visually inspected, including hydrate formulas and table columns.
Its sucrose alternatives and preservative quantity differ from the HTML recipe.
These are source-version choices, not permission to combine convenient values.

MediaDB cites Vogel's 1964 article, DOI `10.1086/282338`. Publisher metadata was
located, but its original Methods were not retrieved. Neither source-name
similarity nor the large existing ion concentrations approves a numeric repair.
The flat ion representation needs reconciliation with the supplied reagents and
stock stages. A uniform division by fifty would ignore chemical stoichiometry,
hydration and nested-stock contributions.

The name search included hidden and ignored normalized files, then verified exact
git-tracked paths. The other hits are candidates only, not established duplicates
or variants. All normalized data and existing growth claims remain unchanged.

The earlier five-record Kazan thiamine source lead also remains unresolved;
publication metadata and a thesis lead are not ingredient-amount evidence.
