from project_slug.toc import add_toc_functions_to_context, has_local_toc


def test_has_local_toc__no_toc():
    assert has_local_toc({}) == ""


def test_has_local_toc__title_only():
    # *** Arrange ***
    title = "Kitchen Sink"
    context = {
        # Intentionally with newlines and spaces
        "toc": f"""<ul>\n  <li>\n     <a class="reference internal" href="#">{title}</a>\n</li>\n</ul>""",
        "title": title,
    }

    # *** Act ***

    # *** Assert ***
    assert has_local_toc(context) is False


def test_added_to_context():
    # *** Arrange ***
    context = {}

    # *** Act ***
    add_toc_functions_to_context(None, None, None, context, None)

    # *** Assert ***
    assert "has_local_toc" in context
