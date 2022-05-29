def insertion(ar):
    n = len(ar)
    for i in range(1, n):
        key = ar[i]
        j = i-1
        while j >= 0 and key < ar[j] :
                ar[j + 1] = ar[j]
                j -= 1
        ar[j + 1] = key
    return ar

def swap(ar, id_1, id_2):
    temp = ar[id_1]
    ar[id_1] = ar[id_2]
    ar[id_2] = temp



print(insertion([5,3,7,2,1]))
print(hoare([2,1,3,4,8,7,5,6], 3))