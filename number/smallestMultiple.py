def smallest_multiple(n):
    output = 1
    primes = []

    for i in range(2, n+1):
        exponent = 1
        multiple = i
        skip = False

        for prime in primes:
            if i % prime == 0:
                skip = True
                break     

        while not skip and pow(i, exponent) <= n:
            multiple = pow(i, exponent)
            exponent += 1
            
        if not skip:
            primes.append(i)
            output *= multiple

    return output

print smallest_multiple(20)
