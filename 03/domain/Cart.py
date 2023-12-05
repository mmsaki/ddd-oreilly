from domain.Item import Item

class Cart:
  cart = []
  
  def __init__(self):
    pass

  def add(self, item: Item):
    self.cart.append(item)
  
  def get_items(self):
    return self.cart

  def __repr__(self):
    return  f"Cart({self.cart})"