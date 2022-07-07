from converter.converter import *
from converter.input import *
from converter.output import *

def process_files(input_filepath, output_filepath) -> None:
  """
  Read the TXT file with prefix expressions, convert them into postfix
  expressions, and write the postfix expressions into another TXT file.
  :param input_filepath: the path to the input TXT file
  :param output_filepath: the path to the output TXT file
  """

  # Run the input function.
  prefix_list = input(input_filepath)

  # Define an empty list for postfix expressions.
  postfix_list = []

  # Run the converter function with the Stack class line by line.
  for prefix_array in prefix_list:
    postfix_array = converter(prefix_array)
    postfix_list.append(postfix_array)

  # Run the output function.
  output(postfix_list, output_filepath)