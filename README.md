# ddd-oreilly

[Session Slides](https://on24static.akamaized.net/event/43/73/19/4/rt/1/documents/resourceList1700586153020/dddbootcamp98221121700586153020.pdf)

1. Code Problem 1:

   - Add a "Apple Pencil to a cart"

   ***

   **Note:** Please do not create User class.
   Please do not create ProductCategory, Brand, Varian, Colour, etc classess

   ***

   1. Run:

   ```sh
   python 01/app.py
   ```

   stdout:

   ```sh
   Cart([Product('Apple Pencil')])
   ```

1. Code Problem 2:

   - Add a "Sony Wireless headphone" to a Cart

   ```sh
   python 02/app.py
   ```

   stdout:

   ```sh
   Cart = Cart([Product('Apple Pencil'), Product('Sony Wireless headphone')])
   products = [Product('Apple Pencil'), Product('Sony Wireless headphone')]
   ```

1. Code Problem 3:

   - Add 2 quantity of "Apple Pencil" to a cart

   ```sh
   python 03/app.py
   ```

   stdout:

   ```sh
   Cart = Cart([Item('Product('Sony Wireless headphone')','1'), Item('Product('Apple Pencil')','2')])
   products = [Item('Product('Sony Wireless headphone')','1'), Item('Product('Apple Pencil')','2')]
   ```

1. Code Problem 4:

   - Remove already added Item “Apple Pencil” (with its all quantities) from Cart.

   ```sh
   python 04/app.py
   ```

   stdout:

   ```sh
   1.Cart Items
      Cart([Item(product=Product(Sony Wireless headphone), quantity=1), Item(product=Product(Apple Pencil), quantity=2)])
   2.After Removing Apple Pencil with 2 quantity
      Cart([Item(product=Product(Sony Wireless headphone), quantity=1)])
   ```
