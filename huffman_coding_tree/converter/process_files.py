from converter.input import *
from converter.output import *
from converter.converter import *
from converter.print import *

def process_files(input_freq_filepath: str, input_expression_filepath: str,
                  output_filepath: str, message_filepath: str) -> None:
  """
  Read the TXT files with decoded or encoded expressions and
  a frequency table, create a huffman encoding tree with the frequency table,
  encoding or decoding the expressions with the tree, and output the encoded
  or decoded expressions and the required messages.
  :param input_freq_filepath: the path to the input TXT file
  :param input_expression_filepath: the path to the input TXT file
  :param output_filepath: the path to the output TXT file
  :param message_filepath: the path to the output TXT file
  """
  # Create a message list for the required printed messages.
  message_list = []

  # Read the files.
  char_freq_dict = input_freq(input_freq_filepath)
  expression_list = input_expression(input_expression_filepath)

  # Create the Huffman encoding tree and encoding dictionary.
  root, tree_info = make_tree(char_freq_dict)
  message_list.append(tree_info)
  huffman_dict = huffman_code_tree(root)
  code_info = print_code_info(huffman_dict)
  message_list.append(code_info)

  # Judge if the expressions are valid.
  # Valid strings to convert: for a decoded expression, only English letters
  # are accepted; for an encoded expression, only 0 and 1 are accepted.
  english_array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
  digit_array = "01 "

  # Check whether the expression list contains decoded expressions, encoded
  # expressions, or invalid expressions.
  decoded_flag = False
  encoded_flag = False
  checked_expression_list = []

  if expression_list[0][0] in english_array:
    decoded_flag = True
    for expression in expression_list:
      # A valid decoded expression should only contain english letters and
      # white spaces.
      # Check whether each expression in the list is valid. If any one is
      # invalid, print a warning message.
      for index in range(len(expression)):
        if expression[index] not in english_array:
          print("Warning: An invalid character detected")
      checked_expression_list.append(expression)

  elif expression_list[0][0] in digit_array:
    encoded_flag = True
    for expression in expression_list:
      # A valid encoded expression should only contain 0 and 1 with possible
      # white spaces.
      for index in range(len(expression)):
        if expression[index] not in digit_array:
          print("Warning: An invalid character detected")
      checked_expression_list.append(expression)

  else:
    print("Error: Invalid input.")

  result_list = []

  # An encoding process
  if decoded_flag == True:
    for decoded_expression in checked_expression_list:
      clean_decoded_expression = clean_decoded(decoded_expression)
      encoded_expression = encode(huffman_dict, clean_decoded_expression)
      result_list.append(encoded_expression)
      space_info = print_space_usage(checked_expression_list, result_list)
      message_list = message_list + space_info

  # A decoding process
  elif encoded_flag == True:
    for encoded_expression in checked_expression_list:
      clean_encoded_expression = clean_encoded(encoded_expression)
      decoded_expression = decode(huffman_dict, clean_encoded_expression)
      result_list.append(decoded_expression)
      space_info = print_space_usage(result_list, checked_expression_list)
      message_list = message_list + space_info

  else:
    result_list = []

  # Run the output function.
  output(result_list, output_filepath)
  output(message_list, message_filepath)