import csv 
print("================================")
print("       MY SHOP INVENTORY")
print("================================")

while True:

    print("\n1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Inventory Value")
    print("7. Low Stock Alert")
    print("8. Generate Bill")
    print("9. Daily Sales")
    print("10. Exit")

    choice = input("\nEnter your choice: ")
    if choice == "1":
        import csv

        name = input("Enter product name: ")
        price = float(input("Enter product price: ₹"))
        quantity = int(input("Enter product quantity: "))

        with open("products.csv", "a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "price", "quantity"]
            )

            writer.writerow({
                "name": name,
                "price": price,
                "quantity": quantity
            })

        print("\nProduct added successfully!")
    elif choice == "2":
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)

            print("\n================================")
            print("        ALL PRODUCTS")
            print("================================")

            for product in reader:
                print("Product:", product["name"])
                print("Price: ₹", product["price"])
                print("Quantity:", product["quantity"])
                print("----------------------------")
    elif choice == "3":
        search_name = input("Enter product name to search: ")

        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)

            found = False

            for product in reader:
                if product["name"].lower() == search_name.lower():
                    print("\nProduct Found!")
                    print("Product:", product["name"])
                    print("Price: ₹", product["price"])
                    print("Quantity:", product["quantity"])
                    found = True

            if not found:
                print("\nProduct not found!")
    elif choice == "4":
        product_name = input("Enter product name: ")
        new_quantity = int(input("Enter new quantity: "))

        products = []

        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)

            for product in reader:
                if product["name"].lower() == product_name.lower():
                    product["quantity"] = new_quantity
                    print("\nStock updated successfully!")

                products.append(product)

        with open("products.csv", "w", newline="") as file:
            fieldnames = ["name", "price", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(products)
    elif choice == "5":
        product_name = input("Enter product name to delete: ")

        products = []
        found = False

        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)

            for product in reader:
                if product["name"].lower() == product_name.lower():
                    found = True
                else:
                    products.append(product)

        with open("products.csv", "w", newline="") as file:
            fieldnames = ["name", "price", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(products)

        if found:
            print("\nProduct deleted successfully!")
        else:
            print("\nProduct not found!")
    elif choice == "6":
        total_value = 0

        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)

            for product in reader:
                price = float(product["price"])
                quantity = int(product["quantity"])

                total_value += price * quantity

        print("\n================================")
        print("      INVENTORY VALUE")
        print("================================")
        print("Total Inventory Value: ₹", total_value)
    elif choice == "7":
        low_stock_limit = 5

        print("\n================================")
        print("        LOW STOCK ALERT")
        print("================================")

        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)

            found = False

            for product in reader:
                quantity = int(product["quantity"])

                if quantity <= low_stock_limit:
                    print("Product:", product["name"])
                    print("Quantity:", quantity)
                    print("----------------------------")
                    found = True

            if not found:
                print("No low stock products!")
    elif choice == "8":
        product_name = input("Enter product name: ")
        buy_quantity = int(input("Enter quantity: "))

        found = False

        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)

            for product in reader:
                if product["name"].lower() == product_name.lower():
                    found = True

                    price = float(product["price"])
                    stock = int(product["quantity"])

                    if buy_quantity <= stock:
                        total = price * buy_quantity

                        print("\n================================")
                        print("             BILL")
                        print("================================")
                        print("Product:", product["name"])
                        print("Price: ₹", price)
                        print("Quantity:", buy_quantity)
                        print("--------------------------------")
                        print("Total Amount: ₹", total)
                        print("================================")
                    else:
                        print("\nNot enough stock!")

        if not found:
            print("\nProduct not found!")
    elif choice == "9":
        total_sales = 0

        try:
            with open("sales.csv", "r") as file:
                reader = csv.DictReader(file)

                for sale in reader:
                    total_sales += float(sale["total"])

            print("\n================================")
            print("         DAILY SALES")
            print("================================")
            print("Total Sales: ₹", total_sales)

        except FileNotFoundError:
            print("\nNo sales recorded yet!")

    elif choice == "10":
        print("\nThank you for using My Shop Inventory!")
        break

    else:
        print("\nYou selected option:", choice)
