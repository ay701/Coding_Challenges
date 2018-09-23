# Given a boolean 2D matrix, find the number of islands.
# A group of connected 1s forms an island.
# For example, the below matrix contains 5 islands
# Use DFS
# Example:

# Input : mat[][] = {{1, 1, 0, 0, 0},
#                   {0, 1, 0, 0, 1},
#                   {1, 0, 0, 1, 1},
#                   {0, 0, 0, 0, 0},
#                   {1, 0, 1, 0, 1}
#
# Output : 5

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)
        self.col = len(graph[0])
        self.visited = [[False for i in range(self.col)] for j in range(self.row)]
        self.row_marks = [-1,-1,-1,0,0,1,1,1]
        self.col_marks = [-1,0,1,-1,1,-1,0,1]

    def isConnected(self, r, c):
        return (r>=0 and c>=0 and
                r<self.row and c<self.col and
                not self.visited[r][c] and
                self.graph[r][c])

    def dfs(self, r, c):
        self.visited[r][c] = True

        for k in range(8):
            if self.isConnected(r+self.row_marks[k], c+self.col_marks[k]):
                self.dfs(r+self.row_marks[k], c+self.col_marks[k])

    def countIslands(self):
        count = 0

        for r in range(self.row):
            for c in range(self.col):
                if not self.visited[r][c] and self.graph[r][c]:
                    self.dfs(r,c)
                    count+=1

        return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

g = Graph(graph)

print "Number of islands is:"
print g.countIslands()
