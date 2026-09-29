from step20_functions_shop import (
    add_product,
    show_products,
    search_product,
    update_stock
)

while True:

    print("\n==============================")
    print("     MY SHOP INVENTORY")
    print("==============================")

    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        show_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        print("\nThank you for using My Shop Inventory!")
        break

    else:
        print("\nInvalid choice!")