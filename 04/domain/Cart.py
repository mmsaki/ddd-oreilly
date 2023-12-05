from domain.Product import Product
from domain.Item import Item

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, item: Item):
    if item: return self.cart.append(item)

  def remove(self, item: Item):
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