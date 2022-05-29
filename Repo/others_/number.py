import math
import sympy

# checks if number is odd, square, cube and divisible by 12 prime numbers
def match_number(number):
    match = False
    divisible_count = 0 # keep track of how many prime numbers can divide number

    if number >= 37: # 12th prime number is 37

        # check if number is a square
        sroot = math.sqrt(number)
        is_square = (number == int(sroot + 0.5) ** 2)

        # check if number is a cube
        croot = number**(1.0/3.0)
        is_cube = (number == int(croot + 0.5) ** 3)
        
        # check if number is odd
        is_odd = (number%2 == 1)

        # check if number is square, cube and odd
        if is_square and is_cube and is_odd:
            match = True
        
        # if number is square, cube and odd
        if match:
            # get all prime numbers less than or equal to number
            primes = list(sympy.primerange(1,number))

            if len(primes) >= 12: # check if there's 12 or more prime numbers from 2 to number
                for prime in primes:
                    if number%prime == 0: # if divisible by prime, increment count
                        divisible_count += 1
                        if divisible_count == 12 and match: # if number divisible by 12 prime
                            return True
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

# finds smallest odd number that is a square, odd and divisible by 12 prime numbers
def smallest_number():
    smallest_match = 1

    # loop through while the target number is not found
    while not match_number(smallest_match):
        smallest_match += 1
    return smallest_match

print(smallest_number())
