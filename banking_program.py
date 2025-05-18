def show_balance(balance):
    print('your balance is VNĐ {:.2f}'.format(balance))

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("\r")
        print("That's not a valid")
    elif amount >= 0:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("\r")
        print("Insufficent funds")
        return 0
    elif amount <= 0:
        print("\r")
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    running = True
    balance = 0


    while running:
        print("\r")
        print("BANKING PROGRAM")
        print("Type 1 for show balance")
        print("Type 2 for deposit")
        print("Type 3 for withdraw")
        print("Type 4 for exit")
        choice = int(input("Please enter 1-4: "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice >= 4:
            running = False
        else:
            print("That's not valid choice")

    
    print("\r")        
    print("Thank you! have a nice day")


if __name__ == '__main__':
    main() 
