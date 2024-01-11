# Joseph Lipski 9/13/2023

# This program will ask the user to input a month, day, and year in the format MM/DD/YYYY
# The program will then detect whether the date is magic
# A date is magic if month * day = year
# e.g. 06/10/1960 is a magic date
def main():
    month, day, year = input_data()
    year_formatted = calcs(year)
    output(month, day, year_formatted, year)


def input_data():
    month = int(input("Please enter a month in the (MM) format: "))
    day = int(input("Please enter a day in the (DD) format: "))
    year = int(input("Please enter a year in the (YYYY) format: "))
    return month, day, year


def calcs(year):
    year_formatted = 0
    if year >= 2000:
        year_formatted = year - 2000
    elif year < 2000:
        year_formatted = year - 1900
    return year_formatted


def output(month, day, year_formatted, year):
    if month * day == year_formatted:
        print(f"The date {month}/{day}/{year} is magic!")
    else:
        print(f"The date {month}/{day}/{year} is not magic...")


main()
