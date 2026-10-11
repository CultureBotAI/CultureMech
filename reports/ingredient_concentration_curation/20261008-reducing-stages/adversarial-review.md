# Adversarial Review Of Five Preparation Repairs

This is a local source/code/data review with mutation tests, not external PR
approval. The reviewed targets are M225, M229, M234, M236 and M243. The frozen
context is SHA256
`dea2ad0d74d2e1b5a2d5f333ce3ebc0fd368f4181aad51fbd7aaca180795ef67`.

## Challenges And Resolutions

| Challenge | Resolution and verification |
| --- | --- |
| A table using 1 L water proves a final 1 L denominator | Rejected. Water remains a batch input in L; mass amounts remain in supported notes. Tests reject both main and stock g/L assumptions. |
| Sum collapsed water or salt as one input | Rejected. M229's 750 ml/1 L water and 20 g/27.7 g NaCl are separate preparation inputs. M236 and M243 each have three water scopes. Independent lineage accounts for every old node; correction counters deduplicate old pointers, including NaCl rather than only water. |
| Self-referencing stock names denote the whole medium | Rejected. Explicit local row-to-table maps select M229 artificial seawater, M236 synthetic seawater and Ni-Se-W stocks, and M243 mineral solutions I/II. Only M142's trace table and M190's vitamin table are inherited. |
| 5% automatically means w/v, or implies a 10 ml dose | Rejected. Eight separate reducing-agent descriptors retain unspecified percentage basis, solvent volume and addition dose. Their 0.5 g child amounts are receiving-batch contributions, not stock-batch recipes. |
| Shared reagents imply shared preparation | Rejected. M229 has medium pH 6.5 and sulfide-stock pH 7.0, without a pressurization instruction. M236 has filtered medium, separately steamed sulfur and later 1 N acid. Only M225/M243 carry their explicitly printed overnight rest. |
| Filtration implies a 0.22 micrometer pore size | Rejected. M236 uses FILTER and exact source prose. No pore size is added. |
| M236's sulfur should become an inferred stock solution | Rejected. Sulfur stays a separately prepared solid with the three-day steaming instruction and its unchanged legacy MIM annotation. |
| A general acid-strength extraction applies to every stage | Rejected. M236 explicitly scopes 1 N H2SO4 to the later readjustment. Neither initial strength nor molarity is invented. |
| Trace-stock pH applies to the receiving medium | Rejected. The KOH reagent and pH 6.5 then 7.0 preparation remain within the trace stock. No M190 whole-medium preparation is inherited. |
| mg can be treated as g, or chemical form can be normalized casually | Rejected. Every numeric table row is corroborated against its bounded original JCM table with an exact form and Decimal amount comparison. Tests inject wrong amounts, ambiguity and altered forms. |
| A valid YAML file proves scientific support | Rejected. An independent audit reconstructs expected membership, notes, quantities and preparation directly from pinned sources and checks attached evidence. The source validator also checks excerpts and titles against fresh matching captures. |
| Partial application or reruns can silently change history | Rejected. Tests mutate the last target, forge the plan and introduce a symlink; no target is written. Applied readback passes and a repeat application changes zero records. Original history/order, IDs, unrelated fields and chemical annotations survive. |

The 149 new tests passed before application. The applied audit accounts for
113 original quantity fields, 222 source rows and 520 claim decisions. It
counts 431 evidence entries, 26 bibliography entries, five history events,
95 removed unsupported quantity fields, 13 corrected stock doses, five water
corrections, 13 additional water fields, 39 relocated old nodes and eight new
reducing-stock descriptors. These categories are not counts of final
concentrations or taxa-media associations.

## Residual Scope

Final preparation volumes and unspecified stock strengths/doses remain unknown;
the repair does not certify legacy ingredient groundings or quality flags.
Missing source authors/year remain absent. Source comments are not generalized
into new taxon-growth claims. Full-corpus merge/freshness failures and the
publication workflow are separate unresolved work. See `validation.json` for
terminal gates; report presence alone does not establish all-record completion.
