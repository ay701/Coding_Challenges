from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self, s):

        # Create a queue for BFS
        queue = [s]

        # Mark all the vertices as not visited
        visited = [s]

        while queue:

            s = queue.pop(0)
            print(s)

            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
 

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)

