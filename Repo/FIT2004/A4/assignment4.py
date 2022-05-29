''' Assignment 4 Answers '''

import math, heapq

__author__ = 'Jonathan Wong Leong Shan'

class WordGraph:
    '''
    Class for a graph with words connected to each other if they have one letter difference and its methods
    :Reference: Modified code given in EdForum, from lectures and online resources
    '''
    class WeightedWordEdge:
        '''
        Class for an edge which connects words with one letter difference 
        :Reference: Modified code given in EdForum
        '''            
        def __init__(self, dest, weight):
            self.dest = dest
            self.weight = weight

    def __init__(self, list_words):
        '''
        Initialise the adjacency list, number of characters in every word, list of words and the number of words
        :Reference: Modified code given in EdForum
        '''
        # initialise adjacency list of graph
        self.adj_list = [[] for _ in range(len(list_words))]
        
        # Store the length of each word
        self.word_length = len(list_words[0])

        # Store the list of words as an class variable
        self.list_words = list_words

        # Store the number of words
        self.num_vertices = len(list_words) 

    def add_edges_task1(self):
        '''
        Adds an undirected edge between vertices with one letter difference
        :Complexity: O(M.N^2) where M is the length of the longest link in adjacency list
                                    N is the number of words in self.list_words
        :Reference: Modified code given in EdForum
        '''
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

    def add_edges_task2(self):
        '''
        Adds an undirected edge between vertices with one letter difference and a weight where it is the ordinance difference between the different character
        :Complexity: O(M.N^2) where M is the length of the longest link in adjacency list
                                    N is the number of words in self.list_words
        :Reference: Modified code given in EdForum
        '''
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                different_count = 0
                weight = 0
                if i == j: # Don't check the same word
                    continue
                else:
                    for k in range(self.word_length): # for each character in the two words we are comparing
                        if (self.list_words[i][k] != self.list_words[j][k]):
                            different_count += 1
                            ord_ik = ord(self.list_words[i][k]) - 96
                            ord_jk = ord(self.list_words[j][k]) - 96
                            if (ord_ik) <= (ord_jk):
                                weight = ord_jk - ord_ik
                            elif (ord_ik) > (ord_jk):
                                weight = ord_ik - ord_jk

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
                            self.adj_list[i].append(WordGraph.WeightedWordEdge(j, weight))
                        if not exist_j:
                            self.adj_list[j].append(WordGraph.WeightedWordEdge(i, weight))

    def best_start_word(self, target_words):
        '''
        Choose word which has the shortest path from each word in target_list
        :Complexity: O(W^3) where W is the number of words in the graph (self.num_vertices)
        :Reference: Referring to Dr Ian's Lectures
        '''
        # add edges between each word as long as they have one letter distance
        self.add_edges_task1()

        # initialise the adjacency matrix for Floyd-Warshall
        adj_matrix = [[] for _ in range(self.num_vertices)]

        # initialise values for the matrix (inf)
        for m in range(self.num_vertices):
            for n in range(self.num_vertices):
                adj_matrix[m].append(math.inf)    
        
        # initialise values for the matrix (0)
        for m in range(self.num_vertices):
            for n in range(self.num_vertices):
                if m == n:
                    adj_matrix[m][n] = 0

        # fill in the adjacency matrix with the weight of each edge
        for i in range(self.num_vertices):
            for edge in self.adj_list[i]:
                adj_matrix[i][edge.dest] = 1

        # update matrix with shortest distance from each word to another
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])
                    
        # get start point which gives the shortest path between all words in target_words
        min_sum = math.inf
        min_index = None

        for i in range(self.num_vertices):
            sum = 0

            # sum up the shortest distance from every vertices to every target words
            for target in target_words:
                sum += adj_matrix[i][target]
                
            # if sum is shorter than previous smallest sum, store in min_sum
            if sum < min_sum:
                min_sum = sum
                min_index = i

        # if no best word is found, return None
        if min_index is None:
            return -1

        # returns the index of the best start word
        return min_index

    def dijkstra(self, start, end):
        """
        Dijkstra algorithm implementation using heapq together with backtracking to determine path from start to finish
        Returns the path if valid. Returns None otherwise
        :Complexity: O(D log W + W log W) where D is the number of pairs of words in WordGraph which differ by exacty one letter
                                                W is the number of words in WordGraph 
        :Reference: Modified code from https://stackoverflow.com/questions/33627309/dijkstras-algorithm-help-in-python
        """

        # initialise the lists for distance, previous word and the minheap array
        distance = [] 
        from_word = []  
        minheap = [] 

        # initialise the distance array (inf)
        for i in range(self.num_vertices):
            distance.append(math.inf)

        # initialise the array that stores the previous word where the distance is minimal (None)
        for i in range(self.num_vertices):
            from_word.append(None)

        # initialise the minheap with a heapq   
        for i in range(self.num_vertices):
            # the distance of source from the source is 0
            if i == start: 
                distance[i] = 0
                heapq.heappush(minheap, [0, i])
            else:
                # the distance of other words from the source initialised to infinity
                heapq.heappush(minheap, [math.inf, i])

            # initialise every index in from_word array to None 
            from_word[i] = None


        while minheap: # while minheap is not empty
            # get the word with the smallest distance / word at the root of the minheap
            current_word = heapq.heappop(minheap)[1] 

            # if current word is the end word, return the path from source to end
            if current_word == end:
                path = []
                current = end
                path.append(current) # Append the end word first in path array
                while from_word[current] is not None: # continue until we find the end word
                    path.append(from_word[current])
                    current = from_word[current]
                return path
            
            # loop through each edge of current_word
            for connected in self.adj_list[current_word]: 
                # get the sum of the minimum distance of current_word from source and the weight of each edge
                connected_new_weight = distance[current_word] + connected.weight 

                # edge relaxation
                if connected_new_weight < distance[connected.dest]: 
                    distance[connected.dest] = connected_new_weight
                    from_word[connected.dest] = current_word

                    # update minheap array with new distance
                    for heap_word in minheap:
                        if heap_word[1] == connected.dest:
                            heap_word[0] = connected_new_weight
                            break
                    
                    # ensure minheap is in heap structure
                    heapq.heapify(minheap)

        # return none if there's no possible path to end word
        return None

    def constrained_ladder(self, start, end, detour):
        """
        Carry out djikstra from start to first item in detour and then from detour item to end
        Returns the path from start to end passing through at least one word in detour
        :Complexity: O(D log W + W log W) where D is the number of pairs of words in WordGraph which differ by exacty one letter
                                                W is the number of words in WordGraph 
        """

        # add edges between each word as long as they have one letter distance together 
        # with the lexigraphical distance between that one different character
        self.add_edges_task2()
        
        # initialise booleans to check if the path is valid
        first_path_pass = False
        second_path_pass = False

        # initialise index looping through detour
        j = 0

        # as long as there is no path from start to end through the detour, continue for the other detours until no more
        while (not first_path_pass or not second_path_pass) and j < len(detour):
            
            first_path_pass = False
            second_path_pass = False
            
            # carry out djikstra from the start to detour
            first_path = self.dijkstra(start, detour[j])

            # carry out djikstra from the detour to end
            second_path = self.dijkstra(detour[j], end)        

            # check if first and second paths have start and end respectively
            if first_path[len(first_path) - 1] == start:
                first_path_pass = True    
            
            if second_path[0] == end:
                second_path_pass = True 

            # increment index to choose next detour
            j += 1

        # if both first and second paths are valid, build the path array for output
        if first_path_pass and second_path_pass:
            path = []
            for i in range(len(first_path)-1, -1, -1):
                path.append(first_path[i])
            for i in range(len(second_path)-2, -1, -1):
                path.append(second_path[i])
            return path
        
        # if both paths are invalid, return None
        return None

