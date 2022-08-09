# This file is the entry point into this program when the module is executed
# as a standalone program.

from pathlib import Path
import argparse

from converter.process_files import *

# Argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_freq_filepath", type=str,
                        help="Input Frequency Table File Pathname")
arg_parser.add_argument("input_expression_filepath", type=str,
                        help="Input Expression File Pathname")
arg_parser.add_argument("output_filepath", type=str,
                        help="Output File Pathname")
arg_parser.add_argument("message_filepath", type=str,
                        help="Message File Pathname")
args = arg_parser.parse_args()

input_freq_filepath = Path(args.input_freq_filepath)
input_expression_filepath = Path(args.input_expression_filepath)
output_filepath = Path(args.output_filepath)
message_filepath = Path(args.message_filepath)

# Use the provided input and output TXT file paths.
# Read the input, process the input, and write the output.
process_files(input_freq_filepath, input_expression_filepath, output_filepath,
              message_filepath)