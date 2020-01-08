# Make a program for a paint store. The program shall ask for the size of square meters of the area to be painted.
# Consider that the paint cover is 1 litre to every 3 square meters and the paint is sold in cans of 18 litres, 
# that cost  R$ 80,00. Inform the user the quantity of paint cans to be bought and the the full price.

painted_area = int(input('Please inform the square meter of the are to be pained: '))
litres = painted_area / 3

if litres < 18:
    print('1 Can of 18 litres needed: R$ 80,00')
else: 
    total_cans = round(litres / 18)
    print(f'You need {total_cans}, with the amount of: {total_cans * 80.00}')