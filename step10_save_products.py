import csv

print("================================")
print("     SAVE PRODUCT DATA")
print("================================")

products = [
    {"name": "Kurti", "price": 500, "quantity": 4},
    {"name": "Plazo", "price": 400, "quantity": 2},
    {"name": "Pant", "price": 600, "quantity": 10},
    {"name": "Top", "price": 300, "quantity": 3},
    {"name": "Lehenga", "price": 900, "quantity": 8}
]

with open("products.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "price", "quantity"]
    )

    writer.writeheader()
    writer.writerows(products)

print("\nProduct data saved successfully!")
print("File created: products.csv")