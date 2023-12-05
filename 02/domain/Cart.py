from domain.Product import Product

import json

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, item: Product):
    self.cart.append(item.name)
  
  def get_products(self):
    return self.cart

  def __repr__(self):
    if self.cart and len(self.cart) == 1:
      return "Cart{" + "products=" + "".join(self.cart) + '}'
    else:
      return "Cart{" + "products=" +  json.dumps(self.cart) + '}'