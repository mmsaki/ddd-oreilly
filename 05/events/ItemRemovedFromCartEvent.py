from events.DomainEvent import DomainEvent
from domain.Item import Item

class ItemRemovedFromCartEvent(DomainEvent):
  item = None

  def __init__(self, item: Item):
    self.item = item

  def get_item(self):
    return self.item
  
  def __repr__(self):
    return f"ItemRemovedFromCartEvent({self.item})"