def input(input_filepath: str) -> list:
  """
  Read the input TXT file line by line.
  :param input_filepath: the path to the input TXT file
  :return: a list of string arrays
  """
  # Open and read the input TXT file.
  with open(input_filepath) as f:
    postfix_array_list = f.read().splitlines()

  # Close the input TXT file.
  f.close()

  return postfix_array_list