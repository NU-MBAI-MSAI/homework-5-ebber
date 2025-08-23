

# The function is_leap_year determines whether a given year is a leap year.
# According to the leap year rules:
# - A year is a leap year if it is divisible by 4 and not divisible by 100,
#   or if it is divisible by 400.
# For example, 2000 and 2400 are leap years, but 1900 and 2100 are not.
# The function returns True if the year is a leap year, otherwise False.


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
