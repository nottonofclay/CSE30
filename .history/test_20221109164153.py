#Python program to print topological sorting of a DAG
from collections import defaultdict # import a better dictionary than default

#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj = defaultdict(list) # adjacency List as a dictionary
        self.V = len(vertices)       # number of vertices
        self.E = 0                   # number of edges

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.adj[ u].append(v)
        self.E += 1

    # A Depth-First Search
    def DFS(self,v,visited,stack):

        # Mark the current node as visited.
        visited[ v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.adj[ v]:
            if visited[ i] == False:
                self.DFS(i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = {}
        for i in self.vertices:
            visited[ i] = False
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in self.vertices:
            if visited[ i] == False:
                self.DFS(i,visited,stack)

        # Print contents of stack
        print(stack)


if __name__ == '__main__':

    g = Graph(['CSE13S','CSE12','CSE12L','CSE30','CSE20','CSE3','CSE16',
               'MATH19A','MATH19B','MATH3','MATH2','MATH21','STAT131',
               'CSE101','CSE102','CSE103','CSE112','CSE120','CSE130'])
    print(g.vertices)

    g.addEdge('CSE12','CSE13S')
    g.addEdge('CSE12L','CSE13S')
    g.addEdge('CSE12','CSE12L')
    g.addEdge('MATH3','CSE30')
    g.addEdge('CSE20','CSE30')
    g.addEdge('MATH19A','MATH19B')
    g.addEdge('MATH3','MATH19A')
    g.addEdge('MATH2','MATH3')
    g.addEdge('CSE3','CSE20')
    g.addEdge('CSE20','CSE12')
    g.addEdge('MATH19A','CSE16')
    g.addEdge('MATH19A','MATH21')

    g.addEdge('CSE16','CSE101')
    g.addEdge('CSE30','CSE101')
    g.addEdge('MATH19B','CSE101')
    g.addEdge('CSE13S','CSE101')
    g.addEdge('CSE101','CSE102')
    g.addEdge('CSE101','CSE103')
    g.addEdge('CSE101','CSE112')
    g.addEdge('CSE13S','CSE120')
    g.addEdge('CSE101','CSE130')
    g.addEdge('CSE12L','CSE130')
    g.addEdge('CSE13S','CSE130')
    g.addEdge('MATH19B','STAT131')

    print("Topological Sorting of the graph:")
    g.topologicalSort()