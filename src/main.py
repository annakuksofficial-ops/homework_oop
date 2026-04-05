class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        """Инициализация продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        """Создаёт новый продукт из словаря"""
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Category:
    """Класс для представления категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает строку со всеми продуктами"""
        result = ""
        for product in self.__products:
            result += (f"{product.name}, {product.price} руб. "
                       f"Остаток: {product.quantity} шт.\n")
        return result
