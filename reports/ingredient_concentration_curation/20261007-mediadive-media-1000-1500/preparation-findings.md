# Preparation-Scope Findings

These are follow-up findings, not additional per-record review entries. The
batch's `records/` directory owns each exact-path report. No unsafe intermediate
preview was applied. Original PDFs were visually inspected in full on 2026-10-07;
the API captures are pinned in the batch plan and source-acquisition snapshot.

## Mutually Exclusive Ingredients

- Follow-up target: `data/normalized_yaml/bacterial/sp4_z_medium.yaml`
- Stable ID: `CultureMech:000510`; DSMZ 1076b.
- Original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1076b.pdf
- PDF SHA256: `c7d8fe10f9be52017dc23eef629faa3098e90766cbd1cb9a482b2f524770a628`
- API: https://mediadive.dsmz.de/rest/medium/1076b
- API SHA256: `ba7de8c83b5f0bbbe374309fe012f6d1a89ac025c939f3c1c887ca647e3ab4ae`

The PDF's urea heading says "For Ureaplasma add instead of Glucose or Arginine".
The API retains that instruction at `$.data.solutions[0].steps[4].step`, but its
urea row has `optional: 0` and no condition. The current record contains both
glucose and urea, and has already linked glucose/arginine source-derived children.
The initial preview proposed four unconditional evidence entries, including
urea. All four are now withheld; the record remains unchanged and its ingredient
claims are conflicts requiring formulation-specific review.

The PDF also distinguishes Yeastolate from the API's Yeast extract label and
includes an arginine alternative absent from its table. The 50% stock basis and
branch representation must be reviewed before correcting concentrations. Do not
create a blended recipe or propagate base evidence to the linked children.

## Stock-To-Medium Ratio

- Follow-up target: `data/normalized_yaml/bacterial/DSMZ_1293_SYMBIOBACTERIUM_THERMOPHILUM_MEDIUM.yaml`
- Stable ID: `CultureMech:000251`; DSMZ 1293.
- Original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1293.pdf
- PDF SHA256: `5e9cd18df6089ab24821d6544807a271b783f2304246c26686439f5b75917d32`
- API: https://mediadive.dsmz.de/rest/medium/1293
- API SHA256: `2bfcd49f86d402605b6d6479d2a6c3579d09c2ebbbc10dc44f66e710fcc2fbb1`

The original PDF states "Final volume: 1000 ml" but also lists 1000 ml distilled
water and instructs "add 1 ml stock solution per 9 ml medium" in step 1. The
3.2% (w/v) bicarbonate stock and this ratio support the stated bicarbonate target,
but the preparation basis of the other ingredients needs reconciliation. Do not
automatically infer a dilution correction or endorse both base and complete
medium concentrations from one table. Three proposed evidence entries are
withheld and the record is unchanged. The PDF's strain-specific gas/pH note is
also absent from the captured API steps; no variant claim is curated here.

## Selected Glucose Branch

- Follow-up target: `data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml`
- Stable ID: `CultureMech:000750`; DSMZ 1286.
- Original recipe: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1286.pdf
- PDF SHA256: `a93ea19c51d16783f76553d0f07ce20c220e4f5571f779ed2c9dbe0231c61b8c`
- API: https://mediadive.dsmz.de/rest/medium/1286
- API SHA256: `7941bf774b7424622a9a5211ce90a369b1938800a9ab334266753fc634da0e49`

The original table says "Glucose (or fructose)" with 0.50 g and lists 1000 ml
water. The captured API and current record both select glucose only, not both
alternatives. The agar concentration and local solid state match the source's
solid-medium instruction. Evidence is limited to that selected formulation;
fructose is not added and its formulation is not implicitly verified.

## Guard Limitations

The new checks recognize explicit incompatible-branch language and explicit
milliliter stock-to-medium mixing ratios. They are rejection guards, not a
general recipe-language parser or proof that all other preparations are valid.
Eleven new regression cases cover rejecting these situations and retaining
ordinary stock addition, specified complete-volume preparation, and nonexclusive
instructions. The independent preflight checks prior accepted records for the
new triggers and preserves all previous data and historical reports.

Other retained follow-ups include source `amount`/`g_l` disagreements, missing
stocks, percent bases, supplier attributes, secondary chemical-form mappings,
and source-only preparation additions. DSMZ 1159 is currently solid, so its
liquid-only CaCO3 omission does not invalidate that row; its agar arithmetic
conflict remains withheld. These source checks do not complete those records.
