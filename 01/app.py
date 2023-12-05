from domain.Cart import Cart
from domain.Product import Product

cart = Cart()
product = Product(name="Apple Pencil")
cart.add(product)


print(cart)
  