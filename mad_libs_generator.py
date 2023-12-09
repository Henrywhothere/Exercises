from tkinter import *



# create topics
def sport():
    name = input('Enter name: ')
    age = input('Enter age: ')
    sport = input('Enter sport: ')
    place = input('Enter place: ')
    verb = input('Enter verb in -ing form: ')
    person = input('Enter person you like: ')
    print("My name is " + name + ",I'm " + age + " now. I like " + sport + ", so I usually play it with " + person + " at " + place + ". Yeah, now you can see I'm" + verb)
    
def work():
    name = input('Enter name: ')
    age = input('Enter age: ')
    job = input('Enter job: ')
    place = input('Enter place: ')
    verb = input('Enter verb in -ing form: ')
    person = input('Enter person you like: ')
    print("My name is " + name + ",I'm " + age + " now. I do " + job + ", I usually do it with " + person + " at " + place + ". now, I'm " + verb + ", so please leave me alone.")

def education():
    name = input('Enter name: ')
    age = input('Enter age: ')
    subject = input('Enter subject: ')
    place = input('Enter place: ')
    verb = input('Enter verb in -ing form: ')
    person = input('Enter person you like: ')
    print("My name is " + name + ",I'm " + age + " now. I like study " + subject + ", I usually study it with " + person + " at " + place + ". But I'm not " + verb + " now, see you later.")

def business():
    name = input('Enter name: ')
    age = input('Enter age: ')
    company = input('Enter company ')
    place = input('Enter place: ')
    verb = input('Enter verb in -ing form: ')
    person = input('Enter person you like: ')
    print("My name is " + name + ",I'm " + age + " now. I work in " + company + ". I want to work with " + person + " at " + place + ", but he/she doesn't want to. I'm very sad about that."
          + "Now I'm " + verb  + " so can you go outside?")

def food():
    name = input('Enter name: ')
    age = input('Enter age: ')
    food = input('Enter food: ')
    place = input('Enter place: ')
    verb = input('Enter verb in -ing form: ')
    person = input('Enter person you like: ')
    print("My name is " + name + ",I'm " + age + " now. I like eat " + food + ", I usually eat them with " + person + " at " + place + ". now, I'm" + verb + ", so can we talk later?")



#create button

namewin = Tk()
namewin.geometry('500x500')
namewin.title('Mad libs generator')
Label(namewin, text = 'Have fun with Mad libs generator', font = 'arial 20 bold').pack()
Label(namewin, text = 'Choose the topic you want:', font = 'arial 17').place(x = 40, y = 80)


Button(namewin, text= 'Sport', font ='arial 15', command= sport, bg = 'ghost white').place(x=60, y=120)
Button(namewin, text= 'Work', font ='arial 15', command = work , bg = 'ghost white').place(x=60, y=180)
Button(namewin, text= 'Education', font ='arial 15', command = education, bg = 'ghost white').place(x=60, y=240)
Button(namewin, text= 'Business', font ='arial 15', command = business, bg = 'ghost white').place(x=60, y=300)
Button(namewin, text= 'Food', font ='arial 15', command = food, bg = 'ghost white').place(x=60, y=360)

namewin.mainloop()
