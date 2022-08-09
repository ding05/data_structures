class Node:
  def __init__(self, left=None, right=None, data=""):
    """
    This class is the node of a binary tree.
    :param left:
    :param right:
    """
    self.left = left
    self.right = right

  def children(self):
    return self.left, self.right

def make_tree(char_freq_dict: dict) -> (Node, str):
  """
  Make a binary tree with the frequency table used for Huffman encoding.
  :param char_freq_dict: a dictionary that contains letters and their
  frequencies.
  :return: the root of the generated binary tree.
  """
  # Covert the frequency dictioanry into a sorted list. The list is used for
  # storing the tree nodes, updated iteratively.
  char_freq_list = sorted(char_freq_dict.items(), key=lambda x: x[1],
                          reverse=True)
  nodes = char_freq_list

  # The tree's information, updated iteratively.
  tree_info = ""

  # The loop stops when there is only one item, i.e. the root. The other
  # nodes and corresponding edges are stored in the root.
  while len(nodes) > 1:

    # Since there are three items stored at one node: the node object,
    # the letters or concatenated letters, and the frequency
    # or the sum of the frequencies, examine if a node contains all and may
    # add the missed information to the node.
    if len(nodes[-1]) == 3:
      nodes[-1] = nodes[-1][0:2] + (str(nodes[-1][2]),)
    else:
      nodes[-1] = nodes[-1] + (str(nodes[-1][0]),)
    if len(nodes[-2]) == 3:
      nodes[-2] = nodes[-2][0:2] + (str(nodes[-2][2]),)
    else:
      nodes[-2] = nodes[-2] + (str(nodes[-2][0]),)

    # Read and temporarily store the three items at the last two nodes.
    (key1, c1, skey1) = nodes[-1]
    (key2, c2, skey2) = nodes[-2]

    # Update the tree's information.
    tree_info = skey2 + ": " + str(c2) + ", " + skey1 + ": " + str(
      c1) + ", " + tree_info

    # Remove the read two nodes from the dictionary.
    nodes = nodes[:-2]

    # Make the two read nodes the children of a new node and add this new node
    # to the dictionary.
    node = Node(key1, key2, ''.join(sorted((skey1 + skey2))) + ": " +
                str(c1 + c2))
    nodes.append((node, c1 + c2, ''.join(sorted((skey1 + skey2)))))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

  # Conclude the tree's information.
  tree_info = "The tree is: " + nodes[0][2] + ": " + str(nodes[0][1]) + ", "\
              + tree_info[:-2] + "."

  return nodes[0][0], tree_info