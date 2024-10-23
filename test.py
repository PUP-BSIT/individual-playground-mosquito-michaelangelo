all_items = []

# Product details
def enter_product_details():
    global product_name, product_price, product_quantity
    product_name = input("a. Product Name: ")
    product_price = int(input("b. Price: "))
    product_quantity = int(input("c. Quantity: "))
    total = product_price * product_quantity

    return [product_name, product_price, product_quantity, total]
