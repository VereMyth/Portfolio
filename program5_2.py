#Jeremy Beam, 2502798
#create value returning function for area
#create main function
#prompt user for radius as float
#call for return function
#create void function
#call for void function
import math

def area(radius):
        return math.pi * radius ** 2
    
def circ(radius):
        cir = 2 * math.pi * radius
        print(f'The circumference is {cir:,.3f}')

def main():
    radius = float(input('Enter radius of circle: '))
    a = area(radius)
    print(f'The area of a circle with radius {radius} is {a:,.4f}')
    circ(radius)
    
    




if __name__ == '__main__':
    main()
