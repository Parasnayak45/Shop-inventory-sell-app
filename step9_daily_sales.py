print("================================")
print("        DAILY SALES")
print("================================")

sales = []

while True:
    product_name = input("\nEnter product name (or 'done' to finish): ")

    if product_name.lower() == "done":
        break

    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter selling price: ₹"))

    total = quantity * price

    sale = {
        "product": product_name,
        "quantity": quantity,
        "price": price,
        "total": total
    }

    sales.append(sale)

print("\n================================")
print("        TODAY'S SALES")
print("================================")

total_sales = 0

for sale in sales:
    print("Product:", sale["product"])
    print("Quantity:", sale["quantity"])
    print("Price: ₹", sale["price"])
    print("Total: ₹", sale["total"])
    print("----------------------------")

    total_sales += sale["total"]

print("TOTAL SALES: ₹", total_sales)