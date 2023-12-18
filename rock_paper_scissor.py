import random


#s for scissor
#r for rock
#p for paper
computer = random.choice(['s', 'r', 'p'])

user = input("Type your choose (r/p/s): ")
print(computer)

if (user == 's' and computer == 'p') or (user == 'r' and computer == 's') or (user == 'p' and computer == 'r'):
    print('you win!')
elif user == computer:
    print('Tie!')
else:
    print('you loose!')
