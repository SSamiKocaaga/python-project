def isleapyear(x):
    a = int(x)
    if a%4 != 0:
        print(a, "is not a leap year.")
    elif a%100 == 0 and not a%400 == 0:
        print(a, "is not a leap year.")
    elif a%400 == 0:
        print(a, "is a leap year.")
    else:
        print(a, "is a leap year.")
isleapyear(input('Write a year? '))