# Jeremy Beam 2502798
#Prompt to enter odd multiple of 19 that is more than 60 and less than 200
#add statement for good input and  input
#display other factor
def main():
    #prompting for input
   x = int(input('Enter odd multiple of 19 that is more than 60 and less than 200. '))
   #if x is more than 60 and less than 200 and a multiple of 19
   if x > 60 and x < 200 and x % 19 == 0 and x % 2 != 0:
       factor = x/19
       print(f'Good input! The other factor is {factor:.0f}')
   else:
       print(f'Bad input')
    

main()
