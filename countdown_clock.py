import time




def countdown(minutes):
    count = 0
    while minutes != count:
        minute, second = divmod(minutes, 60)
        print('{:02}:{:02}'.format(minute, second), end = '\n')
        time.sleep(1)
        minutes -= 1
    print('Time out!')
        
        
userInput = int(input("You want to countdown from: "))

countdown(userInput)
