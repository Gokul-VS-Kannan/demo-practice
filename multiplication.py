# mutiply 2 numbers without * operator

def multiply(n1,n2):
    if n1 == 0 or n2 ==0:
        return 0
    # check the sign for result
    if (n1 < 0) ^ (n2 < 0):
        sign = -1
    else:
        sign = 1
    # convert numbers into positive
    n1 = abs(n1)
    n2 = abs(n2)
    result = 0
    if n1 < n2:
        # swapping values
        n1,n2 = n2,n1

    for i in range (n2):
        result += n1
    return sign * result
    
n = multiply(-5,-8)
print(n)