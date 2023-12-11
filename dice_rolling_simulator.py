
import random



def dice_1():
    print("┌─────────┐")
    print("|         |")
    print("|    O    |")
    print("|         |")
    print("└─────────┘")


def dice_2():
    print("┌─────────┐")
    print("|      O  |")
    print("|         |")
    print("|   O     |")
    print("└─────────┘")
    

def dice_3():
    print("┌─────────┐")
    print("| O       |")
    print("|    O    |")
    print("|       O |")
    print("└─────────┘")


def dice_4():
    print("┌─────────┐")
    print("|  O   O  |")
    print("|         |")
    print("|  O   O  |")
    print("└─────────┘")


def dice_5():
    print("┌─────────┐")
    print("|  O   O  |")
    print("|    O    |")
    print("|  O   O  |")
    print("└─────────┘")


def dice_6():
    print("┌─────────┐")
    print("|  O   O  |")
    print("|  O   O  |")
    print("|  O   O  |")
    print("└─────────┘")


def rolling(number):
    if number == 1:
        dice_1()
    elif number == 2:
        dice_2()
    elif number == 3:
        dice_3()
    elif number == 4:
        dice_4()
    elif number == 5:
        dice_5()
    elif number == 6:
            dice_6()



print("How many dice you want to roll?")
number_dice = int(input())
roll = 0

while roll != number_dice:
    roll += 1
    number = random.randint(1,6)
    rolling(number)



