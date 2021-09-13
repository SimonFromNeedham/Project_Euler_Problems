# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


NUM_ROWS = 20
NUM_COLS = 20


if __name__ == '__main__':
    # We're going to solve this problem using dynamic programming
    # Each entry in the grid represents the number of possible paths which lead to that entry
    # All entries are initialized at 1 for convenience, since that's the number of paths each entry on the border has
    grid = [[1 for col in range(NUM_COLS+1)] for row in range(NUM_ROWS+1)]

    for i in range(NUM_ROWS-1, -1, -1):
        for j in range(NUM_ROWS-1, -1, -1):
            # Each entry can be represented by grid[i+1][j] + grid[i][j+1] because that is the number of possible paths
            # which lead into the squares that sit below and to the right (the only directions of motion) of said entry
            grid[i][j] = grid[i+1][j] + grid[i][j+1]

    print(grid[0][0])
