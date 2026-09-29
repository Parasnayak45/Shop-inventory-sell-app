import csv

def delete_product():

    search = input("Enter product name to delete: ").lower()

    products = []
    found = False

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for product in reader:

            if product["name"].lower() == search:
                found = True
                print("Product deleted:", product["name"])
            else:
                products.append(product)

    with open("products.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "price", "quantity"]
        )

        writer.writeheader()
        writer.writerows(products)

    if found:
        print("Product deleted successfully!")
    else:
        print("Product not found!")


# TEST
#delete_product()