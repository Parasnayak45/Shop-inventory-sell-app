print("================================")
print("   MY SHOP INVENTORY SYSTEM")
print("================================")

products = []

for i in range(5):
    print(f"\n--- Product {i + 1} ---")

    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter product quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

print("\n================================")
print("        ALL PRODUCTS")
print("================================")

for product in products:
    print("Product:", product["name"])
    print("Price: ₹", product["price"])
    print("Quantity:", product["quantity"])
    print("----------------------------")