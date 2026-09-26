print("================================")
print("   MY SHOP INVENTORY SYSTEM")
print("================================")

products = []

name = input("Enter product name: ")
price = float(input("Enter product price: ₹"))
quantity = int(input("Enter product quantity: "))

product = {
    "name": name,
    "price": price,
    "quantity": quantity
}

products.append(product)

print("\nProduct added successfully!")
print("----------------------------")
print("Product:", name)
print("Price: ₹", price)
print("Quantity:", quantity)