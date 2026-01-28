# Filename Sanitization for Media YAML Files

## Overview

All media YAML filenames are sanitized to ensure compatibility with:
- Command-line tools
- CSV exports
- Shell scripts
- Cross-platform file systems
- Version control systems

**Original names are preserved in the `original_name` field** within each YAML file.

---

## Sanitization Rules

### Characters Replaced with Underscore (_)

**ALL non-alphanumeric characters except hyphen (-) and period (.) are replaced with underscore (_)**

#### 1. Shell Metacharacters
These cause issues in command-line processing:

| Character | Name | Reason |
|-----------|------|--------|
| `/` | Slash | Path separator (Unix/Mac) |
| `\` | Backslash | Path separator (Windows), escape character |
| `:` | Colon | Drive separator (Windows), special in URLs |
| `*` | Asterisk | Wildcard expansion |
| `?` | Question mark | Wildcard expansion |
| `"` | Double quote | String delimiter |
| `<` | Less than | Input redirection |
| `>` | Greater than | Output redirection |
| `\|` | Pipe | Pipeline operator |
| `'` | Single quote | String delimiter |
| `` ` `` | Backtick | Command substitution |
| `;` | Semicolon | Command separator |
| `&` | Ampersand | Background process operator |
| `$` | Dollar sign | Variable expansion |
| `!` | Exclamation | History expansion (bash) |
| `#` | Hash | Comment character |
| `%` | Percent | Job control, modulo |
| `@` | At sign | Special parameter |
| `^` | Caret | History substitution |
| `~` | Tilde | Home directory expansion |
| `[` `]` | Brackets | Character class wildcards |
| `{` `}` | Braces | Brace expansion |
| `(` `)` | Parentheses | Subshell, command grouping |

#### 2. CSV/Data Format Issues

| Character | Name | Reason |
|-----------|------|--------|
| `,` | Comma | CSV field separator |
| (space) | Space | Requires quoting in shells |
| (tab) | Tab | Field separator in TSV files |
| (newline) | Newline | Record separator |

#### 3. Special Symbols

| Character | Name | Reason |
|-----------|------|--------|
| `+` | Plus | Can cause issues in URLs |
| `=` | Equals | Parameter separator in URLs |

#### 4. Non-ASCII Characters

All non-ASCII characters are replaced (e.g., `°`, `´`, `ñ`, etc.) to avoid encoding issues.

### Characters KEPT

Only these characters are preserved in filenames:
- **Letters**: `a-z`, `A-Z`
- **Numbers**: `0-9`
- **Hyphen**: `-` (safe separator)
- **Period**: `.` (file extension separator)

---

## Examples from Real Data

| Original Name | Sanitized Filename | Characters Replaced |
|---------------|-------------------|---------------------|
| `BACILLUS "RACEMILACTICUS" MEDIUM` | `BACILLUS_RACEMILACTICUS_MEDIUM` | `"` (quotes), ` ` (spaces) |
| `VY/2, REDUCED MEDIUM` | `VY_2_REDUCED_MEDIUM` | `/` (slash), `,` (comma), ` ` (spaces) |
| `VY/2 AGAR` | `VY_2_AGAR` | `/` (slash), ` ` (space) |
| `MRS MEDIUM (pre-reduced)` | `MRS_MEDIUM_pre-reduced` | `(` `)` (parentheses), ` ` (spaces) |
| `PFENNIG'S MEDIUM I` | `PFENNIG_S_MEDIUM_I` | `'` (apostrophe), ` ` (spaces) |
| `C/10 MEDIUM` | `C_10_MEDIUM` | `/` (slash), ` ` (space) |
| `DESULFOVIBRIO (POSTGATE) MEDIUM` | `DESULFOVIBRIO_POSTGATE_MEDIUM` | `(` `)` (parentheses), ` ` (spaces) |
| `LIVER BROTH (Oxoid CM 77)` | `LIVER_BROTH_Oxoid_CM_77` | `(` `)` (parentheses), ` ` (spaces) |
| `CHOPPED MEAT MEDIUM (N2/CO2)` | `CHOPPED_MEAT_MEDIUM_N2_CO2` | `(` `)` (parentheses), `/` (slash), ` ` (spaces) |
| `WILKINS-CHALGREN ANAEROBE BROTH (N2/CO2)` | `WILKINS-CHALGREN_ANAEROBE_BROTH_N2_CO2` | `(` `)` (parentheses), `/` (slash), ` ` (spaces), `-` kept |

---

## Implementation Details

### Filename Format

```
{SOURCE}_{ID}_{SANITIZED_NAME}.yaml
```

Example:
```
DSMZ_9a_VY_2_REDUCED_MEDIUM.yaml
```

Where:
- `SOURCE`: Database source (e.g., DSMZ, TOGO, ATCC)
- `ID`: Medium ID from source database
- `SANITIZED_NAME`: Sanitized version of the medium name
- `.yaml`: File extension

### Additional Processing

After character replacement:
1. **Collapse consecutive underscores**: `A__B` → `A_B`
2. **Remove leading underscores**: `_NAME` → `NAME`
3. **Remove trailing underscores**: `NAME_` → `NAME`

---

## YAML Content Preservation

### original_name Field

The **complete original name with all special characters** is preserved in the `original_name` field:

```yaml
name: VY/2, REDUCED MEDIUM
original_name: VY/2, REDUCED MEDIUM  # ← Original with all special chars
category: imported
medium_type: COMPLEX
# ...
```

### YAML Quoting

The YAML library automatically handles quoting when necessary:

```yaml
# Comma triggers automatic quoting
name: VY/2, REDUCED MEDIUM
# Rendered as: 'VY/2, REDUCED MEDIUM' in YAML output

# Simple names don't need quotes
name: NUTRIENT AGAR
# Rendered as: NUTRIENT AGAR (no quotes needed)
```

---

## Why This Matters

### 1. Command-Line Safety

**Problem**: Unquoted special characters cause errors
```bash
# ❌ FAILS - comma interpreted as command separator
cat DSMZ_9a_VY/2, REDUCED MEDIUM.yaml

# ✅ WORKS - sanitized filename
cat DSMZ_9a_VY_2_REDUCED_MEDIUM.yaml
```

### 2. CSV Export Safety

**Problem**: Commas in filenames break CSV parsing
```csv
# ❌ BREAKS CSV - comma splits into multiple fields
filename,media_id,name
DSMZ_9a_VY/2, REDUCED MEDIUM.yaml,9a,VY/2

# ✅ WORKS - no problematic characters
filename,media_id,name
DSMZ_9a_VY_2_REDUCED_MEDIUM.yaml,9a,"VY/2, REDUCED MEDIUM"
```

### 3. Cross-Platform Compatibility

**Problem**: Windows forbids certain characters in filenames
```
Forbidden on Windows: < > : " / \ | ? *
```

Our sanitization removes all of these.

### 4. Version Control

**Problem**: Special characters can cause issues with Git on different platforms
```bash
# ❌ Can cause issues
git add "MEDIUM (N2/CO2).yaml"

# ✅ Always works
git add MEDIUM_N2_CO2.yaml
```

---

## Code Location

**Implementation**: `src/culturemech/import/mediadive_importer.py`

**Method**: `_sanitize_filename()`

**Documentation**: See method docstring for complete character list and examples.

---

## Testing

To verify sanitization is working:

```bash
# Find files with problematic characters in original names
grep -r "original_name:.*[\",'/()]" kb/media/

# Verify all filenames are clean (should return empty)
find kb/media -name "*.yaml" | grep -E '[,;:|<>?*()'"'"'"`&$!#%@^~\[\]{}+=]'

# Check specific problematic media
cat kb/media/bacterial/DSMZ_9a_VY_2_REDUCED_MEDIUM.yaml | head -3
# Expected output:
# name: VY/2, REDUCED MEDIUM
# original_name: VY/2, REDUCED MEDIUM
```

---

## FAQs

### Q: Why not keep the original filename?

**A**: Original filenames can break command-line tools, CSV exports, and cross-platform compatibility. Sanitization ensures universal compatibility.

### Q: How do I find the original name?

**A**: Check the `original_name` field in the YAML file, or the `name` field (which also contains the original).

### Q: What if two media have names that sanitize to the same filename?

**A**: The filename includes `{SOURCE}_{ID}_` prefix, ensuring uniqueness even if names are similar.

Example:
```
DSMZ_1_NUTRIENT_AGAR.yaml
DSMZ_1a_NUTRIENT_AGAR.yaml  # Different ID = different file
```

### Q: Can I search by original name?

**A**: Yes, use `grep`:
```bash
grep "name: .*VY/2," kb/media/bacterial/*.yaml
```

Or search within YAML content (original names are preserved).

---

## Duplicate Detection

### Implementation

The importer includes **automatic duplicate filename detection**:

```python
# Tracks filenames during import
self.generated_filenames = {}
self.duplicate_count = 0

# Checks before writing each file
if filename in self.generated_filenames:
    logger.warning("⚠️  DUPLICATE FILENAME detected!")
    # Shows which media conflict
    # Warns that file will be overwritten
```

### Example Warning Output

If duplicates are detected, you'll see:

```
⚠️  DUPLICATE FILENAME: bacterial/DSMZ_1_NUTRIENT_AGAR.yaml
   Category: bacterial
   Current medium: DSMZ:1a ('NUTRIENT AGAR')
   Previous medium(s): DSMZ:1
   File will be OVERWRITTEN!

⚠️  DUPLICATE FILENAME SUMMARY
═══════════════════════════════════════════════════════════════
Total duplicate events: 1
Unique filenames with duplicates: 1

Files that were OVERWRITTEN:
───────────────────────────────────────────────────────────────
Filename: bacterial/DSMZ_1_NUTRIENT_AGAR.yaml
  Conflicts: 2 media mapped to same file
    1. DSMZ:1
    2. DSMZ:1a
  → Only the LAST one (DSMZ:1a) was saved!
═══════════════════════════════════════════════════════════════
```

### Why No Duplicates in Practice

The filename format **{SOURCE}_{ID}_{SANITIZED_NAME}.yaml** ensures uniqueness:
- **SOURCE**: Database source (DSMZ, JCM, CCAP, public)
- **ID**: Medium ID from source (unique within source)
- Combination SOURCE+ID is globally unique

**Verification with MediaDive (3,327 media)**:
```bash
$ find kb/media -name "*.yaml" | wc -l
3327

$ find kb/media -name "*.yaml" | sort | uniq | wc -l
3327

✓ All filenames unique!
```

---

## Summary

✅ **All problematic characters replaced with `_` in filenames**
✅ **Original names preserved in YAML `original_name` field**
✅ **Safe for command-line, CSV, cross-platform use**
✅ **Unique filenames via SOURCE_ID_NAME pattern**
✅ **Automatic duplicate detection and warning**
✅ **Tested with 3,327+ media from MediaDive (0 duplicates)**
