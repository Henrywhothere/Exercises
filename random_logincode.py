


import random
import string


#creat random login code sequence

listloginCode = list(string.ascii_uppercase)



for number in range(0, 10):
    listloginCode.append(number)
    

num1 = random.choice(listloginCode)
num2 = random.choice(listloginCode)
num3 = random.choice(listloginCode)
num4 = random.choice(listloginCode)



dictaccount = {'luanthuan':'220402'}
dict_user = dictaccount.keys()
dict_password = dictaccount.values()



user = input('User: ')
password = input('Password: ')


#if user or password success
if user in dict_user and password in dict_password:
    loginCode = "{}{}{}{}".format(num1, num2, num3, num4)
    print(loginCode)
    typeCode = input('Type login code: ')
    if typeCode == loginCode:
        print('Logged in successfully!')
    else:
        while typeCode != loginCode:
            print('Login failed!')
            typeCode = input('Type login code again: ')
        print('Logged in successfully')


#if user or password wrong         
else:
    while user not in dict_user or password not in dict_password:
        print('Your account or password is incorrect!')
        user = input('User: ')
        password = input('Password: ')
        

    loginCode = "{}{}{}{}".format(num1, num2, num3, num4)
    print(loginCode)
    typeCode = input('Type login code: ')
    if typeCode == loginCode:
        print('Logged in successfully!')
    else:
        while typeCode != loginCode:
            print('Login failed')
            print(loginCode)
            typeCode = input('Type login code: ')
        print('Logged in successfully!')
