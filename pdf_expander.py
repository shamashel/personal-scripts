#!/usr/bin/env python3
"""
PDF Expander

This script creates larger PDFs by duplicating the raw binary content of an input PDF.
It generates multiple output files with increasing sizes up to approximately 15x the original.
"""

import os
import argparse
import shutil
from pathlib import Path


def multiply_pdf_size(input_path, output_path, multiplier):
    """
    Create a larger PDF by duplicating the raw binary content.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (str): Path where the output PDF will be saved
        multiplier (float): How many times to duplicate the original content
    """
    # First, copy the original file
    shutil.copy2(input_path, output_path)
    
    # Get the original content
    with open(input_path, 'rb') as f:
        content = f.read()
    
    # Calculate how much more content to add
    original_size = len(content)
    target_size = int(original_size * multiplier)
    additional_copies = target_size - original_size
    
    if additional_copies <= 0:
        return
    
    # Append more content to increase file size (while keeping it a valid PDF)
    with open(output_path, 'ab') as f:
        # Add comment section that won't affect PDF rendering
        f.write(b'\n%% EXTRA DATA TO INCREASE FILE SIZE\n')
        
        # Add chunks until we reach desired size
        bytes_to_add = additional_copies
        chunk_size = min(original_size, bytes_to_add)
        
        while bytes_to_add > 0:
            # Use a portion of the original content as padding data
            # (removing the first 8 bytes to avoid PDF header conflicts)
            padding_size = min(chunk_size, bytes_to_add)
            padding_data = content[8:8+padding_size]
            
            # Wrap in PDF comment markers to avoid corrupting the file
            f.write(b'%')
            f.write(padding_data)
            f.write(b'\n')
            
            bytes_to_add -= len(padding_data)
    
    # Get file sizes for reporting
    input_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
    output_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
    
    print(f"Created: {output_path}")
    print(f"  Original size: {input_size:.2f} MB")
    print(f"  New size: {output_size:.2f} MB")
    print(f"  Multiplication factor: {output_size/input_size:.2f}x")
    

def main():
    parser = argparse.ArgumentParser(description="Create larger PDFs by duplicating an input PDF")
    parser.add_argument("input_pdf", help="Input PDF file")
    parser.add_argument("--output-dir", default="output", help="Directory to save output PDFs (default: output)")
    parser.add_argument("--factors", nargs="+", type=float, default=[2, 3, 5, 7, 10, 15],
                        help="Multiplication factors for generating PDFs (default: 2 3 5 7 10 15)")
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Generate PDFs at each specified multiplier
    input_name = os.path.basename(args.input_pdf)
    name, ext = os.path.splitext(input_name)
    
    for factor in args.factors:
        output_path = os.path.join(args.output_dir, f"{name}_x{factor:.1f}{ext}")
        multiply_pdf_size(args.input_pdf, output_path, factor)
    
    print(f"\nAll PDFs generated in: {os.path.abspath(args.output_dir)}")


if __name__ == "__main__":
    main() 