# program to print prime numbers in an given range
def prime_number(a):

    if a < 2:
        return []
    primes = [2]
    # skip even number from iteration
    for i in range(3,a+1,2):
        is_prime = True

        j = 3
        while j*j <= i:
            if i % j == 0:
                is_prime = False
                break
            j+=2

        if is_prime:
            primes.append(i)
    return primes
n = prime_number(20)
print(n)