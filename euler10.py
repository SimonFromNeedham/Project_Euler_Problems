# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# Helper methods which implements of the Sieve of Eratosthenes to find all primes up to "num"
def sieve(num):
    # Each entry represents weather or not that entry's index is prime
    sieve_arr = [True for i in range(num)]

    # Initialize at the lowest prime
    p = 2

    # The smallest prime factor of a composite number is less than or equal to that number's square root:
    # https://proofwiki.org/wiki/Composite_Number_has_Prime_Factor_not_Greater_Than_its_Square_Root
    while p * p < num:
        if sieve_arr[p]:
            for i in range(p*2, num, p):
                sieve_arr[i] = False

        p += 1

    # Integer prime array
    primes = []

    # Start at 2 because we don't consider 0 or 1 prime
    for i in range(2, num):
        if sieve_arr[i]:
            primes.append(i)

    return primes


if __name__ == '__main__':
    # Sieve 2 million primes
    print(sum(sieve(2*10**6)))
