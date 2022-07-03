# Jeremy Beam 2502798
#prompt for input from a 2 digit integer
#Check input for acceptance
#Prompt for second 2 digit input
#Check for acceptance
#Calculate which integer is larger
#calculate by how much
def main():
    #prompt for input
    x = int(input('Enter a two-digit integer '))
    if x < 100 and x >= 10:
        
    #prompt for second integer
        
        y = int(input('Enter a two-digit integer again '))
    else:
        print('Bad Input')
        
    #Calculate which integer is the largest.
        
    if x > y:
        l_int = x
        s_int = y
        print(f'{x} is greater than {y}')
    else:
        x < y
        l_int = y
        s_int = x
        print(f'{y} is greater than {x}')
        
    #Calculate how much larger one digit is to another.
        
    diff = l_int - s_int
    print(f'The difference between integers is {diff}')
        


main()
