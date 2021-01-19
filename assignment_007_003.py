
# Variables
armvalue = 0
condition = False

# Receives input from the user until he/she enters data in the expected format
while not condition:
    number = input('Write a number: ')
    if number.isdigit():
      condition = True
    else:
        print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")  

list_digits_numbers = list(number)
#calculates whether it is a armstrong number or not.
for i in range(len(list_digits_numbers)):
    armvalue = armvalue + int(list_digits_numbers[i])**len(list_digits_numbers)
if int(number) == armvalue:
    print('{} is an armstrong number'.format(number))
else:
    print('{} is not an armstrong number'.format(number))
