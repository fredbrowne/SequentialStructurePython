# Make a program for a paint store. The program shall ask for the size of square meters of the area to be painted.
# Consider that the paint cover is 1 litre to every 6 square meters and the paint is sold in cans of 18 litres, 
# that cost  R$ 80,00, or gallons of 3,6 litres, that cost R$ 25,00. 
    # Inform the user the quantity of paint cans to be bought and the the full price in 3 scenarios:
    # Buy only cans of 18 litres;
    # Buy only gallons of 3,6 litres;
    # mix cans and gallons, so that the price is cheaper. Add 10% and round the values up, considering as full cans.
import math

painted_area = int(input('Please inform the square meter of the are to be pained: '))
litres = painted_area / 6

total_cans = math.ceil(litres / 18)
total_gallons = math.ceil(litres / 3.6)
can = litres / 18
rem = litres % 18
r1 = can % 1
can = can - r1
rem = rem + r1
gal = math.ceil(rem/3.6)

print(f'You need {total_cans} cans, with the amount of: {total_cans * 80.00}')
print(f'You need {total_gallons} gallons, with the amount of: {total_gallons * 25.00}')
print(f'You need {int(can)} cans and {int(gal)}, total: { (can * 80.00) + (gal * 25.00)}')

