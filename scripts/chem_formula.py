"""Chemical-formula parsing used by the id↔label plausibility gate.

Many CultureMech ingredient labels ARE formulas ("KH2PO4", "MnCl2 x 4 H2O")
rather than prose, so a lexical comparison against an ontology label can never
validate them. Comparing the *element multiset* parsed from the label against
the ontology term's own molecular formula does, and it is exact.

The comparison deliberately tolerates two benign differences:

* **hydration** — "NiCl2 x 6 H2O" grounded to CHEBI's anhydrous "nickel
  dichloride" is an intentional relaxation (the upstream loaders do this via
  ``fuzzy_hydrate``), so an equal non-water skeleton counts as a match.
* **subscript loss** — CultureMech's scraped names sometimes lost their
  subscript glyphs ("NaCO3" for Na2CO3, "ZnCl" for ZnCl2). Identical element
  *sets* with differing counts are reported separately so the name can be
  repaired without condemning a correct grounding.

What it does NOT tolerate is a different element skeleton: "MnCl .4H O"
grounded to 2-hydroxybenzoyl-AMP (C17H18N5O9P) has no manganese and no
chlorine, and is a real error.
"""

from __future__ import annotations

import re

__all__ = [
    "looks_like_formula",
    "parse_formula",
    "parse_ontology_formula",
    "compare_formulas",
    "build_formula_lookup",
]

# semantic-sql predicate carrying the molecular formula in OAK sqlite builds.
_FORMULA_PREDICATE = "chemrof:generalized_empirical_formula"

ELEMENTS = (
    "Ac Ag Al Am Ar As At Au B Ba Be Bh Bi Bk Br C Ca Cd Ce Cf Cl Cm Cn Co Cr Cs Cu "
    "Db Ds Dy Er Es Eu F Fe Fl Fm Fr Ga Gd Ge H He Hf Hg Ho Hs I In Ir K Kr La Li Lr "
    "Lu Lv Mc Md Mg Mn Mo Mt N Na Nb Nd Ne Nh Ni No Np O Og Os P Pa Pb Pd Pm Po Pr Pt "
    "Pu Ra Rb Re Rf Rg Rh Rn Ru S Sb Sc Se Sg Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm Ts "
    "U V W Xe Y Yb Zn Zr"
).split()
_ELEM_RE = re.compile(r"(" + "|".join(sorted(ELEMENTS, key=len, reverse=True)) + r")(\d*)")

# Roman-numeral oxidation states: "Fe(III)PO4" — strip before element parsing,
# otherwise "III" parses as iodine ×3.
_OXSTATE_RE = re.compile(r"\((?:I{1,3}|IV|V|VI{0,3}|IX|X)\)", re.IGNORECASE)
_HYDRATE_TAIL_RE = re.compile(r"[x·・*]\s*(\d*)\s*H2\s*O\s*$", re.IGNORECASE)
_HYDRATE_DOT_RE = re.compile(r"^(.*?)\.\s*(\d*)\s*H2O$", re.IGNORECASE)


def looks_like_formula(name: str) -> bool:
    """True when a label reads as a chemical formula rather than prose.

    Any run of 4+ lowercase letters ("water", "acid", "glucose") means prose;
    formulas are capitalised element symbols with optional digits.
    """
    if not name:
        return False
    core = _HYDRATE_TAIL_RE.sub("", name.strip())
    core = _OXSTATE_RE.sub("", core)
    core = core.replace("(", "").replace(")", "").replace("·", "")
    if not core or len(core) > 30:
        return False
    if re.search(r"[a-z]{4,}", core):
        return False
    return bool(re.match(r"^[A-Z][A-Za-z0-9().·\s]*$", core))


def parse_formula(text: str) -> dict[str, int] | None:
    """Element multiset for a formula string, or None if it doesn't parse.

    Handles parenthesised groups ``(NH4)2``, trailing hydrates ``x 6 H2O`` /
    ``·2H2O``, and Roman oxidation states ``Fe(III)``. Returning None means
    "cannot judge" — callers must not treat that as a mismatch.
    """
    if not text:
        return None
    s = _OXSTATE_RE.sub("", text.strip())
    counts: dict[str, int] = {}

    def add(elem: str, n: int) -> None:
        counts[elem] = counts.get(elem, 0) + n

    m = _HYDRATE_TAIL_RE.search(s)
    if m:
        n = int(m.group(1) or 1)
        add("H", 2 * n)
        add("O", n)
        s = s[: m.start()].strip()
    m = _HYDRATE_DOT_RE.match(s)
    if m:
        n = int(m.group(2) or 1)
        add("H", 2 * n)
        add("O", n)
        s = m.group(1).strip()

    def expand(mo: re.Match) -> str:
        inner, mult = mo.group(1), int(mo.group(2) or 1)
        return "".join(
            e + str(int(n or 1) * mult) for e, n in _ELEM_RE.findall(inner)
        )

    prev = None
    while prev != s and "(" in s:
        prev = s
        s = re.sub(r"\(([A-Za-z0-9]+)\)(\d*)", expand, s)

    s = s.replace(" ", "")
    if not s:
        return counts or None
    pos, seen = 0, False
    while pos < len(s):
        mo = _ELEM_RE.match(s, pos)
        if not mo:
            return None
        add(mo.group(1), int(mo.group(2) or 1))
        pos = mo.end()
        seen = True
    return counts if seen else None


def parse_ontology_formula(formula: str) -> dict[str, int] | None:
    """Element multiset for an ontology molecular formula.

    CHEBI writes adducts and stoichiometry dot-separated with a leading
    multiplier: ``C15H16N4.HCl``, ``2HO.Mg``, ``5H2O.2Na.O3S2``. Formulas
    carrying an ``R`` group or ``*`` are unparseable by design (generic
    structures) and yield None.
    """
    if not formula or "R" in formula or "*" in formula:
        return None
    total: dict[str, int] = {}
    for part in formula.split("."):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^(\d+)(.*)$", part)
        mult, body = (int(m.group(1)), m.group(2)) if m else (1, part)
        sub = parse_formula(body)
        if sub is None:
            return None
        for k, v in sub.items():
            total[k] = total.get(k, 0) + v * mult
    return total or None


def build_formula_lookup(adapter: object):
    """Return ``curie -> molecular formula`` lookup for ``adapter``.

    ``entity_metadata_map()`` costs ~450 ms per term — 280x a ``label()`` call —
    which makes per-row formula checks unusable over a corpus this size. When the
    adapter is a SQL-backed OAK implementation we pull every formula in ONE query
    (~195k rows for CHEBI, well under a second) and serve lookups from a dict.

    Falls back to a cached ``entity_metadata_map`` probe for adapters with no SQL
    engine (in-memory test doubles, non-sqlite backends), so behaviour is
    identical either way — only the cost differs.
    """
    engine = getattr(adapter, "engine", None)
    if engine is not None:
        try:
            from sqlalchemy import text

            with engine.connect() as conn:
                rows = conn.execute(
                    text(
                        "SELECT subject, value FROM statements "
                        "WHERE predicate = :pred AND value IS NOT NULL"
                    ),
                    {"pred": _FORMULA_PREDICATE},
                )
                table = {str(s): str(v) for s, v in rows if s and v}
            if table:
                return lambda curie: table.get(curie, "")
        except Exception:
            pass  # fall through to the per-term probe

    cache: dict[str, str] = {}

    def probe(curie: str) -> str:
        if curie in cache:
            return cache[curie]
        formula = ""
        try:
            meta = adapter.entity_metadata_map(curie) or {}
            for key, val in meta.items():
                if "formula" in key.lower():
                    formula = (val[0] if isinstance(val, list) else val) or ""
                    break
        except Exception:
            formula = ""
        cache[curie] = formula
        return formula

    return probe


def _skeleton(counts: dict[str, int]) -> dict[str, int]:
    """Non-water elements — what actually identifies the compound."""
    return {k: v for k, v in counts.items() if k not in ("H", "O")}


def compare_formulas(label: str, ontology_formula: str) -> str | None:
    """Compare a formula-style label against an ontology molecular formula.

    Returns one of ``MATCH``, ``HYDRATE_RELAXED``, ``SUBSCRIPTS_LOST``,
    ``CONFLICT`` — or None when either side cannot be parsed, meaning the
    comparison is not applicable and the caller must fall back to other checks.
    """
    want = parse_formula(label)
    got = parse_ontology_formula(ontology_formula)
    if not want or not got:
        return None
    if want == got:
        return "MATCH"
    ws, gs = _skeleton(want), _skeleton(got)
    if ws and ws == gs:
        return "HYDRATE_RELAXED"
    if ws and set(ws) == set(gs):
        return "SUBSCRIPTS_LOST"
    return "CONFLICT"
