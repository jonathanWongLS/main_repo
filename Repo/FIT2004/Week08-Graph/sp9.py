class Graph:
    def __init__(self, n) -> None:
        # adjacency list representation
        self.vertices = [None]*n
        print(self.vertices)
        for i in range(1,n+1):
            self.vertices[i-1] = Vertex(i)
        print(self.vertices)
        

    def add_edge(self, u, v, w):
        '''
        Adds edge object to vertexes u and v
        '''
        edge = Edge(u,v,w)
        self.vertices[u-1].edges.append(edge)
        self.vertices[v-1].edges.append(edge)

    def __str__(self):
        '''
        Prints the each vertex in the graph in a human-readable format
        '''
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex " + str(vertex) + '\n'
        return return_string

class Vertex:
    def __init__(self, id):
        self.edges = []
        self.id = id

    def __str__(self):
        '''
        Prints vertex and its id in a human-readable format
        '''
        return_string = str(self.id)
        return return_string
        
class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        '''
        Prints edges and its vertices with the weight in a human-readable format
        '''
        return_string = str(self.u) + ' ' + str(self.v) + ' ' + str(self.w) 
        return return_string


g = Graph(4)