# Create Recipe Skill - Quick Reference

**Skill**: `create-recipe`
**Purpose**: Generate CultureMech YAML records from input data
**Location**: `.claude/skills/create-recipe/`

---

## ✅ **Skill Complete and Ready**

The `create-recipe` skill is now available for creating new growth media or solution records.

---

## 🚀 **How to Use the Skill**

### **In Claude Code**

Just ask naturally:

```
"Create a recipe for LB Broth with 10 g/L tryptone, 5 g/L yeast extract,
and 10 g/L NaCl. pH 7.0, autoclave at 121°C for 15 min."
```

Claude Code will:
1. Parse your input
2. Generate proper YAML structure
3. Assign CultureMech ID
4. Validate against schema
5. Save to correct location

### **Direct Script Usage**

```bash
source .venv/bin/activate

# From JSON file
python scripts/create_recipe_from_input.py \
  --json recipe_data.json \
  --category bacterial

# From command line
python scripts/create_recipe_from_input.py \
  --name "LB Broth" \
  --ingredients '[
    {"name": "Tryptone", "concentration": "10 g/L"},
    {"name": "Yeast extract", "concentration": "5 g/L"}
  ]' \
  --category bacterial \
  --id CultureMech:015432

# Dry run (preview only)
python scripts/create_recipe_from_input.py \
  --json recipe.json \
  --dry-run
```

---

## 📋 **Input Formats**

### **1. JSON File** (Recommended)

```json
{
  "name": "LB Broth",
  "type": "complex",
  "state": "liquid",
  "category": "bacterial",
  "ph": 7.0,
  "ingredients": [
    {"name": "Tryptone", "concentration": "10 g/L"},
    {"name": "Yeast extract", "concentration": "5 g/L"},
    {"name": "NaCl", "concentration": "10 g/L"}
  ],
  "notes": "Standard LB medium"
}
```

### **2. Natural Language** (via skill)

```
"Create M9 minimal medium:
- Na2HPO4: 6 g/L
- KH2PO4: 3 g/L
- NaCl: 0.5 g/L
- NH4Cl: 1 g/L
- Glucose: 4 g/L
pH 7.4"
```

### **3. From Paper/Document**

```
"Create a recipe from this paper:
[paste text or provide PDF path]"
```

---

## 📤 **Output**

### **Generated File**

**Location**: `data/normalized_yaml/{category}/{sanitized_name}.yaml`

**Example**: `data/normalized_yaml/bacterial/LB_Broth.yaml`

**Structure**:
```yaml
name: LB Broth
original_name: LB Broth
category: bacterial
medium_type: COMPLEX
physical_state: LIQUID

ingredients:
  - preferred_term: Tryptone
    concentration:
      value: 10.0
      unit: G_PER_L
  - preferred_term: Yeast extract
    concentration:
      value: 5.0
      unit: G_PER_L

ph_value: 7.0

curation_history:
  - timestamp: 2026-03-15T04:33:23.085095+00:00
    curator: create-recipe-skill
    action: Created new recipe from input data
```

---

## ⚙️ **Options**

| Option | Description | Example |
|--------|-------------|---------|
| `--json` | JSON input file | `recipe.json` |
| `--name` | Recipe name | "LB Broth" |
| `--ingredients` | Ingredients JSON | `'[{"name":"NaCl","concentration":"10 g/L"}]'` |
| `--category` | Recipe category | bacterial, algae, fungal, etc. |
| `--id` | CultureMech ID | CultureMech:015432 |
| `--output` | Output path | `custom/path/recipe.yaml` |
| `--dry-run` | Preview only | (no value needed) |

---

## 🎯 **Categories**

| Category | Description | Example Media |
|----------|-------------|---------------|
| `bacterial` | Bacterial growth media | LB, TSB, M9 |
| `algae` | Algae/cyanobacteria | BG-11, TAP |
| `archaea` | Archaeal media | DSM 120 |
| `fungal` | Fungal/yeast media | YPD, PDA |
| `specialized` | Cross-kingdom | Mixed culture media |
| `solutions` | Stock solutions | 10× PBS, Tris buffer |

---

## 🔍 **Workflow**

### **Complete Workflow**

```bash
# 1. Create recipe (dry run first)
python scripts/create_recipe_from_input.py \
  --json my_recipe.json \
  --dry-run

# 2. Create for real
python scripts/create_recipe_from_input.py \
  --json my_recipe.json \
  --category bacterial

# 3. Validate
just validate-schema data/normalized_yaml/bacterial/My_Recipe.yaml

# 4. Run quality pipeline
just fix-all-data-quality

# 5. Regenerate indexes
just generate-indexes

# 6. Commit
git add data/normalized_yaml/bacterial/My_Recipe.yaml
git commit -m "Add My Recipe medium"
```

---

## 📝 **Examples**

### **Example 1: Simple Medium**

**Input JSON**:
```json
{
  "name": "Nutrient Broth",
  "type": "complex",
  "state": "liquid",
  "ingredients": [
    {"name": "Peptone", "concentration": "5 g/L"},
    {"name": "Beef extract", "concentration": "3 g/L"}
  ]
}
```

**Command**:
```bash
python scripts/create_recipe_from_input.py --json nutrient_broth.json
```

**Output**: `data/normalized_yaml/bacterial/Nutrient_Broth.yaml`

### **Example 2: Agar Plate**

**Input JSON**:
```json
{
  "name": "LB Agar",
  "type": "complex",
  "state": "solid",
  "ingredients": [
    {"name": "Tryptone", "concentration": "10 g/L"},
    {"name": "Yeast extract", "concentration": "5 g/L"},
    {"name": "NaCl", "concentration": "10 g/L"},
    {"name": "Agar", "concentration": "15 g/L"}
  ]
}
```

### **Example 3: Stock Solution**

**Input JSON**:
```json
{
  "name": "10× PBS",
  "category": "solutions",
  "state": "liquid",
  "ingredients": [
    {"name": "NaCl", "concentration": "80 g/L"},
    {"name": "KCl", "concentration": "2 g/L"},
    {"name": "Na2HPO4", "concentration": "14.4 g/L"},
    {"name": "KH2PO4", "concentration": "2.4 g/L"}
  ],
  "notes": "Dilute 1:10 for use"
}
```

---

## ✅ **Validation**

After creating, always validate:

```bash
# Validate schema
just validate-schema data/normalized_yaml/bacterial/New_Recipe.yaml

# Check for issues
just validate-recipes summary
```

---

## 🔧 **Troubleshooting**

### **Issue**: "JSON must include 'name' field"
**Solution**: Add `"name"` to your JSON

### **Issue**: "JSON must include 'ingredients' list"
**Solution**: Add `"ingredients": [...]` array

### **Issue**: "Invalid category"
**Solution**: Use one of: bacterial, algae, archaea, fungal, specialized, solutions

### **Issue**: File already exists
**Solution**: Choose a different name or delete existing file

---

## 🎓 **Tips**

1. **Always dry-run first** to preview output
2. **Provide concentration units** (g/L, mg/L, %, mM, M)
3. **Include pH** when known
4. **Add notes** for preparation details
5. **Cite sources** in notes or references
6. **Validate immediately** after creation
7. **Regenerate indexes** when done

---

## 📚 **Related**

- **Skill definition**: `.claude/skills/create-recipe/skill.md`
- **Schema**: `src/culturemech/schema/culturemech.yaml`
- **ID management**: `manage-identifiers` skill
- **Validation**: `just validate-schema {file}`
- **Indexes**: `just generate-indexes`

---

**Status**: ✅ Skill ready to use!

**Try it**: Ask Claude Code to "Create a recipe for [your medium]"
