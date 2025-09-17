from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiramo ProductManager
manager = ProductManager()

# Dodajemo proizvode u inventar
manager.add_product(Product("Laptop", 80000, 5))
manager.add_product(Product("Telefon", 50000, 10))
manager.add_product(Product("Slusalice", 3000, 50))

# Prikaz proizvoda i ukupne vrednosti
print("Proizvodi u inventaru:")
manager.show_products()
print(f"Ukupna vrednost inventara: {manager.total_value()} RSD")

# Kreiramo korpu
shopping_cart = Cart()

# Dodajemo proizvode u korpu pre uklanjanja
shopping_cart.add_to_cart(manager.products[0], 2)  # Laptop
shopping_cart.add_to_cart(manager.products[1], 1)  # Telefon
shopping_cart.add_to_cart(manager.products[2], 5)  # Slusalice

print("\nSadržaj korpe:")
shopping_cart.show_cart()
print(f"Ukupna vrednost za naplatu: {shopping_cart.total_amount()} RSD")

# Uklanjanje proizvoda iz inventara
manager.remove_product("Slusalice")

print("\nNakon uklanjanja proizvoda 'Slusalice':")
manager.show_products()
print(f"Ukupna vrednost inventara: {manager.total_value()} RSD")
