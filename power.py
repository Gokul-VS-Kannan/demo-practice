# find power without using ** operator

def power(base,exponent):

    if base == 0:
        return 0
    if exponent == 0:
        return 1
    result = 1
    for i in range(exponent):
        result *= base

    return result

n = power(5,2)
print(n)