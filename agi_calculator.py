# Joseph Lipski
# Basic 'while loop' demonstration.
# This program will prompt the user to enter their monthly income. It will then ask if
# the user has another source of income to input. The program will repeat this action
# until the user inputs 'N'. The program will then start another loop, which asks
# the user to enter their monthly expenses. The program will ask if there are any
# other expenses to enter, and will loop until the user inputs 'N'. The program will
# then calculate the user's adjusted gross income (agi), and display their total income,
# total expenses, and left over income.

income = 0
expense = 0
total_income = 0
total_expenses = 0
inc_loop = "Y"
exp_loop = "Y"
while inc_loop == "Y":
    income = float(input("Please enter your monthly income: "))
    total_income += income
    inc_loop = input("Do you have another source of income to enter? (Y/N): ")
    if inc_loop == "N":
        break
while exp_loop == "Y":
    expense = float(input("Please enter your monthly expenses: "))
    total_expenses += expense
    exp_loop = input("Do you have any other expenses to enter? (Y/N): ")
    if exp_loop == "N":
        break

agi = total_income - total_expenses

print(f"Total monthly income: ${total_income:,.2f}")
print(f"Total monthly expenses: ${total_expenses:,.2f}")
print(f"Monthly income left over: ${agi:,.2f}")
