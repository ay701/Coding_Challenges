# Write a function that returns whether two words are exactly "one edit" away using the following signature:
# bool OneEditApart(string s1, string s2);
# An edit is:
# Inserting one character anywhere in the word (including at the beginning and end)
# Removing one character
# Replacing one character
#
# Examples:
# OneEditApart("cat", "dog") = false
# OneEditApart("cat", "cats") = true
# OneEditApart("cat", "cut") = true
# OneEditApart("cat", "cast") = true
# OneEditApart("cat", "at") = true
# OneEditApart("cat", "act") = false

# Dynamic Programming
# https://www.geeksforgeeks.org/edit-distance-dp-5/
# Time Complexity: O(m x n)
# Auxiliary Space: O(m x n)


def edit_distance(st1, st2):

    n1 = len(st1)
    n2 = len(st2)

    if abs(n1-n2) > 1:
        return False

    table = [[0 for i in range(n2+1)] for j in range(n1+1)]

    for i in range(n1+1):
        for j in range(n2+1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif st1[i-1] == st2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min(table[i-1][j], table[i][j-1], table[i-1][j-1])

            if i == j and i != 0 and table[i][j] > 1:
                return False

    return True

print("Valid" if edit_distance("cat", "cats") else "Invalid")
print("Valid" if edit_distance("cat", "catss") else "Invalid")


