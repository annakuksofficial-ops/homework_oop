# Homework

## Описание
Проект для изучения основ объектно-ориентированного программирования на Python.
Реализованы классы `Product` и `Category` для интернет-магазина.

## Функциональность
- Класс `Product` с атрибутами: name, description, price, quantity
- Класс `Category` с атрибутами: name, description, products
- Классы-наследники: Smartphone, LawnGrass
- Подсчёт общей стоимости товаров на складе (магический метод __add__)
- Проверка типов при сложении товаров

## Тестирование
```bash
pytest tests/ -v
```
## Установка и запуск
python src/main.py

### Требования
- Python 3.12+
- Poetry

### Установка
```bash
# Клонируйте репозиторий
git clone https://github.com/annakuksofficial-ops/homework_oop.git

# Установите зависимости
poetry install
```
