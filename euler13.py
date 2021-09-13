# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (euler13_number).


if __name__ == '__main__':
    total = 0

    # Read in the large number lines as a string
    nums = open('euler13_number.txt').readlines()

    for line in nums:
        total += int(line)

    print("First 10 digits: " + str(total)[:10])
