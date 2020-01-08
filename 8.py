# Make a program that will ask how much you make by the hour and the number o hours you worked in a month.
# Calculate and show the total of your income for that month.

income_hour = float(input('Type much you make by the hour: '))
hours_month = float(input('Type the number of hours you worked this month: '))

print(f'Your salary this month is {income_hour * hours_month}')