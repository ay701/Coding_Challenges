from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = [] # Mark all the vertices as not visited

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self, s):

        self.visited.append(s)
        print(s)

        for i in self.graph[s]:
            if i not in self.visited:
                # print(self.visited)
                self.dfs(i)


# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is DFS from (starting from vertex 2)"
g.dfs(2)

