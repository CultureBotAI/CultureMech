# Reference Validator Follow-Up

Tracked in [CultureMech #571](https://github.com/CultureBotAI/CultureMech/issues/571).
The original concentration repair remains tracked separately in #150.

Confirmed local entry point: `project.justfile`, recipe `validate-references`
(line 1293 at the reviewed worktree state). It determines the record target
class, then invokes the installed `linkml-reference-validator validate data`
CLI with the repository schema. The installed version is 0.1.6.

The installed `SupportingTextValidator._split_query` unconditionally performs
`re.sub(r"\[.*?\]", " ", text)` before matching. That explains the loss of
literal `[M190]` from the TOGO JSON excerpt. It is designed for editorial notes
in quotations, which are not the same thing as accession brackets in structured
recipe data. Do not solve this by removing the accession from stored evidence.

The remaining two behaviors need an explicit supported-source strategy:
HTML chemical-subscript extraction differs from the exact rendered-text
captures, and official TOGO JSON title extraction falls back to its URL rather
than `meta.name`. Inspect the installed fetcher/cache and supported extension
API before adding a wrapper or changing the maintained dependency. Do not edit
an installed dependency and mistake that for a reproducible repository fix.

Use hash-pinned captures as offline fixtures. Keep exact source/ingredient
binding, amounts, signs, hydration, units and batch/stock/final context intact.
Negative tests must reject altered amounts and wrong chemicals even when source
formatting is normalized. Do not broadly loosen matching or suppress failures.

The local literal-source audit is independent of the installed reference gate:
206/206 new primary snippets match; 200/206 pass the installed matcher. All
seven actual CLI checks fail, including title mismatches. `reference-validation.json`
records both outcomes without relabeling either one.
