# Reference

## File layout structure

{{ project }} follows a fairly specific file system layout. This standardized structure eases maintenance and switching between multiple projects.

All tasks, like build and preview, are in the [noxfile.py file](#nox-tasks), and this documentation assumes the structure.

```
.
├── build/                  ┐
│   └── <builder>/          | Output files
│       └── <language>/     |
│           └── ...         ┘
├── source/                 ┐
│   ├── _static/            |
│   │   ├── favicon.svg     |
│   │   └── logo.svg        |
│   ├── _templates/         | Sphinx project sources
│   ├── conf.py             | (documents, images, conf.py)
│   ├── index.md            |
│   ├── overview.md         |
│   └── ...                 ┘
├── .gitignore              ┐
├── CHANGELOG.md            |
├── LICENSE                 |
├── noxfile.py              | Meta files
├── package-lock.json       |
├── package.json            |
└── pyproject.toml          ┘
```

The files and folders are for three purposes:

- Sphinx project sources. Regular files found in Sphinx projects like .md, .rst, images, conf.py.
- When built by [tasks](#nox-tasks), output goes to (by default) to `build/`.
- Meta files. Not the documentation itself. Like dependencies in `pyproject.toml`, license, standard `.gitignore`, etc.

Everything except the output directory should be versioned.
