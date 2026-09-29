import csv


def inventory_value():

    total_value = 0

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for product in reader:
            price = float(product["price"])
            quantity = int(product["quantity"])

            total_value += price * quantity

    print("\n================================")
    print("       INVENTORY VALUE")
    print("================================")
    print("Total Inventory Value: ₹", total_value)


def low_stock():

    low_stock_limit = 5
    found = False

    print("\n================================")
    print("        LOW STOCK ALERT")
    print("================================")

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for product in reader:

            quantity = int(product["quantity"])

            if quantity <= low_stock_limit:

                print("Product:", product["name"])
                print("Quantity:", quantity)
                print("----------------------------")

                found = True

    if not found:
        print("No low stock products!")


# TEST
#inventory_value()
#low_stock()