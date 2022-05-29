def countSort(arr):

    output = []
    count = []
    ans = []
    
    for i in range(len(arr)):
        output.append(0)

    for i in range(256):
        count.append(0)

    for _ in arr:
        ans.append("")

    for i in arr: 
        count[ord(i)] += 1

    for  i in range(1, 256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans



# print(countSort("geeks"))
a = [3, 5, 1, 4]
print(ord("g"))