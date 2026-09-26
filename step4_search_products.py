print("================================")
print("   SEARCH PRODUCT")
print("================================")

products = [
    {"name": "Kurti", "price": 500, "quantity": 5},
    {"name": "Plazo", "price": 400, "quantity": 2},
    {"name": "Pant", "price": 600, "quantity": 2},
    {"name": "Top", "price": 300, "quantity": 3},
    {"name": "Lehenga", "price": 900, "quantity": 2}
]

search = input("Enter product name to search: ")

found = False

for product in products:
    if product["name"].lower() == search.lower():
        print("\nProduct Found!")
        print("Name:", product["name"])
        print("Price: ₹", product["price"])
        print("Quantity:", product["quantity"])
        found = True

if not found:
    print("\nProduct not found!")