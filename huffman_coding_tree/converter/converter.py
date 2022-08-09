from converter.tree import *

def huffman_code_tree(node: Node, encoded='') -> dict:
  """
  Create encoding rules with a a binary tree built with the frequency table.
  :param node: the root of a binary tree built with the frequency table
  :param encoded: the encoded expression, updated recursively
  :return: a dictionary of Huffman encoding with the binary tree
  """
  # There are two types of a node's value: the Node object and the string.
  if type(node) is str:
    return {node: encoded}
  (left, right) = node.children()

  # Connect each letter with encoded digits.
  huffman_dict = dict()
  huffman_dict.update(huffman_code_tree(left, encoded + '0'))
  huffman_dict.update(huffman_code_tree(right, encoded + '1'))

  return huffman_dict

def clean_decoded(expression: str) -> str:
  """
  Make the expression to be a valid decoded expression for Huffman encoding.
  :param expression: a decoded expression.
  :return: a valid decoded expression.
  """
  # Only the capital letters are kept. The small letters are converted into
  # capital letters and other characters, including white spaces, are removed.
  letter_array = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  expression = expression.upper()
  clean_expression = ""
  for char in expression:
    if char in letter_array:
      clean_expression += char

  return clean_expression

def clean_encoded(expression: str) -> str:
  """
  Make the expression to be a valid encoded expression for Huffman encoding.
  :param expression: an encoded expression.
  :return: a valid encoded expression.
  """
  # Only the two digits 0 and 1 are kept. Other characters, including
  # white spaces, are removed.
  digit_array = "01"
  clean_expression = ""
  for char in expression:
    if char in digit_array:
      clean_expression += char

  return clean_expression

def encode(huffman_dict: dict, clean_expression: str) -> str:
  """
  Encode a valid expression with a Huffman encoding dictionary.
  :param huffman_dict: a Huffman encoding dictionary.
  :param clean_expression: a valid expression for encoding.
  :return: an encoded expression.
  """
  # Given a key, find the value in the encoding dictionary.
  encoded = ""
  for char in clean_expression:
    if char in huffman_dict:
      encoded += huffman_dict[char]

  return encoded

def decode(huffman_dict: dict, clean_expression: str) -> str:
  """
  Decode a valid expression with a Huffman encoding dictionary.
  :param huffman_dict: a Huffman encoding dictionary.
  :param clean_expression: a valid expression for decoding.
  :return: a decoded expression.
  """
  # Swap the keys and values in the encoding dictionary. It is possible since
  # the keys and values are unique.
  reversed_huffman_dict = {y: x for x, y in huffman_dict.items()}

  # Given a value, find the key in the encoding dictionary.
  decoded = ""
  max_length = len(max(reversed_huffman_dict, key=reversed_huffman_dict.get))
  for i in range(len(clean_expression)):
    cur_length = max_length
    while cur_length > 0:
      if clean_expression[i:i+cur_length] in reversed_huffman_dict:
        decoded += reversed_huffman_dict[clean_expression[i:i+cur_length]]
        clean_expression = clean_expression[:i] + "!" * cur_length + \
                           clean_expression[i+cur_length:]
        break
      else:
        cur_length -= 1

  return decoded