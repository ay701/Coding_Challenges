class Solution:
    # @return an integer
    def c(self, m, n):
        mp = {}
        for i in range(m):
            for j in range(n):
                if(i == 0 or j == 0):
                    mp[(i, j)] = 1
                else:
                    mp[(i, j)] = mp[(i - 1, j)] + mp[(i, j - 1)]
        return mp[(m - 1, n - 1)]

    def uniquePaths(self, m, n):
        return self.c(m, n)

s = Solution()
print s.uniquePaths(1,7)
print s.uniquePaths(7,1)
print s.uniquePaths(3,7)