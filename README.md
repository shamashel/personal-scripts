# Mike's personal scripts

This repository contains a handful of standalone utilities written for my own use. The focus is on keeping each script lightweight and easy to run.

## Requirements
- Python 3.13
- [Poetry](https://python-poetry.org/) for dependency management

## Provided scripts

### `pdf_splitter.py`
Splits a PDF into smaller documents of a given number of pages (default 300). It relies on the `pypdf` library.

```bash
poetry run python pdf_splitter.py input.pdf --output-dir splits --chunk-size 100
```

### `pdf_expander.py`
Creates larger copies of a PDF by appending raw data so you can test tools with files of increasing size. This script uses only the Python standard library.

```bash
poetry run python pdf_expander.py input.pdf
```

Example flags and more details can be found in `CLAUDE.md`.

## Things to know
1. The project does not include automated tests or CI; run the scripts manually.
2. `pdf_splitter.py` is the only script that requires an external dependency (`pypdf`).
3. `pdf_expander.py` reuses the original PDF content as padding and appends it as comments to keep the files valid.

## Getting started
Install dependencies with:

```bash
poetry install
```

Then run any of the scripts using `poetry run`. Feel free to add new utilities following the same simple approach.


