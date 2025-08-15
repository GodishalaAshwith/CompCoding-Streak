import math

def isPowerOfFour(n):
    if n <= 0:
        return False
    x = math.log(n, 4)
    return x.is_integer()
