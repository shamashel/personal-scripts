# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal scripts folder containing utilities for various tasks. The main script currently is `pdf_expander.py`, which creates larger PDF files by appending binary data as PDF comments, useful for testing OCR systems with PDFs of increasing file sizes.

## Common Commands

### Running the PDF Expander
```bash
# Basic usage - creates PDFs at 2x, 3x, 5x, 7x, 10x, and 15x sizes
poetry run python pdf_expander.py <input.pdf>

# Custom output directory
poetry run python pdf_expander.py <input.pdf> --output-dir <directory>

# Custom multiplication factors
poetry run python pdf_expander.py <input.pdf> --factors 1.5 4 8 12
```

### Development Setup
```bash
# Install dependencies (though none are actually used)
poetry install
```

## Architecture Notes

The PDF expansion algorithm in `multiply_pdf_size()` works by:
1. Copying the original PDF to preserve structure
2. Calculating additional bytes needed based on multiplication factor
3. Appending data as PDF comments (`%% EXTRA DATA...`) to maintain file validity
4. Reusing portions of original content (minus PDF header) as padding

Key design decision: No external dependencies are used despite `pypdf` being in poetry.lock - the script uses only Python standard library modules (os, argparse, shutil, pathlib).

## Project Notes

This is a personal scripts repository, so formal testing and CI/CD are not required. Scripts are tested manually as needed.