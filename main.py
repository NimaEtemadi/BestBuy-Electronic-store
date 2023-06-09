import products
import promotions
import store
import test_product

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds",
                                 price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct(
                    "Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


def start(store_obj):
    while True:
        print("---------- MENU ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("------ Products in Store ------")
            products = store_obj.get_all_products()
            for product in products:
                print(product.show())
            print("-------------------------------\n")

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}\n")

        elif choice == "3":
            print("------ Make an Order ------")
            shopping_list = []

            while True:
                product_name = input("Enter product name (or 'q' to exit): ")
                if product_name == "q":
                    break

                product = None
                for prod in store_obj.products:
                    if prod.name == product_name:
                        product = prod
                        break

                if product is None:
                    print(f"Product '{product_name}' not found in the store.")
                    continue

                try:
                    quantity = int(input("Enter quantity: "))
                    shopping_list.append((product, quantity))
                except ValueError:
                    print("Invalid quantity. Please enter a valid integer.")

            total_price = store_obj.order(shopping_list)
            print(f"Total price of the order: {total_price}\n")

        elif choice == "4":
            print("Quitting the program...")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-4).\n")
