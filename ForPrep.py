# Jeremy Beam COP1000
# Use for loop with range
# Using above  process integers 5 to 50
# for num in range (6,50,5)
# Format to table using print(format(num, etc.
# Repeat using Squares and Cubes
def main():
    print(f'{"INTS":^7}{"SQUARES":>8}{"CUBES":>12}')
    for num in range(5,51,5):
        sq = num ** 2
        cb = num ** 3
        print(f'{num:^7,}{sq:>8,}{cb:>12,}')
main()
