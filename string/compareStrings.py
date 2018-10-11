# Compare two strings A and B, determine whether A contains all of the characters in B.
# The characters in string A and B are all Upper Case letters.

# Example
# For A = "ABCD", B = "ABC", return true.
# For A = "ABCD" B = "AABC", return false.

from collections import defaultdict


def compare_strings(st1, st2):

    map_1 = defaultdict(int)
    map_2 = defaultdict(int)

    for s in st1:
        map_1[s] += 1

    for s in st2:
        map_2[s] += 1

        if map_2[s] > map_1[s]:
            return False

    return True

print compare_strings("AAABB", "ABC")

