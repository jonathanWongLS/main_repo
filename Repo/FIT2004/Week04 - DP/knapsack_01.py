def knapsack_01(weight, items):
    # items[i][0] = weight
    # items[i][1] = profit
    
    # intiailising memo
    memo = [None] * (len(items) + 1)
    for i in range(len(items) + 1):
        memo[i] = [None] * (weight + 1)
        
    for i in range(len(memo)):
        if i == 0:
            for j in range(weight + 1):
                memo[i][j] = 0
        else:
            memo[i][0] = 0

    # filling up memo 
    for i in range(1, len(items) + 1):  # loop through the rows (items)
        for j in range(1, weight + 1):  # loop through the columns (weights)
            exclude = memo[i-1][j]
            include = 0

            if items[i-1][0] <= j:
                include = items[i-1][1] + memo[i-1][j - items[i-1][0]]

            memo[i][j] = max(include, exclude)
       
    return memo
    # return memo[i][j] # to print out max profit
    

# items[i][0] = weight
# items[i][1] = profit
ret_memo = knapsack_01(12,[(6, 230), (1,40), (5, 350), (9, 550)])
print(ret_memo)
# print array in 'table' form
# rows = items
# columns = weight
for i in range(len(ret_memo)):
    ret = ''
    for j in range(len(ret_memo[0])):
        ret += str(ret_memo[i][j]) + ' '
    print(ret + '\n')