# John Fisher-Talk, good man, bought a microcomputer to control his daily income. 
# Everytime he brings fish weighting more then the regulation of São Paulo state (50 kilos) it needs to pay
# a fee of R$ 4.00 for every excess kilo.
# John needs you to write a program that would read a variable weight (fish weight) and calculate the excess.
# Save into excess variable the quantity of kilos beyond the limit and in variable fee the value of the tax
# John will have to pay. Print the data of the program with appropriate messages. 


weight = float(input('Type in the total weight of the fish: '))

if weight > 50.0:
    excess = weight - 50.0
    fee = excess * 4.00
else: 
    excess = 0
    fee = 0

print(f'You have exceed {excess} and should pay {fee}.')