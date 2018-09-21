def fib(n):
    if n in [0,1] :
        return n

    return fib(n-1)+fib(n-2)

print fib(5)

# use generator
def fib2():
    a,b = 0,1

    while True:
       yield a
       a, b = b, a+b 

for ind, res in enumerate(fib2()):
    if ind==6:
        print ind, res
        break
