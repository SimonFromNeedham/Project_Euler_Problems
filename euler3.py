# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


import math


def print_prime_factors(num):
    # Print out the number of 2s which divide the number
    # This makes checking for other factors much easier because we can eliminate half the candidates
    while num % 2 == 0:
        print(2)
        num /= 2

    # The smallest prime factor of a composite number is less than or equal to that number's square root:
    # https://proofwiki.org/wiki/Composite_Number_has_Prime_Factor_not_Greater_Than_its_Square_Root
    # Increment by 2 because we know that the remaining factors are odd
    for i in range(3, int(math.sqrt(num)), 2):
        while num % i == 0:
            print(i)
            num /= i


if __name__ == '__main__':
    # The answer is the last prime factor printed
    print_prime_factors(600851475143)
