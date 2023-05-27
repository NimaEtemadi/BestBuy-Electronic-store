import products
class Store:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print(f"Product '{product.name}' not found in the store.")

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            found = False
            for store_product in self.products:
                if store_product == product:
                    try:
                        price = store_product.buy(quantity)
                        total_price += price
                        found = True
                        break
                    except ValueError as e:
                        print(f"Error purchasing {store_product.name}: {str(e)}")
                        found = True
                        break
            if not found:
                print(f"Product '{product.name}' not found in the store.")

        return total_price


def main():
    import products
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
   

if __name__ == "__main__":
    main()