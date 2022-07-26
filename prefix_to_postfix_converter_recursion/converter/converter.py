def converter(prefix_list: list) -> list:
  """
  Convert a prefix expression in the list form directly to a postfix
  expression in the list form with recursion.
  :param list: a string list to convert, must consists of operands
               (English letters ow numbers) and/or operators.
  :return: a converted string list.
  """
  # Valid strings to convert
  operand_array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                  "0123456789"
  operator_array = "+-*/$"
  valid_string_array = operand_array + operator_array

  # Remove and store the first character, which is always an operator in a
  # prefix expression.

  # Make sure the current list is non-empty.
  if len(prefix_list) != 0:
    temp_item_a = prefix_list.pop(0)
  else:
    temp_item_a = ""
  temp_item_b = ""
  temp_item_c = ""

  # Make sure the current list is non-empty.
  if len(prefix_list) != 0:
    # If the next character is an operator, perform recursion until an operand
    # is found.
    if prefix_list[0][0] in operator_array:
      temp_item_b = converter(prefix_list)

      # Generate an "undefined" as a dummy operand to make sure there are
      # always sufficient operands corresponding to operators, though
      # not all are used. The dummy operand is used once when needed,
      # by defining temp_item_a.
      prefix_list.append("undefined")

    elif prefix_list[0][0] in operand_array:
      temp_item_b = prefix_list.pop(0)
    else:
      temp_item_b = ""

  if len(prefix_list) != 0:
    # Similarly, get another operand.
    if prefix_list[0][0] in operator_array:
      temp_item_c = converter(prefix_list)
      prefix_list.append("undefined")
    elif prefix_list[0][0] in operand_array:
      temp_item_c = prefix_list.pop(0)
    else:
      temp_item_c = ""

  # Combine the two operands and one operator in a nested list.
  nested_postfix_list = []
  nested_postfix_list.append(temp_item_b)
  nested_postfix_list.append(temp_item_c)
  nested_postfix_list.append(temp_item_a)

  return nested_postfix_list

def flatten_nested_list(nested_list: list) -> list:
  """
  Convert a nested list into a normal list with recursion.
  :param list: a nested list
  :return: a normal list
  """
  new_list = []

  # Iterate over all the elements in the nested list.
  for element in nested_list:

    # Perform recursion on a list until a string is found.
    if type(element) == list:
      new_list.extend(flatten_nested_list(element))
    else:
      new_list.append(element)

  return new_list
