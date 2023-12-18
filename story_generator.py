import random


#list for short sentence
setence_starter = []
character1 = []
timeline = []
story_plot = []
place = []
age = []
job = []





#type number sentence and what is sentence
setenceStarter_type = int(input("How many setence starter do you want?: "))
for number_ss in range(setenceStarter_type):
    type_setenceStarter = input("Sentence is: ")
    setence_starter.append(type_setenceStarter)


print("\n")
    

character1_type = int(input("How many character do you want?: "))
for number_cha1 in range(character1_type):
    type_character1 = input("Character 1 is: ")
    character1.append(type_character1)


print("\n")


timeline_type = int(input("How many timeline do you want?: "))
for number_timeline in range(timeline_type):
    type_timeline = input("Timeline is: ")
    timeline.append(type_timeline)


print("\n")


storyPlot_type = int(input("How many story plot do you want?: "))
for number_storyPlot in range(storyPlot_type):
    type_storyPlot = input("Story plot is: ")
    story_plot.append(type_storyPlot)


print("\n")


place_type = int(input("How many place do you want?: "))
for number_place in range(place_type):
    type_place = input("Place is: ")
    place.append(type_place)

print("\n")


age_type = int(input("How many age do you want?: "))
for number_age in range(age_type):
    type_age = input("Age is: ")
    age.append(type_age)

print("\n")

job_type = int(input("How many job do you want?: "))
for number_job in range(job_type):
    type_job = input("Job is: ")
    job.append(type_job)

print("\n")


#pick random sentences and print they

if __name__ == '__main__':
    random_ss = random.choice(setence_starter)
    random_cha1 = random.choice(character1)
    random_time = random.choice(timeline)
    random_storyplot = random.choice(story_plot)
    random_place = random.choice(place)
    random_age = random.choice(age)
    random_job = random.choice(job)

    print("{} {} {} {} {} {} {}".format(random_ss, random_cha1, random_time, random_storyplot, random_place, random_age, random_job))
