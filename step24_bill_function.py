import csv


def generate_bill():

    search = input("Enter product name: ").lower()
    quantity = int(input("Enter quantity: "))

    products = []
    found = False

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for product in reader:

            if product["name"].lower() == search:

                found = True

                price = float(product["price"])
                stock = int(product["quantity"])

                if quantity <= stock:

                    total = price * quantity

                    print("\n================================")
                    print("          SHOP BILL")
                    print("================================")
                    print("Product:", product["name"])
                    print("Price: ₹", price)
                    print("Quantity:", quantity)
                    print("Total: ₹", total)
                    print("================================")

                    product["quantity"] = stock - quantity

                else:
                    print("\nNot enough stock!")

            products.append(product)

    if not found:
        print("\nProduct not found!")

    with open("products.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "price", "quantity"]
        )

        writer.writeheader()
        writer.writerows(products)


# TEST
#generate_bill()