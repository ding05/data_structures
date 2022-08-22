def output(sorted_integer_list: list, output_filepath: str) -> None:
  """
  Write a list of sorted integers into an output DAT file.
  :param postfix_array_list: a list of sorted integers
  :param output_filepath: the path to the output DAT file
  """
  # Open and write the list into the output DAT file.
  with open(output_filepath, 'w') as f:
    for integer in sorted_integer_list:
      f.write(str(integer))
      f.write('\n')

  # Close the output DAT file.
  f.close()

def message(perform_list: list, message_filepath: str) -> None:
  """
  Write a list of the sorts' performance into an output TXT file.
  :param perform_list: a list of strings
  :param output_filepath: the path to the output TXT file
  """
  # Open and write the list into the output TXT file.
  with open(message_filepath, 'w') as f:
    for string in perform_list:
      f.write(string)
      f.write('\n')

  # Close the output DAT file.
  f.close()