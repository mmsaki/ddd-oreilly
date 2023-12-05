import json

class Product:
  name = ""

  def __init__(self, name: str):
    self.name = name

  def get_item(self):
    return self.name

  def __repl__(self):
    return "Product{" + "name='" + self.product + '\'' + '}'

