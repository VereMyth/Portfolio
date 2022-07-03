# Jeremy Beam, 2502798,
#Program 6_1.py
#Use While loop
#Write a file with names, Regular price and price reductions(percentages).
#Data should be entered by user
#Each item should be stored on a seperate line.


#define main
def main():
#open file
    f = open('sale.txt', 'w')
#intiate test variable:
    item = '1'
    #Start while loop
    while item != '':
        item = input('Enter item name or Enter to quit ')
        if item != '':
        #prompt for item price and sale amount
            price = float(input("Enter item's regular price: "))
            sale = int(input('Enter reduction percent for sale '))
        #calculate sale into float
##            sale_dec = sale / 100
##            sale_price = price - (price * sale_dec)
##            total_saved = price - sale_price
##            print(f'{item} reduction price is {sale_price:,.2f}')
##            print(f'You saved {total_saved:,.2f} on {item}! ')
            f.write(item + '\n')
            f.write(str(price) + '\n')
            f.write(str(sale) + '\n')
##          f.write(str(sale_price) + '\n')
##          f.write(str(total_saved) + '\n')
        if item == '':
            print('File was created')
        else:
            pass

    f.close()
        
        
        






if __name__ == '__main__':
    main()
