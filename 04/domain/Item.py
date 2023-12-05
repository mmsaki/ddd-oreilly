import json
from domain.Product import Product

class Item:
  product = None
  quantity = 0

  def __init__(self, product: Product, quantity: int):
    self.product = product
    self.quantity = quantity

  def __repr__(self):
    return  f"Item(\'{self.product}\',\'{self.quantity}\')"

  def __eq__(self, other):
    return self.product == other.product

  def __ne__(self, other):
    return not self.__eq__(other)
  
  def __sub__(self, other):
    self.quantity -= other
    return self

  def __add__(self, other):
    self.quantity += other
    return self