"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture
def cart():
    return Cart()


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert True is product.check_quantity(1000)
        assert True is product.check_quantity(999)
        assert False is product.check_quantity(1001)

    def test_product_buy(self, product):
        old_quaniti = product.quantity
        product.buy(100)
        assert product.quantity == old_quaniti - 100
        # TODO напишите проверки на метод buy

        pass

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1005)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        cart.add_product(product, 10)
        assert product in cart.products and cart.products[product] == 10

    def test_cart_product_full_remove(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 5)
        assert product in cart.products and cart.products[product] == 5

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert not cart.products

    def test_cart_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == product.price * 10

    def test_cart_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

    def test_cart_buy_value_error(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()
