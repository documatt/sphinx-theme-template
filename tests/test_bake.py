"""
Tests if generating template works.
"""

import difflib
import os
import subprocess
from pathlib import Path

from copier import run_copy
from deep_dircmp import DeepDirCmp

PROJECT_ROOT = str(Path(__file__).parent.parent)

# Sync with the date in tests/test_bake/defaults/CHANGELOG.md
# FROZEN_TEST_DATE = "2025-01-25"


def deep_compare_dirs(
    left: Path, right: Path, diff_files=[], left_only=[], right_only=[]
):
    """Compare dirs recursively, including file content, and ignore .pickle and .doctree files."""
    cmp = DeepDirCmp(left, right)

    def ignored_names(name):
        # binary or files which always differ
        ignored_names = [".pickle", ".doctree", ".doctrees", ".copier-answers.yml"]
        return not any(name.endswith(ignored) for ignored in ignored_names)

    def get_diff_files(cmp):
        """Filter out files based on the ignored names list."""
        diff_files = list(filter(ignored_names, cmp.get_diff_files_recursive()))

        # show diff of diff_files
        for file in diff_files:
            show_diff(cmp.left / file, cmp.right / file)

        return diff_files

    def get_left_files(cmp):
        return list(filter(ignored_names, cmp.get_left_only_recursive()))

    def get_right_files(cmp):
        return list(filter(ignored_names, cmp.get_right_only_recursive()))

    assert get_diff_files(cmp) == diff_files, "Different file contents"
    assert get_left_files(cmp) == left_only, "Left only files"
    assert get_right_files(cmp) == right_only, "Right only files"


def shallow_compare_dirs(dir1, dir2):
    def get_files(directory):
        file_set = set()
        for root, _, files in os.walk(directory):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                file_set.add(relative_path)
        return file_set

    files_in_dir1 = get_files(dir1)
    files_in_dir2 = get_files(dir2)

    assert files_in_dir1 == files_in_dir2


def show_diff(file1: Path, file2: Path):
    """Show the diff between two files."""
    with open(file1, "r") as f1, open(file2, "r") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    diff = difflib.unified_diff(
        f1_lines, f2_lines, fromfile=str(file1), tofile=str(file2)
    )
    for line in diff:
        print(line, end="")


def copier_copy(workaround_tmp_path):
    """Run copier to generate the project."""
    run_copy(
        PROJECT_ROOT,
        workaround_tmp_path,
        # ! When running test locally (on dirty repo), add vcs_ref="HEAD" to run_copy()
        vcs_ref="HEAD",
        data={
            "project_name": "Sphinx Minimal Theme",
            "project_slug": "sphinx_minimal_theme",
            "description": "Minimal but full-fledged three-column docs theme.",
            "sample_docs_slug": "sample_docs",
        },
    )


def test_defaults(workaround_tmp_path: Path, datadir: Path):
    """Compare the contents of the "copier copy" with the expected contents in the test data directory."""

    # *** Arrange ***

    # *** Act ***
    copier_copy(workaround_tmp_path)

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "defaults")


def test_nox_build(workaround_tmp_path: Path):
    """Tests that `nox -s build` in the generated project does NOT crash."""
    # *** Arrange ***

    # *** Act ***
    copier_copy(workaround_tmp_path)

    # *** Assert ***
    subprocess.run(["nox", "-s", "build"], cwd=workaround_tmp_path, check=True)
