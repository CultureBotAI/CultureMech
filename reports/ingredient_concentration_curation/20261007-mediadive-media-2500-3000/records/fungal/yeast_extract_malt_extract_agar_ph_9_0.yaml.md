# Medium Concentration Review: YEAST EXTRACT-MALT EXTRACT AGAR (pH 9.0)

- Record: data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_ph_9_0.yaml
- ID: CultureMech:010533
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `91bba7292974654b0b65ff83fcf774c77b4ba3523abe4024d3f0c13624612306`
- Proposed/result SHA256: `91bba7292974654b0b65ff83fcf774c77b4ba3523abe4024d3f0c13624612306`
- Source: https://mediadive.dsmz.de/rest/medium/J528
- Source SHA256: 4148e6d5b4220f832eb6f8f2541fbf4690d97bfd9f774a1796db810118bdf0ab
- Retrieved: 2026-10-07T14:36:04.501085+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J528 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Malt extract | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J528 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Glucose | {"unit": "G_PER_L", "value": "4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J528 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J528 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J528 | {<br>                        "step": "Prepare Yeast extract-malt extract agar (ISP-2) (see Medium No. 43). After autoclaving, adjust pH to 9.0 with sterilized 10% Na2CO3 solution."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
