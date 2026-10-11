# Applied Resazurin Stock Identity Follow-Up

- Follow-up target: data/normalized_yaml/archaea/methanofollis_medium.yaml
- ID: CultureMech:001100
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally
- Before SHA256: e4930e4ceaf68ffbea48767e64811a882c358cb77fb8c5d2dbd866568e23179f
- Result SHA256: 5447dfa3e11fbefc0ffcf979a5aa7978a42c28377ec2ef8fbf58cf551f111909

This is a narrow identity follow-up, not a fresh full-recipe concentration certification.
All quantity fields, source names, previous snippets, references, preparation and earlier history are unchanged.
The existing report remains canonical; no additional record is counted as covered.

| Field | Old | Current | Decision | DOI/PURL | Exact snippet | Scope and locator |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[9].term | {"id": "CHEBI:8806", "label": "Resazurin"} | unknown / not asserted | correct: withdraw unsupported exact identity | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium161.pdf | Sodium resazurin (0.1% w/v)                                        0.50        ml | ingredients[9].term: Withdrawn unsupported exact primary identity CHEBI:8806. The quoted recipe specifies a sodium-resazurin stock, whereas the local ChEBI snapshot identifies CHEBI:8806 as sodium-free Resazurin (formula C12H7NO4, charge 0; http://purl.obolibrary.org/obo/CHEBI_8806). No replacement chemical identifier or absence of a suitable ontology term is asserted. The source name, 0.0005 L preparation input and all other quantities are preserved. Locator=page 1, main formulation; accessed=2026-10-09T08:54:14.964059+00:00; text SHA256=8cc1d165274c4c0ce7a215cbe458c48d9880b183c7d62cbefa2d54e637d7625a; PDF SHA256=0f4ea6194efcb146abe36366dd72ce890643e9cfe39bc947a9df7281959478e0. The immutable MIM label-index snapshot (SHA256=a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262) still resolves this exact label to CHEBI:8806 even without the local term. That publication-time identity conflict remains unresolved and needs an upstream mapping review; the resolver and snapshot have not been altered. Live ChEBI lookup was unavailable through the web tool; ontology-form comparison uses the local snapshot. |
| ingredients[9].concentration | {"unit": "L", "value": "0.0005"} | {"unit": "L", "value": "0.0005"} | verified and preserved | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium161.pdf | Sodium resazurin (0.1% w/v)                                        0.50        ml | 0.50 ml / 1000 = 0.0005 L preparation input, not a final-medium concentration. Same page/stage as the identity claim. |

The existing ingredient evidence entry is extended in place. There are zero new evidence entries, zero new references and one appended codex event for this record.

**Open:** the packaged MIM resolver still returns CHEBI:8806 for this source label. Publication identity is not fixed. No replacement ID or global absence of a suitable ontology term is asserted.

Validation: [preview and source checks](../preview-validation-v2.json), [application/readback/no-op](../apply.json), [post-edit checks](../post-validation.json), [corpus gates](../corpus.json), [adversarial findings](../adversarial-review.md). Only terminal receipts establish outcomes; failures remain disclosed.
