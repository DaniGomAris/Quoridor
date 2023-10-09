class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, v, p, current):
    if(current is not None):
      if(current.value == p): #es el padre que busco?
        if(current.left is not None): #tiene izquierdo?
          if(current.right is not None): #tiene derecho?
            return False
          else:
            current.right = Node(v) #agrego en el derecho de current
            return True
        else:
          current.left = Node(v) #agrego en el izquierdo de current
          return True
      else:
        x = self.insert(v, p, current.left)
        print(x)
        if(x): #pudo agregar a la izquierda?
          return True
        self.insert(v, p, current.right) #salto al hijo izquierdo

  def print(self, node, prefix="", is_left=True):
    if not node:
      print("Empty Tree")
      return
    if node.right:
      self.print(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left:
      self.print(node.left, prefix + ("    " if is_left else "│   "), True)  