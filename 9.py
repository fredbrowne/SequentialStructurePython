# Make a program that will take the temperature in Farenheit, convert and show it in Celsius.

farenheit = int(input('Type the temperature in Farenheit: '))
converted_celcius = int((farenheit - 32) * (5/9))
print(f'Temperature Farenheit: {farenheit}°F - Temperature Celcius: {converted_celcius}°C')