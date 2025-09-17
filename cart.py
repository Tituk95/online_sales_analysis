from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        # Dodaje proizvod i količinu u korpu
        if quantity <= product.quantity:
            self.cart_items.append((product, quantity))
            product.update_quantity(product.quantity - quantity)
        else:
            print(f"Nema dovoljno proizvoda {product.name} na stanju!")

    def total_amount(self):
        return sum(product.price * quantity for product, quantity in self.cart_items)

    def show_cart(self):
        for product, quantity in self.cart_items:
            print(f"{product.name} - {product.price} RSD x {quantity}")

