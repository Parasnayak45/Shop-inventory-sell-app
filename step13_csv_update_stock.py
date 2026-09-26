import csv

print("================================")
print("       UPDATE STOCK - CSV")
print("================================")

products = []

with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    for product in reader:
        products.append(product)

search = input("Enter product name: ")

found = False

for product in products:
    if product["name"].lower() == search.lower():

        print("\nProduct Found!")
        print("Old Quantity:", product["quantity"])

        new_quantity = input("Enter new quantity: ")

        product["quantity"] = new_quantity

        found = True
        break

if found:
    with open("products.csv", "w", newline="") as file:
        fieldnames = ["name", "price", "quantity"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(products)

    print("\nStock Updated Successfully!")
    print("Product:", search)
    print("New Quantity:", new_quantity)
    print("Data saved in products.csv")

else:
    print("\nProduct not found!")