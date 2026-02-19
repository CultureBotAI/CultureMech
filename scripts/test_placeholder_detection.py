#!/usr/bin/env python3
"""Test placeholder detection in isolation."""

import re

# Placeholder patterns
PLACEHOLDER_PATTERNS = [
    r'see\s+source',
    r'refer\s+to',
    r'available\s+at',
    r'contact\s+source',
    r'not\s+specified',
    r'unknown',
    r'medium\s+no\.',
    r'composition\s+not\s+available',
    r'proprietary',
]

def is_placeholder(name: str) -> bool:
    """Check if ingredient name is a placeholder."""
    name_lower = name.lower()
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, name_lower, re.IGNORECASE):
            return True
    return False

# Test cases
test_ingredients = [
    "See source for composition",
    "Refer to original paper",
    "NaCl",
    "Yeast extract",
    "Unknown composition",
    "Medium no. 123",
    "Glucose",
    "Composition not available",
]

print("Testing placeholder detection:")
print()
for ing in test_ingredients:
    result = is_placeholder(ing)
    status = "❌ PLACEHOLDER" if result else "✓ VALID"
    print(f"{status:20s} {ing}")
