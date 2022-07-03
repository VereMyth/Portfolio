# Jeremy Beam, 2502798
# Define def main
# Begin with an empty dictionary
# Start a while loop
# enable course code and percent grades as inputs
# Enter data for at least 5 courses
# use a for loop and the keys to show status of all courses
# Use the above loop to determine worst course and average of courses
# The worst course should be dropped adn reported
# Use another loop and use the items method to display the revised courses and grades
# Then report the revised average
def main():
    #Empty dictionary
    courses = {}
    #Priming input
    new = input('Input course code or Enter to quit ')
    #While loop for course input
    while new != '':
    #asking for INT input to pass to dictionary is value
        grade = int(input(f'Grade in {new} as % '))
    #adding value to key
        courses[new] = grade
    #repeating conditional statement
        new = input('Input course code or Enter to quit ')
    #for loop using key method
    for key in courses.keys():
    #printing dictionary using key method
        print(f'Grade in {key} is {courses[key]}% ')
    #Finding minimum using min function by passing the key argument to the get function
        less = min(courses, key=courses.get)
    #Finding average after ensuring the key input is INT not STR
        avg1 = sum(courses.values()) / len(courses)
    #reporting the minimum and current term average
    print(f'Current term average is {avg1}')
    print(f'Worst course is {less} : {min(courses.values())}% ')
    #popping the worst class and reporting
    drop = courses.pop(less, )
    print(f'Dropped {less}')
    print(f'Here are my revised grades... ')
    #Using items() method to print out revised dictionary and averages.
    for k,v in courses.items():
        print(f'grade in {k} is {v}% ')
        avg = sum(courses.values()) / len(courses)
    print(f'Revised term average is {avg:.1f} ')
    
        
        
        
        
        
        














if __name__ == '__main__':
    main()    
