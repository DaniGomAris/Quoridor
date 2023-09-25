class EmptyList(Exception):
  pass

class OutRande(Exception):
  pass

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def add_head(self, value):
    new_node = Node(value)
    if self.is_empty():
      self.head = new_node
      self.size += 1
    else:
      new_node.next = self.head
      self.head = new_node
      self.size += 1

  def add_end(self, current, value):
    new_node = Node(value)
    if self.is_empty():
      self.head = new_node
      self.size += 1
    elif current.next is None:
      current.next = new_node
      self.size += 1
    else:
      self.add_end(current.next, value)

  def add_arbitrary_pos(self, current, value, pos, x=0):
    new_node = Node(value)
    if self.is_empty():
      self.head = new_node
      self.size += 1
    if pos < 0 or pos > self.size:
      raise OutRande("Posicion fuera de rango")
    elif pos == 0:
      self.add_head(value)
    elif x == pos - 1:
      new_node.next = current.next
      current.next = new_node
      self.size += 1
    else:
      self.add_arbitrary_pos(current.next, value, pos, x+1)
  
  def delete_head(self, current):
    if self.is_empty():
      raise EmptyList("Lista vacia")
    elif current.next is None:
      self.head = None
      self.size -= 1
    else:
      self.head = current.next

  def delete_end(self, current):
    if self.is_empty():
      raise EmptyList("Lista vacia")
    elif self.head.next == None:
      self.head = None
      self.size -= 1
    elif current.next.next is None:
      current.next = None
      self.size -= 1
    else:
      self.delete_end(current.next)

  def delete_arbitrary_position(self, current, pos, x = 0):
    if self.is_empty():
      raise EmptyList("Lista vacia")
    if pos < 0 or pos > self.size:
      raise OutRande("Posicion fuera de rango")
    elif pos == 0:
      self.delete_head()
    elif x == pos - 1:
      current.next = current.next.next
      self.size -= 1
    else:
      self.delete_arbitrary_position(current.next, pos, x+1)

  def traverse(self, current):
    if current.next is None:
      print(current.value)
    else:
      print(current.value)
      self.traverse(current.next)

  def is_empty(self):
    return self.size == 0