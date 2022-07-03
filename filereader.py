#filereader.py
#start with def main()
#open file with the friends.txt name.
#Read data for variables
#Display data back to user
#Activate an Accumulator and counter
#Create While loop to process file, Print the Data,
#modify the accumulator and counter.

def main():
    #accumulator
    total_age = 0
    TOTAL_NUM = 0

    #open file for reading
    f = open('friends.txt','r')
    
    #read names from file
    name = f.readline()
    
    #set counter and accumulator
    
    
    while name != '':
        # read the ages of friends
        age = float(f.readline())
        #strip \n
        name = name.rstrip('\n')
        total_age += age
        TOTAL_NUM += 1
        print(f'My friend {name} is {age} ')
        print(f'{total_age}')
        name = f.readline()
    f.close()
    avg = total_age / TOTAL_NUM
    print(f'Average age of friends is {avg:.1f}')
    print('File was saved')
        
if __name__ == '__main__':
    main()
        
        
        
        
        
        
if __name__ == '__main__':
    main()

        
        
