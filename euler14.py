# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


# Helper method that returns the length of a number's collatz sequence
def len_collatz_sequence(num):
    len = 1

    while num > 1:
        if num % 2 == 0:
            num /= 2

        else:
            num *= 3
            num += 1

        len += 1

    return len


# Helper method that finds the collatz chains of all numbers starting below "num"
def collatz_sieve(num):
    # Each entry represents the length of that entry's collatz sequence (e.g. index 4 = 2)
    starting_nums = list(0 for i in range(num))

    # Index used to iterate through starting_nums, starts at 1 because 0 has no sequence
    i = 1

    while i < num:
        if starting_nums[i] == 0:
            cur_index = i
            len_seq = len_collatz_sequence(cur_index)

            # Increase efficiency by calculating sequences for each of the number's exponents
            while cur_index < num:
                starting_nums[cur_index] = len_seq

                cur_index *= 2
                len_seq += 1

        i += 1

    return starting_nums


if __name__ == '__main__':
    collatz_sequence_lengths = collatz_sieve(10**6)
    print(collatz_sequence_lengths.index(max(collatz_sequence_lengths)))
