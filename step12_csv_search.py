import csv

print("================================")
print("       SEARCH PRODUCT")
print("================================")

search = input("Enter product name: ")

found = False

with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    for product in reader:
        if product["name"].lower() == search.lower():
            print("\nProduct Found!")
            print("Name:", product["name"])
            print("Price: ₹", product["price"])
            print("Quantity:", product["quantity"])

            found = True
            break

if not found:
    print("\nProduct not found!")