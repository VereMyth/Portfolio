#Jeremy Beam, 2502798
#import the last assignment(5_2)
#create main function
#prompt user for radius as float
#execute import functions
import program5_2 as rad

def main():
    radius = float(input('Enter the radius of circle: '))
    area_circ = rad.area(radius)
    print(f'The area of a circle with radius {radius} is {area_circ:,.4f}')
    rad.circ(radius)
    
    











if __name__ == '__main__':
    main()
