def power(x,n):
    if n == 0:
        return 1
    elif n == 1: 
        return x
    else:
        return x*power(x, n-1)
    
def power_squaring(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n%2 == 0:
        return power_squaring(x*x, n//2)
    elif n%2 == 1:
        return power_squaring(x*x, n//2)*n

print(power_squaring(2,3))