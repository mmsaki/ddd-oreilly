import json

class Product:
  name = ""

  def __init__(self, name: str):
    self.name = name

  def __repr__(self):
    return  "Product{name='" + self.name + "\'" + '}'

