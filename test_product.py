import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-1450, quantity=100)


def test_product_reaches_zero_quantity():
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=2)
    assert product.is_active()
    product.buy(2)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("Google Pixel 7", price=500, quantity=10)
    assert product.quantity == 10
    assert product.buy(3) == 1500
    assert product.quantity == 7


def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        product.buy(10)
