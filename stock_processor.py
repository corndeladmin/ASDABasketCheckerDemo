def process_stock(basket: dict, stocklist):
    # COPY THE LIST OF KEYS BEFORE WE START WORKING WITH THE BASKET
    # THIS AVOID ERRORS WHEN DELETING THINGS FROM THE BASKET
    item_ids = list(basket.keys())

    # ITERATE OVER THE ITEMS IN THE BASKET
    # USE FOR LOOP
    # FOR A GIVEN ITEM
    for item in item_ids:
        print(item)
        
        # LOOKUP THE ITEM IN THE STOCKLIST
        stock = stocklist[item]

        print(stock)
        
        # CHECK THERE IS ANY QUANTITY
        # IF NO QUANTITY REMOVE FROM BASKET
        if stock == 0:
            basket.pop(item)

    notifications = []

    return (basket, notifications)