# division without / operator
# reduced time coplexity

def division(dividend,divisor):
    if divisor == 0:
        return "Division by zero not possible"
    
    quotient = 0
    
    # checking sign
    
    if dividend<0 or divisor<0:
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        temp = divisor
        multiple = 1

        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1

        dividend -= temp
        quotient += multiple

    return sign * quotient, dividend

n1,n2 = division(43,5)

n1 = print("Quotient :",n1)
n2 = print("Remainder:",n2)