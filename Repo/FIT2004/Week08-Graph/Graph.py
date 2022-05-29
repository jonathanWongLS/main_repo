

class Graph:
    def __init__(self, V) -> None:
        '''
        # matrix
        self.matrix = [None] * len(V)
        for i in range(len(V)):
            self.matrix[i] = [None] * len(V)
        '''

        # array
        self.vertices = [None]*len(V)
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])
        

    def __str__(self):
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex " + str(vertex) + '\n'
        return return_string

    def bfs(self, source):
        '''
        function for BFS, starting from source
        Very basic bfs
        '''
        return_bfs = []
        discovered = []             # discovered is a queue
        discovered.append(source)
        while len(discovered) > 0:
            # serve from 
            u = discovered.serve()  
            u.visited = True        # means I have visited u
            return_bfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True     # means I have discovered v, adding it to the queue
        return return_bfs

    def bfs_distance(self, source):
        '''
        function for BFS, starting from source
        Very basic bfs
        '''
        discovered = []             # discovered is a queue
        discovered.append(source)
        while len(discovered) > 0:
            # serve from 
            u = discovered.serve()  
            u.visited = True        # means I have visited u
            return_bfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True     # means I have discovered v, adding it to the queue
                    v.distance = u.distance + 1
                    v.previous = u
            # implement backtracking

    def dfs(self, source):
        '''
        function for BFS, starting from source
        Very basic bfs
        '''
        return_dfs = []
        discovered = []             # discovered is a stack, LIFO
        discovered.append(source)   # append = push
        while len(discovered) > 0:
            # serve from 
            u = discovered.pop()    # pop last item  
            u.visited = True        # means I have visited u
            return_dfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.push(v)
                    v.discovered = True     # means I have discovered v, adding it to the queue
        return return_dfs

    def dfs_recur(self, current_vertex):
        pass 
        # given in slides

    def dijkstra(self, source):
        '''
        function for dijkstra
        '''
        discovered = Heap()             # discovered is a queue
        discovered.append(source)
        while len(discovered) > 0:
            # serve from 
            u = discovered.serve()  
            u.visited = True        # means I have visited u
            return_bfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True     # means I have discovered v, adding it to the queue
                    v.distance = u.distance + edge.w
                    v.previous = u
                else if (v.visited == False):
                    if v.distance > u.distance + edge.w:
                        # update distance
                        v.distance = u.distance + edge.w
                        v.previous = u
                        # update heap (code by yourself)
                        


class Vertex:
    def __init__(self, id):
        # list
        self.edges = []
        self.id = id
        self.discovered = False
        self.distance = 0
        # backtracking
        self.previous = None

    def __str__(self):
        return_string = str(self.id)
        return return_string

    def added_to_queue(self):
        self.discovered = True
        
    def visit_node(self):
        self.visited = True

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w



# create a graph with $ vertices
if __name__ == "__main__":
    vertices = [0,1,2,3,4]
    my_graph = Graph(V = vertices)
    print(my_graph)

