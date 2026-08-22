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
    type=click.Path(path_type=Path),
    default="data/normalized_yaml",
    help="Input directory with normalized YAML files",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path),
    default="pages/media",
    help="Directory for per-medium HTML pages",
)
@click.option(
    "--index-dir",
    type=click.Path(path_type=Path),
    default="pages",
    help="Directory for the generated index and static assets",
)
@click.option(
    "--template-dir",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Custom template directory",
)
@click.option(
    "--file",
    "source_files",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    multiple=True,
    help="Render exactly this YAML file; repeat to render multiple files",
)
@click.option("--force", is_flag=True, help="Regenerate pages even when fresh")
def render(input_dir, output_dir, index_dir, template_dir, source_files, force):
    """Generate HTML pages from YAML media files."""
    from culturemech.render_media_pages import TEMPLATES_DIR, render_pages

    result = render_pages(
        yaml_dir=input_dir,
        source_files=source_files or None,
        out_dir=output_dir,
        index_dir=index_dir,
        templates_dir=template_dir or TEMPLATES_DIR,
        force=force,
    )
    if result:
        raise click.ClickException("Rendering failed; see diagnostics above")


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
    default="app/umap.html",
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
@click.option(
    "--method",
    type=click.Choice(["pacmap", "umap", "sfdp"]),
    default="pacmap",
    help="2D reducer to use (default: pacmap)",
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
    method,
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
            method=method,
        )
        click.echo(f"\n✓ Success! Visualization saved to: {output}")
        click.echo("\nTo view, open in browser or deploy to GitHub Pages")

    except Exception as e:
        click.echo(f"\n✗ Error: {e}", err=True)
        raise click.Abort() from e


if __name__ == "__main__":
    cli()
