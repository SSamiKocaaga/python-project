# variables
condition = False
prime = True
# Receives an input from the user until he/she enters data in the expected format.
while not condition:
    number = input('Write a number: ')
    if number.isdigit():
      condition = True
      number = int(number)
    else:
        print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
# Checks the number If it is a prime number. If it is not, set prime variable False
for i in range(2, number-1):
    if number%i == 0:
        prime = False
        break                        # while loop finds a positive divisor, break ends loop
#Prints whether it is a prime or not.
if prime:
    print("{} is a prime number.".format(number))
else:
    print("{} is not a prime number.".format(number))

