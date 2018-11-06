# 2D Spiral Array
# Find the pattern and complete the function:
# int[][] spiral(int n);
# where n is the size of the 2D array.
# Sample Result
# input = 3
# 123
# 894
# 765
#
# input = 4
# 01 02 03 04
# 12 13 14 05
# 11 16 15 06
# 10 09 08 07
#
# input = 8
# 1 2 3 4 5 6 7 8
# 28 29 30 31 32 33 34 9
# 27 48 49 50 51 52 35 10
# 26 47 60 61 62 53 36 11
# 25 46 59 64 63 54 37 12
# 24 45 58 57 56 55 38 13
# 23 44 43 42 41 40 39 14
# 22 21 20 19 18 17 16 15


class Solution:
    def __init__(self, n):
        self.n = n
        self.result = [[0 for i in range(n)] for j in range(n)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, x, y):
        return x in range(self.n) and y in range(self.n) and self.result[x][y] == 0

    def spiral(self):

        if self.n == 1:
            return [1]

        x, y = 0, 0
        cur = 1
        self.result[x][y] = cur

        while cur < self.n**2:
            for d in self.directions:
                while self.is_valid(x+d[0], y+d[1]):
                    x += d[0]
                    y += d[1]
                    cur += 1
                    self.result[x][y] = cur

        return self.result


print(Solution(4).spiral())
