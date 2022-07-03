#prep9.py
#Jeremy Beam, COP1000
#Create a dictionary with four state abbreviations and capitals with abbreviations being keys and the capital being values
#Start with four states
#then report the number of k.v pairs with a seperate function.
#Insert a while lopp to continue with input of more optional states using the same k.v option
# inside the while loop if the state entered is already in the dictionary report the capital
#if not prompt user to enter the captial of that state
#add to dictionary
# report the new count of k.v pairs
#add a second loop to report the totals using the items() method
# Add another dictionary comprehension with odd integers 1-9 as keys and their cubes as values
# use a for lopp to display the keys and values without using the items() method.

#define main
def main():
    #create first four dictionary elements
    states  = {'FL':'Tallahassee',
                   'AL:':'Montgemory',
                   'NY':'Albany',
                   'PA':'Harrisburg'}
    
    #print the length of the states dictionary using function count
    print(f'{count(states)} states are in the dicitonary ')
    #prime the while loop input
    new = input(f'Enter a state abbrev. Or Enter to quit ')
    #While loop start
    while new != '' :
    #start if statements for checking if dictionary element already exists
        if new in states:
            cap = states.get(new)
            print(f'Already have {new}, capital is {cap} ')
            new = input(f'Enter a state abbrev. Or Enter to quit ')
    #continue statement if element does exist otherwise prompt for capital
        else:
    #prompt for capital
             cap = input(f'Enter capital of {new} ')
    #Adding to dictionary
             states[new] = cap
    #repeating priming condition
             new = input(f'Enter a state abbrev. Or Enter to quit ')
    print()
    print(f'Got {count(states)} now, Here they are...')
    #For loop to display keys and values nicely using Item() method
    for k,v in states.items():
        print(f'The capital of {k} is {v}')
    #Dictionary comprehension
    print()
    num = {x : x ** 3 for x in range(1,10) if x % 2 != 0}
    print(f'Some cubes made with a dictionary comprehension...')
    #printing dictionary comprehension with item() method.
    for k,v in num.items():
        print(f'{k} cubed is {v}')
        print(sum(num.values()))

    #get count of list in argument
def count(c):
    return len(c)





    #Dunders decision
if __name__ == '__main__':
    main()
