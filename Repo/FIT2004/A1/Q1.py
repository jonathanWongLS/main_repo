def num_rad_sort(list, b) :
    '''
    A list of numbers and the base is given as input. 
    The function returns a sorted list based on the base given.

    :Time Complexity: O(N + B) * logbM where : N is the length of list
                                             : B is the base
                                             : M is the largest element in list
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
    '''
    retval = num//(pow(base,place))%base
    return retval
    
if __name__ == '__main__':
    pass

