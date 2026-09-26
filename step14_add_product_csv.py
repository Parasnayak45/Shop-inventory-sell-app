import csv
import os

print("================================")
print("       ADD NEW PRODUCT")
print("================================")

name = input("Enter product name: ")
price = float(input("Enter product price: ₹"))
quantity = int(input("Enter product quantity: "))

file_exists = os.path.exists("products.csv")

with open("products.csv", "a", newline="") as file:

    fieldnames = ["name", "price", "quantity"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()

    writer.writerow({
        "name": name,
        "price": price,
        "quantity": quantity
    })

print("\nProduct added successfully!")
print("Product:", name)
print("Price: ₹", price)
print("Quantity:", quantity)