class Node:
  def __init__(self, position):
    self.position = position
    self.children = []

class GeneralTree:
  def __init__(self):
    self.root = None

  def add_node(self, position, parent = None, current = None):
    if current is None:
      current = self.root
    if current:
      if current.position == parent:
        current.children.append(Node(position))
      else:
        for child in current.children:
          self.add_node(position, parent, child)
    else:
      self.root = Node(position)

  def traverse(self, current):
    if current is not None:
      print(current.position)
      for child in current.children:
        self.traverse(child)