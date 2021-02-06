condition = False
prime = False
prime_list = [2]
# Receives an input from the user until he/she enters data in the expected format.
while not condition:
    number = input('Write a number: ')
    if number.isdigit():
      condition = True
      number = int(number)
    else:
        print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

# Checks the number If it is a prime number. If it is not, set prime variable False
for j in range(2, number):
    for i in range(2, j):
        if j%i == 0:   
            prime = False    # if while loop finds a positive divisor, break ends loop
            break 
        else:
            prime = True                 
    if prime == True:
        prime_list.append(j)

print(prime_list)