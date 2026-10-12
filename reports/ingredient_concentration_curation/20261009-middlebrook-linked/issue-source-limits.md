# Resolve Linked Middlebrook Source Limits

Status: open local issue draft. No GitHub issue was created. An ignored-inclusive
search of existing `issue*.md` files under the curation reports found no matching
645a/linked-Middlebrook issue before this draft was added.

## Scientific Limits

- KOMODO and DSMZ report different quantity encodings. The exact KOMODO tables
  and DSMZ batch/stock routes are now preserved separately; no independently
  supported conversion mechanism reconciles them.
- DSMZ 645a specifies 60 micromoles hemin without a volume denominator, 1N
  NAOH without an addition dose, and historical product identifiers. Its family
  link remains `UNCERTAIN`, not parent-plus-only-hemin or an exact duplicate.
- Six strain-modified KOMODO entries have explicit modified-for-strain titles,
  but their displayed ingredient tables do not identify a numerical change.
- Source secondary names can disagree on chemical form. Existing annotations
  are not recertified by matching a display label or copying a nearby record.

Resolution requires an inspectable source for the exact version, ingredient
form and preparation scope, with a persistent identifier and exact excerpt.
Do not invent density, final volume, NaOH dose or an unreported modification.
Review source editions/supplier specifications before changing the amounts or
promoting the uncertain relationship. No organism-growth assertion follows
from these formulation tables alone.

## Retrieval Limit

`live.json` and `live-retry.json` retain later HTTP 403 failures after seven
and eight successful fetches, respectively. The helper's urllib HTTP error was
surfaced by the cache
as `source_cache: ... HTTPError`; that label does not make the failure a local
disk problem. `source-refresh.json` records the earlier all-fourteen HTTP 200
capture, and `cached.json` separately verifies those exact bytes. No blocked
request was bypassed or treated as successful. A future live check should use
normal permitted public access and preserve any new failure as a separate receipt.
