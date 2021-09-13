# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2... = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n,
# and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.

# By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.

# However, this upper limit cannot be reduced any further by analysis even though it is known that:
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

MAX_N = 28123


# Helper method that returns a list of every divisor of n
def get_divisors(n):
    divisors = []

    for i in range(1, int(n/2)+1):
        if n % i == 0:
            divisors.append(i)

    return divisors


if __name__ == '__main__':
    total = 0

    # Integer list of abundant numbers up to but not including MAX_N
    abundant_nums = []

    # Each entry represents weather that entry's index is is an abundant sum
    abundant_sums = [False for i in range(MAX_N)]

    # Abundant sum sieve:
    for n in range(1, MAX_N):
        # If int n is abundant...
        if sum(get_divisors(n)) > n:
            abundant_nums.append(n)

            for abundant_n in abundant_nums:
                # Avoid IndexOutOfBounds errors
                if abundant_n + n < MAX_N:
                    abundant_sums[abundant_n + n] = True

    for i in range(1, len(abundant_sums)):
        # We're only counting sums that are NOT abundant
        if not abundant_sums[i]:
            total += i

    print(total)
