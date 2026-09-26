import csv

print("================================")
print("        DELETE PRODUCT")
print("================================")

products = []

with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    for product in reader:
        products.append(product)

search = input("Enter product name to delete: ")

found = False

for product in products:
    if product["name"].lower() == search.lower():
        products.remove(product)
        found = True
        break

if found:
    with open("products.csv", "w", newline="") as file:
        fieldnames = ["name", "price", "quantity"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(products)

    print("\nProduct deleted successfully!")
    print("Deleted Product:", search)

else:
    print("\nProduct not found!")