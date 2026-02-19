"""YAML error detection and fixing for CultureMech recipe files.

Provides progressive fixing strategies for common YAML parsing errors:
- Invalid escape sequences (backslash-x, backslash-u)
- Quote imbalances
- Indentation issues
- Encoding problems
"""

import logging
import re
from typing import List, Tuple
from enum import Enum

import yaml


logger = logging.getLogger(__name__)


class YAMLErrorCategory(Enum):
    """Categories of YAML parsing errors."""
    ESCAPE_SEQUENCE = "escape_sequence"
    QUOTE_IMBALANCE = "quote_imbalance"
    INDENTATION = "indentation"
    ENCODING = "encoding"
    STRUCTURE = "structure"
    UNKNOWN = "unknown"


class YAMLFixer:
    """Progressive YAML error detection and fixing.

    Applies multiple fixing strategies in order:
    1. Escape sequence fixes (hex and unicode patterns)
    2. Quote balancing
    3. Structural repairs

    Each strategy is applied independently and the result is validated.
    """

    def __init__(self):
        """Initialize the YAML fixer."""
        self.fixes_applied = []

    def fix_yaml_content(self, content: str) -> Tuple[str, List[str]]:
        """Apply progressive YAML fixes to content.

        Args:
            content: Raw YAML content string

        Returns:
            Tuple of (fixed_content, list_of_warnings)

        Raises:
            ValueError: If YAML is unfixable
        """
        warnings = []
        fixed_content = content

        # Strategy 1: Fix escape sequences
        fixed_content, escape_warnings = self._fix_escape_sequences(fixed_content)
        warnings.extend(escape_warnings)

        # Try to parse after each fix
        try:
            yaml.safe_load(fixed_content)
            return fixed_content, warnings
        except yaml.YAMLError as e:
            # Continue to next strategy
            logger.debug(f"YAML still invalid after escape sequence fixes: {e}")

        # Strategy 2: Fix quote imbalances
        fixed_content, quote_warnings = self._fix_quote_imbalances(fixed_content)
        warnings.extend(quote_warnings)

        try:
            yaml.safe_load(fixed_content)
            return fixed_content, warnings
        except yaml.YAMLError as e:
            logger.debug(f"YAML still invalid after quote fixes: {e}")

        # Strategy 3: Fix common structural issues
        fixed_content, struct_warnings = self._fix_structural_issues(fixed_content)
        warnings.extend(struct_warnings)

        try:
            yaml.safe_load(fixed_content)
            return fixed_content, warnings
        except yaml.YAMLError as e:
            # Final attempt failed
            category = self.categorize_error(e)
            raise ValueError(f"YAML unfixable ({category.value}): {e}")

    def _fix_escape_sequences(self, content: str) -> Tuple[str, List[str]]:
        """Fix invalid escape sequences in YAML strings.

        Common issues:
        - Hex escapes (not valid in YAML)
        - Unicode escapes in unquoted strings

        Args:
            content: YAML content

        Returns:
            Tuple of (fixed_content, warnings)
        """
        warnings = []
        original = content

        # Fix \xNN hex escape sequences - replace with degree symbol
        # These typically come from PDF parsing failures
        hex_pattern = r'\\x[0-9A-Fa-f]{2}'
        if re.search(hex_pattern, content):
            content = re.sub(hex_pattern, '°', content)
            warnings.append("Replaced \\xNN escape sequences with degree symbol")

        # Fix \uNNNN unicode escapes in unquoted strings
        # YAML requires these to be in quoted strings
        unicode_pattern = r'(?<!")\\u[0-9A-Fa-f]{4}(?!")'
        if re.search(unicode_pattern, content):
            content = re.sub(unicode_pattern, '°', content)
            warnings.append("Replaced \\uNNNN escape sequences with degree symbol")

        if content != original:
            logger.info(f"Applied escape sequence fixes")

        return content, warnings

    def _fix_quote_imbalances(self, content: str) -> Tuple[str, List[str]]:
        """Fix unbalanced quotes in YAML strings.

        This is a best-effort attempt - not all quote issues can be auto-fixed.

        Args:
            content: YAML content

        Returns:
            Tuple of (fixed_content, warnings)
        """
        warnings = []
        # For now, just detect and warn - actual fixing is complex
        # and risks data corruption

        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            # Count unescaped quotes
            single_quotes = line.count("'") - line.count("\\'")
            double_quotes = line.count('"') - line.count('\\"')

            if single_quotes % 2 != 0:
                warnings.append(f"Line {i}: Unbalanced single quotes")
            if double_quotes % 2 != 0:
                warnings.append(f"Line {i}: Unbalanced double quotes")

        return content, warnings

    def _fix_structural_issues(self, content: str) -> Tuple[str, List[str]]:
        """Fix common YAML structural issues.

        - Extra colons in keys
        - Missing spaces after colons
        - Inconsistent indentation

        Args:
            content: YAML content

        Returns:
            Tuple of (fixed_content, warnings)
        """
        warnings = []
        original = content

        # Fix missing space after colon in key: value pairs
        # Look for patterns like "key:value" and fix to "key: value"
        # But be careful not to break URLs or times
        lines = []
        for line in content.split('\n'):
            # Match "key:value" but not "http:" or "12:30"
            if ':' in line and not re.search(r'(https?:|ftp:|[\d]+:[\d]+)', line):
                # Find colons not followed by space
                fixed_line = re.sub(r':([^\s])', r': \1', line)
                if fixed_line != line:
                    warnings.append(f"Added space after colon: {line[:50]}...")
                lines.append(fixed_line)
            else:
                lines.append(line)

        content = '\n'.join(lines)

        if content != original:
            logger.info("Applied structural fixes")

        return content, warnings

    def categorize_error(self, error: yaml.YAMLError) -> YAMLErrorCategory:
        """Categorize a YAML parsing error.

        Args:
            error: YAML error exception

        Returns:
            Error category enum
        """
        error_str = str(error).lower()

        if 'escape' in error_str or '\\x' in error_str or '\\u' in error_str:
            return YAMLErrorCategory.ESCAPE_SEQUENCE
        elif 'quote' in error_str or "'" in error_str or '"' in error_str:
            return YAMLErrorCategory.QUOTE_IMBALANCE
        elif 'indent' in error_str or 'space' in error_str:
            return YAMLErrorCategory.INDENTATION
        elif 'encode' in error_str or 'decode' in error_str or 'utf' in error_str:
            return YAMLErrorCategory.ENCODING
        elif 'mapping' in error_str or 'sequence' in error_str or 'block' in error_str:
            return YAMLErrorCategory.STRUCTURE
        else:
            return YAMLErrorCategory.UNKNOWN

    def load_yaml_file(self, file_path: str) -> Tuple[dict, List[str]]:
        """Load and fix a YAML file.

        Args:
            file_path: Path to YAML file

        Returns:
            Tuple of (parsed_dict, warnings)

        Raises:
            ValueError: If YAML cannot be parsed even after fixes
            FileNotFoundError: If file doesn't exist
        """
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        # Try to fix and parse
        fixed_content, warnings = self.fix_yaml_content(content)

        try:
            data = yaml.safe_load(fixed_content)
            return data, warnings
        except yaml.YAMLError as e:
            category = self.categorize_error(e)
            raise ValueError(f"YAML parsing failed ({category.value}): {e}")
