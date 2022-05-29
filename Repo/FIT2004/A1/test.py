# import matplotlib.pyplot as plt
import math
import random
x = [1,2,3,4,5,6]
y = [2,3,4,5,6,7]
# plt.plot(x, y)
# plt.show()

# #num = [12, 234, 45, 678]
# num = 4243
# base = 1000000
# ar = []
# for i in range(len(ar)):
#         ar[i] = []
ar = []
num = 28448815
base = 36
while num > 0:
    n = num%base
    ar.append(n)
    num = num // base
# print(ar)


# # get no. of digits of max
# dig = 0
# while num > 0 :
#     dig += 1
#     num = num//10

# print(dig)


data1 = [random.randint(0,2**25) for _ in range(2**15)]
data2 = [random.randint(0,2**25) for _ in range(2**16)]
bases1 = [2**i for i in range(1,23)]
bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]
# print(bases1)
# print(data1)
# print('\n')
# print(data2)

# word = 'tacoman'
# count = [[], [],['hello']]
list = []
list1 = ['yes', 'no']
list2 = ['yes', 'no']
print(list1 == list2)
# index = 0
# for each_array in count:
#     for item in each_array:
#         list[index] = item
#         index += 1
# print(list)




list = [('first','a'),('second','b'),('third','b'), ('fourth', 'c'), ('fifth', 'd'),('sixth', 'd')]

length = len(list)
j = 0
i = 0
while i < length-1:
    if list[j][1] == list[i+1][1]:
        i += 1
    else:
        list[j+1], list[i+1] = list[i+1], list[j+1]
        j += 1
        i += 1

print(list)











