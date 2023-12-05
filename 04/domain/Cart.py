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

  def remove(self, product: Optional[Product] = None, item: Optional[Item] = None):
    if item:
      product = item.product
      quantity = item.quantity
      for i, v in enumerate(self.cart):
        if v.product == product:
          self.cart[i] -= quantity
          if self.cart[i].quantity == 0 and len(self.cart[i:]) == 1:
            self.cart = self.cart[:i]
          elif self.cart[i].quantity == 0 and len(self.cart[i:]) > 1:
            self.cart = self.cart[:i] + self.cart[i+1:]
  
  def get_products(self):
    return self.cart

  def __repr__(self):
    return  f"Cart({self.cart})"