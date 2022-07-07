class Stack:
  def __init__(self):
    """
    This class is used to hold strings in a traditional stack.
    """
    self.items = []

  def is_empty(self) -> bool:
    """
    Determine if the stack is empty, i.e. not holding any element.
    :return: True if the number of elements is zero.
    """
    return len(self.item) == 0

  def pop(self) -> str:
    """
    Remove the first element, i.e. one string from the top, of the stack and
    return it.
    :return: the current string on the top of the stack.
    """
    return self.items.pop()

  def push(self, inserted_item: str):
    """
    Insert one string to the top of the stack.
    :param insert_item:a string to insert, must be a 'str' type.
    """
    if type(inserted_item) is not str:
      raise AssertionError(f"This is a character stack. Insert a string.")
    self.items.append(inserted_item)

  def peek(self) -> str:
    """
    Return the first element of the stack.
    :return: the current string on the top of the stack.
    """
    return self.items[len(self.items)-1]

  def size(self) -> int:
    """
    Return the size of the stack.
    :return: an integer that represents the size of the stack.
    """
    return len(self.items)

  def get_stack(self) -> list:
    """
    Return the stack in a list form.
    :return: the list implementation of the stack.
    """
    return self.items