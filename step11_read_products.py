import csv

print("================================")
print("       PRODUCTS FROM CSV")
print("================================")

with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    for product in reader:
        print("Product:", product["name"])
        print("Price: ₹", product["price"])
        print("Quantity:", product["quantity"])
        print("----------------------------")