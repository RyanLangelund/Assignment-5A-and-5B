"""
Assignment 5B - The ATM
Intro to Python
"""

balance = 1000

while True:

    print("ATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    choice = input("Select an option: ")

    match choice:

        case "1":
            print(f"Current Balance: ${balance:.2f}")

        case "2":
            amount = input("Enter deposit amount: ")

            if amount.isdigit():
                amount = int(amount)

                if amount > 0:
                    balance = balance + amount
                    print(f"Deposit successful. New Balance: ${balance:.2f}")
                else:
                    print("Amount must be positive.")
            else:
                print("Invalid input.")

        case "3":
            amount = input("Enter withdrawal amount: ")

            if amount.isdigit():
                amount = int(amount)

                if amount > 0:
                    if amount <= balance:
                        balance = balance - amount
                        print(f"Withdrawal successful. New Balance: ${balance:.2f}")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Amount must be positive.")
            else:
                print("Invalid input.")

        case "4":
            amount = input("Enter transfer amount: ")

            if amount.isdigit():
                amount = int(amount)

                if amount > 0:
                    if amount <= balance:
                        balance = balance - amount
                        print(f"Transfer successful. New Balance: ${balance:.2f}")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Amount must be positive.")
            else:
                print("Invalid input.")

        case "5":
            print("Goodbye.")
            break

        case _:
            print("Invalid selection.")
