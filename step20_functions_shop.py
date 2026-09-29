import csv


# ==============================
# 1. ADD PRODUCT
# ==============================

def add_product():
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


# ==============================
# 2. SHOW PRODUCTS
# ==============================
# search_product()
#  update_stock()

def show_products():
    print("\n================================")
    print("         ALL PRODUCTS")
    print("================================")

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for product in reader:
            print("Product:", product["name"])
            print("Price: ₹", product["price"])
            print("Quantity:", product["quantity"])
            print("----------------------------")


# ==============================
# TEST
# ==============================

print("Shop Inventory Functions")
print("------------------------")

show_products()# ==============================
# 3. SEARCH PRODUCT
# ==============================

def search_product():
    search = input("Enter product name to search: ").lower()

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        found = False

        for product in reader:
            if product["name"].lower() == search:
                print("\nProduct Found!")
                print("Product:", product["name"])
                print("Price: ₹", product["price"])
                print("Quantity:", product["quantity"])
                found = True

        if not found:
            print("\nProduct not found!")


# ==============================
# 4. UPDATE STOCK
# ==============================

def update_stock():
    search = input("Enter product name: ").lower()
    new_quantity = int(input("Enter new quantity: "))

    products = []

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for product in reader:
            if product["name"].lower() == search:
                product["quantity"] = new_quantity

            products.append(product)

    with open("products.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "price", "quantity"]
        )

        writer.writeheader()
        writer.writerows(products)

    print("\nStock updated successfully!")
    # ==============================
# TEST FUNCTIONS
# ==============================
