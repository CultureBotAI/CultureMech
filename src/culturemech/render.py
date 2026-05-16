"""
HTML page generator for media recipes.
Converts YAML to browsable HTML using Jinja2 templates.
"""

import argparse
from pathlib import Path
from typing import Optional
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


# CURIE to URL mappings. When a prefix is not present here, ``resolve_curie``
# returns an empty string so the template renders the reference as plain text
# rather than emitting an unusable ``href="CURIE:..."`` link that browsers
# treat as a custom protocol.
CURIE_RESOLVERS = {
    "CHEBI": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{id}",
    "NCBITaxon": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={id}",
    # NCBI BioProject / GenBank / SRA accessions — referenced from media notes.
    "NCBI": "https://www.ncbi.nlm.nih.gov/bioproject/{id}",
    "DSMZ": "https://mediadive.dsmz.de/medium/{id}",
    "TOGO": "http://togodb.org/db/medium/{id}",
    "ATCC": "https://www.atcc.org/products/{id}",
    # Algae culture collections.
    "CCAP": "https://www.ccap.ac.uk/catalogue/strain-{id}",
    "UTEX": "https://utex.org/products/utex-{id}",
    "SAG": "https://sagdb.uni-goettingen.de/detailedList.php?str_number={id}",
    # Ontology terms occasionally cited as references.
    "ENVO": "http://purl.obolibrary.org/obo/ENVO_{id}",
    "FOODON": "http://purl.obolibrary.org/obo/FOODON_{id}",
    "UBERON": "http://purl.obolibrary.org/obo/UBERON_{id}",
    "MEDIADB": "https://mediadb.systemsbiology.net/medium/{id}",
    "NCIT": "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code={id}",
    "PMID": "https://pubmed.ncbi.nlm.nih.gov/{id}/",
    "DOI": "https://doi.org/{id}",
    "mediadive.solution": "https://mediadive.dsmz.de/solution/{id}",
    "mediadive.compound": "https://mediadive.dsmz.de/compound/{id}",
}


class RecipeRenderer:
    """Generate HTML pages for recipes."""

    def __init__(self, template_dir: Optional[Path] = None, output_dir: Optional[Path] = None):
        if template_dir is None:
            template_dir = Path(__file__).parent / "templates"
        if output_dir is None:
            output_dir = Path("pages")

        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Set up Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=select_autoescape(['html', 'xml', 'j2'])
        )

        # Register custom filters
        self.env.globals['resolve_curie'] = self.resolve_curie

    def resolve_curie(self, curie: str) -> str:
        """Convert CURIE to URL, or return empty string for unknown prefixes.

        Returning ``""`` lets the template detect the unresolved case and
        render the reference as plain text instead of emitting an unusable
        ``href="CURIE:..."`` link (browsers treat those as custom protocols).
        """
        if not curie or ':' not in curie:
            return ""
        if curie.startswith(("http://", "https://")):
            # Already a URL — emit as-is.
            return curie
        prefix, id_part = curie.split(":", 1)
        template = CURIE_RESOLVERS.get(prefix)
        if template:
            return template.format(id=id_part)
        # Unknown prefix → no resolvable URL; template renders as plain text.
        return ""

    def _sanitize_filename(self, name: str) -> str:
        """
        Sanitize filename for filesystem compatibility.

        Replaces problematic characters with underscores.
        """
        import re
        # Replace problematic characters with underscores
        sanitized = name.replace(' ', '_')
        sanitized = re.sub(r'[/\\:*?"<>|,\']', '_', sanitized)
        # Remove multiple consecutive underscores
        sanitized = re.sub(r'_+', '_', sanitized)
        # Remove leading/trailing underscores
        sanitized = sanitized.strip('_')
        return sanitized

    def render_recipe(self, recipe_path: Path, kb_dir: Optional[Path] = None) -> Path:
        """Generate HTML page for a single recipe.

        Output layout: ``<output_dir>/<category>/<yaml_stem>.html`` where
        ``category`` is the immediate parent directory of ``recipe_path``
        relative to ``kb_dir`` (e.g. ``algae``, ``bacterial``, ``solutions``).
        Using the YAML *stem* — not the ``name`` field — guarantees a unique
        filename per source YAML (cross-category collisions like
        ``algae/a_medium.yaml`` vs ``bacterial/a_medium.yaml`` and within-
        category collisions like 223 ``Solution_A`` YAMLs all in
        ``bacterial/`` are both resolved).

        ``kb_dir`` defaults to a one-up search if not provided so the CLI's
        single-file mode keeps working without the caller supplying it.
        """
        recipe_path = Path(recipe_path)
        with open(recipe_path) as f:
            recipe_data = yaml.safe_load(f)

        template = self.env.get_template("recipe.html.j2")

        html = template.render(
            recipe=recipe_data,
            source_file=recipe_path.name,
        )

        # Derive `<category>/<stem>.html` from the source path.
        if kb_dir is not None:
            kb_dir = Path(kb_dir).resolve()
            rel = recipe_path.resolve().relative_to(kb_dir)
            category = rel.parts[0] if len(rel.parts) > 1 else ""
        else:
            # Single-file mode: take immediate parent dir name.
            category = recipe_path.parent.name
        stem_safe = self._sanitize_filename(recipe_path.stem)
        output_dir = (self.output_dir / category) if category else self.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{stem_safe}.html"

        output_path.write_text(html)
        return output_path

    def render_all(self, kb_dir: Path) -> list[Path]:
        """Generate HTML pages for all recipes in knowledge base."""
        kb_dir = Path(kb_dir)
        generated = []

        for recipe_file in kb_dir.rglob("*.yaml"):
            try:
                output_path = self.render_recipe(recipe_file, kb_dir=kb_dir)
                generated.append(output_path)
                print(f"✓ Generated {output_path.relative_to(self.output_dir)}")
            except Exception as e:
                print(f"✗ Error rendering {recipe_file}: {e}")

        return generated


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate HTML pages for CultureMech recipes"
    )
    parser.add_argument(
        "recipe_file",
        type=Path,
        nargs="?",
        help="Single recipe YAML file to render"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Render all recipes in the knowledge base"
    )
    parser.add_argument(
        "-i", "--input-dir",
        type=Path,
        default="data/normalized_yaml",
        help="Input directory containing normalized recipe YAML files (Layer 3, for --all)"
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default="pages",
        help="Output directory for HTML pages"
    )
    parser.add_argument(
        "-t", "--template-dir",
        type=Path,
        help="Custom template directory"
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.all and not args.recipe_file:
        parser.error("Must specify either a recipe file or --all")

    renderer = RecipeRenderer(
        template_dir=args.template_dir,
        output_dir=args.output_dir
    )

    if args.all:
        generated = renderer.render_all(args.input_dir)
        print(f"\n✓ Generated {len(generated)} recipe pages in {args.output_dir}/")
    else:
        output_path = renderer.render_recipe(args.recipe_file)
        print(f"✓ Generated {output_path}")


if __name__ == "__main__":
    main()
