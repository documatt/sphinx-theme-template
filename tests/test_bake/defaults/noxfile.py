import os
import subprocess
from pathlib import Path

import nox

# *****************************************************************************
# *** Settings ***
# *****************************************************************************

THEME_NAME = "sphinx_minimal_theme"

DOCS_ROOT = "sample_docs"
DOCS_INDIR = os.path.join(DOCS_ROOT, "source")
DOCS_OUTDIR = os.path.join(DOCS_ROOT, "build")

# Sphinx options for both build and preview
SPHINX_OPTS = [
    # Speed up the build by using multiple cores
    "-j",
    "auto",
    # Print traceback
    "-T",
    # Be quiet
    "-q",
]

# Extra options for sphinx-autobuild
AUTOBUILD_OPTS = [
    #  When developing themes, it is recommended to disable Sphinx's incremental build
    "-a"
]

DEFAULT_BUILDER = "html"

DEFAULT_LANGUAGE = "en"

NPM_THEME_INSTALL = ["npm", "install"]
NPM_THEME_BUILD = ["npm", "run", "theme:build"]
NPM_THEME_WATCH = ["npm", "run", "theme:watch"]

# Speed up builds by reusing virtualenvs
nox.options.reuse_existing_virtualenvs = True

# No default sessions when "nox" is run (explicit is better than implicit)
nox.options.sessions = []

# Massively speed up the build by using uv
nox.options.default_venv_backend = "uv"

# *****************************************************************************
# *** Helpers ***
# *****************************************************************************


def get_outdir_path(builder: str, lang: str) -> str:
    """Constructs the output path."""
    return os.path.join(DOCS_OUTDIR, builder, lang)


def get_sphinx_opts(lang: str) -> list[str]:
    """Generate a default list of Sphinx options for a given language."""
    return SPHINX_OPTS + [
        # Set lang
        "-D",
        f"language={lang}",
        # Add the tag for including based on a language
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#including-content-based-on-tags
        "-t",
        f"language_{lang}",
    ]


def get_builder_language(session) -> tuple[str, str]:
    """Get builder and language. Either defaults or from commandline."""
    if session.posargs:
        return session.posargs[0], session.posargs[1]
    else:
        return DEFAULT_BUILDER, DEFAULT_LANGUAGE


def install_dependencies(session, *extra_deps: str):
    """Install project dependencies (theme and docs dependencies, and a theme itself)."""
    # Read dependencies from theme
    deps = nox.project.load_toml("pyproject.toml")["project"]["dependencies"]

    # Read dependencies from sample docs
    docs_pyproject_toml = Path(DOCS_ROOT, "pyproject.toml").resolve()
    docs_deps = nox.project.load_toml(docs_pyproject_toml)["project"]["dependencies"]

    # "-e ." mean install theme itself in editable mode
    session.install(*deps, *docs_deps, "-e", ".", *extra_deps)


def install_and_build_theme(session):
    """Build the theme."""
    session.run(*NPM_THEME_INSTALL, external=True)
    session.run(*NPM_THEME_BUILD, external=True)


def install_and_watch_theme(session):
    """Watch the theme for changes."""
    session.run(*NPM_THEME_INSTALL, external=True)
    # Runs on background
    subprocess.Popen(NPM_THEME_WATCH)


# *****************************************************************************
# *** Nox sessions ***
# *****************************************************************************
# To invoke session(s), use "nox -s <name1>" or "nox -s <name1> <name2>"


@nox.session
def build(session):
    """Build documentation for a builder/language."""
    install_and_build_theme(session)

    install_dependencies(session)

    builder, language = get_builder_language(session)
    session.run(
        "sphinx-build",
        "-b",
        builder,
        DOCS_INDIR,
        get_outdir_path(builder, language),
        *get_sphinx_opts(language),
        # Warning as error
        "-W",
    )


@nox.session
def clean(session):
    """Clean the build directory."""
    session.run("rm", "-rf", DOCS_OUTDIR, external=True)


@nox.session
def preview(session):
    """Build and serve the docs with automatic reload on change."""
    install_and_watch_theme(session)

    install_dependencies(session, "sphinx-autobuild==2024.10.3")

    # Build sample and serve
    builder, language = get_builder_language(session)
    session.run(
        "sphinx-autobuild",
        "-b",
        builder,
        # Sample docs are watched by default
        DOCS_INDIR,
        # But watch also for changes in theme
        "--watch",
        os.path.join("src", THEME_NAME),
        # Output dir as usual
        get_outdir_path(builder, language),
        # Standard Sphinx options
        *get_sphinx_opts(language),
        *AUTOBUILD_OPTS,
    )
