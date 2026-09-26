print("================================")
print("     INVENTORY VALUE")
print("================================")

products = [
    {"name": "Kurti", "price": 500, "quantity": 4},
    {"name": "Plazo", "price": 400, "quantity": 2},
    {"name": "Pant", "price": 600, "quantity": 2},
    {"name": "Top", "price": 300, "quantity": 3},
    {"name": "Lehenga", "price": 900, "quantity": 2}
]

total_value = 0

for product in products:
    value = product["price"] * product["quantity"]

    print(
        product["name"],
        "₹", product["price"],
        "x", product["quantity"],
        "=", "₹", value
    )

    total_value += value

print("----------------------------")
print("Total Inventory Value: ₹", total_value)