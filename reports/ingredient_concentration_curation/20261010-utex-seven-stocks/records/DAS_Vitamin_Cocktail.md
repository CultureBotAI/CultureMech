# UTEX Stock Ingredient Follow-Up

- Record: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
- ID: CultureMech:015445
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; source and mapping limitations retained explicitly
- Input SHA256: f32d5d9b26f17279871214fbf46cdb08de779c8661b2d09011c59e5cd14ec4bf
- Result SHA256: d143385b1f41d48d17049fd88e9389975dedd8349fdaad2d5b3c27cb795a67be
- Record kind: SolutionRecipe; category and permanent identifiers unchanged
- Source: https://utex.org/products/das-vitamin-cocktail
- Source capture SHA256: 3c99e1a28bf0d43c1e4fcc2956b2ab5f739c5018068852f1754d6d1dde4be021

| Original field / ingredient | Current field | Old amount | Current amount | Disposition | Exact source evidence | Action / calculation |
| --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration / Tricine (pH 8) | composition[0].concentration | {"unit": "G_PER_L", "value": "9.0"} | {"unit": "G_PER_L", "value": "9.0"} | evidence_only | {"basis_snippet": "For 100 mL Total", "locator": "formulation table row 1; Amount column and volume heading", "reference": "https://utex.org/products/das-vitamin-cocktail", "snippet": "0.9 g/100 mL", "source_component": "Tricine(adjust to pH 8)(Sigma T 5816-256)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "0.9 g / 0.1 L = 9.0 g/L; explicit total volume."} |
| composition[1].concentration / Thiamine (Vitamin B1) | composition[1].concentration | {"unit": "G_PER_L", "value": "0.67"} | {"unit": "G_PER_L", "value": "0.67"} | evidence_only | {"basis_snippet": "For 100 mL Total", "locator": "formulation table row 2; Amount column and volume heading", "reference": "https://utex.org/products/das-vitamin-cocktail", "snippet": "0.067 g/100 mL", "source_component": "Thiamine(Sigma T 1270)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "0.067 g / 0.1 L = 0.67 g/L; explicit total volume."} |
| composition[2].concentration / Biotin | composition[2].concentration | {"unit": "G_PER_L", "value": "0.01"} | {"unit": "G_PER_L", "value": "0.01"} | evidence_only | {"basis_snippet": "For 100 mL Total", "locator": "formulation table row 3; Amount column and volume heading", "reference": "https://utex.org/products/das-vitamin-cocktail", "snippet": "0.001 g/100 mL", "source_component": "Biotin(Sigma B 4639)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "0.001 g / 0.1 L = 0.01 g/L; explicit total volume."} |
| composition[3].concentration / Vitamin B12 (Cobalamin) | composition[3].concentration | {"unit": "G_PER_L", "value": "0.008"} | {"unit": "G_PER_L", "value": "0.008"} | evidence_only | {"basis_snippet": "For 100 mL Total", "locator": "formulation table row 4; Amount column and volume heading", "reference": "https://utex.org/products/das-vitamin-cocktail", "snippet": "0.0008 g/100 mL", "source_component": "Vitamin B12(add after autoclaving)(Sigma V 6629)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "0.0008 g / 0.1 L = 0.008 g/L; explicit total volume."} |
| composition[4].concentration / Pantothenate (Pantothenic acid) | composition[4].concentration | {"unit": "G_PER_L", "value": "0.02"} | {"unit": "G_PER_L", "value": "0.02"} | evidence_only | {"basis_snippet": "For 100 mL Total", "locator": "formulation table row 5; Amount column and volume heading", "reference": "https://utex.org/products/das-vitamin-cocktail", "snippet": "0.002 g/100 mL", "source_component": "Pantothenate(Sigma P 2250)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "0.002 g / 0.1 L = 0.02 g/L; explicit total volume."} |
| composition[5].concentration / PABA (Para-aminobenzoic acid) | composition[5].concentration | {"unit": "G_PER_L", "value": "0.04"} | {"unit": "G_PER_L", "value": "0.04"} | evidence_only | {"basis_snippet": "For 100 mL Total", "locator": "formulation table row 6; Amount column and volume heading", "reference": "https://utex.org/products/das-vitamin-cocktail", "snippet": "0.004 g/100 mL", "source_component": "PABA(p-aminobenzoic acid)(Sigma A 1174)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "0.004 g / 0.1 L = 0.04 g/L; explicit total volume."} |

## Supplied Chemical Forms

| Field | Old identity | Current identity | Identity sources / snippets |
| --- | --- | --- | --- |
| composition[1] | {"id": "CHEBI:18385", "label": "thiamine(1+)"} | {"id": "CHEBI:49105", "label": "Thiamine hydrochloride"} | [{"locator": "Product T1270 heading; CAS 67-03-8 and InChIKey DPJRMOMPQZCRJU-UHFFFAOYSA-M separately inspected", "reference": "https://www.sigmaaldrich.com/CA/en/product/sigma/t1270", "snippet": "Thiamine hydrochloride"}, {"locator": "Formula field", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:49105", "snippet": "C12H17N4OS.Cl.HCl"}] |
| composition[4] | {"id": "CHEBI:7916", "label": "pantothenic acid"} | {"id": "CHEBI:31345", "label": "Calcium D-(+)-pantothenate"} | [{"locator": "Section 1.1, page 1; formula and CAS in section 3.1, page 2", "reference": "https://www.sigmaaldrich.com/US/en/sds/SIGMA/P2250", "snippet": "D-Pantothenic acid hemicalcium salt"}, {"locator": "Formula field", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:31345", "snippet": "2C9H16NO5.Ca"}] |
| composition[5] | {"id": "CHEBI:17836", "label": "4-aminobenzoate"} | {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"} | [{"locator": "Formula and conjugate-acid relationship to CHEBI:17836", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:30753", "snippet": "C7H7NO2"}] |

## Preparation And Stock Context

{"explanation": "Supports the preparation, storage and concentration-stage corrections in notes; sterilization contradiction is unresolved. Separate source excerpts (Directions/table headings/footnote): 'approximately 85 mL'; 'Adjust the pH to 8.0.'; 'Bring total volume to 100 mL'; '0.45 \u00b5m Millipore filter'; 'add after autoclaving'; 'freezer temperature'; 'Stock Solution Concentration'; 'Final Concentration in DAS'", "reference": "https://utex.org/products/das-vitamin-cocktail", "snippet": "approximately 85 mL", "supports": "SUPPORT"}

The applied root notes retain exact preparation and storage scope without invented titrants or exact freezer/refrigerator temperatures.

## Remaining Scope

The B12 table note and filtration directions give contradictory sterilization context. No autoclaving sequence or titrant is invented. Printed stock/receiving molarities are not independently verified here. The P2250 identity uses the earlier manual SDS inspection documented in the source ledger; fresh PDF/product requests failed. No fresh successful supplier retrieval is asserted.

No organism-medium association or role assignment is added. Numerical mass concentrations are unchanged. All new concentration assertions in this batch are the two source-explicit DAS component-stock strengths; its existing dose fractions are moved to stock descriptors. Bibliographic authors, publication year and DOI remain absent when not established.

## Validation

See [preview](../preview.json), [formatting follow-up](../preview-style.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The proposal passes 28 baseline/proposed schema/strict commands and 99 guard tests. The independent source audit checks all 36 cohort concentration fields and rejects 92 altered proposals. It distinguishes captured-source snippet checks from manual identity-ledger provenance. Application, readback and repeat no-op pass. Missing, running and failed later receipts are not passes.

Report presence does not assert that every source annotation, ontology mapping or preparation conflict is resolved.
