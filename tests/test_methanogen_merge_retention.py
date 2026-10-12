"""Regression for the source-pinned M1038/M781/M3009 grouping collision."""

from pathlib import Path

import pytest
import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger

ROOT = Path(__file__).resolve().parents[1]
PATHS = [
    ROOT / "data/normalized_yaml" / suffix
    for suffix in (
        "archaea/TOGO_M1038_Methanomethylovorans_Uponensis_Medium.yaml",
        "bacterial/TOGO_M781_Geobacter_Daltonii_Medium.yaml",
        "bacterial/modified_bn_medium_for_m08dhb.yaml",
    )
]


def test_actual_candidate_collision_is_split_without_losing_any_recipe_claim():
    matcher = RecipeMatcher()
    assert list(matcher.group_recipes(PATHS).values()) == [PATHS]
    with pytest.raises(ValueError, match="formulation"):
        RecipeMerger().merge_group(PATHS)
    groups = matcher.group_formulations(PATHS)
    assert len(groups) == 3
    for paths in groups.values():
        assert len(paths) == 1
        source = yaml.safe_load(paths[0].read_text())
        merged = RecipeMerger().merge_group(paths)
        for key, value in source.items():
            assert merged[key] == value, (paths[0], key)
    m1038 = yaml.safe_load(PATHS[0].read_text())
    assert len(m1038["solutions"]) == 7
    assert m1038["evidence"] and m1038["references"]
