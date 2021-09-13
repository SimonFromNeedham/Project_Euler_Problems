# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


if __name__ == '__main__':
    even_valued_total = 0

    # Fibonacci addends
    num1 = 1
    num2 = 2

    while num2 < 4 * 10**6:
        num2_original = num2

        # Calc next term
        num2 = num1 + num2
        num1 = num2_original

        # Add num1 because the final value of num2 will just exceed four million
        if num1 % 2 == 0:
            even_valued_total += num1

    print(even_valued_total)
