def natural_merge_sort(unsorted_integer_list: list):
  """
  Perform a Natural Merge Sort on a given integer list.
  :param unsorted_integer_list: a list of unsorted integers
  :return: a list of sorted integers
  :return num_compare: an integer of the number of comparisons
  """
  num_compare = 0

  # The length of the list
  num_items = len(unsorted_integer_list)

  # Create a temp list.
  temp_list = [0] * num_items

  # Create the starting list.
  start_list = [0] * (num_items + 1)

  # Identify the parts.
  part_count = 0
  for i in range(num_items + 1):
    if i == num_items or unsorted_integer_list[i] < unsorted_integer_list[i-1]:
      num_compare += 1
      start_list[part_count] = i
      part_count += 1

  # Merge the parts until one part is left.
  break_from = unsorted_integer_list
  break_to = temp_list
  while part_count > 1:
    new_part_count = 0

    # Merge two parts each time
    for i in range(0, part_count, 2):
      temp_num_compare = merge(break_from, break_to, start_list[i], start_list[i+1],
            start_list[i+2])
      num_compare += temp_num_compare
      start_list[new_part_count] = start_list[i]
      new_part_count += 1

    # Prepare for next round.
    start_list[new_part_count] = num_items
    part_count = new_part_count

    # Swap the break_from and break_to lists.
    break_from, break_to = break_to, break_from

  # If final part is not in the unsorted list, copy them.
  if break_from != unsorted_integer_list:
    unsorted_integer_list = break_from

  sorted_integer_list = unsorted_integer_list

  return sorted_integer_list, num_compare

def merge(source, target, start_left, start_right, end_right) -> int:
  """
  Merge two parts for the Natural Merge Sort.
  :param source: the source part
  :param target: the target part
  :param start_left: the left side of the starting list
  :param start_right: the right side of the starting list
  :param end_right: the right side of the ending list
  :return num_compare: an integer of the number of comparisons
  """
  num_compare = 0

  # The steps refer to the thread of Jose M. J. on the discussion forum.
  left_pos = start_left
  right_pos = start_right
  target_pos = start_left

  while left_pos < start_right and right_pos < end_right:
    num_compare += 1
    left_val = source[left_pos]
    right_val = source[right_pos]
    if left_val <= right_val:
      num_compare += 1
      target[target_pos] = left_val
      target_pos += 1
      left_pos += 1
    else:
      num_compare += 1
      target[target_pos] = right_val
      target_pos += 1
      right_pos += 1

  while left_pos < start_right:
    num_compare += 1
    target[target_pos] = source[left_pos]
    target_pos += 1
    left_pos += 1

  while right_pos < end_right:
    num_compare += 1
    target[target_pos] = source[right_pos]
    target_pos += 1
    right_pos += 1

  return num_compare