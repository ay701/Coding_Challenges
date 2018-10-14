# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
# Use Dynamic programming
# O(M*N)


def longest_palindromic_substring(s):

    n = len(s)
    table = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue

            if s[i] == s[j]:
                table[i][j] = table[i+1][j-1] + 2
            else:
                table[i][j] = max(table[i+1][j], table[i][j-1])

    print(table)
    return table[0][n-1]

print(longest_palindromic_substring("abc"))
print(longest_palindromic_substring("aba"))

