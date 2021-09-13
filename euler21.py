# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


MAX_N = 10000


# Helper method that returns a list of every divisor of n
def get_divisors(n):
    divisors = []

    for i in range(1, int(n/2)+1):
        if n % i == 0:
            divisors.append(i)

    return divisors


if __name__ == "__main__":
    total = 0

    for n in range(MAX_N):
        compliment = sum(get_divisors(n))

        if n != compliment and n == sum(get_divisors(compliment)):
            # Don't add compliment because it will be counted as "n" later
            total += n

    # I could write some fancy code to ensure that each pair was only counted once,
    # but this is efficient enough considering how rare amicable pairs actually are
    print(total)
