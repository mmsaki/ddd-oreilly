from domain.Product import Product
from domain.Item import Item
from events.ItemAddedToCartEvent import ItemAddedToCartEvent
from events.ItemRemovedFromCartEvent import ItemRemovedFromCartEvent

class Cart:
  items = []
  events = []
  
  def __init__(self):
    pass

  def __repr__(self):
    return  f"Cart(\nitems={self.items}, \nevents={self.events}\n)"
  
  def get_items(self):
    return self.items

  def add(self, item: Item):
    self.items.append(item)
    event = ItemAddedToCartEvent()
    event.item_added_to_cart(item)
    self.events.append(event)

  def remove(self, item: Item):
    product = item.product
    quantity = item.quantity
    for i, v in enumerate(self.items):
      if v.product == product:
        if self.items[i].quantity >= quantity:
          self.items[i] -= quantity
          event = ItemRemovedFromCartEvent()
          event.item_removed_from_cart(item)
          self.events.append(event)

        else:
          # raise ValueError("Cannot remove more items than is present in the items")
          return
        if self.items[i].quantity == 0 and len(self.items[i:]) == 1:
          self.items = self.items[:i]
        elif self.items[i].quantity == 0 and len(self.items[i:]) > 1:
          self.items = self.items[:i] + self.items[i+1:]

  def get_removed_product_names(self):
    items = []
    for e in self.events:
      if isinstance(e, ItemRemovedFromCartEvent):
        items.append(e.product)
    return items