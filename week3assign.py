def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = 0.2 * price
        final_price = price - discount
    else:
        final_price = price
    return final_price

price = int(input('Enter the price of the item: '))
discount_percent = int(input('Enter the discount percent: '))

price_to_pay = calculate_discount(price, discount_percent)

print('You are to pay', price_to_pay)