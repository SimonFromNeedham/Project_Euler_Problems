# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


# I'm aware that this approach is more complex than necessary and that I could just use a long to store the number,
# But I honestly find it a lot more interesting to work through the problem trying to save memory by using an array
if __name__ == '__main__':
    # Use an array instead of an int/long to store the number because
    # with hundreds of digits, the latter would take up a ton of memory
    digits = [1]

    for i in range(1000):
        digits[0] *= 2

        if digits[0] > 9:
            digits[0] %= 10
            digits.insert(0, 1)

        # If the first digit == 1, then the second digit was already doubled because
        # the higher digit (> 10) was "carried" over to the next digit --> inserted at index 0
        for j in range(1 if digits[0] != 1 else 2, len(digits)):
            digits[j] *= 2

            if digits[j] > 9:
                digits[j] %= 10
                digits[j-1] += 1

    print(sum(digits))
