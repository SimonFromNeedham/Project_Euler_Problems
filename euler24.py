# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# Recursive helper method that returns !n
def factorial(n):
    if n < 2:
        return 1

    else:
        return n * factorial(n-1)


# I'm proud of this solution, it's original and (IMO) pretty creative
# To find the nth permutation, we search digit by digit, calculating the number of perms that can be generated with
# starting numbers less than the next projected permutation piece, subtracting that number of permutations after each
# new digit is found. Ex: There are 9! * 2 = 725760 < 10**6 (< 9! * 3) perms that can be generated with starting num 0
# or 1, so the first digit must be a 2. By continuing this process until every digit of the permutation is found, we'll
# find the solution without actually calculating any permutations!
if __name__ == '__main__':
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # The nth permutation we're looking for
    n = 10 ** 6

    # Stores each digit of the perm solution
    solution = []

    # Num of perms excluding current digit
    num_perms = factorial(len(digits)-1)

    for i in range(len(digits)-1, 0, -1):
        # Index of the perm's next digit
        index = int(n/num_perms-.01)

        # Add the new digit to the solution
        solution.append(digits.pop(index))

        # New "target" for remaining perms
        n -= num_perms * index

        # Update num_perms, one less digit
        num_perms /= i

    # Append unused (only possible) digit
    solution.append(digits[0])

    # Print solution as an int for clarity
    for digit in solution:
        print(digit, end="")
