from datetime import date

project = "Sample Docs"
author = "Sample Docs Team"
copyright = f"{date.today().year}, {author}"

html_theme = "sphinx_minimal_theme"

# Due to sphinx-intl issue, we need to explicitly set the locale_dirs to its default value
# https://github.com/sphinx-doc/sphinx-intl/issues/116
locale_dirs = ["locales/"]

html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.svg"

html_theme_options = {"language_switcher": {"en": "English", "ja": "Japanese"}}
