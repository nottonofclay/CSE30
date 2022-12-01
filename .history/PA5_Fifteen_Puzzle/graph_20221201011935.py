#
# DO NOT FORGET TO ADD COMMENTS!!!
#

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connected_to = []
        self.color = 'purple'

    def add_neighbor(self, neighbor):
        self.connected_to.append(neighbor.id)

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([i for i in self.connected_to])

    def get_connections(self):
        return self.connected_to

    def get_id(self):
        return self.id

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self,key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex

    def get_vertex(self,n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vert_list.values()

    def add_edge(self,f,t):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t])
        self.vert_list[t].add_neighbor(self.vert_list[f])

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


if __name__ == '__main__':

    g = Graph()
    for i in range(1,17):
        g.add_vertex(i)

    g.add_edge(1,2)
    g.add_edge(2,1)
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(3,4)

    print(g.get_vertices())

    for v in g:
        print(v)