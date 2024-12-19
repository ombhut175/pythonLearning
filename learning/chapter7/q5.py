# . Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *

# n=7



def print_star_pattern(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            # Print a full row of stars for the first and last rows
            print("* " * n)
        else:
            # Print a row with stars at the beginning and end, spaces in between
            print("* " + "  " * (n - 2) + "*")


# Number of rows and columns
n = 7
print_star_pattern(n)
