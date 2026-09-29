from add_product_db import add_product
from show_products_db import show_products
from search_product_db import search_product
from update_stock_db import update_stock
from delete_product_db import delete_product
from inventory_value_db import inventory_value
from low_stock_db import low_stock
from billing_db import generate_bill
from sales_history_db import sales_history


while True:

    print("\n================================")
    print("     SHOP INVENTORY SYSTEM")
    print("================================")

    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Inventory Value")
    print("7. Low Stock Alert")
    print("8. Generate Bill")
    print("9. Sales History")
    print("10. Exit")

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
        sales_history()

    elif choice == "10":
        print("\nThank you for using Shop Inventory System!")
        break

    else:
        print("\nInvalid choice!")