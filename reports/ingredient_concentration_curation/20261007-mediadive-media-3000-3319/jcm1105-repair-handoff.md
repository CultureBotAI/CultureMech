# JCM 1105: Unapplied Structural Repair Handoff

Target: `data/normalized_yaml/bacterial/virgibacillus_merv_medium.yaml`,
ID `CultureMech:002283`. This seventh-pass record was withheld unchanged.
Its baseline/after SHA256 is
`349e8317e227697953c3b6feafc3cba1aabc29c827f35c792803896cb2e311e7`.
Do not rewrite that historical plan or its report when applying a successor.

The complete [official recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1105)
was re-read, including both tables and the following preparation. Capture:
`/tmp/ingredient-media-20261007/JCM_GRMD1105-scope.html`, SHA256
`2c7d8a4ae523578495afb0f7de58f4185a15a9cd5a489e938f46602d714356f8`.
The API's 10 ml denominator is the carbonate dose alone, not the base volume.

## Source-Supported Representation

The first table defines five base inputs. Its following instruction says
**"bring volume to 1.0 L"**. These base concentrations are therefore supported
without assuming a final receiving-medium volume:

| Base ingredient | Source batch mass | Current incorrect direct g/L | Supported base g/L |
| --- | ---: | ---: | ---: |
| Yeast extract | 10.0 g | 1000 | 10 |
| Trisodium citrate trihydrate | 3.0 g | 300 | 3 |
| MgSO4 heptahydrate | 1.0 g | 100 | 1 |
| KCl | 3.0 g | 300 | 3 |
| NaCl | 100.0 g | 10000 | 100 |

For each row, divide its verified grams by the explicit 1.0 L prepared-base
volume. Preserve the source's unusual citrate trihydrate and existing chemical
IDs; amount evidence does not independently verify those mappings.

After autoclaving the base, the second table supplies
**"10% Na2CO3 solution"**, 10.0 ml. Represent this as a separate solution dose
of 0.010 L per recipe batch, not 10 g/L carbonate or an inferred final-medium
mass concentration. The percentage basis is unspecified; preserve it in notes
with the source row, without guessing `PERCENT_W_V` or a carbonate stock g/L.
The existing Na2CO3 node's unsupported 10 g/L quantity must not become a stock
composition quantity merely by relocation.

The current schema allows the existing batch-volume convention
`ConcentrationValue(value, unit: L)` on `SolutionDescriptor.concentration`.
Use an explicitly scoped 1 L base addition and 0.010 L carbonate-stock addition,
with root evidence identifying each solution field. Ingredient-level evidence
belongs on the five base-composition nodes, each with its source row, the separate
makeup excerpt, and calculation. A source-supported unquantified carbonate
composition node may retain identity and notes without a concentration slot.
Do not add unsupported schema keys or a fabricated complete-medium volume.

Retain liquid physical state; the optional agar instruction is not permission
to add agar to this base record. Separate base preparation from the later stock
addition and retain pH readjustment. Existing `high_metal`, mappings, IDs and
unrelated metadata remain outside this repair's evidence scope.

## Guarded Successor Required

Before applying, verify the exact heading, two table boundaries, all rows and
units, complete preparation, source hash, exact tracked path and baseline hash.
Follow the existing stock-boundary repair patterns for round-trip YAML,
whole-record validation, append-only history, preview/apply/readback/no-op,
adversarial source/context fixtures and independent diff inversion.

The successor must be linked into seventh-cohort readback, offline cohort tests,
coverage and the independent semantic-diff audit. Check actual merge-group
retention after the ingredient relocation. This handoff is not an applied
correction, an extra per-record review marker, or a claim that merge gates pass.
