#filemaker.py
#start with def main()
#open a file with the friends.txt name.
# Use a while loop that prompts for first name and age of each friend
# repeat until user presses enter
#File should close and a confirmation message should display.

def main():

    #open file
    f = open('friends.txt','w')
    #input for name
    name = input('Enter the first name of friend or Enter to quit ')
    #While loop for continuos input
    while name != '':
        age = int(input(f'Enter the age of {name} '))

        f.write(name + '\n')
        f.write(str(age) + '\n')

        name = input('Enter friends name or Enter to quit ')

    f.close()
    print('File was created')

if __name__ == '__main__':
    main()

        
        
