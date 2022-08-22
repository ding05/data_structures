# This package is required for reading filenames in a given directory.
from os import walk

def get_filenames(input_dirpath: str) -> list:
  """
  Read the filenames in the given folder.
  :param input_dirpath: the path to the directory that contains input DAT
  files
  :return: a list of string arrays
  """
  filenames = []

  # Walk through the directories and files in the given directory.
  for (dirpath, dirname, filename) in walk(input_dirpath):
    filenames.extend(filename)
    break

  return filenames

def input(input_filepath: str) -> list:
  """
  Read the input DAT file that contains unsorted integers.
  :param input_filepath: the path to the input DAT file
  :return: a list of unsorted integers
  """
  # Open and read the input DAT file.
  with open(input_filepath) as f:
    # Read the items from the DAT file as the items in a list.
    unsorted_integer_list = f.read().splitlines()

  # Close the input DAT file.
  f.close()

  # If the items in the DAT file is divided by white spaces, split the items
  # by white space.
  if len(unsorted_integer_list) == 1:
    unsorted_integer_list = unsorted_integer_list[0].split()

  # Convert the string type into the integer type in the list.
  unsorted_integer_list = [int(i) for i in unsorted_integer_list]

  return unsorted_integer_list