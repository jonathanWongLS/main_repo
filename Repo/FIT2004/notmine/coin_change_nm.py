import math

coins = [1, 5, 6, 9]
def coin_change_bottomup(N):
    memo = [-1]*(N+1)
    least_coins = 0
    memo[0] = 0
    for value in range(1, N+1):
        temp = value
        for j in range(len(coins)): # go through coins
            if coins[j] > value:
                break
            divided = value // coins[j]
            balance = value - (coins[j] * divided)
            least_coins = min(least_coins,divided + memo[balance])
        memo[value] = temp
    return temp


# Top-down approach
def coin_change_td_driver(n):
    def coin_change_topdown_aux(n, memo):
        if n == 0:
            memo[0] = 0
            return 0
        elif memo[n] != -1:
            return memo[n]
        else:
            temp = math.inf
            for i in range(len(coins)):
                if coins[i] <= n:
                    no_of_coins = 1 + coin_change_topdown_aux(n - coins[i], memo)
                    if no_of_coins < temp:
                        temp = no_of_coins
            memo[n] = temp
            return temp

    def coin_change_topdown(n, memo):
        if memo[n] == 0:
            return []
        if memo[n] == 1:
            return [n]
        for i in range(n, -1, -1):
            temp = n
            retval = []
            if memo[i] < memo[n]:
                while temp > 0:
                    retval += coin_change_topdown(i, memo)
                    i = temp - i
                    temp = i
        if len(retval) == memo[n]:
            return retval

    memo = [-1]*(n+1)
    coin_change_topdown_aux(n, memo)
    print(memo)
    print(coin_change_topdown(n,memo))
    return memo[n]
  