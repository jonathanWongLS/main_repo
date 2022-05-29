# Node data structure
class Node:
    def __init__(self, data = None, size = 27, level = None) -> None:
        # terminal $ at index 0
        self.link = [None] * size

        # data payload
        self.data = data

        # level of node
        self.level = level


# The Trie data structure
class Trie:
    def __init__(self) -> None:
        self.root = Node(level = 0)

    def insert(self, key, data):
        count_level = 1

        # begin from root
        current = self.root

        # go through the key one by one
        
        for char in key:
            # if path exists
            # convert ascii to index
            index = ord(char) - 97 + 1
            if current.link[index] is not None:
                current = current.link[index]                
            # if path doesn't exist
            else:
                current.link[index] = Node(level = count_level)
                current = current.link[index]
            count_level += 1
        # go through the terminal $
        index = 0
        if current.link[index] is not None:
            current = current.link[index]                
        # if path doesn't exist
        else:
            current.link[index] = Node()
            current = current.link[index]

        # add in the payload
        current.data = data

    def insert_recur(self, key, data):
        current = self.root
        self.insert_recur_aux(current, key, data)

    def insert_recur_aux(self, current, key, data=None):
        # base
        if len(key) == 0:
            # what happen when I gone through all of my characters in key
            return

        # recur
        else:
            #calculate index
            index = ord(key[0]) - 97 + 1
            if current.link[index] is not None:
                current = current.link[index]                
            # if path doesn't exist
            else:
                current.link[index] = Node()
                current = current.link[index]
                self.insert_recur_aux(current, key[1:], data)


    def search(self, key):
        # begin from root
        current = self.root

        # go through the key one by one
        for char in key:
            print(current.level)
            # if path exists
            # convert ascii to index
            index = ord(char) - 97 + 1
            if current.link[index] is not None:
                current = current.link[index]                
            # if path doesn't exist
            else:
                raise Exception(str(key) + " key doesn't exist")
        # go through the terminal $
        index = 0
        print(current.level)
        if current.link[index] is not None:
            current = current.link[index]
        # if path doesn't exist
        else:
            raise Exception(str(key) + " key doesn't exist")

        # now we are at the leaf
        print(current.level)
        return current.data 

        

bla = Trie()
bla.insert("lol", "123")
bla.insert("loa", "456")
# bla.insert("lol", ["hello", "its me"])
# bla.insert("uwu", None)

print(bla.search("loa"))

# try:
#     print(bla.search("lol"))
# except Exception as e:
#     print(e)
# try:
#     print(bla.search("loa"))
# except Exception as e:
#     print(e)
# try:
#     print(bla.search("uwu"))
# except Exception as e:
#     print(e)
# try:
#     print(bla.search("l"))
# except Exception as e:
#     print(e)
