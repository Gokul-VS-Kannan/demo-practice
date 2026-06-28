# division without using / operator

def division(dividend,divisor):
    # checking zero division
    if divisor == 0:
        return "Division by zero not possible"
    
    quotient = 0
    
    # checking sign
    
    if (dividend<0) ^ (divisor<0):
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    # looping
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    return sign*quotient, dividend

n1,n2 = division(43,9)

n1 = print("Quotient :",n1)
n2 = print("Remainder:",n2)