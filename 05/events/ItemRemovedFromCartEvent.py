from events.DomainEvent import DomainEvent
from domain.Item import Item

class ItemRemovedFromCartEvent(DomainEvent):
  product = ""

  def item_removed_from_cart(self, item: Item):
    self.product = item.product

  def get_product(self):
    return self.product
  
  def __repr__(self):
    return f"ItemRemovedFromCartEvent({self.product})"