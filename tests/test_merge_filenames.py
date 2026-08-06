"""Guard merge_recipes' collision-free output filenames (#218).

Keying a merged group's file on its canonical name alone dropped 1,691 of 6,286
records: distinct groups (different ingredient fingerprints) that share a name
overwrote each other, and case-variant names collided on macOS/Windows on top of
that. `unique_filename` disambiguates both; these tests pin that.
"""
from __future__ import annotations

from culturemech.merge.merge_recipes import unique_filename


def test_distinct_names_do_not_collide():
    used: set[str] = set()
    f1, c1 = unique_filename("Nutrient Agar", "aaaa1111", used)
    f2, c2 = unique_filename("LB Broth", "bbbb2222", used)
    assert (f1, c1) == ("Nutrient_Agar.yaml", False)
    assert (f2, c2) == ("LB_Broth.yaml", False)


def test_same_name_different_fingerprint_is_disambiguated():
    """Genuinely different media that share a canonical name must both land."""
    used: set[str] = set()
    f1, c1 = unique_filename("nutrient_agar", "fp111111", used)
    f2, c2 = unique_filename("nutrient_agar", "fp222222", used)
    assert c1 is False and f1 == "nutrient_agar.yaml"
    assert c2 is True and f2 == "nutrient_agar__fp222222.yaml"
    assert f1 != f2


def test_case_variant_names_collide_on_insensitive_filesystems():
    """Foo.yaml and foo.yaml are one file on macOS/APFS and Windows; the second
    must be disambiguated or a case commit silently loses it (the CI-Linux vs
    macOS-commit mismatch that would break the freshness gate)."""
    used: set[str] = set()
    f1, _ = unique_filename("Medium", "fpAAAAAA", used)
    f2, collided = unique_filename("medium", "fpBBBBBB", used)
    assert f1 == "Medium.yaml"
    assert collided is True
    assert f2.lower() != f1.lower()
    assert f2 == "medium__fpBBBBBB.yaml"


def test_three_way_collision_all_distinct():
    used: set[str] = set()
    outs = [unique_filename("x", fp, used)[0] for fp in ("f1111111", "f2222222", "f3333333")]
    assert len(set(o.lower() for o in outs)) == 3, outs


def test_slashes_and_spaces_are_normalized():
    used: set[str] = set()
    f, _ = unique_filename("A/B medium mix", "fp000000", used)
    assert f == "A_B_medium_mix.yaml"
