from typing import List

# Items are unlimited
def knapsack_unbounded(weight, items: List):
    memo = [0] * (weight + 1)
    memo[0] = 0

    for w in range(1, weight+1):
        for item in items:
            # item = [(weight, profit)]
            if item[0] <= w:
                balance = w - item[0]
                profit = item[1] + memo[balance-1]
                if profit > item[w]:
                    memo[w] = profit

    return memo[weight]

