"""
Register theme with Sphinx.
"""

from pathlib import Path

from sphinx.application import Sphinx

from . import toc

THEME_NAME = "sphinx_minimal_theme"


def setup(app: Sphinx) -> dict[str, bool]:
    """Setup the Sphinx application."""
    theme_path = str(Path(__file__).parent.resolve())
    app.add_html_theme(THEME_NAME, theme_path)

    app.connect("html-page-context", toc.add_toc_functions_to_context)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
