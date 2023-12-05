import json

class Product:
  name = ""

  def __init__(self, name: str):
    self.name = name

  def __repr__(self):
    return  f"Product({self.name})"

  def __eq__(self, other):
    return self.name == other.name
  
  def __ne__(self, other):
    return not self.__eq__(other)
