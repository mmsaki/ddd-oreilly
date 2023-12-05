from domain.Cart import Cart
from domain.Product import Product

cart = Cart()

apple = Product(name="Apple Pencil")
cart.add(apple)

headphone = Product(name="Sony Wireless headphone")
cart.add(headphone)


products = cart.get_products()

print("Cart = ", cart)
print("products = ", products)
  