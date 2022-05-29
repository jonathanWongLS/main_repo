data = [("nuka", ["birds", "napping"]),("hadley", ["napping birds", "nash equilibria"]),("yaffe", ["rainy evenings", "the colour red", "birds"]),("laurie", ["napping", "birds"]),("kamalani", ["birds", "rainy evenings", "the colour red"])]


def interest_groups(data):

    # sort each interest list alphabetically
    for i in range(len(data)):

        # Preprocessing
        retval = preprocessing(data[i][1])

        list = retval[0]
        max_len = retval[1]
        
        list = alpha_rad_sort(list, max_len)     
        for j in range(len(list)):
            data[i][1][j] = list[j]

    
    return data


def preprocessing(list):
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
                        for j in range(len(each_array)):
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

print(alpha_rad_sort(["ACACIA$", "CACIA$A", "ACIA$AC", "CIA$ACA", "IA$ACAC" ,"A$ACACI", "$ACACIA"], 7))
