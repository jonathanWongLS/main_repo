''' Node class, Trie class, and lex_pos functions '''

__author__ = "Jonathan Wong Leong Shan"

# Node data structure
class Node:
    def __init__(self, size = 27):
        # teminal $ at index 0
        self.link = [None] * size
        # data payload
        self.freq = 0

# Trie data structure
class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert_recur(self, key):
        current = self.root
        self.insert_recur_aux(current, key)

    def insert_recur_aux(self, current, key):
        # base
        if len(key) == 0:
            # what happen when I gone through all of my characters in key
            index = 0
            # when there are no other similar words, add a terminal ($)
            if current.link[index] is None:
                current.link[index] = Node()
            # Add freq of terminal
            current = current.link[index]
            current.freq += 1
            return
        else:
            #calculate index
            index = ord(key[0]) - 97 + 1
            if current.link[index] is not None:
                current.link[index].freq += 1
                current = current.link[index]    
                self.insert_recur_aux(current, key[1:])            
            # if path doesn't exist
            else:
                current.link[index] = Node()
                current = current.link[index]
                current.freq += 1
                self.insert_recur_aux(current, key[1:])

def lex_pos(text, queries):
    """
    
    """

    # Initialise a list for count of texts lexicographically greater than queries
    lex_list = [0] * len(queries)
    trie = Trie()
    # insert every item in text
    for item in text:
        trie.insert_recur(item)

    # Traverse through each word in queries list
    for j in range(len(queries)):
        total = 0
        current = trie.root

        # If query is empty character
        if queries[j] == "":
            lex_list[j] = len(text)
        else:
            # Traverse through each character in queries[j]
            # Adding nodes horizontal to it's data
            for char in queries[j]:
                index_char = ord(char) - 97 + 1
                # Traverse through link array from index 1 to 26
                for m in range(1,27):
                    if current.link[m] is not None:
                        if m > index_char:
                            total += current.link[m].freq
                current = current.link[index_char]

            # Adding child nodes data   
            for m in range(1,27):
                if current.link[m] is not None:
                    total += current.link[m].freq
            lex_list[j] = total
    return lex_list

