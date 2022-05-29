def sort_counting_stable(new_list):
    '''
    Precondition : new_list have at least 1 item
    Time complexity : O(M + N)
    Space complexity : O(M + N) where: N is the number of elements in new_list
                                       M is the length of count_array
    Auxiliary complexity : O(M + N) where: N is the number of elements in new_list
                                           M is the length of count_array
    '''
    if len(new_list) == 0:
        return('New list must contain at least one items')

    # find the maximum
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item

    # initialize count array
    count_array = [None]*(max_item+1)
    for i in range(len(count_array)): # Different list for each item
        count_array[i] = []

    # update count_array
    for item in new_list:
        count_array[item].append(item)

    # update input array
    index = 0
    for each_array in count_array:
        if len(each_array) != 0:
            for j in range(len(each_array)):
                new_list[index] = each_array[j]
                index += 1

    # new_list will be sorted
    return new_list
