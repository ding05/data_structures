def output(list: list, output_filepath: str) -> None:
  """
  Write the list of strings into an output TXT file.
  :param postfix_array_list: a list of strings
  :param output_filepath: the path to the output TXT file
  """
  # Open and write the list into the output TXT file.
  with open(output_filepath, 'w') as f:
    for array in list:
      f.write(array)
      f.write('\n')

  # Close the output TXT file.
  f.close()