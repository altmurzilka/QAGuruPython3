import pytest

from task_8.models import Product, Cart

"""
Протестируйте классы из модуля homework/models.py
"""


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000
        product.buy(1)
        assert product.quantity == 999
        product.buy(999)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 999)
        assert cart.products[product] == 1000

    def test_remove_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, 1)
        cart.remove_product(product, 2000)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product, 40)
        assert cart.products == {product: 60}

    def test_clear(self, product, cart):
        cart.add_product(product, 5)
        cart.clear()
        assert product not in cart.products

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 1)
        assert cart.get_total_price() == 100, 'Wrong total price'

        cart.add_product(product, 4)
        assert cart.get_total_price() == 500, 'Wrong total price'

    def test_buy(self, product, cart):
        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 900, "Wrong quantity for left product"

        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 800, "Wrong quantity for left product"

        cart.add_product(product, 800)
        cart.buy()
        assert product.quantity == 0, "Wrong quantity for left product"
