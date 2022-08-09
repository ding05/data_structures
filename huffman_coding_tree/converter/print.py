def print_code_info(huffman_dict: dict) -> str:
  """
  Print the Huffman code's information.
  :param huffman_dict: a dictionary of Huffman encoding with the binary tree
  :return: a string of Huffman code's information
  """
  # Use a string to describe a dictionary.
  sorted_encoding_keys = sorted(huffman_dict.keys())
  code_info = "The code is"
  for key in sorted_encoding_keys:
    code_info += " " + key + " = " + huffman_dict[key] + ","
  code_info = code_info[:-1] + "."

  return code_info

def print_space_usage(decoded_list: list, encoded_list: list) -> list:
  """
  Print the space usage before and after encoding
  :param decoded_list: a list of decoded expressions
  :param encoded_list: a list of encoded expressions
  :return: a list of space usage information
  """
  space_info = []
  for decoded in decoded_list:
    decoded_space = len(decoded) * 8
    space_info.append("Space usage before encoding for " + decoded + ": " +
                      str(decoded_space) + " bits.")
  for encoded in encoded_list:
    encoded_space = len(encoded)
    space_info.append("Space usage after encoding for " + encoded + ": " +
                      str(encoded_space) + " bits.")

  return space_info