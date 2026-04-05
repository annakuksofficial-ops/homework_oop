from src.main import Category, Product


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
