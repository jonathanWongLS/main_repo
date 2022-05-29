from typing import List
import math

def coin_change(value: int, coins: List):
    memo = [math.inf] * (value+1)
    memo[0] = 0

    for sum in range(1, value+1):
        for i in range(len(coins)):
            coin = coins[i]
            if sum >= coin:
                balance = sum - coin
                count = 1 + memo[balance]
                if count < memo[sum]:
                    memo[sum] = count

    return memo[value]

if __name__ == "__main__":
    print(coin_change(12, [1,5, 6, 9]))
