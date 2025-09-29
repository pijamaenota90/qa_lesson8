class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        True если количество продукта больше либо равно запрашиваемому и False в обратном случае
        """

        return self.quantity >= quantity


    def buy(self, quantity):
        """
        Проверьте количество продукта используя check_quantity, если продуктов не хватает - используйте ValueError
        """

        if not self.check_quantity(quantity):
            raise ValueError

        self.quantity -= quantity

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """

        if not product.check_quantity(buy_count):
            raise ValueError
        if product not in self.products:
            self.products[product] = 0
        self.products[product] += buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """

        if product not in self.products:
            return

        if remove_count is None:
            del self.products[product]
            return

        if remove_count >= self.products[product]:
            del self.products[product]
            return

        self.products[product] -= remove_count


    def clear(self):
        """
        Очистка корзины
        """
        self.products.clear()

    def get_total_price(self) -> float:
        """
        Расчёт общей стоимости
        """
        total_price = 0.0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price


    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        for product, quantity_in_cart in self.products.items():
            if not product.check_quantity(quantity_in_cart):
                raise ValueError

        for product, quantity_in_cart in self.products.items():
            product.buy(quantity_in_cart)
        self.clear()
