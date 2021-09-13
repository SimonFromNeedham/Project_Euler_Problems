# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!


MAX_FACTOR = 100


# Using a similar approach to Euler16...
# I'm aware that this approach is more complex than necessary and that I could just use a long to store the number,
# But I honestly find it a lot more interesting to work through the problem trying to save memory by using an array
if __name__ == '__main__':
    # Use an array instead of an int/long to store the number because
    # with hundreds of digits, the latter would take up a ton of memory
    digits = [1]

    for factor in range(2, MAX_FACTOR+1):
        for i in range(len(digits)):
            digits[i] *= factor

        # Insert new digit places before modular arithmetic to avoid IndexOutOfBounds errors
        # Reverse to get the biggest places last --> they'll be inserted into the array first
        first_digit_str = str(digits[0])[::-1]

        for i in range(1, len(first_digit_str)):
            digits.insert(0, int(first_digit_str[i]))

        # % 10 to avoid adding places twice
        digits[len(first_digit_str)-1] %= 10

        # Distribute places for every digit
        for i in range(len(digits)-1, 0, -1):
            digit_str = str(digits[i])[::-1]

            # Instantiate j == 0 to avoid counting the ones place twice,
            for j in range(1, len(digit_str)):
                digits[i-j] += int(digit_str[j])

            digits[i] %= 10

    print(sum(digits))
