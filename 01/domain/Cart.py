from domain.Product import Product

import json

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, item: Product):
    self.cart.append(item)
  
  def get_products(self):
    return self.cart

  def __repr__(self):
    return f"Cart({self.cart})"