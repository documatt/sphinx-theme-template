# Welcome to My Documentation!

The following special markup is toctree directive that constitute book's documents into global table of contents.

In this minimal book template there are only three other documents

- {doc}`sample` (file `sample.md`)
- {doc}`sections` (file `sections.md`)
- {doc}`demo` (file `demo.rst`)

```{tip}
You can mix Markdown (.md) and reStructuredText (.rst) markup.
```

```{toctree}
:caption: 'Contents:'
:maxdepth: 2

sample
sections
demo
```

```{note}
Note that documents in `toctree` and `doc` are listed *without* a file extension.
```
