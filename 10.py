# Make a Program that will take the temperature in Celsius, convert and show in Farenheit.

celcius = int(input('Type the temperature in Celcius: '))
converted_farenheit = int((celcius * (9/5)) + 32)
print(f'Temperature Celcius: {celcius}°C - Temperature Farenheit: {converted_farenheit}°F')