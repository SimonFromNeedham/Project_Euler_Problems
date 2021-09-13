# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# Helper method that returns true if the parameter "num" is a palindrome, false otherwise
def is_palindrome(num):
    # Cast the "num" to String to enable iteration and indexing
    str_num = str(num)
    len_num = len(str_num)

    for i in range(int(len_num / 2)):
        # [len_num-1-i] avoids index out of range error
        if str_num[i] != str_num[len_num-1-i]:
            return False

    return True


# Brute force approach to find the largest palindrome within the range(min_factor, max_factor)
def largest_palindrome(min_factor, max_factor):
    max_palindrome = 0

    for i in range(min_factor, max_factor-1):
        for j in range(i+1, max_factor):
            product = i * j

            if product > max_palindrome and is_palindrome(product):
                max_palindrome = product

    return max_palindrome


if __name__ == '__main__':
    print(largest_palindrome(100, 1000))
