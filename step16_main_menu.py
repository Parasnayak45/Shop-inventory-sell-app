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

    if choice == "10":
        print("\nThank you for using My Shop Inventory!")
        break

    else:
        print("\nYou selected option:", choice)
