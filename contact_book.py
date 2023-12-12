def welcome():
    typenumber = int(input('''

                        1. Show
                        2. Add
                        3. Check
                        4. Delete
                        5. Quit

                        enter your number: '''))

    return typenumber

def phonebook():
    contacts = []
    while True:
        typenumber = welcome()
        #show function
        if typenumber == 1:
            f = open("directory.txt", 'r', encoding="utf-8")
            contacts = f.readlines()
            f.close()
            if not contacts:
                print("empty directory")
            else:
                for i in contacts:
                    print(i)
        #add function
        elif typenumber == 2:
            checked = False
            phone_number = input("phone number: ")
            contact_name = input("contact name: ")
            f = open("directory.txt", 'r', encoding = "utf-8")
            contacts = f.readlines()
            f.close()
            for i in contacts:
                if i.find(contact_name) != -1:
                    print('Contact already exists')
                    checked = True
                    break
            if checked == False:
                f = open('directory.txt', 'a', encoding='utf-8')
                contacts.append(contact_name + ": " + phone_number + "\n" + "\n")
                contacts = f.write(contacts[-1])
                f.close()
                print("Contact has been saved!")
        #check function
        elif typenumber == 3:
            checked = False
            f = open("directory.txt", 'r', encoding = 'utf-8')
            contacts = f.readlines()
            f.close()
            name = input("type contact name: ")
            for i in contacts:
                if i.find(name) != -1:
                    print(i)
                    checked = True
                    break
            if checked == False:
                print("contact does not exist")
        #delete function
        elif typenumber == 4:
            checked = False
            delete_var = 0
            f = open("directory.txt", 'r', encoding = 'utf-8')
            contacts = f.readlines()
            f.close()
            name = input('type contact name: ')
            for i in contacts:
                if i.find(name) != -1:
                    print(i)
                    delete_var = contacts.index(i)
                    checked = True
                    confirm = input("Are you sure you want to delete? Y/N:")
                    if confirm.capitalize() == "Y":
                        contacts.pop(delete_var)
                        f = open('directory.txt', 'w', encoding = 'utf-8')
                        for i in contacts:
                            f.write(i)
                        f.close()
                    else:
                        print("Return to the main screen!")
                    break
            if checked == False:
                print('Contact does not exist')
        #quit function
        elif typenumber == 5:
            print('Thank you!')
            break
        else:
            print('Type again!')

phonebook()
