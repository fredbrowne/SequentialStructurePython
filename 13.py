# Having as data input the height (h) of a person, build an algorithm that calculates the ideal weight, using the
# following formulas:   
    # To men: (72.7*h) - 58
    # To women: (62.1*h) - 44.7

h = float(input('Please inform your height in meters: '))
sex = str(input('Please, inform your sex (m = Male, f=Female): '))
if sex == 'm':
    weight = int((72.7 * h) - 50)
elif sex == 'f':
    weight = int((62.1 * h) - 44.7)

print(f'Your ideal weight is {weight}')