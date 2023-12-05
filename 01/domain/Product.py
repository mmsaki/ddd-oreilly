import json

class Product:
  product = ""

  def __init__(self, name: str):
    self.product = name

  def get_item(self):
    return self.product

