
#Người dùng sẽ nhập thức ăn và lượng calo của thức ăn đó vào, nó sẽ được lưu vào file, hệ thống sẽ tính tổng calo bữa ăn và tổng calo một ngày của người dùng sau đó ghi chép vào một file
#Hệ thống cũng sẽ chỉ ra số calo cần trừ đi hay cộng thêm sau mỗi bữa ăn dựa trên: cân nặng, chiều cao, mức độ tập luyện
#hệ thống tính luôn chỉ số BMR, AMR


#note for user
#1kg = 7700 calo
#1g protein = 4 calo
#1g carbohydrate = 4 calo
#1g fat = 9 calo

import datetime

def BMR(sex, weight, height, age):
    BMR = 0
    if sex.title() == 'Male':
        BMR = 10*weight + 6.25*height - 5*age + 5
    elif sex.title() == 'Female':
        BMR = 10*weight + 6.25*height - 5*age - 165
        
    return round(BMR,1)


def AMR(userBMR, activity):
    AMR = 0
    workoutnumber = 0
    if activity.title() == 'Always':
        workoutnumber = 1.9
    elif activity.title() == 'Usually':
        workoutnumber = 1.725
    elif activity.title() == 'Often':
        workoutnumber = 1.55
    elif activity.title() == 'Sometimes':
        workoutnumber = 1.375
    elif activity.title() == 'Rarely':
        workoutnumber = 1.2

    AMR = userBMR*workoutnumber
    return round(AMR,1)



def countingcalo(tdee):
    print('\n')
    print("You can look up the calories in foods on the website: https://www.calories.info/ ")
    print("Some notes for you: ")
    print('1g protein = 4 calo')
    print('1g carbohydrate = 4 calo')
    print('1g fat = 9 calo')
    print('Prepared food is considered a food')
    print('\n')
    

    dictmorningcalo = {}
    dictlunchcalo = {}
    dictnightcalo = {}



    #counting calorie for morning meal
    morning = int(input('Number of foods in your morning: '))

    for i in range(0, morning):
        morningfood = input('Food name: ')
        morningcalo = int(input('Calories: '))
        dictmorningcalo.update({morningfood : morningcalo})
        morningcalomeal = sum(dictmorningcalo.values())
        resultmorningcalo = "\rCalorie morning: {}".format(morningcalomeal)
    


   
    #counting calorie for lunch meal
    lunch = int(input('Number of foods in your lunch: '))

    for i in range(0, lunch):
        lunchfood = input('Food name: ')
        lunchcalo = int(input('Calories: '))
        dictlunchcalo.update({lunchfood : lunchcalo})
        lunchcalomeal = sum(dictlunchcalo.values())
        resultlunchcalo = "\rCalorie lunch: {}".format(lunchcalomeal)



    
    #counting calorie for night meal
    night = int(input('Number of foods in your night: '))
    for i in range(0, night):
        nightfood = input('Food name: ')
        nightcalo = int(input('Calories: '))
        dictnightcalo.update({nightfood : nightcalo})
        nightcalomeal = sum(dictnightcalo.values())
        resultnightcalo = "\rCalorie night: {}".format(nightcalomeal)


    daycalo = morningcalomeal + lunchcalomeal + nightcalomeal
    resultdaycalo = "\rCalorie day: {}".format(daycalo)

    
    #balance function
    
    print('\n')
    print('Please enter your goals for the calorie balance program')                 
    goal = input('Losing weight / Weight gain / Maintain Weight (losing/gain/maintain): ')
    calorie = 0
    
    if goal.title() == 'Losing':
        if daycalo < tdee:
            result = '\rYou lose weight successfully!'
        elif daycalo > tdee:
            calorie = daycalo - tdee
            result = '\rYou need to eat less than {} calories'.format(calorie)
        elif daycalo == tdee:
            result = '\rYour total calories a day should be less than {} calories'.format(tdee)
            
    elif goal.title() == 'Gain':
        if daycalo < tdee:
            calorie = tdee - daycalo
            result = '\rYou need to eat more than {} calories'.format(calorie)
        elif daycalo > tdee:
            result = '\rYou have successfully gained weight!'
        elif daycalo == tdee:
            result = '\rYour total calories today should be more than {} calories'.format(tdee)
        
    elif goal.title() == 'Maintain':
        if daycalo < tdee:
            calorie = tdee - daycalo
            result = '\rYou need to gain {} calories'.format(calorie)
        elif daycalo > tdee:
            calorie = daycalo - tdee
            result = '\rYou need to loose {} calories'.format(calorie)
        elif daycalo == tdee:
            result = '\rYou maintain your weight successfully'


    
    datemonth = datetime.datetime.now()


    return datemonth.strftime("%x"), resultmorningcalo, resultlunchcalo, resultnightcalo, resultdaycalo, result
    
        

#save function
def Calosave(datemonth, resultmorningcalo, resultlunchcalo, resultnightcalo, resultdaycalo, result):
    with open('historyCALO.txt', 'a+') as filein:
        filein.write('\r')
        filein.write(datemonth)
        filein.write(resultmorningcalo)
        filein.write(resultlunchcalo)
        filein.write(resultnightcalo)
        filein.write(resultdaycalo)
        filein.write(result)
        filein.write('\r')
        filein.close()

    print('Saved successfully!')
    




   
        









#user type




name = input('Your name: ')
sex = input('Your gender (Male/Female): ')
weight = int(input('Your weight: '))
height = int(input('Your height (cm): '))
age = int(input('Your age: '))
activity = input('Your activity (Always (practice twice a day); Usually (6-7 sessions/week); Often (4-5 sessions/week); Sometimes (1-3 sessions/week); Rarely(eating, working and sleeping): ')



print('\n')
print("Type 'start' to start counting your BMR, AMR and TDEE")
print("***If you already have BMR, AMR, TDDE Indexes you can skip 'start' and enter '5' to add the indexes***")

user  = input('Please enter: ')

userBMR = 0
userAMR = 0
userTDEE = 0
if user.title() == 'Start':
    userBMR = BMR(sex, weight, height, age) 
    print("Your BMR: ", userBMR, "(BMR: metabolic rate index)")
    userAMR = AMR(userBMR,activity)
    print("Your AMR: ", userAMR, "(AMR: calorie consumption index)")
    userTDEE = userBMR + userAMR
    print("Your TDEE: ", round(userTDEE,1), "(TDEE: total energy consumed one day)")

elif user.title() == '5':
    userBMR = int(input('Type your BMR: '))
    userAMR = int(input('Type your AMR: '))
    userTDEE = int(input('Type your TDEE: '))



print('\n')
print("Enter 'start' for the program to calculate the calories of your meals today")
print("Type 'end' to end the program")
nextstep = input('Please enter: ')

if nextstep.title() == 'Start':
    countResult = countingcalo(userTDEE)
    date = countResult[0]
    morningResult = countResult[1]
    lunchResult = countResult[2]
    nightResult = countResult[3]
    dayResult = countResult[4]
    finalResult = countResult[5]
    print(date)
    print(morningResult)
    print(lunchResult)
    print(nightResult)
    print(dayResult)
    print(finalResult)
    print('\n')
    print('Do you want to save this results?')
    checkagain = input("Please enter 'yes' or 'no': ")
    if checkagain.title() == 'Yes':
        Calosave(date, morningResult, lunchResult, nightResult, dayResult, finalResult)
    elif checkagain.title() == 'No':
        print('Program end')
elif nextstep.title() == 'End':
    print('Program end')
