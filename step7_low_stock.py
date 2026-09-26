print("================================")
print("        LOW STOCK ALERT")
print("================================")

products = [
    {"name": "Kurti", "price": 500, "quantity": 4},
    {"name": "Plazo", "price": 400, "quantity": 2},
    {"name": "Pant", "price": 600, "quantity": 10},
    {"name": "Top", "price": 300, "quantity": 3},
    {"name": "Lehenga", "price": 900, "quantity": 8}
]

low_stock_limit = 5

for product in products:
    if product["quantity"] < low_stock_limit:
        print("⚠️ LOW STOCK:", product["name"])
        print("Quantity:", product["quantity"])
        print("----------------------------")
    else:
        print("Stock OK:", product["name"])
        print("Quantity:", product["quantity"])
        print("----------------------------")