"""
Foo but full-bar theme.
"""

__version__ = "0.1.0"


from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

THEME_NAME = "sphinx_foo_theme"


def setup(app: Sphinx) -> ExtensionMetadata:
    """Setup the Sphinx application."""
    theme_path = str(Path(__file__).parent.resolve())
    app.add_html_theme(THEME_NAME, theme_path)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
