# DSMZ 12 Extraction-Scope Finding

- Follow-up target: data/normalized_yaml/bacterial/soil_extract_medium.yaml
- ID: CultureMech:000762
- State: repaired by the [explicit extraction follow-up](../20261007-extraction-boundaries/README.md); this finding preserves the pre-repair diagnosis.
- Baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Pre-repair record SHA256: `2eb2abc4d5b320861afa1894261eedaefcfe56543a29699d2f33086b18949fd5`
- Repaired record SHA256: `fd4c42ebb7018bab05628d40958898adf8933e621c3534627463418adb8d4161`
- Source: https://mediadive.dsmz.de/rest/medium/12
- Source SHA256: `aae1357e31d914ca483bea213eafb7d4a462aa252fc9008b483e42791202bd8b`
- Historical review: [first source pass](../20261007-mediadive-media-0000-0500/records/bacterial/soil_extract_medium.yaml.md)

## Finding

Before repair, `ingredients[0].concentration` was 400 `G_PER_L` for air-dried garden soil.
The source recipe row reports that loading, but its preparation removes solids
before agar is added to the resulting liquid. The exact excerpt
"Centrifuge the supernatant." occurs in
`$.data.solutions[0].steps[0].step`. The existing API response was read in full
and its hash/access metadata verified through the capture reader.
The [original one-page DSMZ 12 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf)
was also downloaded and visually inspected in full on 2026-10-07. It confirms
the separation stage and agar addition per volume of recovered supernatant;
it does not give an extraction yield. PDF SHA256:
`1b4394336f7ace4e09c66fc67ed2e745e3c633b725e436d94335b99289243580`.

The evidence appended by the first pass called this a provider-declared
main-recipe concentration without explicitly limiting it to extraction input.
That wording must not be treated as support for a finished-medium soil
concentration, dissolved yield, or a working stock dose. Its exact numerical
match and literal snippet survive read-back, but those checks do not prove the
preparation-stage interpretation. This is a major scientific-scope issue, not
a schema failure or a missing citation.

## Correction Applied

The [hash-linked plan](../20261007-extraction-boundaries/plan.json) now separates
the extraction inputs from agar addition. It withdraws the soil concentration,
preserves the 400 g starting mass in notes, corrects starting water to 1 L, and
retains agar at 15 g per liter of recovered supernatant. Existing source excerpts
and history remain traceable; a new curation event documents the changed scope.
No extraction yield, recovered volume, or absolute extract dose is inferred.
The original report remains historical without a duplicate `Record` entry.

The reviewer blocks analogous automatic soil/manure support when preparation
describes solids separation. The follow-up also repairs DSMZ 657's extraction
boundary; see [its repair report](../20261007-extraction-boundaries/657.md).
Source-duplicate relationships and secondary chemical mappings are not revalidated
by these concentration repairs.
