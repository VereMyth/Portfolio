#Jeremy Beam COP1000
#Prompt for input
#Assume user knows only integers as input
#Use while loop
#Continue until Zero
def main():
    #prompt for input
    num = int(input('Enter an integer or 0 to quit '))
    #num = int(num)
    #insert loop after condition
    while num != 0:
        if num % 2 == 0:
            print(f'{num:,} is an even number')
        else:
            print(f'{num:,} is an odd number')
        num = int(input('Enter an integer or 0 to quit '))
main()
