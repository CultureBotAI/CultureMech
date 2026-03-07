"""
CultureMech CLI - Command-line interface for CultureMech tools.
"""

from pathlib import Path

import click


@click.group()
def cli():
    """CultureMech - Microbial Growth Media Knowledge Base"""
    pass


@cli.command()
@click.option(
    "--input-dir",
    type=click.Path(exists=True, path_type=Path),
    default="data/normalized_yaml",
    help="Input directory with normalized YAML files",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path),
    default="docs",
    help="Output directory for HTML pages",
)
@click.option(
    "--template-dir",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Custom template directory",
)
def render(input_dir, output_dir, template_dir):
    """Generate HTML pages from YAML media files."""
    from culturemech.render import main as render_main
    import sys

    # Set up arguments for render module
    original_argv = sys.argv
    sys.argv = [
        "render",
        "--input-dir", str(input_dir),
        "--output-dir", str(output_dir),
    ]
    if template_dir:
        sys.argv.extend(["--template-dir", str(template_dir)])

    try:
        render_main()
    finally:
        sys.argv = original_argv


@cli.group()
def umap():
    """Generate UMAP visualizations of media embeddings."""
    pass


@umap.command()
@click.option(
    "--media-dir",
    type=click.Path(exists=True, path_type=Path),
    default="data/normalized_yaml",
    help="Directory containing media YAML files",
)
@click.option(
    "--embeddings-path",
    type=click.Path(exists=True, path_type=Path),
    required=True,
    help="Path to KG-Microbe embeddings TSV.gz file",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default="docs/media_umap.html",
    help="Output HTML file path",
)
@click.option(
    "--cache-dir",
    type=click.Path(path_type=Path),
    default=".umap_cache",
    help="Directory for caching embeddings",
)
@click.option(
    "--force-reload",
    is_flag=True,
    help="Force reload embeddings from source (bypass cache)",
)
@click.option(
    "--n-neighbors",
    type=int,
    default=15,
    help="UMAP n_neighbors parameter (controls local vs global structure)",
)
@click.option(
    "--min-dist",
    type=float,
    default=0.1,
    help="UMAP min_dist parameter (controls compactness)",
)
@click.option(
    "--min-coverage",
    type=float,
    default=0.5,
    help="Minimum embedding coverage for derived embeddings (0-1)",
)
def generate(
    media_dir,
    embeddings_path,
    output,
    cache_dir,
    force_reload,
    n_neighbors,
    min_dist,
    min_coverage,
):
    """Generate interactive UMAP visualization of media embeddings."""
    from culturemech.visualization.umap_generator import UMAPVisualizationGenerator

    try:
        generator = UMAPVisualizationGenerator()
        generator.generate_both_plots(
            media_dir=media_dir,
            embeddings_path=embeddings_path,
            output_html=output,
            cache_dir=cache_dir,
            force_reload=force_reload,
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            min_coverage=min_coverage,
        )
        click.echo(f"\n✓ Success! Visualization saved to: {output}")
        click.echo(f"\nTo view, open in browser or deploy to GitHub Pages")

    except Exception as e:
        click.echo(f"\n✗ Error: {e}", err=True)
        raise click.Abort()


if __name__ == "__main__":
    cli()
