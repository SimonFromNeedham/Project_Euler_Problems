# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Helper method that returns true if the parameter "num" is divisible by all nums in range(max_divider), false otherwise
def divisible(num, max_divider):
    for divider in range(2, max_divider):
        if num % divider != 0:
            return False

    return True


# This brute force method is very inefficient and the only thing in this project that takes more than 10s to complete,
# but ultimately it works within minutes and produces an accurate answer so it's a sufficient solution for the problem
if __name__ == '__main__':
    i = 2520

    # Increment until a divisible number is found
    while not divisible(i, 21):
        i += 1

    print(i)
