# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# I know I could use the calender module to solve the problem, but this is much more interesting approach:
FIRST_YEAR = 1901
LAST_YEAR = 2000


if __name__ == '__main__':
    # The days in each month according to the rhyme
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_sundays = 0

    # Days since Jan 1st on FIRST_YEAR + first day
    # Let 1 == Monday, 2 == Tuesday, 3... 7 == Sunday
    # Initialized at 2 because Jan 1st, 1901 is a Tuesday
    days_since = 2

    for year in range(FIRST_YEAR, LAST_YEAR+1):
        if year % 4 == 0 and year % 400 != 0:
            months[1] += 1

        # If last year was a leap year...
        elif year % 4 == 1 and months[1] > 28:
            months[1] -= 1

        for month in months:
            # Check for Sundays at the beginning of each month
            if days_since % 7 == 0:
                num_sundays += 1

            # Increase days_since by the number of days in each month
            days_since += month

    print(num_sundays)
