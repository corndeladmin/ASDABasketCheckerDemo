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
    filepath = "./test_cases/example_basket.json"
    file = open(filepath)
    filetext = file.read()
    basket = json.loads(filetext)

    filepath = "./test_cases/example_stocklist.json"
    file = open(filepath)
    filetext = file.read()
    stocklist = json.loads(filetext)

    # Act
    changed_basket, _ = process_stock(basket, stocklist)

    # Assert
    banana_id = "Banana ID"
    assert changed_basket.get(banana_id) is None

def test_item_has_enough_quantity_to_fulfil_order_remains_in_basket_with_the_same_quantity_as_before():
    # Arrange
    filepath = "./test_cases/example_basket2.json"
    file = open(filepath)
    filetext = file.read()
    input_basket = json.loads(filetext)

    filepath = "./test_cases/example_stocklist2.json"
    file = open(filepath)
    filetext = file.read()
    stocklist = json.loads(filetext)

    # Act
    output_basket, _ = process_stock(input_basket, stocklist)

    # Assert
    banana_id = "Banana ID"
    assert output_basket.get(banana_id) is not None
    banana_output_basket_entry = output_basket.get(banana_id)
    banana_input_basket_entry = input_basket.get(banana_id)
    assert banana_output_basket_entry["Quantity"] == banana_input_basket_entry["Quantity"]

    tomato_id = "Tomato ID"
    assert output_basket.get(tomato_id) is not None
    tomato_output_basket_entry = output_basket.get(tomato_id)
    tomato_input_basket_entry = input_basket.get(tomato_id)
    assert tomato_output_basket_entry["Quantity"] == tomato_input_basket_entry["Quantity"]

def test_item_not_enough_stock_to_fufil_order_remains_in_basket_with_reduced_qty():
    # Arrange 
    filepath = "./test_cases/example_basket_not_enough_qty.json"
    file = open(filepath)
    filetext = file.read()
    input_basket = json.loads(filetext)

    filepath = "./test_cases/example_stocklist_not_enough_qty.json"
    file = open(filepath)
    filetext = file.read()
    stocklist = json.loads(filetext)
    
    # Act
    output_basket, notification = process_stock(input_basket, stocklist)
    
    # Assert
    apple_id = "Apple ID"
    assert output_basket.get(apple_id) is not None 
    apple_out_qty = output_basket[apple_id]["Quantity"]
    apple_qty_in_stock = stocklist[apple_id]
    assert apple_out_qty == apple_qty_in_stock
    