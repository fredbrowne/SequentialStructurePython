# Having as data input the height of a person, build an algorithm that calculates the ideal weight,
# using the following formula: (72.7*height) - 58

height = float(input('Please inform your height in meters: '))
weight = int((72.7 * height) - 50)

print(f'Your ideal weight is {weight}')