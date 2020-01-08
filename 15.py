# Make a program that will ask you how much you make by the hour and number of hours worked in a month. 
# Calculate and display the Gross Salary for that month, knowing that the following discounts should be added
# 11% for FISCO Tax, 8% for INSS and 5% for the union, make a program that shows:
    #gross salary.
    #how much INSS tax.
    #how much for the union.
    #net salary.
    #calculate the discounts and net salary using below information:
    #+ Gross Salary : R$
    #- IR (11%) : R$
    #- INSS (8%) : R$
    #- Union ( 5%) : R$
    #= Net Salary : R$
    #Obs.: Gross Salary - Discounts = Net Salary.

income_hour = float(input('Type much you make by the hour: '))
hours_month = float(input('Type the number of hours you worked this month: '))
gross_salary = income_hour * hours_month
ir = gross_salary * (11/100)
inss = gross_salary * (8/100)
union = gross_salary * (5/100)
net_salary = gross_salary - ir - inss - union

print(f'Gross Salary: R$ {gross_salary}')
print(f'IR: R$ {ir}')
print(f'INSS: R$ {inss}')
print(f'Union: R$ {union}')
print(f'Net salary: R$ {net_salary}')