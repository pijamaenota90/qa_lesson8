"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture()
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # проверки на метод check_quantity
        assert product.check_quantity(999) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1001) == False

    def test_product_buy(self, product):
        # проверки на метод buy

        product.buy(999)
        assert product.quantity == 1
        product.buy(1)
        assert product.quantity == 0

        product.quantity = 1000
        product.buy(1000)
        assert product.quantity == 0


    def test_product_buy_more_than_available(self, product):
        # напишите проверки на метод buy, которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        product.quantity = 1000
        with pytest.raises(ValueError):
            product.buy(1001)
        assert product.quantity == 1000


class TestCart:
    """
    Напишите тесты на методы класса Cart
    На каждый метод у вас должен получиться отдельный тест
    На некоторые методы у вас может быть несколько тестов.
    Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product_less_and_equal_than_available(self, product):
        cart = Cart()
        cart.add_product(product, 999)
        assert product in cart.products
        assert cart.products[product] == 999

        cart.add_product(product, 1)
        assert product in cart.products
        assert cart.products[product] == 1000

    def test_add_product_more_than_available(self, product):
        cart = Cart()
        with pytest.raises(ValueError):
            cart.add_product(product, 1001)

            assert product not in cart.product

    def test_remove_product_less_than_available(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product, 9)
        assert product in cart.products
        assert cart.products[product] == 1

    def test_remove_product_equal_available(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product, 10)
        assert product not in cart.products

    def test_remove_product_more_than_available(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product, 11)
        assert product not in cart.products

    def test_remove_product_none(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_empty_cart(self, product):
        cart = Cart()
        cart.clear()
        assert len(cart.products) == 0

    def test_clear_cart_with_product(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.clear()
        assert len(cart.products) == 0

    def test_total_price(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

    # def test_buy_more_than_quantity(self, product):
    #     cart = Cart()
    #     cart.add_product(product, 1001)
    #     with pytest.raises(ValueError):
    #         cart.buy()
    #     assert product.quantity == 1000


    def test_buy_less_than_available(self, product):
        cart = Cart()
        cart.add_product(product, 1000)
        cart.buy()
        assert product.quantity == 0

    def test_buy_equal_available(self, product):
        cart = Cart()
        cart.add_product(product, 999)
        cart.buy()
        assert product.quantity == 1

