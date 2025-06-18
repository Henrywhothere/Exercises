#tool: generate strong password
#at least 1 uppercase word
#at least 8 symbols
#at least 1 number
#at least 1 special simple


import string
import random


lst_password = []
count = 0 
password = ""
symbol = ['#','@','!','$','%','^','&','*','?']

while count < 8: 
    
    random_symbol = [random.choice(symbol),random.choice(string.ascii_lowercase),
              random.choice(string.ascii_uppercase),str(random.randrange(9))]
    lst_password.append(random.choice(random_symbol))
    count += 1


for i in lst_password:
    password += i

print(f"Your random password is: {password}")