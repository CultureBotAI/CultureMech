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
    "algae": "#10b981",
    "specialized": "#6366f1",
    "defined": "#059669",
    "complex": "#dc2626",
    "minimal": "#2563eb",
    "selective": "#7c3aed",
    "enrichment": "#f97316",
    "differential": "#ec4899",
    "liquid": "#06b6d4",
    "solid_agar": "#84cc16",
    "semisolid": "#a3e635",
    "biphasic": "#c084fc"
  },

  // Resolver functions for external links
  "linkResolvers": {
    "DSMZ": (id) => `https://mediadive.dsmz.de/medium/${id.split(':')[1]}`,
    "TOGO": (id) => `https://togomedium.org/medium/${id.split(':')[1]}`,
    "ATCC": (id) => `https://www.atcc.org/products/${id.split(':')[1]}`,
    "JCM": (id) => `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=${id.split(':')[1]}`,
    "NBRC": (id) => `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=${id.split(':')[1]}`,
    "KOMODO": (id) => `https://komodo.modelseed.org/detail?id=${id.split(':')[1]}`,
    "komodo.medium": (id) => `https://komodo.modelseed.org/detail?id=${id.split(':')[1]}`,
    "NCIT": (id) => `https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=${id.split(':')[1]}`
  }
};

// Dispatch event to notify schema is ready
dispatchEvent(new CustomEvent('searchSchemaReady'));
