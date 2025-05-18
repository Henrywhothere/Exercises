import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    results = []


    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("|".join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 4
        if row[0] == '🍋':
            return bet * 5
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '⭐':
            return bet * 20

    return 0

def main():
    balance = 100

    print("Welcome to Python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while balance > 0:
        print(f'Current balance: ${balance}')

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f'you won ${payout}')
            print("\r")
        else:
            print("Sorry you lost this round")
            print("\r")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ")
        if play_again.upper() != "Y":
            break

        
    print(f'your final balance is ${balance}') 

if __name__ == '__main__':
    main()
