#Jeremy Beam, 2502798
#prompt user for the number of different items being purchased
#make a loop to prompt for description, price, and quantity of each item purchased.
#pass these values as arguments to a custom function that is defined in seperate module file
#imported function should print subtotal for item and return it to main.
#total should be printed in main after loop
#----------------------------------------------
#prompting user for input
import cash
def main():
    ITEMS = int(input('How many different items are being purchased? '))
    total = 0.0
#set loop for items
    for ITEMS in range(0,ITEMS):
        ITEMS += 1
        desc = input(f'Enter description of item {ITEMS} ')
        price = float(input(f'Enter the price for item {ITEMS} '))
        qty = int(input(f'Enter the quantity of items '))
#call function
        subtotal = cash.sub(qty,price,desc)
        subtotal1 = qty * price
        total = subtotal1 + total
    print(f'Your total is ${total:.2f}')
    


if __name__ == '__main__':
    main()
