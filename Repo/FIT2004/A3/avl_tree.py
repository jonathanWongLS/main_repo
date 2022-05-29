''' Node class, AVLTree class, and helper functions '''

__author__ = "Jonathan Wong Leong Shan"

# import random, math

outputdebug = False 

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()
 
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 

    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 

    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.key == key: 
                debug("Deleting ... " + str(key))  
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check 
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))  
                        self.node.key = replacement.key 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.key)
                    
                self.rebalance()
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
                        
            self.rebalance()
        else: 
            return 

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 

    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')

    def array_to_AVL(self, arr):
        '''
        Inserts items in a sorted array into self AVL tree 
        :Complexity: O(n) where n is the length of the sorted array, arr
        '''

        # if array is empty then return
        if len(arr) == 0:
            return 

        # find the middle element of the array
        middle = len(arr) // 2

        # insert the middle element into the AVL tree
        self.insert(arr[middle])

        # recurse for left part of avl tree first with elements to the left of array then
        # recurse for right part of avl tree with elements to the right of array
        self.array_to_AVL(arr[:middle])
        self.array_to_AVL(arr[middle + 1:])


    def uncorrupted_merge(self, other, corrupted):
        '''
        Merge self AVL tree and other AVL tree without items in corrupted
        :Complexity: O(M + N) where M is the number of items in self 
                                    N is the number of items in other
        '''

        # initialise the AVL tree we will return
        res_avl = AVLTree()

        # Do an inorder traverse to get a sorted array of self AVL tree
        self_list = self.inorder_traverse()

        # Use counting sort to sort other and corrupted lists
        other_list = sort_counting_stable(other)
        corrupted = sort_counting_stable(corrupted)

        # combine both self_list and other_list excluding items from corrupted
        a_list = merge_arrays_uncorrupted(self_list, other_list, corrupted)

        # transform the modified merged array into an AVL
        res_avl.array_to_AVL(a_list)
        
        return res_avl
    
def sort_counting_stable(new_list):
    '''
    Sorts the items in new_list using counting sort
    Time complexity : O(M + N)  where: N is the number of elements in new_list
                                       M is the length of count_array
    '''

    if len(new_list) == 0:
        return('New list must contain at least one items')
        
    # find the maximum
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item
    
    # find the minimum
    min_item = new_list[0]
    for item in new_list:
        if item < min_item:
            min_item = item

    # initialize count array
    count_array = [None]*(max_item + abs(min_item) + 1)

    # Different list for each item
    for i in range(len(count_array)): 
        count_array[i] = []

    # update count_array
    for item in new_list:
        index = item + abs(min_item) 
        count_array[index].append(item)

    # update input array
    index = 0
    for each_array in count_array:
        if len(each_array) != 0:
            for j in range(len(each_array)):
                new_list[index] = each_array[j]
                index += 1
    # new_list will be sorted
    return new_list


# Helper functions
def merge_arrays_uncorrupted(first, second, corrupted):
    '''
    Combine both first list and second list excluding items from corrupted
    :Complexity: O(M + N) where M is the number of items in first 
                                N is the number of items in second
    '''

    # initialize 
    new_list = []
    i = j = k = 0

    while i < len(first) and j < len(second):
        # if ith element in first is lesser or equal than ith element in second
        if first[i] <= second[j]:
            # if ith element in first is not the kth item in corrupted, then append ith item in first into arr
            if first[i] != corrupted[k]:
                new_list.append(first[i])
            # if it does then increment k and proceed
            else:
                if k < len(corrupted) - 1:
                    k += 1

            i += 1  # increment i counter
        else:
            # if jth element in second is not the kth item in corrupted, then append jth item in first into arr
            if second[j] != corrupted[k]:
                new_list.append(second[j])
            # if it does then increment k and proceed
            else:
                if k < len(corrupted) - 1:
                    k += 1

            j += 1  # increment j counter

    # Done for remaining items in both list
    # Append remaining items in first list without items in corrupted
    while i < len(first):
        # if ith element in first is not the kth item in corrupted, then append ith item in first into arr
        if first[i] != corrupted[k]:
            new_list.append(first[i])
        # if it does then increment k and proceed
        else:
            if k < len(corrupted) - 1:
                k += 1
        
        i += 1  # increment i counter

    # Append remaining items in second list without items in corrupted
    while j < len(second):
        # if jth element in second is not the kth item in corrupted, then append jth item in first into arr
        if second[j] != corrupted[k]:
            new_list.append(second[j])
        # if it does then increment k and proceed
        else:
            if k < len(corrupted) - 1:
                k += 1

        j += 1  # increment j counter

    return new_list
 

# Usage example
if __name__ == "__main__": 
    a = AVLTree()
    # b = AVLTree()
    # print ("----- Inserting -------")
    # inlist = [5, 12, -4, 21, 19, 25]
    # inlist1 = [7, 2, 6, 3, 4, 1, 8, 9]

    inlist = [1,2,3,4,5]
    inlist1 = [6,7,8,9,10]

    corrupted = [1, 3, 5]

    for i in inlist:
        a.insert(i)

    print(a.inorder_traverse())

    # a.uncorrupted_merge(inlist1, corrupted).display()

    # corrupted = [1,3,5]
    # other = [7,10,8,6,9]
    # print(a.uncorrupted_merge(other,corrupted).display())

    # a.display()
    # print(a.inorder_traverse())
    # print(merge_sorted_arr(a.inorder_traverse(), sort_counting_stable(other)))
    # a.display()
        
    # print(a.height)
    
    # # print ("----- Deleting -------")
    # # a.delete(3)
    # # a.delete(4)
    # # a.delete(5) 
    # # a.display()
    
    # # print ()
    # # print ("Input            :", inlist )
    # # print ("deleting ...       ", 3)
    # # print ("deleting ...       ", 4)
    # # print ("deleting ...       ", 5)
    # print ("Inorder traversal:", a.inorder_traverse())

    # print(a.display())