from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = float(price)  # Convert to float
        self.quantity = float(quantity)  # Convert to float
        self.active = True
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = float(quantity)  # Convert to float
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "No Promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError(
                "Invalid quantity. Quantity must be a positive integer.")

        if not self.active:
            raise ValueError("Product is not active.")

        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available.")

        total_price = 0
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * float(quantity)  # Convert to float

        self.quantity -= float(quantity)  # Convert to float

        if self.quantity == 0:
            self.deactivate()

        return total_price


class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscountPromotion(Promotion):
    def __init__(self, percentage):
        self.name = f"{percentage}% off"
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        if quantity == 0:
            return 0

        original_price = product.price * float(quantity)
        discount_amount = (self.percentage / 100) * original_price
        discounted_price = original_price - discount_amount

        return discounted_price


class SecondItemHalfPricePromotion(Promotion):
    def __init__(self):
        self.name = "Second item at half price"

    def apply_promotion(self, product, quantity):
        if quantity <= 1:
            return product.price * float(quantity)

        full_price_items = quantity // 2
        half_price_items = quantity % 2

        total_price = (full_price_items * product.price) + \
            (half_price_items * (product.price / 2))

        return total_price


class Buy2Get1FreePromotion(Promotion):
    def __init__(self):
        self.name = "Buy 2, get 1 free"

    def apply_promotion(self, product, quantity):
        if quantity <= 2:
            return product.price * float(quantity)

        full_sets = quantity // 3
        remaining_items = quantity % 3

        total_price = (full_sets * 2 * product.price) + \
            (remaining_items * product.price)
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum
