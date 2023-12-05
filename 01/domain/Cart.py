from domain.Product import Product

import json

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, item: Product):
    self.cart.append(item.product)
  
  def get_products(self):
    if self.cart and len(self.cart) == 1:
      return "".join(self.cart)
    else:
      return ", ".join(self.cart[0:-1]) + " and " + self.cart[-1]