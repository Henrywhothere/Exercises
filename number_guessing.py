import random

num_start = int(input("number start: "))
num_end = int(input("number end: "))

number_guess = None
number_random = random.randint(num_start,num_end)

while number_guess != number_random:
    print("please type exact number from {} to {}".format(num_start,num_end))
    number_guess = int(input("type number: "))
    if number_guess < number_random:
        print("You have to guess higher ")
    elif number_guess > number_random:
        print("You have to guess lower ")

print("Congratulations! The player wins")
