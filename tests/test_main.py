import pytest
from src.main import Category, Product, Smartphone, LawnGrass


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Test Product", "Test Description", 100.50, 10)

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 100.50
        assert product.quantity == 10

    def test_product_with_zero_price(self):
        """Тест продукта с нулевой ценой"""
        product = Product("Free Item", "Description", 0.0, 100)
        assert product.price == 0.0

    def test_product_with_zero_quantity(self):
        """Тест продукта с нулевым количеством"""
        product = Product("Out of Stock", "Description", 100.0, 0)
        assert product.quantity == 0

    def test_price_setter_positive(self):
        """Тест сеттера цены с положительным значением"""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 200.0
        assert product.price == 200.0

    def test_price_setter_negative(self, capsys):
        """Тест сеттера цены с отрицательным значением (цена не меняется)"""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = -50.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

    def test_price_setter_zero(self, capsys):
        """Тест сеттера цены с нулевым значением (цена не меняется)"""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

    def test_new_product_classmethod(self):
        """Тест класс-метода new_product"""
        product_dict = {
            "name": "Phone",
            "description": "Smartphone",
            "price": 500.0,
            "quantity": 10,
        }
        product = Product.new_product(product_dict)

        assert product.name == "Phone"
        assert product.description == "Smartphone"
        assert product.price == 500.0
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category"""

    def test_category_initialization(self):
        """Тест корректной инициализации категории"""
        products = [
            Product("Product 1", "Description 1", 100.0, 5),
            Product("Product 2", "Description 2", 200.0, 3),
        ]
        category = Category("Test Category", "Test Description", products)

        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert Category.category_count > 0

    def test_products_getter_returns_string(self):
        """Тест геттера products - возвращает строку"""
        product = Product("Test Product", "Desc", 100.0, 5)
        category = Category("Test Category", "Test Desc", [product])

        result = category.products
        assert isinstance(result, str)
        assert "Test Product" in result
        assert "100.0 руб." in result
        assert "Остаток: 5 шт." in result

    def test_products_getter_format(self):
        """Тест формата вывода геттера products"""
        product = Product("Laptop", "Powerful laptop", 1500.0, 3)
        category = Category("Electronics", "Devices", [product])

        expected = "Laptop, 1500.0 руб. Остаток: 3 шт.\n"
        assert category.products == expected

    def test_add_product(self):
        """Тест метода add_product"""
        category = Category("Test Category", "Desc", [])
        product = Product("New Product", "Desc", 100.0, 5)

        initial_count = Category.product_count
        category.add_product(product)

        assert "New Product" in category.products
        assert Category.product_count == initial_count + 1

    def test_add_product_multiple(self):
        """Тест добавления нескольких продуктов"""
        category = Category("Test Category", "Desc", [])

        product1 = Product("P1", "D1", 100, 2)
        product2 = Product("P2", "D2", 200, 3)

        category.add_product(product1)
        category.add_product(product2)

        assert "P1" in category.products
        assert "P2" in category.products

    def test_category_count_increment(self):
        """Тест подсчета количества категорий"""
        initial_count = Category.category_count

        Category("Category 1", "Description", [])

        assert Category.category_count == initial_count + 1

    def test_product_count_increment(self):
        """Тест подсчета количества продуктов"""
        initial_count = Category.product_count

        products = [
            Product("Product 1", "Desc", 100.0, 5),
            Product("Product 2", "Desc", 200.0, 3),
        ]
        Category("Category 1", "Description", products)

        assert Category.product_count == initial_count + len(products)

    def test_multiple_categories(self):
        """Тест нескольких категорий"""
        Category.category_count = 0
        Category.product_count = 0

        cat1_products = [Product("P1", "D1", 100, 2)]
        Category("Cat1", "Desc1", cat1_products)

        cat2_products = [Product("P2", "D2", 200, 3),
                         Product("P3", "D3", 300, 4)]
        Category("Cat2", "Desc2", cat2_products)

        assert Category.category_count == 2
        assert Category.product_count == 3

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком продуктов"""
        initial_prod_count = Category.product_count

        category = Category("Empty Category", "No products", [])

        assert category.products == ""
        assert Category.product_count == initial_prod_count

    def test_category_attributes(self):
        """Тест атрибутов категории"""
        products = [Product("P1", "D1", 100, 5)]
        category = Category("Test Name", "Test Desc", products)

        assert category.name == "Test Name"
        assert category.description == "Test Desc"


class TestProductMagicMethods:
    """Тесты для магических методов Product"""

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Test Product", "Description", 100.50, 5)
        expected = "Test Product, 100.5 руб. Остаток: 5 шт."
        assert str(product) == expected

    def test_product_add(self):
        """Тест сложения двух продуктов"""
        product1 = Product("Product A", "Desc", 100.0, 10)
        product2 = Product("Product B", "Desc", 200.0, 2)
        result = product1 + product2
        expected = (100 * 10) + (200 * 2)  # 1000 + 400 = 1400
        assert result == expected

    def test_product_add_different_types(self):
        """Тест сложения продукта с не-продуктом (должен вызвать ошибку)"""
        product = Product("Test", "Desc", 100.0, 5)
        try:
            product + 100
            assert False, "Должна быть ошибка TypeError"
        except TypeError as e:
            assert str(e) == "Можно складывать только одинаковые типы товаров"


class TestCategoryMagicMethods:
    """Тесты для магических методов Category"""

    def test_category_str(self):
        """Тест строкового представления категории"""
        product1 = Product("Product 1", "Desc", 100.0, 5)
        product2 = Product("Product 2", "Desc", 200.0, 3)
        category = Category("Test Category", "Description", [product1, product2])

        expected = "Test Category, количество продуктов: 8 шт."
        assert str(category) == expected

    def test_category_str_empty(self):
        """Тест строкового представления пустой категории"""
        category = Category("Empty Category", "No products", [])
        expected = "Empty Category, количество продуктов: 0 шт."
        assert str(category) == expected

    def test_category_str_with_one_product(self):
        """Тест строкового представления категории с одним продуктом"""
        product = Product("Single Product", "Desc", 100.0, 7)
        category = Category("Single Cat", "Desc", [product])
        expected = "Single Cat, количество продуктов: 7 шт."
        assert str(category) == expected


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_initialization(self):
        """Тест создания смартфона"""
        phone = Smartphone("iPhone 15", "Apple phone",
                           100000.0, 10, 98.5,
                           "15 Pro", 256, "Black")
        assert phone.name == "iPhone 15"
        assert phone.description == "Apple phone"
        assert phone.price == 100000.0
        assert phone.quantity == 10
        assert phone.efficiency == 98.5
        assert phone.model == "15 Pro"
        assert phone.memory == 256
        assert phone.color == "Black"

    def test_smartphone_inherits_from_product(self):
        """Тест: Smartphone наследуется от Product"""
        phone = Smartphone("Test", "Desc", 100.0,
                           5, 90.0, "Model",
                           128, "Red")
        assert isinstance(phone, Product)

    def test_smartphone_str(self):
        """Тест строкового представления смартфона"""
        phone = Smartphone("Samsung", "Desc",
                           50000.0, 3, 95.0,
                           "S23", 256, "Gray")
        expected = "Samsung, 50000.0 руб. Остаток: 3 шт."
        assert str(phone) == expected


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_initialization(self):
        """Тест создания газонной травы"""
        grass = LawnGrass("Газонная трава", "Элитная трава",
                          500.0, 20, "Россия",
                          "7 дней", "Зеленый")
        assert grass.name == "Газонная трава"
        assert grass.description == "Элитная трава"
        assert grass.price == 500.0
        assert grass.quantity == 20
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"

    def test_lawn_grass_inherits_from_product(self):
        """Тест: LawnGrass наследуется от Product"""
        grass = LawnGrass("Test", "Desc",
                          100.0, 5, "USA",
                          "5 days", "Green")
        assert isinstance(grass, Product)

    def test_lawn_grass_str(self):
        """Тест строкового представления газонной травы"""
        grass = LawnGrass("Grass", "Desc",
                          300.0, 10,
                          "Russia", "7d",
                          "Green")
        expected = "Grass, 300.0 руб. Остаток: 10 шт."
        assert str(grass) == expected


class TestTypeRestrictions:
    """Тесты для ограничений"""

    def test_cannot_add_smartphone_and_grass(self):
        """Тест: нельзя сложить смартфон и траву"""
        phone = Smartphone("Phone", "Desc",
                           1000.0, 10, 95.0,
                           "Model", 128, "Red")
        grass = LawnGrass("Grass", "Desc",
                          500.0, 20, "RU",
                          "7d", "Green")

        with pytest.raises(TypeError) as exc_info:
            phone + grass
        assert "Можно складывать только одинаковые типы товаров" in str(exc_info.value)

    def test_cannot_add_product_to_category_wrong_type(self):
        """Тест: нельзя добавить в категорию не продукт"""
        category = Category("Test", "Desc", [])

        with pytest.raises(TypeError) as exc_info:
            category.add_product("not a product")
        assert ("Можно добавлять только объекты Product или его наследников"
                in str(exc_info.value))

    def test_cannot_add_integer_to_category(self):
        """Тест: нельзя добавить число в категорию"""
        category = Category("Test", "Desc", [])

        with pytest.raises(TypeError):
            category.add_product(123)

    def test_can_add_smartphone_to_category(self):
        """Тест: можно добавить смартфон в категорию"""
        category = Category("Phones", "Desc", [])
        phone = Smartphone("iPhone", "Desc", 1000.0,
                           10, 95.0, "15",
                           256, "Black")

        category.add_product(phone)
        assert "iPhone" in category.products

    def test_can_add_lawn_grass_to_category(self):
        """Тест: можно добавить траву в категорию"""
        category = Category("Grass", "Desc", [])
        grass = LawnGrass("Green Grass", "Desc",
                          500.0, 20, "Russia",
                          "7d", "Green")

        category.add_product(grass)
        assert "Green Grass" in category.products
