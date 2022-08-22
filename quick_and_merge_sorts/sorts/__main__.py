# This file is the entry point into this program when the module is executed
# as a standalone program.

from pathlib import Path
import argparse

from sorts.process_files import *

# Argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_dirpath", type=str,
                        help="Input Directory Pathname")
arg_parser.add_argument("output_dirpath", type=str,
                        help="Output Directory Pathname")
arg_parser.add_argument("message_filepath", type=str,
                        help="Message File Pathname")
args = arg_parser.parse_args()

input_dirpath = Path(args.input_dirpath)
output_dirpath = Path(args.output_dirpath)
message_filepath = Path(args.message_filepath)

# Use the provided input and output TXT file paths.
# Read the input, process the input, and write the output.
process_files(input_dirpath, output_dirpath, message_filepath)