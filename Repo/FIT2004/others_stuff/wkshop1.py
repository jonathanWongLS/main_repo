def find_minimum(my_list):
    minimum = None
    for i in range(0, len(my_list)):
        if minimum is None:
            minimum = my_list[i]
        else:
            if minimum > my_list[i]:
                minimum = my_list[i]
    return minimum