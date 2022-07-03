# Jeremy Beam, 2502798,
#Program 6_2.py
#open file
#open file to read
#create tables headings
#make for loop for number of items
# print out using f.readline() command
#format for table using F.strings

#defining


def main():
    #opening file in read only
    f = open('sale.txt', 'r')
    #printing header
    print(f'{"ITEM":<7}{"REG.PRICE":>10}{"REDUCED":>8}{"SALE PRICE":>12}')
    #prime file reading
    item = f.readline()
    #Initiate loop
    while item != '':
        #strip new line
        item = item.rstrip('\n')
        price = f.readline()
        #convert str to float no need to strip \n Python does it automatically
        price = float(price)
        sale = f.readline()
        #convert str to int, above^ applies to int as well
        sale = int(sale)
        #Calculating sale price
        sale_price = price - (price * sale / 100)
        #calculating difference between original price and sale
        reduced = price - sale_price
        #Printing output formatting6
        print(f'{item:<8} {price:>4} {reduced:>9,.2f} {sale_price:>11,.2f}')
        #continue loop
        item = f.readline()
        
        
        
    #close file
    f.close()

        
        
        
        

















if __name__ == '__main__':
    main()
