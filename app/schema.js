// CultureMech Browser Schema Configuration
// Defines facets, search fields, and display configuration

window.searchSchema = {
  "title": "CultureMech - Microbial Growth Media Browser",
  "description": "Browse and search culture media recipes and formulations",
  "searchPlaceholder": "Search media by name, organism, ingredient, or application...",

  // Fields to include in full-text search
  "searchableFields": [
    "name",
    "description",
    "target_organism_names",
    "ingredient_names",
    "applications",
    "category",
    "organism_culture_type",
    "organism_ids"
  ],

  // Facets for filtering
  "facets": [
    {
      "field": "category",
      "label": "Category",
      "type": "string"
    },
    {
      "field": "medium_type",
      "label": "Medium Type",
      "type": "string"
    },
    {
      "field": "physical_state",
      "label": "Physical State",
      "type": "string"
    },
    {
      "field": "target_organism_names",
      "label": "Target Organisms",
      "type": "array"
    },
    {
      "field": "ingredient_names",
      "label": "Key Ingredients",
      "type": "array"
    },
    {
      "field": "applications",
      "label": "Applications",
      "type": "array"
    },
    {
      "field": "sterilization_method",
      "label": "Sterilization",
      "type": "string"
    },
    {
      "field": "media_database",
      "label": "Source Database",
      "type": "string"
    },
    {
      "field": "organism_culture_type",
      "label": "Culture Type",
      "type": "string"
    }
  ],

  // Fields to display in results
  "displayFields": [
    {
      "field": "name",
      "label": "Medium",
      "type": "string",
      "primary": true,
      "link": true,
      "linkField": "html_page"
    },
    {
      "field": "category",
      "label": "Category",
      "type": "string",
      "badge": true
    },
    {
      "field": "medium_type",
      "label": "Type",
      "type": "string",
      "badge": true
    },
    {
      "field": "physical_state",
      "label": "State",
      "type": "string"
    },
    {
      "field": "target_organism_names",
      "label": "Organisms",
      "type": "array",
      "color": "blue",
      "maxItems": 3
    },
    {
      "field": "organism_culture_type",
      "label": "Culture Type",
      "type": "string",
      "badge": true
    },
    {
      "field": "num_ingredients",
      "label": "# Ingredients",
      "type": "number"
    },
    {
      "field": "media_database_id",
      "label": "Database ID",
      "type": "string",
      "link": true
    },
    {
      "field": "description",
      "label": "Description",
      "type": "text",
      "truncate": 200
    }
  ],

  // Color scheme for badges
  "colors": {
    "bacterial": "#3b82f6",
    "fungal": "#8b5cf6",
    "archaea": "#f59e0b",
    "specialized": "#10b981",
    "DEFINED": "#059669",
    "COMPLEX": "#dc2626",
    "MINIMAL": "#2563eb",
    "SELECTIVE": "#7c3aed",
    "LIQUID": "#06b6d4",
    "SOLID_AGAR": "#84cc16"
  },

  // Resolver functions for external links
  "linkResolvers": {
    "DSMZ": (id) => `https://mediadive.dsmz.de/medium/${id.split(':')[1]}`,
    "TOGO": (id) => `http://togodb.org/db/medium/${id.split(':')[1]}`,
    "ATCC": (id) => `https://www.atcc.org/products/${id.split(':')[1]}`,
    "NCIT": (id) => `https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=${id.split(':')[1]}`
  }
};

// Dispatch event to notify schema is ready
dispatchEvent(new CustomEvent('searchSchemaReady'));
