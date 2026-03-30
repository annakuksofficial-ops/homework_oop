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
        assert len(category.products) == 2
        assert category.products == products

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

        assert len(category.products) == 0
        assert Category.product_count == initial_prod_count

    def test_category_attributes(self):
        """Тест атрибутов категории"""
        products = [Product("P1", "D1", 100, 5)]
        category = Category("Test Name", "Test Desc", products)

        assert category.name == "Test Name"
        assert category.description == "Test Desc"
        assert category.products == products
