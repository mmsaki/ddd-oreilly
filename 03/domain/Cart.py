from domain.Product import Product
from domain.Item import Item
from typing import Optional

import json

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, product: Optional[Product] = None, item: Optional[Item] = None):
    if product: return self.cart.append(product)
    if item: return self.items.append(item)
  
  def get_products(self):
    return self.cart

  def __repr__(self):
    if self.cart and len(self.cart) == 1:
      return f"Cart(\'{''.join(self.cart)}\')"
    else:
      return  f"Cart({self.cart})"