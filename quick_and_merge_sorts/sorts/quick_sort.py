from sorts.insertion_sort import *

def quick_sort(unsorted_integer_list: list, type="A"):
  """
  Perform a Quicksort on a given integer list.
  There are four types of Quicksorts:
  A: Select the first item of the partition as the pivot. Treat partitions of
  size one and two as stopping cases.
  B: Select the first item of the partition as the pivot. For a partition of
  size 100 or less, use an insertion sort to finish.
  C: Select the first item of the partition as the pivot. For a partition of
  size 50 or less, use an insertion sort to finish.
  D: Select the median-of-three as the pivot. Treat partitions of size one
  and two as stopping cases.
  :param unsorted_integer_list: a list of unsorted integers
  :param type: one of the four preset types of Quicksorts
  :return sorted_integer_list: a list of sorted integers
  :return num_compare: an integer of the number of comparisons
  """
  low = 0
  high = len(unsorted_integer_list) - 1
  size = len(unsorted_integer_list)
  num_compare = 0

  # Create a stack for temporarily storing items.
  stack = [0] * size

  # Initialize the top of the stack.
  top = -1

  # Push initial values of the starting and ending indices to stack.
  top = top + 1
  stack[top] = low
  top = top + 1
  stack[top] = high

  # Pop from the stack while it is not empty.
  while top >= 0:

    # Pop the starting and ending indices.
    high = stack[top]
    top = top - 1
    low = stack[top]
    top = top - 1

    # Set the pivot at its correct position in the sorted list.
    # If the type is A, B or C, run the partition_first function.
    # Further, if the type is B, run the insertion_sort function when the
    # partition's size is smaller than 100; if the type is C, run the
    # insertion_sort function when the partition's size is smaller than 50.
    # If the type is D, run the partition_median function
    if type == "B" and high + 1 <= 100:
      temp_unsorted_integer_list, temp_num_compare = \
        insertion_sort(unsorted_integer_list[:high])
      unsorted_integer_list = temp_unsorted_integer_list + \
                              unsorted_integer_list[high:]
      num_compare += temp_num_compare
      break
    if type == "C" and high + 1 <= 50:
      temp_unsorted_integer_list, temp_num_compare = \
        insertion_sort(unsorted_integer_list[:high])
      unsorted_integer_list = temp_unsorted_integer_list + \
                              unsorted_integer_list[high:]
      num_compare += temp_num_compare
      break

    if type == "A" or "B" or "C":
      pivot, temp_num_compare = partition_first(unsorted_integer_list, low, high)
      num_compare += temp_num_compare
    else:
      pivot, temp_num_compare = partition_median(unsorted_integer_list, low, high)
      num_compare += temp_num_compare

    # If there are elements on left side of pivot,
    # then push left side to stack
    if pivot - 1 > low:
      num_compare += 1
      top = top + 1
      stack[top] = low
      top = top + 1
      stack[top] = pivot - 1

    # If there are elements on right side of pivot,
    # then push right side to stack
    if pivot + 1 < high:
      num_compare += 1
      top = top + 1
      stack[top] = pivot + 1
      top = top + 1
      stack[top] = high

  sorted_integer_list = unsorted_integer_list

  return sorted_integer_list, num_compare

def partition_first(list: list, low: int, high: int):
  """
  Partition the list with the first item of the partition as the pivot.
  :param list: a list for partition
  :param low: the starting index
  :param high: the ending index
  :return: the pivot's index
  :return num_compare: an integer of the number of comparisons
  """
  num_compare = 0

  # The pivot is the first item.
  pivot = low

  # If the current item is smaller than or equal to the pivot, increase the
  # index of the items.
  for i in range(low + 1, high + 1):
    if list[i] <= list[low]:
      num_compare += 1
      pivot += 1
      list[i], list[pivot] = list[pivot], list[i]
  list[pivot], list[low] = list[low], list[pivot]

  return pivot, num_compare

def partition_median(list: list, low: int, high: int):
  """
  Partition the list with the median item of the first, middle and last
  items of the partition as the pivot.
  :param list: a list for partition
  :param low: the starting index
  :param high: the ending index
  :return: the pivot's index
  :return num_compare: an integer of the number of comparisons
  """
  num_compare = 0

  # The pivot is the median item of the first, middle and last items.
  pivot = list.index(sorted([list[low], list[high], list[(low+high)//2]])[1])

  # Update the pivot.
  list[low], list[pivot] = list[pivot], list[low]
  pivot_value = pivot[low]
  pivot = low

  # If the current item is smaller than or equal to the pivot, increase the
  # index of the items.
  for i in range(low + 1, high + 1):
    if list[i] <= pivot_value:
      num_compare += 1
      pivot += 1
      list[i], list[pivot] = list[pivot], list[i]
  list[pivot], list[low] = list[low], list[pivot]

  return pivot, num_compare