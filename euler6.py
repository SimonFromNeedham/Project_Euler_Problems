# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the dif between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
# Find the dif between the sum of the squares of the first one hundred natural numbers and the square of the sum.


if __name__ == '__main__':
    square_of_sum = 0
    sum_of_squares = 0

    for i in range(101):
        square_of_sum += i
        sum_of_squares += i**2

    square_of_sum **= 2

    print(square_of_sum - sum_of_squares)
