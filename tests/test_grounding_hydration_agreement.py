"""An ingredient naming a hydrate must not be grounded to a different hydrate (#278).

Until #275, a wrong grounding was visible by accident: `term.label` held the ingredient
string while `term.id` pointed elsewhere, so `Na2-EDTA x 2 H2O` sat next to a term that is
actually *EDTA disodium salt (anhydrous)*. That mismatch is what surfaced the 413 rows
#275 corrected, and what made #256/#257 findable at all.

#275 sets every label from the ontology, so every label now agrees with its id — including
the wrong ones. The accidental detector is gone. This is its deliberate replacement, and
it compares the thing that is still independent: the ingredient's own `preferred_term`
against the grounded term's label.

Hydration is the tractable case. `#278` tracks the two harder ones (salt-vs-ion, and
element mismatch, which is what CHEBI:86463-for-magnesium was).
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
ROOTS = [REPO / "data" / "normalized_yaml", REPO / "data" / "merge_yaml" / "merged"]

WORD = {"mono": 1, "di": 2, "tri": 3, "tetra": 4, "penta": 5,
        "hexa": 6, "hepta": 7, "octa": 8, "nona": 9, "deca": 10}

# Names whose hydrate CHEBI has no term for. Each is a real mismatch that cannot be
# fixed by regrounding, so it is allowlisted explicitly rather than silently tolerated —
# an empty allowlist and a fuzzy matcher would hide the next real one.
KNOWN_UNGROUNDABLE = {
    "FeSO4 x 6 H2O", "FeSO4・6H2O", "FeSO4·6H2O", "FeSO4 x 5 H2O", "VOSO4 x 5 H2O",
}


def waters(text: str) -> int | None:
    """Waters of crystallisation stated in a string, or None if it says nothing."""
    s = str(text or "")
    if re.search(r"\banhydrous\b", s, re.I):
        return 0
    m = re.search(r"(\d+)\s*H2O", s, re.I)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca)hydrate\b", s, re.I)
    if m:
        return WORD[m.group(1).lower()]
    return None                      # includes a bare "hydrate": unspecified, not a claim


PREFERRED = re.compile(r"^\s*-?\s*preferred_term:\s*(.+?)\s*$")
LABEL = re.compile(r"^\s*label:\s*(.*)$")


def _unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        return s[1:-1].replace("''", "'") if s[0] == "'" else s[1:-1]
    return s


def _mismatches() -> Counter:
    """Line-based, not yaml.safe_load: parsing both corpora costs over two minutes,
    past this suite's budget, and the check needs only preferred_term and the label
    that follows it. The scan runs in a few seconds."""
    found: Counter = Counter()
    for root in ROOTS:
        if not root.is_dir():
            continue
        for path in root.rglob("*.yaml"):
            text = path.read_text(errors="replace")
            if "H2O" not in text and "hydrate" not in text:
                continue
            name = ""
            for line in text.splitlines():
                m = PREFERRED.match(line)
                if m:
                    name = _unquote(m.group(1))
                    continue
                ml = LABEL.match(line)
                if not (ml and name) or name in KNOWN_UNGROUNDABLE:
                    continue
                label = _unquote(ml.group(1))
                wn, wl = waters(name), waters(label)
                if wn is not None and wl is not None and wn != wl:
                    found[(name, label)] += 1
    return found


@pytest.fixture(scope="module")
def mismatches():
    return _mismatches()


def test_no_ingredient_names_a_hydrate_its_grounded_term_contradicts(mismatches):
    assert not mismatches, (
        f"{sum(mismatches.values())} ingredient row(s) name a hydration their grounded "
        f"term contradicts — the class #275 fixed 413 of (#278):\n  "
        + "\n  ".join(f"{n!r} -> {l!r} x{k}" for (n, l), k in mismatches.most_common(15)))


def test_the_detector_actually_detects():
    """Anti-vacuous guard. A parser that silently stops matching would make the check
    above pass forever — the failure mode of #277 and the #272 classifier bug."""
    assert waters("Na2-EDTA x 2 H2O") == 2
    assert waters("EDTA disodium salt (anhydrous)") == 0
    assert waters("cobalt(2+) sulfate heptahydrate") == 7
    assert waters("sodium molybdate dihydrate") == 2
    assert waters("glucose") is None
    assert waters("some hydrate") is None, "an unspecified hydrate is not a claim"


def test_the_allowlist_is_still_needed_and_not_a_dumping_ground():
    """If CHEBI gains these terms, the allowlist should shrink rather than rot."""
    assert len(KNOWN_UNGROUNDABLE) <= 8, "allowlist growing — investigate before adding"
