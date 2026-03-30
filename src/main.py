class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        """Инициализация продукта"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
