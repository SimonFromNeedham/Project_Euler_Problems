# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23. That is, 3 + 7 + 4 + 9 = 23:

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# Find the maximum total from top to bottom of the triangle below (euler18_triangle):
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method!


if __name__ == '__main__':
    # Read the triangle into a 2-d array
    file = open('euler18_triangle.txt', 'r')
    triangle = []

    for line in file:
        # Append a list of every number in the line
        triangle.append([int(num) for num in line.split()])

    # Use dynamic programming to solve the problem...
    # The best "path" a number can take is determined by the maximum value of the paths (possible numbers) below it
    # This is true for all values up to len(triangle) - 2, at which point there is only one line of numbers below
    # By finding the best path of each number in reverse order, the answer becomes clear as we move up the triangle,
    # because once all paths have been exhausted in reverse (just O(n)!) the answer is merely the top number itself
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    print(triangle[0][0])
