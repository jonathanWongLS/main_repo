def find_unique_characters(text):
    characters = []
    for character in text:
        if character not in characters:
            characters.append(character)

    return characters

def print_vertical(text):
    for char in text:
        print(char)

def sort_counting_alpha(new_list):
    '''
    Precondition : new_list have at least 1 item
    '''

    # find the maximum
    max_item = ord(new_list[0]) - 64
    for item in new_list:
        item = ord(item) - 64
        if item > max_item:
            max_item = item
    # print(max_item)

    # initialize count array
    count_array = [0]*(max_item+1)
    # print(count_array)
    
    # update count_array
    for item in new_list:
        count_array[item] += 1
    # print(count_array)

    # update input array
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index = index + 1

    # new_list will be sorted
    return new_list


print_vertical('$CEIMNOOPRSS')
