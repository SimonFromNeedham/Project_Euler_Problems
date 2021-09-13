# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


NUM_DIGITS = 1000


# I could use a generalized array approach similar to Euler16/Euler20 to save memory,
# But at this point it's just so much easier to use longs to represent fibonacci terms
if __name__ == '__main__':
    # Initial Fibonacci terms
    num1 = 1
    num2 = 1

    # Sequence starts with two terms
    term_index = 2

    while len(str(num2)) < NUM_DIGITS:
        next_term = num1 + num2

        num1 = num2
        num2 = next_term

        term_index += 1

    print(term_index)
