# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
# You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
#
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
# So return 7.
# https://www.youtube.com/watch?v=8K98WexA8m8

import sys


class Solution:

    def __init__(self, board):
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.hits = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.distance_sums = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.buildings = []
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def shortest_distance_from_all_buildings(self):

        # Calculate number of buildings
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    self.buildings.append((i,j))

        # BFS
        for building in self.buildings:
            if not self.bfs(building[0], building[1]):
                return -1

        result = sys.maxint
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 0 and self.hits[i][j] == len(self.buildings):
                    result = min(result, self.distance_sums[i][j])

        return result


    def bfs(self, x, y):

        count_one = 1
        visited = []
        l = [(x, y)]
        dist = 0

        while len(l):
            n = len(l)
            dist += 1

            for i in range(n):
                cur = l.pop(0)

                for direction in self.directions:
                    x = cur[0] + direction[0]
                    y = cur[1] + direction[1]

                    if x >= 0 and y >= 0 and x < self.m \
                            and y < self.n \
                            and (x, y) not in self.visited:
                        visited.append((x, y))

                        if self.board[x][y] == 0:
                            l.append((x, y))
                            self.hits[x][y] += 1
                            self.distance_sums[x][y] += dist
                        else:
                            count_one += 1

        return count_one == len(self.buildings)
