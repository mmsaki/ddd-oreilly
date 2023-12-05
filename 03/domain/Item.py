from domain.Product import Product

class Item:
  product = None
  quantity = 0

  def __init__(self, product: Product, quantity: int):
    self.product = product
    self.quantity = quantity

  def __repr__(self):
    return  f"Item(product={self.product}, quantity={self.quantity})"
    
  def get_product(self):
    return self.product