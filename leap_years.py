def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False




year = int(input("Enter year: "))

if leap_year(year):
    print("{} is leap year".format(year))
else:
    print("{} is not leap year".format(year))



