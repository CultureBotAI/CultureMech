"""Audit citation-only successors without exempting canonical recipe content."""

from collections import Counter


def check(before, after, item):
    """Require unchanged recipe fields and append-only claims/history.

    This is a structural successor audit, not fresh scientific source approval.
    The registry pins the reviewed bytes; historical source audits still run.
    """
    allowed = {"references", "evidence", "variants", "curation_history"}
    assert before["id"] == after["id"] == item["id"]
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
    }, "Citation successor changed canonical recipe content"
    delta = Counter()
    for key in allowed:
        old, new = before.get(key, []), after.get(key, [])
        old_count = len(old)
        if key == "references" and item["id"] == "CultureMech:004981":
            # This reviewed DOI/PMC pair identifies Rogosa 1969, not two papers.
            alias = "https://doi.org/10.1128/jb.98.2.756-766.1969"
            assert old == [
                {"reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC284882/"},
                {"reference": alias},
            ]
            assert len(new) == 1
            assert f"Verified alternate native URL={alias}." in new[0]["notes"]
            old = old[:1]
        assert len(new) >= len(old), f"Removed {key}"
        if key == "references":
            for prior, current in zip(old, new, strict=False):
                assert all(current.get(k) == v for k, v in prior.items()), "Rewrote citation"
                assert set(current) - set(prior) <= {"title", "authors", "year", "notes"}
        else:
            assert new[: len(old)] == old, f"Rewrote prior {key}"
        if key != "variants":
            delta["new_" + key] = len(new) - old_count
    assert delta["new_curation_history"] > 0
    references = {entry["reference"] for entry in after.get("references", [])}
    for key in ("evidence", "variants"):
        for entry in after.get(key, [])[len(before.get(key, [])) :]:
            claims = entry.get("evidence", []) if key == "variants" else [entry]
            assert claims, "New variant has no evidence"
            for claim in claims:
                assert claim.get("reference") in references
                assert claim.get("snippet") and claim.get("explanation")
                assert claim.get("supports") in {"SUPPORT", "PARTIAL", "REFUTE"}
            if key == "variants":
                delta["new_evidence"] += len(claims)
    names = [variant["name"] for variant in after.get("variants", [])]
    assert len(names) == len(set(names)), "Duplicate inline variant name"
    return delta
