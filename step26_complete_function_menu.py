from step20_functions_shop import (
    add_product,
    show_products,
    search_product,
    update_stock
)

from step22_delete_function import delete_product
from step23_inventory_functions import inventory_value, low_stock
from step24_bill_function import generate_bill
from step25_sales_functions import save_sale, sales_history


while True:

    print("\n================================")
    print("       MY SHOP INVENTORY")
    print("================================")

    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Inventory Value")
    print("7. Low Stock Alert")
    print("8. Generate Bill")
    print("9. Save Sale")
    print("10. Sales History")
    print("11. Exit")

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
        delete_product()

    elif choice == "6":
        inventory_value()

    elif choice == "7":
        low_stock()

    elif choice == "8":
        generate_bill()

    elif choice == "9":
        save_sale()

    elif choice == "10":
        sales_history()

    elif choice == "11":
        print("\nThank you for using My Shop Inventory!")
        break

    else:
        print("\nInvalid choice!")