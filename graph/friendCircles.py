# Leetcode - 547. Friend Circles

# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.


class Solution:

    def __init__(self, classroom):
        self.classroom = classroom
        self.r_cnt = len(self.classroom)
        self.c_cnt = len(self.classroom[0])
        self.visited = [[False for _ in range(self.c_cnt)] for _ in range(self.r_cnt)]
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # print(self.visited)
        # print(self.r_cnt)
        # print(self.c_cnt)

    def friend_circles(self):

        num_of_circles = 0

        for i in range(self.r_cnt):
            for j in range(self.r_cnt):

                if self.classroom[i][j] == 1 and not self.visited[i][j]:
                    self.dfs(i, j)
                    num_of_circles += 1

        return num_of_circles

    def dfs(self, x, y):

        self.visited[x][y] = True

        for direction in self.directions:

            # Make sure use new variables
            i = x + direction[0]
            j = y + direction[1]

            if i >= 0 and j >= 0 \
                    and i < self.r_cnt \
                    and j < self.c_cnt \
                    and not self.visited[i][j] \
                    and self.classroom[i][j] == 1:
                self.dfs(i, j)


classroom = [[1,1,0],
             [1,1,0],
             [0,0,1]]

print(Solution(classroom).friend_circles())
