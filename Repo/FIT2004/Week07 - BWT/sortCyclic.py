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
            # Terminal append to 0th sub array
            elif (ord(item[i]) - 64) == -28:
                count_array[0].append(item) 
            # Append to appropriate sub array based on alphabet
            else:
                count_array[ord(item[i])-64].append(item)
            k-=1
    
    # List is sorted alphabetically
    return list

def print_for_table(list):
    for i in range(len(list)):
        print(list[i])

def get_last_char(list):
    length = len(list[0])
    chars = ""
    for word in list:
        chars += word[length-1]
    print(f'Characters : {chars}' )


if __name__ == '__main__':
    sortedList = alpha_rad_sort(["ACACIA$", "CACIA$A", "ACIA$AC", "CIA$ACA", "IA$ACAC" ,"A$ACACI", "$ACACIA"], 7)
    print_for_table(sortedList)
    get_last_char(sortedList)
