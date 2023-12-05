class Product:
  name = ""

  def __init__(self, name: str):
    self.name = name

  def get_item(self):
    return self.name

  def __repr__(self):
    return f"Product(\'{self.name}\')"

