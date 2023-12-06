from events.DomainEvent import DomainEvent
from domain.Item import Item

class ItemAddedToCartEvent(DomainEvent):
  item = None

  def __init__(self, item: Item):
    self.item = item

  def get_product(self):
    return self.item.product

  def get_quantity(self):
    return self.item.quantity

  def __repr__(self):
    return f"ItemAddedToCartEvent({self.item})"