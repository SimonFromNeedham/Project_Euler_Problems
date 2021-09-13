# Sort names.txt, a 46K text file containing over five-thousand first names, into alphabetical order
# Score each name in the following way: multiply its alphabetical value by its numerical position in the list

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?


# Helper method that scores each name according to Project Euler's guidelines
def get_name_score(name):
    score = 0

    for char in name:
        # If the character is a letter (not a quotation mark or comma)...
        if char.isalnum():
            # Sub 96 because 'a' == 97
            score += ord(char.lower()) - 96

    return score


if __name__ == '__main__':
    total = 0

    # Read each name (split with a comma in the file) from names.txt into a list
    file = open('names.txt')
    names_list = file.read().split(",")

    # Sort the list because the quick sort function I wrote is in java
    names_list.sort()

    for i in range(len(names_list)):
        total += (i+1) * get_name_score(names_list[i])

    print(total)
