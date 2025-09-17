from product import Product
from product_manager import ProductManager

# Kreiramo ProductManager
manager = ProductManager()

# Dodajemo proizvode
manager.add_product(Product("Laptop", 80000, 5))
manager.add_product(Product("Telefon", 50000, 10))
manager.add_product(Product("Slusalice", 3000, 50))

# Prikaz svih proizvoda
print("Proizvodi u inventaru:")
manager.show_products()

# Prikaz ukupne vrednosti
print(f"Ukupna vrednost inventara: {manager.total_value()} RSD")

# Uklanjanje proizvoda "Slusalice"
manager.remove_product("Slusalice")
print("\nNakon uklanjanja proizvoda 'Slusalice':")
manager.show_products()

