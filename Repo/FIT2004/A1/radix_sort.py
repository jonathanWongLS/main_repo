def num_rad_sort(list, b) :
    
    # COUNTING SORT

    # get maximum number in list
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    #print(max)

    # get no. of digits of max
    dig_max = 0
    while max > 0 :
        dig_max += 1
        max = max // b
    #print(dig_max)
     
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
  place = 1, most right
  '''
  retval = num//(pow(base,place))%base
  return retval

#print(get_digit_at(34, 1, 10))
ar = [34, 524, 3, 4243, 423425,42, 34]
print(num_rad_sort(ar,5))
