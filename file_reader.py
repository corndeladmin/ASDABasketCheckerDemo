import json

filepath = "./test_cases/example_basket.json"

file = open(filepath)

filetext = file.read()

basket = json.loads(filetext)

print(basket)