#!/usr/bin/env python3
"""
PDF Splitter - Splits PDF documents into chunks of specified number of pages.
Default chunk size is 300 pages.
"""

import os
import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def split_pdf(input_path, output_dir, chunk_size=300):
    """
    Split a PDF into chunks of specified size.
    
    Args:
        input_path: Path to input PDF file
        output_dir: Directory to save output chunks
        chunk_size: Number of pages per chunk (default: 300)
    """
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    base_name = input_path.stem
    
    print(f"Reading {input_path.name}...")
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    
    print(f"Total pages: {total_pages}")
    print(f"Splitting into {chunk_size}-page chunks...")
    
    chunks_created = []
    
    for i in range(0, total_pages, chunk_size):
        start_page = i
        end_page = min(i + chunk_size, total_pages)
        chunk_num = (i // chunk_size) + 1
        
        writer = PdfWriter()
        
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        output_path = output_dir / f"{base_name}_part{chunk_num:03d}.pdf"
        
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        chunks_created.append((output_path, start_page + 1, end_page))
        print(f"Created: {output_path.name} (pages {start_page + 1}-{end_page})")
    
    print(f"\nSummary:")
    print(f"Total pages: {total_pages}")
    print(f"Chunks created: {len(chunks_created)}")
    print(f"Output directory: {output_dir}")
    
    return chunks_created


def main():
    parser = argparse.ArgumentParser(
        description='Split PDF documents into chunks of specified number of pages.'
    )
    parser.add_argument(
        'input_pdf',
        help='Path to the input PDF file'
    )
    parser.add_argument(
        '--output-dir', '-o',
        default='split_output',
        help='Output directory for split PDFs (default: split_output)'
    )
    parser.add_argument(
        '--chunk-size', '-s',
        type=int,
        default=300,
        help='Number of pages per chunk (default: 300)'
    )
    
    args = parser.parse_args()
    
    try:
        split_pdf(args.input_pdf, args.output_dir, args.chunk_size)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()