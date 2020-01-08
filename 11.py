# Make a program that will ask for 2 integers and 1 float. Calculate and show:
    # the product of the double for the first number with half the second number
    # sum the triple of the first number with the third number
    # third number cubed

num1 = int(input('Type an integer number: '))
num2 = int(input('Type another integer number: '))
num3 = float(input('Type a float (decimal) number: '))

calc_product = (num1*num1) * (num2/2)
calc_sum = (num1*3) + (num3)
calc_cube = num3 ** 3

print(f'Product of the double for the first with half the second: {calc_product}')
print(f'Sum the triple of the first with the third: {calc_sum}')
print(f'Third number cubed: {calc_cube}')