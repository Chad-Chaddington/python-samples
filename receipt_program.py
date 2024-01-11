# Joseph Lipski
# 10/13/2023
# This program will take the user's email address,
# the price of their items, and a date, and build a receipt from these items.

# Datetime to validate dates
from datetime import datetime
# Regex is to help with email validation
import re


def main():
    validate_email(email)
    user_date = validate_date()
    item1, item2 = number_input()
    subtotal, tax, tip, total_cost = calcs(item1, item2)
    output(item1, item2, tax, tip, subtotal, total_cost, user_date)


# This is the section that accepts and validates the user's email.
def validate_email(email):
    # This if statement is just ensuring the email does not contain an @ anywhere except the middle.
    # It also makes sure there is at least one period for the .com portion.
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        # If it matches the above criteria, it returns true, otherwise, it loops and returns false.
        return True
    return False


while True:
    # This is where the email is accepted. It's accepted inside the loop to
    # ensure that the program will continue to ask for input if the email is invalid.
    email = input("Please enter your email: ")
    if validate_email(email):
        # Calling our function to compare the email.
        # If it comes back a match, the program displays that it is valid.
        print(f"The email {email} is valid.")
        break
    else:
        # If it's not a match, the program displays that the email is invalid.
        print(f"The email {email} is invalid. Please try again.")
        continue


def validate_date():
    # This is where the date is input and compared.
    while True:
        try:
            # The date is input below.
            user_date = input("Please enter today's date: ")
            # This compares the date to our format (MM/DD/YYYY) to ensure it was entered correctly.
            datetime.strptime(user_date, '%m/%d/%Y')
            print(f"The date is {user_date}")
            break
        except ValueError:
            # If the date was not entered correctly, the blow executes.
            print(f"The date {user_date} is invalid, please try again! ")
            continue
    return user_date


def number_input():
    while True:
        try:
            # Getting price of item 1 from our user
            item1 = float(input("Please enter the cost of your first item: "))
            break
        except Exception as e:
            # This is here to ensure a number is entered. If a letter is entered, the program will make the user
            # try again.
            print("You didn't enter a number, try again. ")
    while True:
        try:
            # Obtaining price of item 2
            item2 = float(input("Please enter the cost of your second item: "))
            break
        except Exception as e:
            # Same exception clause as above. Ensuring that a number is entered.
            print("You didn't enter a number, try again. ")
    return item1, item2


def calcs(item1, item2):
    # Calculating our subtotal, tax, tip, and final total
    subtotal = item1 + item2
    tax = 0.07 * subtotal
    tip = 0.16 * subtotal
    total_cost = subtotal + tax + tip
    return subtotal, tax, tip, total_cost


def output(item1, item2, tax, tip, subtotal, total_cost, user_date):
    # The following should output like an actual receipt.
    print("                MEAL RECEIPT           ")
    print(f"{user_date}                 {email}")
    print()
    print()
    print(f"ITEM 1: ${item1:.2f}            ITEM 2: ${item2:.2f}")
    print(f"TAX (7%): ${tax:.2f}            TIP (16%): {tip:.2f}")
    print(f"SUBTOTAL: ${subtotal:.2f}       TOTAL: ${total_cost:.2f}")
    print("                 THANK YOU           ")


main()
