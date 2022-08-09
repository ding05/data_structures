def input_expression(input_expression_filepath: str) -> list:
  """
  Read the input TXT file that contains decoded or encoded expressions
  line by line.
  :param input_expression_filepath: the path to the input TXT file
  :return: a list of string arrays
  """
  # Open and read the input TXT file.
  with open(input_expression_filepath) as f:
    expression_list = f.read().splitlines()

  # Close the input TXT file.
  f.close()

  return expression_list

def input_freq(input_freq_filepath: str) -> dict:
  """
  Read the input TXT file that contains a frequency table line by line.
  :param input_freq_filepath: the path to the input TXT file
  :return: a nested list of characters and their frequencies
  """
  # Open and read the input TXT file.
  with open(input_freq_filepath) as f:
    read_list = f.read().splitlines()

  # Close the input TXT file.
  f.close()

  # Parse the read list. Read the character and its frequency divided by
  #  " - ", convert them into strings and integers respectively, and store
  # them into a dictionary.
  char_freq_dict = {}
  for item in read_list:
    char_freq_dict.update({item.split(" - ")[0]: int(item.split(" - ")[1])})

  return char_freq_dict