# Ingredient Concentration Curation

- Record: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
- ID: CultureMech:010255
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Source inspection date: 2026-10-07
- Before SHA256: `ae31883eb13553f605fe3e5db91ac155c7c7f6a0426ebdb2f8cb29f2fd4b6387`
- After SHA256: `63cc467886a9d69742df552b1cb986a3791259fa41a131a94c9a468303697453`

Each source quote is exact; numeric-only snippets are table cells, with identity and units established by the row locator. Source inspection is manual. Unknown final-volume bases are not inferred. The baseline audit remains an immutable historical snapshot.

| Field / ingredient | Before | After | Status / action | Source; snippet; locator | Reason / calculation |
| --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` / R2A broth (DAIGO) (Nihon Pharm. Co.) | {"value": "0.32", "unit": "G_PER_L"} | {"value": "0.32", "unit": "G_PER_L"} | evidence_only / applied | https://www.bacmedia.dsmz.de/pdf/J805; `R2A Broth (DAIGO) (Nihon Pharm. Co.) 0.32 g`; PDF page 1 | PDF page 1, broth row and heading "Final volume: 1000 ml". 0.32 g / 1 L = 0.32 g/L. |
| `ingredients[1].concentration` / Distilled water | {"value": "1.0", "unit": "L"} | {"value": "1.0", "unit": "L"} | evidence_only / applied | https://www.bacmedia.dsmz.de/pdf/J805; `Distilled water 1000.00 ml`; PDF page 1 | PDF page 1, water row. 1000.00 ml / 1000 = 1.0 L preparation water; retain volume unit. |

## Validation

Closed-schema validation passed before writing. See the batch README for post-edit gates and limitations.
