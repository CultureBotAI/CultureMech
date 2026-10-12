# Source Conflicts And Limits

Local issue record only; no public issue was created.

1. **JCM1029 original unavailable.** The captured live response was HTTP 200
   with the requested accession and "Nothing found", not a parser-only error.
   The separate diagnostic and official dataset captures are pinned in the
   predecessor's `next-330-*` receipts. Dataset agreement does not verify the
   original final volume. Keep DJ1029 and M1093 masses as batch inputs in notes.
2. **Different quantity bases.** DSMZ330's nominal 1003 ml differs from the
   1003.6 ml arithmetic sum of its liquid inputs. MediaDive's g_l fields and
   KOMODO's displayed per-liter fields are different source assertions, not
   interchangeable measured concentrations. No averaging or implicit density.
3. **Variant is not an exact duplicate.** DSM17630 has sixteen changed KOMODO
   rates and an added rumen-fluid row. Null provider pH remains null. The original
   DSMZ strain supplement is context, not evidence to replace the provider row.
4. **KOMODO stock Instructions conflict.** Accessions3032/3131 name medium330
   stocks but themselves point to DSMZ3032/3131. Preserve that conflict; do not
   assert independent DSMZ/MediaDive equivalence or copy neighboring rates.
5. **Stock and reagent boundaries.** Hemin-stock water is make-up water, NaOH
   is a 1 N liquid input, and resazurin input is a 0.1% w/v stock. Seven acid
   input volumes are not supported as percentages or density-derived masses.
6. **Linked VFA scope only.** M1093 -> M124 -> JCM133 supports seven VFA rows,
   not the entire Medium10 recipe. The current JCM1029 access gap remains open.
7. **Chemical grounding scope.** Withdraw copied salt-specific annotations
   for KOMODO's generic Resazurin. Preserve unrelated annotations without
   treating this concentration review as comprehensive ontology recertification.

The proposal addresses supported local defects but does not resolve source
inaccessibility, unknown denominators, all chemical mappings, global merge
failures or the remaining corpus. No invented publication years or authors.
