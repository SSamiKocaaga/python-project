UserName = 'Sami'
Password = '4sftd'
Entered = input()
if Entered == UserName:
    print('Hello {}! The password is : {} '.format(Entered, Password))
else:
    print('Hello {}! See you later.'.format(Entered))