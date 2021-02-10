listofchars = list(input("Write a sentence: "))
uniquechars = list(set(listofchars))
my_dict = {}
# solution one
for i in uniquechars:
    my_dict[i] = listofchars.count(i)
print(my_dict)
# solution 2
print({i:listofchars.count(i) for i in uniquechars})
