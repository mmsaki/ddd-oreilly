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

print("1.Cart Items =", cart)

apple_pencil_1 = Product(name="Apple Pencil")
apple_pencil_item_1 = Item(product=apple_pencil_1, quantity=2)
cart.remove(item=apple_pencil_item_1)

products = cart.get_items()

print("2.Removed Items =", cart.get_removed_product_names())
print(cart)




  