# Applied Resazurin Stock Identity Follow-Up

- Follow-up target: data/normalized_yaml/bacterial/synthrophomonas_medium.yaml
- ID: CultureMech:001310
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally
- Before SHA256: fa1f1bdc8bab910a1230ded043d4b85d8e3dea2e1da2d9ced1ba7974088e0b8d
- Result SHA256: 868797edcf6faca6d9933a46077a92df3dcf021ef56659f4e887742b5bf1fb0c

This is a narrow identity follow-up, not a fresh full-recipe concentration certification.
All quantity fields, source names, previous snippets, references, preparation and earlier history are unchanged.
The existing report remains canonical; no additional record is counted as covered.

| Field | Old | Current | Decision | DOI/PURL | Exact snippet | Scope and locator |
| --- | --- | --- | --- | --- | --- | --- |
| solutions[0].composition[7].term | {"id": "CHEBI:8806", "label": "Resazurin"} | unknown / not asserted | correct: withdraw unsupported exact identity | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium212.pdf | Sodium resazurin (0.1% w/v)                                      0.50       ml | solutions[0].composition[7].term: Withdrawn unsupported exact primary identity CHEBI:8806. The quoted recipe specifies a sodium-resazurin stock, whereas the local ChEBI snapshot identifies CHEBI:8806 as sodium-free Resazurin (formula C12H7NO4, charge 0; http://purl.obolibrary.org/obo/CHEBI_8806). No replacement chemical identifier or absence of a suitable ontology term is asserted. The source name, 0.0005 L preparation input and all other quantities are preserved. Locator=page 2, Solution A (continued from page 1); accessed=2026-10-09T09:57:33.466267+00:00; text SHA256=b3b7e36e7b4ebcc4df6ee5eecf8f72e8707792782130975b8a810cea11ec4df0; PDF SHA256=b418dfff6502a47f1ae30498518488079a7360c03b5a355fc1d4973bc9557f98. The immutable MIM label-index snapshot (SHA256=a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262) still resolves this exact label to CHEBI:8806 even without the local term. That publication-time identity conflict remains unresolved and needs an upstream mapping review; the resolver and snapshot have not been altered. Live ChEBI lookup was unavailable through the web tool; ontology-form comparison uses the local snapshot. |
| solutions[0].composition[7].concentration | {"unit": "L", "value": "0.0005"} | {"unit": "L", "value": "0.0005"} | verified and preserved | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium212.pdf | Sodium resazurin (0.1% w/v)                                      0.50       ml | 0.50 ml / 1000 = 0.0005 L preparation input, not a final-medium concentration. Same page/stage as the identity claim. |

The existing ingredient evidence entry is extended in place. There are zero new evidence entries, zero new references and one appended codex event for this record.

**Open:** the packaged MIM resolver still returns CHEBI:8806 for this source label. Publication identity is not fixed. No replacement ID or global absence of a suitable ontology term is asserted.

Validation: [preview and source checks](../preview-validation-v2.json), [application/readback/no-op](../apply.json), [post-edit checks](../post-validation.json), [corpus gates](../corpus.json), [adversarial findings](../adversarial-review.md). Only terminal receipts establish outcomes; failures remain disclosed.
