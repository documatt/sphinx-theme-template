"""Methods to build the toctree used in the html pages."""

from typing import Any

from bs4 import BeautifulSoup
from docutils.nodes import document
from sphinx.application import Sphinx


def add_toc_functions_to_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: document | None,
) -> None:
    """Add ToC related variables and functions to Jinja context."""

    context["has_local_toc"] = has_local_toc(context)


def has_local_toc(context: dict[str, Any]) -> bool:
    """Whether the current document has some headings."""
    if "toc" not in context:
        return ""

    html = context["toc"]
    toc = BeautifulSoup(html, "html.parser")

    title = context["title"]
    no_toc = BeautifulSoup(
        f'<ul><li><a class="reference internal" href="#">{title}</a></li></ul>',
        "html.parser",
    )

    # compare two BeautifulSoups objects but ignore formatting (newlines etc.)
    # `toc == no_toc` would not work because of the different formatting
    return not (toc.prettify() == no_toc.prettify())
