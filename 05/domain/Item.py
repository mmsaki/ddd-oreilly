from domain.Product import Product

class Item:
  product = None
  quantity = 0

  def __init__(self, product: Product, quantity: int):
    self.product = product
    self.quantity = quantity

  def __repr__(self):
    return  f"Item(product={self.product}, quantity={self.quantity})"

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

  def __hash__(self):
    return hash((self.name,  self.quantity))

  def get_product(self):
    return self.product
  
  def get_quantity(self):
    return self.quantity