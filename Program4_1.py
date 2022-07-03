# Jeremy Beam ID:2502798
# Set Tax rate to constant(TAX = .07)
# Show changes to subtotals: range(0.20,5.00,0.20)
# Centered in columns 9 characters wide.
# Include underlined headings.
def main():
    print(f'{"SUBTOTAL":^9}{"SALES TAX":^9}{"TOTAL":^9}')
    print('-------- ---------  -----')
    TAX = .07
    subtotal = .20
    while subtotal <= 5.00:
        subtotal += .20
        sale_tax = subtotal * TAX
        total = sale_tax + subtotal
        print(f'{subtotal:^9.2f}{sale_tax:^9.2f}{total:^9.2f}')
main()
