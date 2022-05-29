class WordGraph:
    '''
    Class for a graph with words connected to each other if they have one letter difference
    :Reference: Modified code from EdForum
    '''
    class WeightedWordEdge:
        def __init__(self, dest, weight):
            self.dest = dest
            self.weight = weight

    def __init__(self, list_words):
        self.adj_list = [[] for _ in range(len(list_words))]
        self.word_length = len(list_words[0])
        self.list_words = list_words
        self.num_vertices = len(list_words)
        self.add_edges_word_ladder()

    def add_directed_edge(self, source, dest, weight):
        self.adj_list[source].append(WordGraph.WeightedWordEdge(dest, weight))

    def add_edges_word_ladder(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                different_count = 0
                if i == j: # Don't check the same word
                    continue
                else:
                    for k in range(self.word_length): # for each character in the two words we are comparing
                        if (self.list_words[i][k] != self.list_words[j][k]):
                            different_count += 1
                            
                    # Check if there's only one different character (no more or less)
                    if different_count == 1:
                        exist_i = False
                        exist_j = False

                        # Check if there are any repeating edges 
                        for edge_i in self.adj_list[i]:
                            if edge_i.dest == j:
                                exist_i = True
                                break
                        
                        for edge_j in self.adj_list[j]:
                            if edge_j.dest == i:
                                exist_j = True
                                break    
                        
                        # if there are no repeating edges, add the edge into the adjacency list where the word's position is. 
                        if not exist_i:
                            self.adj_list[i].append(WordGraph.WeightedWordEdge(j, 1))
                        if not exist_j:
                            self.adj_list[j].append(WordGraph.WeightedWordEdge(i, 1))

    def display_wordgraph(self):
        '''
        Displays the graph with each word and the words they are connected to with their weights
        :Complexity: O(MN) where M is the number of words and 
                                 N is the the largest number of words one or more of the words is/are connected to 
        '''
        for i in range(len(self.adj_list)): # Loop through the entire adjacent list
            print("Word " + str(i+1) + ": " + self.list_words[i])
            for j in range(len(self.adj_list[i])): # Loop throught the list of edges of ith word
                # print the connected word and its weight
	            print(g.list_words[self.adj_list[i][j].dest], str(self.adj_list[i][j].weight))
            print("\n")


if __name__ == "__main__":
    words = ["aaa","aad","dad","daa","aca","acc","aab","abb"]
    g = WordGraph(words)
    g.display_wordgraph()