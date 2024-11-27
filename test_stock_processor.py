import json
from stock_processor import process_stock


def test_hello_world():
    # Arrange
    number1 = 2
    number2 = 3


    # Act
    sum = number1 + number2


    # Assert
    assert sum == 5


def test_item_out_of_stock_removes_item_from_basket():
    # Arrange
    banana_id = "Banana ID"

    filepath = "./test_cases/example_basket.json"
    file = open(filepath)
    filetext = file.read()
    basket = json.loads(filetext)

    filepath = "./test_cases/example_stocklist.json"
    file = open(filepath)
    filetext = file.read()
    stocklist = json.loads(filetext)

    # Act
    changed_basket, notifications = process_stock(basket, stocklist)

    # Assert
    assert changed_basket.get(banana_id) is None