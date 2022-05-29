# Top - down (always recursive)

memo = [-1]*N
memo[0] = 1
memo[1] = 1

def fib_dpa(N):
    if memo[N] != -1:
        return memo[N]
    memo[N] = fib_dpa(N-1) + fib_dpa(N-2)
    return memo[N]

# Bottom - up (always iterative)
memo = [-1]*N
memo[0] = 0
memo[1] = 1

for i in range(2,N):
    memo[i] = memo[i-1] + memo[i-2]