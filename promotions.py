from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        full_sets = quantity // 2
        remaining_items = quantity % 2
        total_price = (full_sets * product.price) + \
            (remaining_items * product.price * 0.5)
        return total_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        full_sets = quantity // 3
        remaining_items = quantity % 3
        total_price = (full_sets * 2 * product.price) + \
            (remaining_items * product.price)
        return total_price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * quantity * (1 - self.percent / 100)
        return discounted_price
