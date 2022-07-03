#Jeremy Beam, 2502798
#program7
# cels = [x for x in range(-40, 41, 10)]
#fahs = [c * 9/5 + 32 for c in cels]
#Define the main function
#import random
#generate 50 random integers from -40 to 40 using range
#The above represents Celsius temperatures
# use f string to output lowest and highest temperature from the list
# determine if 0C is in the list
# If it is identify and report where it is and if no report that.
# Again generate a sub list of 10 unique Celsius temperatures
# sort in ascending order
#Pass the clesius sub list as the sole argument for the value returning function
import random as ra

def main():
    #Generate random list with integers of -40 to 40 inclusive
    cels = [ra.randrange(-40,40) for c in range(50)]
    #name the lowest element
    low = min(cels)
    #name the highest element
    high = max(cels)
    #output lowest and highest element
    print(f'Lowest temp is {low}C and highest is {high}C')
    #conditional output if 0C is included in generation
    if 0 in cels:
        zero = cels.index(0)
        print(f'Found 0C at index {zero}')
    else:
        print('0C is not listed')
    #Slicing specific amount of UNIQUE integers
    c = ra.sample(cels, k = 10)
    #Sorting in ascending order
    c.sort()
    #Calling on fah() for list comprehension and sorting
    fa = fah(c)
    fa.sort()
    #getting number of list elements from each list.
    list1 = len(c)
    list2 = len(fa)
    #printing column headings
    print(f'{"CELSIUS":^10}{"FAHRENHEIT":^15}')
    #Setting accumulators
    total1 = 0
    total2 = 0
    #loop for totaling fa list
    for add in fa:
        total2 += add
    #loop using range to print table
    for index in range(len(c)):
        total1 += index
        print(f'{c[index]:^12}{fa[index]:^10.1f}', end = '')
        print()
    #averages
    avg = total1 / list1
    avg2 = total2 / list2
    print()
    print(f'{avg:^12.1f}{avg2:^10.1f} {"<---averages"}')

                  
                  
        
        
        
        

    
#Function using list comprehension to get fahrenheit
def fah(cels):
    return [9/5 * c + 32 for c in cels]



if __name__ == '__main__':
    main()
