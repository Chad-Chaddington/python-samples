# Joseph Lipski
# 10/2/2023
# Software Sales program.
# This program will ask the user to enter the amount of packages to be purchased.
# The program will then calculate the discount to be given to the customer
# for buying in bulk. The program will then display the quantity purchased,
# the discount percentage, the total before the discount, the discount amount,
# and the total after the discount.

def main():
    packages_ordered = input_data()
    package_price, package_discount, before_discount, discount_amount, after_discount, discount_percentage \
        = calcs(packages_ordered)
    output(packages_ordered, discount_percentage, before_discount, discount_amount, after_discount)


def input_data():
    packages_ordered = int(input("Please enter the number of packages you are ordering: "))
    return packages_ordered


def calcs(packages_ordered):
    package_price = 99
    package_discount = 0
    if 9 < packages_ordered < 20:
        package_discount = 0.1
    elif 19 < packages_ordered < 50:
        package_discount = 0.2
    elif 49 < packages_ordered <= 99:
        package_discount = 0.3
    elif packages_ordered >= 100:
        package_discount = 0.4
    else:
        package_discount = 0

    before_discount = packages_ordered * package_price
    discount_amount = before_discount * package_discount
    after_discount = before_discount - discount_amount
    discount_percentage = package_discount * 100
    return package_price, package_discount, before_discount, discount_amount, after_discount, discount_percentage


def output(packages_ordered, discount_percentage, before_discount, discount_amount, after_discount):
    print("        Software Sales        ")
    print(f"Quantity Purchased:       {packages_ordered}")
    print(f"Discount Percentage:      {discount_percentage:.0f}%")
    print(f"Package Sales:            ${before_discount:,.2f}")
    print(f"Discount Amount:          ${discount_amount:,.2f}")
    print(f"Overall Sale Total:       ${after_discount:,.2f}")
