# LeetCode - Minimum Path Sum(Cost)
#
# Given a m x n grid filled with non-negative numbers
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# https://www.programcreek.com/2014/05/leetcode-minimum-path-sum-java/


def min_path_sum(board):

    r_cnt = len(board)
    c_cnt = len(board[0])

    # create dp table
    dp = [[0 for _ in range(c_cnt)] for _ in range(r_cnt)]

    for i in range(r_cnt):
        dp[i][0] = board[i][0]

    for j in range(c_cnt):
        dp[0][j] = board[0][j]

    for i in range(1, r_cnt):
        for j in range(1, c_cnt):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + board[i][j]

    i = r_cnt-1
    j = c_cnt-1
    output = [board[i][j]]

    while i > 0 and j > 0:
        if dp[i-1][j] < dp[i][j-1]:
            output.append(board[i-1][j])
            i -= 1
        else:
            output.append(board[i][j-1])
            j -= 1

    while i > 0:
        output.append(board[i-1][0])
        i -= 1

    while j > 0:
        output.append(board[0][j-1])
        j -= 1

    return output[::-1]


board = [ [1, 3, 4], [4, 7, 8], [6, 9, 2] ]
print(min_path_sum(board))
