cond1, cond2, cond3 = True, True, True
while cond1:
    input1 = input('Are you a cigarette addict older than 75 years old? (yes/no) :')
    if input1.lower() == 'yes':
        age = True
        cond1 = False
    elif input1.lower() == 'no':
        age = False
        cond1 = False
    else:
        print('Wrong input. Try again')
while cond2:
    input2 = input('Do you have a severe chronic disease? (yes/no) :')
    if input2.lower() == 'yes':
        chronic = True
        cond2 = False
    elif input2.lower() == 'no':
        chronic = False
        cond2 = False
    else:
        print('Wrong input. Try again')
while cond3:
    input3 = input('Is your immune system too weak? (yes/no) :')
    if input3.lower() == 'yes':
        immune = True
        cond3 = False
    elif input3.lower() == 'no':
        immune = False
        cond3 = False
    else:
        print('Wrong input. Try again')
if age and chronic and immune:
    print("You are in risky group")
else:
    print("You are not in risky group" )
