# division without using / operator

def division(divident,divisor):
    # checking zero division
    if divisor == 0:
        return "Division by zero not possible"
    
    quotient = 0
    
    # checking sign
    
    if divident<0 or divisor<0:
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    # looping
    while divident >= divisor:
        divident -= divisor
        quotient += 1

    return sign*quotient, divident

n1,n2 = division(43,9)

n1 = print("Quotient :",n1)
n2 = print("Remainder:",n2)