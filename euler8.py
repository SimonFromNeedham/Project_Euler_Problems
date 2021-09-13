# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the following 1000-digit number (euler8_number) that have the greatest product.
# What is the value of this product?


# Helper method which returns the product of every integer digit in string "digits"
def calc_product(digits):
    product = 1

    for digit in digits:
        product *= int(digit)

    return product


if __name__ == '__main__':
    # Read in the number as a string without newlines
    big_number = open('euler8_number.txt').read().replace('\n', '')

    max_product = 0

    for i in range(len(big_number)-13):
        # Parse thirteen digits from the number
        product = calc_product(big_number[i:i+13])

        if product > max_product:
            max_product = product

    print(max_product)
