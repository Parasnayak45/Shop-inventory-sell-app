print("================================")
print("        SHOP BILL")
print("================================")

products = [
    {"name": "Kurti", "price": 500, "quantity": 4},
    {"name": "Plazo", "price": 400, "quantity": 2},
    {"name": "Pant", "price": 600, "quantity": 10},
    {"name": "Top", "price": 300, "quantity": 3},
    {"name": "Lehenga", "price": 900, "quantity": 8}
]

product_name = input("Enter product name: ")
buy_quantity = int(input("Enter quantity: "))

found = False

for product in products:
    if product["name"].lower() == product_name.lower():

        found = True

        if buy_quantity <= product["quantity"]:
            total = product["price"] * buy_quantity

            print("\n========== BILL ==========")
            print("Product:", product["name"])
            print("Price: ₹", product["price"])
            print("Quantity:", buy_quantity)
            print("--------------------------")
            print("Total Amount: ₹", total)
            print("==========================")

        else:
            print("\nNot enough stock!")

        break

if not found:
    print("\nProduct not found!")