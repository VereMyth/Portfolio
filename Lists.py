
#import random
#create main func
#create empy list
#create for loop
#Make statement to add 12 random integers range(50,101)
#Make second for loop to iterate and display all elements seperated by one space.
#Display the 4th element
#display index 9
#display the smallest element
#Create second function called change_list with the list as only argument
#Slice new list from previous list with just the middle 6 elements
#determine size of list and print
#lists_prep
#sort new list in ascending order and return the sort list to main
import random as ra

def main():
    #Empty list
    nums = []
    # generating list from empty list using for loop to implement range.
    print('Here is the list of random integers...')
    nums = [ra.randint(50,100) for n in range(12)]
    #For loop to display list on one line spaced by empty strings
    for n in nums:
        print(f'{n}', end = ' ')
    #Breaking loop to display fourth element   
    print()
    #displaying fourth element
    print(f'The 4th element in the list is {nums[3]}')
    #printing ninth index
    print(f'The element at index 9 is {nums[9]}')
    #getting smallest element and outputting
    small = min(nums)
    #print output
    print(f'The smallest element in the list is {small}')
    #call and catch the value returning function
    sort = change_list(nums)
    #output the function
    print(sort)
def change_list(nums):
    #Splice the list
    sub = nums[3:9]
    #count the number of elements in the list
    len(sub)
    #print outputs
    print(f'The size of the list is now', len(sub))
    print(f'change_list returned this sorted list...')
    #sort in ascending order
    sub.sort()
    #return
    return sub
    
    
    
    
    
    
    
        
                   

if __name__ == '__main__':
    main()
