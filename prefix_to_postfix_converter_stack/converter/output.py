def output(post_list: list, output_filepath: str) -> None:
  """
  Write the list of converted string arrays into an output TXT file.
  :param post_list: a list of the stacks of the converted postfix expressions
  :param output_filepath: the path to the output TXT file
  """
  # Open and write the list into the output TXT file.
  with open(output_filepath, 'w') as f:
      for stack in post_list:
          f.write(stack)
          f.write('\n')

  # Close the output TXT file.
  f.close()