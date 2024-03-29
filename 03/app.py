from domain.Cart import Cart
from domain.Product import Product
from domain.Item import Item

cart = Cart()

headphone = Product(name="Sony Wireless headphone")
headphone_item = Item(product=headphone, quantity=1)
cart.add(headphone_item)

apple_pencil = Product(name="Apple Pencil")
apple_pencil_item = Item(product=apple_pencil, quantity=2)
cart.add(apple_pencil_item)


products = cart.get_items()

print("Cart =", cart)
print("products =", products)
  