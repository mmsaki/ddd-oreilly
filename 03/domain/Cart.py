from domain.Product import Product
from domain.Item import Item

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, product: Product, item: Item):
    if product: return self.cart.append(product)
    if item: return self.items.append(item)
  
  def get_products(self):
    return self.cart

  def __repr__(self):
    return  f"Cart({self.cart})"