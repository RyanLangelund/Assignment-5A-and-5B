"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

"""
Assignment 5A - Input validation
Intro to Python
Description- Trip Registration form with input validation
"""
first_name = input("Enter First Name:")
while first_name == "":
    print("First Name cannot be blank.")
    first_name = input("Please enter First Name:")

last_name = input("Enter Last Name:")
while last_name == "":
    print("Last Name cannot be blank.")
    last_name = input("Please enter Last Name: ")

chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("Please enter only Y or N.")
    chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()

phone = input("Enter Phone Number")
while phone == "":
    print("Phone Number cannot be blank")
    phone = input("Please enter Phone Number")

tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break
        print("Must be at least 1 ticket.")
    except ValueError:
        print("Please enter a NUMBER (e.g., 5, not 'five').")

print(f"{first_name} Ordered {tickets} tickets.")
