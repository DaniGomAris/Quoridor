class EmptyList(Exception):
  pass

class OutRange(Exception):
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

  def delete_arbitrary_position(self, current, pos, x = 0):
    if self.is_empty():
      raise EmptyList("Lista vacia")
    if pos < 0 or pos > self.size:
      raise OutRange("Posicion fuera de rango")
    elif pos == 0:
      self.delete_head()
    elif x == pos - 1:
      current.next = current.next.next
      self.size -= 1
    else:
      self.delete_arbitrary_position(current.next, pos, x+1)

  def is_empty(self):
    return self.size == 0