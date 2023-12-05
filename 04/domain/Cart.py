from domain.Product import Product
from domain.Item import Item

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, item: Item):
    self.cart.append(item)

  def remove(self, item: Item):
    product = item.product
    quantity = item.quantity
    for i, v in enumerate(self.cart):
      if v.product == product:
        if self.cart[i].quantity >= quantity:
          self.cart[i] -= quantity
        else:
          # raise ValueError("Cannot remove more items than is present in the cart")
          return
        if self.cart[i].quantity == 0 and len(self.cart[i:]) == 1:
          self.cart = self.cart[:i]
        elif self.cart[i].quantity == 0 and len(self.cart[i:]) > 1:
          self.cart = self.cart[:i] + self.cart[i+1:]
  
  def get_items(self):
    return self.cart

  def __repr__(self):
    return  f"Cart({self.cart})"