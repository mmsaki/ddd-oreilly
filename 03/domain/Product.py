class Product:
  name = ""

  def __init__(self, name: str):
    self.name = name

  def __repr__(self):
    return  f"Product({self.name})"

