# CultureMech Stock-Solution Recovery Template

A **structural** deep-research prompt for the flattened-cocktail repair (#150).
It does not look for organisms (`media_growth_research.md`) and does not audit the
whole formulation (`media_recipe_validation.md`). It asks for exactly two facts that
the corpus cannot supply and MediaDive does not serve for this record.

## The defect being repaired

This medium's `ingredients` list contains trace-element and/or vitamin entries at
**stock-solution strength** — concentrations that are implausible as final
per-litre values (e.g. ZnSO4 at 22 g/L, where a real medium uses ~0.02 g/L). They
were flattened out of a stock solution during import: the stock's components were
written straight into the ingredient list, and the *volume at which the stock is
added* was lost.

Repairing it needs the stock nested back under a `solutions:` entry with its
addition volume, so the true final concentration is recoverable as:

    final_concentration = stock_concentration x addition_volume / stock_prepared_volume

For most media this comes from MediaDive's API. **For this record it cannot**: its
source id has no trustworthy MediaDive counterpart, so the two numbers must come
from the literature or the culture-collection catalogue instead.

## Target Medium

- **Record path:** {record_path}
- **CultureMech ID:** {media_id}
- **Name:** {media_name}
- **Original/source name:** {original_name}
- **Category:** {category}
- **Physical state:** {physical_state}
- **Media term (source catalogue reference):** {media_term}
- **Synonyms:** {synonyms}
- **Conditions:** {conditions}
- **Target organisms:** {target_organisms}
- **Notes / provenance:** {notes}

### Full ingredient list as currently recorded (SUSPECT — see above)

{ingredients}

### Solutions currently recorded

{solutions}

## What to determine

### 1. Which named stock solution(s) do the stock-strength entries belong to?

Many are standard, reused formulations with published names — "Trace element
solution SL-10", "Wolfe's mineral elixir", "Wolin's vitamin solution", "Seven
vitamins solution", "Pfennig's trace elements", "Hutner's basal salts", "f/2 trace
metals", "Bold's Basal Medium trace elements". Identify the specific one **this
medium** uses, by name, as published for this medium.

For each stock solution, report its **full composition** as published: every
component with its amount and unit, and the total volume the stock is prepared in
(commonly 1 L).

### 2. At what volume is each stock added to the final medium?

The single most important number. Report it as **volume per litre of final medium**
(e.g. "1 ml/L", "10 ml/L"). State it exactly as the source gives it, and give the
source's own wording in the snippet.

**Do not confuse** the addition volume with the volume the stock is *prepared* in.
"Dissolve in 1000 ml, then add 1 ml per litre of medium" contains both: the addition
volume is 1 ml/L, the preparation volume is 1000 ml.

## Evidence requirements

- Prefer the **original publication describing this medium**, or the culture
  collection's own medium sheet (DSMZ, JCM, ATCC, CCAP, NBRC).
- Every number must carry a citation (DOI, PMID, or catalogue URL) and a short
  verbatim snippet showing where it came from.
- Give the concentration **as printed in the source**; do not convert units.
- If the source states the stock composition but NOT the addition volume, say so
  explicitly rather than inferring a typical value. A plausible-looking invented
  volume is worse than an acknowledged gap — it would be applied to a real recipe.
- If this medium's identity is ambiguous (several published media share the name),
  report the ambiguity and what distinguishes them instead of choosing one.

## Output format

Return a YAML block, then prose discussion.

```yaml
medium: {media_name}
culturemech_id: {media_id}
identity_confidence: high | medium | low   # is this the same medium as the record?
identity_notes: <what confirmed or complicated the identification>
stock_solutions:
  - name: <published stock solution name>
    addition_volume: <e.g. "1 ml/L">        # omit entirely if not found
    addition_volume_found: true | false
    prepared_in: <e.g. "1000 ml">
    composition:
      - compound: <name as printed>
        amount: <number>
        unit: <g | mg | ml | ...>
    citation: <DOI / PMID / URL>
    snippet: <verbatim sentence carrying the volume and/or composition>
unresolved:
  - <anything the sources did not settle>
```

Report `addition_volume_found: false` and omit `addition_volume` whenever the
sources do not state it. That case is a useful result, not a failure.
