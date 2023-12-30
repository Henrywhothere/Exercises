import datetime
import time


invalid = True

while(invalid):
    print("Set a valid time for the alarm (Ex: 6:30)")
    userInput = input("Enter: ")

    timeforalarm = [int(n) for n in userInput.split(":")]

    if timeforalarm[0] >= 24 or timeforalarm[0] < 0:
        invalid = True
    elif timeforalarm[1] >= 60 or timeforalarm[1] < 0:
        invalid = True
    else:
        invalid = False


#seconds in an hour, minute, and second
seconds = [3600, 60, 1]

alarm_seconds = sum([a*b for a,b in zip(seconds[:len(timeforalarm)], timeforalarm)])


now = datetime.datetime.now()
current_seconds = sum([a*b for a,b in zip(seconds, [now.hour, now.minute, now.second])])

untilAlarm = alarm_seconds - current_seconds

if untilAlarm < 0:
    untilAlarm += 86400 #seconds in a day


print("Alarm is set!")
print("The alarm will ring at {}".format(datetime.timedelta(seconds = untilAlarm)))


time.sleep(untilAlarm)
print("Time to wake uppp!")


