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

  # Valid strings to convert
  operand_array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                  "0123456789"
  operator_array = "+-*/$"
  valid_string_array = operand_array + operator_array

  # Run the input function.
  prefix_array_list = input(input_filepath)

  # Define an empty list for postfix expressions.
  postfix_array_list = []

  # Run the converter function with recursion line by line.
  for prefix_array in prefix_array_list:

    # Raise a warning of white space:
    if prefix_array.isspace() == True:
      prefix_array = ""
    if " " in prefix_array:
      print("WARNING: There is white space in the array, "
            "which has been automatically removed.")
    prefix_array = prefix_array.replace(" ", "")

    # Raise a warning of illegal characters:
    for element in prefix_array:
      if element not in valid_string_array:
        prefix_array = prefix_array.replace(element, "")
        print("WARNING: There is one illegal character in the prefix array, "
              "which has been automatically removed.")
        # break

    prefix_list = list(prefix_array)
    nested_postfix_list = converter(prefix_list)
    postfix_list = flatten_nested_list(nested_postfix_list)
    postfix_array = "".join(postfix_list)
    postfix_array_list.append(postfix_array)

  # Run the output function.
  output(postfix_array_list, output_filepath)