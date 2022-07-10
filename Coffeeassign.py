
#Coffeeassign.py
#pseudocode
#Prompt for how much coffee in pounds (no floats just ints)
#insert boolean expression for pounds for the following rates
#provide constant for shipping prices
#Add subtotal before tax if above 150$ shipping is free
#add tax
#display price in three parts, Subtotal, tax and total.

def main():
    
    #prompting for order amount
    lbs = int(input('Enter pounds of coffee desired: '))
    float(lbs)
    COFFEE40 = 7.50 * lbs
    COFFEE20 = 8.75 * lbs
    COFFEE10 = 10.00 * lbs
    COFFEE9 = 12.00 * lbs
    SHIPPING = 1.00 * lbs
    TAX = float(0.07)
    #conditinal statements
    if lbs >= 40:
        coffee = COFFEE40
        print(f'Price of Coffee/Subtotal is: ${coffee:,.2f}')
    else:
        if lbs >= 20:
            coffee = COFFEE20
            print(f'Price of Coffee/Subtotal is: ${coffee:,.2f}')
        else:
            if lbs >= 10:
                coffee = COFFEE10
                print(f'Price of Coffee/Subtotal is: ${coffee:,.2f}')
            else:
                if lbs <= 9:
                    coffee = COFFEE9
                    print(f'Price of Coffee/Subtotal is: ${coffee:,.2f}')
            float(coffee)
    #shipping conditional statements
    shipfee = 1.00 * lbs
    if coffee >= 150.00:
        shipping = shipfee * 0
        print(f'Shipping is free on orders with a subtotal of at least $150!')
    else:
        shipping = shipfee
        print(f'You could get free shipping with a 150$ subtotal!')
    #Taxes and totals output
    tax = TAX * coffee
    subtotal = coffee
    print(f'Your subtotal is ${subtotal:,.2f}')
    print(f'Sales tax is ${tax:,.2f}')
    print(f'Your shipping cost is ${shipping:,.2f}')
    total = subtotal + tax + shipping
    print(f'Your total including shipping is {total:,.2f}')
main()
