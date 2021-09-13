# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers complies with British usage.


if __name__ == '__main__':
    # The basic digits which make up the ones place in all other numbers
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # Teens have unique names not directly associated with the basic digits
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]

    # Additional lists of numbers that represent the tens and hundreds places
    tens = ["", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # No space between digit, "hundred", and "and" makes counting w/o spaces easier
    hundreds = [digit + "hundred" + "and" for digit in digits]

    # Numbers below 100 have no digit in their hundreds place --> empty string
    hundreds[0] = ""

    # A list of every number (not in order), as a string, between 1 and 1000 (e.g. 215 as "two-hundred and fifteen")
    # While the code could be written more efficiently without this array, including it lets us see numbers generated
    nums_as_strings = []

    for hundred in hundreds:
        # Separate construction for teens and "normal" numbers
        for teen in teens:
            nums_as_strings.append(hundred + teen)

        for ten in tens:
            for digit in digits:
                if ten == "" and digit == "":
                    # No "and" w/o tens or ones digit
                    nums_as_strings.append(hundred[:-3])

                else:
                    # Standard three-digit number construction
                    nums_as_strings.append(hundred + ten + digit)

    # 1000 hasn't been constructed yet
    nums_as_strings.append("onethousand")

    print(sum(len(num) for num in nums_as_strings))
