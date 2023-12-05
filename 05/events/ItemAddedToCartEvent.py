from events.DomainEvent import DomainEvent
from domain.Item import Item

class ItemAddedToCartEvent(DomainEvent):
  product = ""
  quantity = 0

  def item_added_to_cart(self, item: Item):
    self.product = item.product
    self.quantity = item.quantity

  def get_product(self):
    return self.product

  def get_quantity(self):
    return self.quantity

  def __repr__(self):
    return f"ItemAddedToCartEvent({self.product})"