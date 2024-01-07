import tkinter as tk
import random


root = tk.Tk()
root.geometry('500x500')
root.title("Welcome to Spin a Yarn")


#create the first sentence for the story
#create the label to display the story starter
storyLabel1 = tk.Label(root, text= "Press the button below to start the first sentence...", font = 'arial 11')
storyLabel1.place(x=60, y=80)
    
#create the button to spin the yarn
spinButton1 = tk.Button(root, text="PRESS HERE", command=lambda: spinYarn1(), font = 'arial 11')
spinButton1.place(x=150, y=100)
    


storyStarters1 = [
        "Once upon a time, there was a brave knight who saved a princess from a dragon.",
        "A young man set out on a journey to find his true calling.",
        "A man went on an adventure to find a lost treasure.",
        "A scientist invented a machine that could travel through time.",
        "A detective solved a mystery that had baffled the police for years."]


    #create randomly select a story starter
def spinYarn1():
    storyText = random.choice(storyStarters1)
    return storyText






#create the second sentence for the story
storyLabel2 = tk.Label(root, text = "Press the button below to start the second setence...", font = 'arial 11')
storyLabel2.place(x=60, y=180)
    
spinButton2 = tk.Button(root, text="PRESS HERE", command=lambda:spinYarn2(), font = 'arial 11')
spinButton2.place(x=150, y=200)
    


storyStarters2 = [
        " And he took a treasure mirror and brought it back to the king.",
        " On the way he met a princess.",
        " And the treasure is kept in a secret location on the deadly island.",
        " He was chased by a herd of dinosaurs.",
        " This embarrassed the police court with its incompetence."]


    #create randomly select a story starter
def spinYarn2():
    storyText = random.choice(storyStarters2)
    return storyText
    





#create the third sentence for the story
storyLabel3 = tk.Label(root, text = "Press the button below to start the third setence...", font='arial 11')
storyLabel3.place(x=60, y=280)
    
spinButton3 = tk.Button(root, text="PRESS HERE", command=lambda:spinYarn3(), font = 'arial 11')
spinButton3.place(x=150, y=300)
    


storyStarters3 = [
        " And then the king killed him right in the palace...",
        " He was very surprised and ran away into the forest.",
        " No one knows about it, except an evil witch.",
        " Suddenly he saw an ancient man.",
        " So they decided to arrest this man."]


    #create randomly select a story starter
def spinYarn3():
    storyText = random.choice(storyStarters3)
    return storyText
    




final = tk.Label(root, text = "Press the button below to see what your final story is...", font = 'arial 11')
final.place(x=60, y=380)

finalButton = tk.Button(root, text = "PRESS HERE", command=lambda:connectStory(), font = 'arial 11')
finalButton.place(x=150, y=400)




def connectStory():
    finalStory = spinYarn1() + spinYarn2() + spinYarn3()
    final.config(text=finalStory)





root.mainloop()











    
