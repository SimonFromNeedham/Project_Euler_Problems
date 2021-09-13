# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# Helper method used instead of main method to easily return out of the double for loop
def get_triplet_product():
    # Hypotenuse must be larger than a, b --> only check potential legs up to length 333
    # The second leg must also be smaller --> a + b + c = 1000 --> b < (1000 - a) / 2
    for a in range(334):
        for b in range(a, int((1000 - a) / 2)):
            # By substituting c^2 for (1000 - a - b)^2, we find that 10^6 - 2000a - 2000b + 2ab = 0
            # Using brute force, we can plug in values of a, b in the given ranges to get a quick answer
            if 10 ** 6 - 2000 * a - 2000 * b + 2 * a * b == 0:
                c = 1000 - a - b

                print("a: " + str(a))
                print("b: " + str(b))
                print("c: " + str(c))

                return a * b * c


if __name__ == '__main__':
    print("Solution: " + str(get_triplet_product()))
