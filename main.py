import random


def display_intro():
    print(" " * 27 + "BIG6")
    print(" " * 20 + "CREATIVE COMPUTING")
    print(" " * 18 + "MORRISTOWN, NEW JERSEY")
    print("\n" * 3)
    print("  THIS PROGRAM IS A DICE WHEEL GAME IN WHICH")
    print("YOU CAN BET ON ANY NUMBER BETWEEN ONE AND SIX")
    print("AND UP TO THREE NUMBERS.")
    print("  THE HOUSE LIMIT IS FROM $1 TO $500!!")
    print("TO END THIS PROGRAM TYPE THE WORD 'STOP'.")
    print("GOOD LUCK!\n")


def get_bet_numbers():
    while True:
        try:
            n = input("HOW MANY NUMBERS DO YOU WANT TO BET ON? ")
            if n.strip().upper() == "STOP":
                return "STOP"
            n = int(n)
            if 1 <= n <= 3:
                return n
            print("YOU CANNOT BET ON LESS THAN ONE OR MORE THAN THREE NUMBERS.")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER OR 'STOP'.")


def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num <= 6:
                return num
            print("YOU CAN ONLY BET ON AN INTEGER FROM ONE TO SIX.")
        except ValueError:
            print("PLEASE ENTER A VALID INTEGER.")


def get_wager(prompt):
    while True:
        try:
            wager = int(input(prompt))
            if 1 <= wager <= 500:
                return wager
            print("THE HOUSE LIMIT IS FROM $1 TO $500.")
        except ValueError:
            print("PLEASE ENTER A VALID WAGER AMOUNT.")


def generate_lucky_numbers():
    numbers = [random.randint(1, 6) for _ in range(3)]
    numbers.sort()
    print(f"THE LUCKY NUMBERS ARE: {numbers}")
    return numbers


def process_bet(lucky_numbers, bet_number, wager):
    count = lucky_numbers.count(bet_number)
    if count > 0:
        winnings = wager * count
        print(f"YOU WIN {count} TIMES ON: {bet_number}")
    else:
        winnings = -wager
        print(f"YOU LOSE ON: {bet_number}")
    return winnings


def main():
    display_intro()
    total_winnings = 0

    while True:
        bet_count = get_bet_numbers()
        if bet_count == "STOP":
            break

        bets = []
        wagers = []

        for i in range(bet_count):
            bets.append(get_number(f"WHAT NUMBER {i + 1}? "))
            wagers.append(get_wager(f"WAGER ON NUMBER {i + 1}: "))

        lucky_numbers = generate_lucky_numbers()

        for bet, wager in zip(bets, wagers):
            total_winnings += process_bet(lucky_numbers, bet, wager)

        if total_winnings == 0:
            print("YOU'RE EVEN!!\n")
        elif total_winnings > 0:
            print(f"YOU'RE AHEAD ${total_winnings}\n")
        else:
            print(f"YOU'RE BEHIND ${-total_winnings}\n")

    print("\nSO YOU WANT TO CASH IN YOUR CHIPS, I SEE!!")
    if total_winnings > 0:
        print(f"YOU WON EXACTLY ${total_winnings}!! NOT BAD !!!")
    else:
        print("YOU DIDN'T WIN ANY MONEY, BUT I'M WILLING TO CALL IT EVEN!!")


if __name__ == "__main__":
    main()