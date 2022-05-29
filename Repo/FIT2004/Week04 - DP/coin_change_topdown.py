import math 
from typing import List

def coin_change(value, coins: List):
    memo = [-1] * (value + 1)
    memo[0] = 0
    return coin_change_aux(value, coins, memo)

def coin_change_aux(value, coins, memo):
    if memo[value] != -1:
        return memo[value]
    else:
        min_coins = math.inf
        for i in range(0, len(coins)):
            if coins[i] <= value:
                c = 1 + coin_change_aux(value - coins[i], coins, memo)
                if c < min_coins:
                    min_coins = c
        memo[value] = min_coins
        return memo[value]

print(coin_change(12, [1, 5, 6, 9]))
