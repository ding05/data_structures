from converter.stack import *

def converter(prefix_array: str) -> str:
  """
  Convert a prefix expression directly to a postfix expression.
  :param string: a string array to convert, must consists of operands
                 (English letters) and/or operators.
  :return: a converted string array.
  """
  # Valid strings to convert
  operand_array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                  "0123456789"
  operator_array = "+-*/$"
  valid_string_array = operand_array + operator_array

  # Stack for temporarily storing the items.
  stack = Stack()

  # Reverse the string array.
  reversed_prefix_array = prefix_array[::-1]

  # If the prefix array is empty, return an empty postfix array.
  if reversed_prefix_array == "":
    postfix_array = ""

  else:
    # Iterate every item in the string array.
    for item in reversed_prefix_array:

      # If the item is an operator, pop two items from the stack,
      # combine the two popped items with the operator,
      # and push the combined array back to the stack.
      if item in operator_array:

        # If there are less than two items in the stack, push an "undefined"
        # operadan to the back of the stack.
        if stack.size() == 0:
          stack.push("undefined")
          stack.push("undefined")
        elif stack.size() == 1:
          temp_item_a = stack.pop()
          stack.push("undefined")
          stack.push(temp_item_a)
        else:
          pass

        # Pop two items from the stack.
        temp_item_b = stack.pop()
        temp_item_c = stack.pop()
        temp_combined_array = temp_item_b + temp_item_c + item
        stack.push(temp_combined_array)

      # If the item is an operand, simply push it to the stack.
      elif item in operand_array:
        stack.push(item)

      # If the item is some other kind of characters,
      # ignore it and pass to the next item.
      else:
        pass

      # Convert the stack implemented using a list object into an array.
      postfix_array = ""
      for item in stack.get_stack():
        postfix_array += item

  return postfix_array