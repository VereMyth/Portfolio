# Jeremy Beam ID:2502798
#Prompt for input(item name)
#Primpt for input(quantity) Should display item name
#prompt for input(price) should display item name
#calculate subtotal of each item
def main():
    #set max number of transactions
    MAX = 3
    total = 0.0
    #prompting for item name, quantity, and price.
    for counter in range(MAX):
        item = input('Enter Item name ')
    
        qty = int(input(f'Enter quantity of {item} '))
    
        price = float(input(f'Enter unit price of {item} $'))
    #Calculate subtotal of items
        subtotal = qty * price
        print(f'{qty} {item} @ {price:.2f} is {subtotal:.2f}')
        total = subtotal + total
        print(f'The total of these 3 items is: {total:.2f}')
    
main()
