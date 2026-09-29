import csv


def save_sale():

    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    total = float(input("Enter total amount: "))

    file_exists = False

    try:
        with open("sales.csv", "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open("sales.csv", "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["product", "quantity", "total"]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "product": product_name,
            "quantity": quantity,
            "total": total
        })

    print("\nSale saved successfully!")


def sales_history():

    print("\n================================")
    print("         SALES HISTORY")
    print("================================")

    try:
        with open("sales.csv", "r") as file:

            reader = csv.DictReader(file)

            found = False

            for sale in reader:

                print("Product:", sale["product"])
                print("Quantity:", sale["quantity"])
                print("Total: ₹", sale["total"])
                print("----------------------------")

                found = True

            if not found:
                print("No sales found!")

    except FileNotFoundError:
        print("No sales file found!")


# TEST
##save_sale()
#sales_history()