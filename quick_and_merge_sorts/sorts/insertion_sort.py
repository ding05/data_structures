def insertion_sort(unsorted_integer_list: list):
  """
  Perform an Insertion Sort on a given integer list.
  :param unsorted_integer_list: a list of unsorted integers
  :return sorted_integer_list: a list of sorted integers
  :return num_compare: an integer of the number of comparisons
  """
  num_compare = 0

  for i in range(1, len(unsorted_integer_list)):

    key = unsorted_integer_list[i]

    # Move from the first item to the (i-1)th item that are greater than key
    # to one position ahead of their current positions.
    j = i - 1
    while j >= 0 and key < unsorted_integer_list[j]:
      num_compare += 1
      unsorted_integer_list[j + 1] = unsorted_integer_list[j]
      j -= 1

    unsorted_integer_list[j + 1] = key

  sorted_integer_list = unsorted_integer_list

  return sorted_integer_list, num_compare