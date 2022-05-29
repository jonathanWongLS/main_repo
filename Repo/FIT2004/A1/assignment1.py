""" Assignment 1 Answers"""

__author__ = "Jonathan Wong Leong Shan (31435297)"

import random
import time
import math
import matplotlib.pyplot as plt

# Question 1

def num_rad_sort(list, b) :
    '''
    A list of numbers and the base is given as input. 
    The function returns a sorted list based on the base given.

    :Time Complexity: O(N + B) * logbM where : N is the length of list
                                             : B is the base
                                             : M is the largest element in list
                                            
    Reference: Modified code from Dr Ian's lecture and tutorial videos
    ''' 

    # get maximum number in list
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]

    # get no. of columns needed 
    dig_max = 0
    while max > 0 :
        dig_max += 1
        max = max // b

    # loop for dig_max (length of largest element in base b) times
    for j in range(dig_max):
        # initialize count array
        count = [None]*b
        for i in range(len(count)):
            count[i] = []
        
        # update count_array
        for item in list:
            digit_at = int(get_digit_at(item, j, b))
            count[digit_at].append(item)

        # update input array
        # new_list will be sorted
        index = 0
        for each_array in count:
            for item in each_array:
                list[index] = item
                index += 1
            
    return list


def get_digit_at(num, place, base):
    '''
    Gets digit at place using mathematical approach

    :Time Complexity: O(1)

    Reference: Code taught in Dr Ian's lecture and tutorial videos
    '''
    retval = num//(pow(base,place))%base
    return retval

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Question 2

def base_timer(num_list, base_list):
    '''
    Calculate time taken to sort num_list based on bases in base_list.

    :Time Complexity: O(K * (N + B) * logbM) where  : N is the length of num_list
                                                    : B is the base from base_list
                                                    : M is the largest element in num_list
                                                    : K is the length of base_list

    Reference : Post on edforum FIT2004
    '''
    time_taken = []
    for i in range(len(base_list)):
        start = time.time()
        num_rad_sort(num_list, base_list[i])
        end = time.time() - start
        time_taken.append(end)

    return time_taken 

def plot_graph():
    '''
    Plots the graphs of y1, y2, y3 and y4

    Reference: Modified code given in question sheet 
    '''
    random.seed("FIT2004S22021")
    data1 = [random.randint(0,2**25) for _ in range(2**15)]
    data2 = [random.randint(0,2**25) for _ in range(2**16)]
    bases1 = [2**i for i in range(1,23)]
    bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]

    # logarithmic scale 
    log_bases1 = []
    log_bases2 = []
    for i in range(len(bases1)):
        log_bases1.append(math.log(bases1[i]))
        
    for i in range(len(bases2)):
        log_bases2.append(math.log(bases2[i]))

    y1 = base_timer(data1, bases1)
    y2 = base_timer(data2, bases1)
    y3 = base_timer(data1, bases2)
    y4 = base_timer(data2, bases2)

    plt.subplot(1,2,1)
    plt.plot(log_bases1,y1)
    plt.plot(log_bases1,y2)
    plt.legend(['y1','y2'])
    plt.title('Logarithmic Scale')
    plt.xlabel('Base')
    plt.ylabel('Runtimes')

    plt.subplot(1,2,2)
    plt.plot(bases2, y3)
    plt.plot(bases2, y4)
    plt.legend(['y3','y4'])
    plt.title('Linear Scale')
    plt.xlabel('Base')
    plt.ylabel('Runtimes')

    plt.show()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
 
# Question 3

def interest_groups(data):
    '''
    Finds people with similar interest and groups the names together in alphabetical order.

    :Time Complexity: O(N*M) where N is the length of the data list
                                   M is the longest word among every list
    '''

    interest_list = []
    name_list = []
    # sort each interest list alphabetically
    for i in range(len(data)):

        # Preprocessing
        retval = preprocessing(data[i][1])

        list = retval[0]
        max_len = retval[1]
        
        # Sort the lists in alphabetical order
        list = alpha_rad_sort(list, max_len)     

        # Replace data list with correct values
        for j in range(len(list)):
            data[i][1][j] = list[j]

    # Extract all possible list of interests
    for item in data:
        if item[1] not in interest_list:
            interest_list.append(item[1])
    
    # Initialising name_list
    name_list = [None]*len(interest_list)
    for i in range(len(name_list)):
        name_list[i] = []
          
    # Append names with same list of interests
    for i in range(len(interest_list)):
        for j in range(len(data)):
            if data[j][1] == interest_list[i]:
                name_list[i].append(data[j][0])
    
    # Sort names in alphabetical order
    for i in range(len(name_list)):
        # Preprocessing
        preprocessed = preprocessing(name_list[i])

        list = preprocessed[0]
        max_len = preprocessed[1]
        
        # Sort the lists in alphabetical order
        name_list_n = alpha_rad_sort(list, max_len)

        # Replace data list with correct values
        for j in range(len(name_list_n)):
            name_list[i][j] = list[j]
    
    return name_list


def preprocessing(list):
    '''
    Sorts all interest lists to be sorted based on length of strings

    Time Complexity: O(N + M) where: N is the number of items in the list
                                      M is the length of the longest string

    Reference: Idea taken from Dr Ian's tutorial video
    '''
    # find the maximum
    max = 0
    for item in list:
        if len(item) > max:
            max = len(item)

    # initialize count array
    count = [None]*(max+1)
    for i in range(len(count)):
        count[i] = []
    
    # update count_array
    for item in list:
        count[len(item)].append(item)

    # update input array
    index = 0
    for each_array in count:
        if len(each_array) != 0:
            for j in range(len(each_array)):
                list[index] = each_array[j]
                index += 1

    # return new_list sorted
    return (list, max)


def alpha_rad_sort(list, max_len) :
    '''
    Sorts the list in alphabetical order.
    Time Complexity: O(N) where N is the total number of alphabets in the list 
    
    Reference: Idea taken from Dr Ian's tutorial video
    '''
    # go through every column
    for i in range(max_len-1, -1, -1):

        # initialize count_array
        count_array = [None]*27
        for j in range(len(count_array)):
            count_array[j] = []

        # go through each word based on column, i
        index = 0
        k = len(list) -1
        flag = True
        while k >= -1 and flag is True:
            item = list[k]
            
            # No sorting, rearrange words in order based on alphabet
            if i >= len(item) or k == -1:
                index = k+1
                for each_array in count_array:
                    if len(each_array) != 0:
                        for j in range(len(each_array)-1, -1, -1):
                            list[index] = each_array[j]
                            index += 1
                flag = False
            # Spaces append to 0th sub array
            elif (ord(item[i]) - 96) < 0:
                count_array[0].append(item) 
            # Append to appropriate sub array based on alphabet
            else:
                count_array[ord(item[i])-96].append(item)

            k-=1
    
    # List is sorted alphabetically
    return list
