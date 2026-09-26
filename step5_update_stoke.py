print("================================")
print("       UPDATE STOCK")
print("================================")

products = [
    {"name": "Kurti", "price": 500, "quantity": 5},
    {"name": "Plazo", "price": 400, "quantity": 2},
    {"name": "Pant", "price": 600, "quantity": 2},
    {"name": "Top", "price": 300, "quantity": 3},
    {"name": "Lehenga", "price": 900, "quantity": 2}
]

search = input("Enter product name: ")

found = False

for product in products:
    if product["name"].lower() == search.lower():

        print("\nProduct Found!")
        print("Old Quantity:", product["quantity"])

        new_quantity = int(input("Enter new quantity: "))

        product["quantity"] = new_quantity

        print("\nStock Updated Successfully!")
        print("Product:", product["name"])
        print("New Quantity:", product["quantity"])

        found = True
        break

if not found:
    print("\nProduct not found!")