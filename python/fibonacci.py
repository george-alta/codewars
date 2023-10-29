def productFib(prod):
    a = 0
    b = 1

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    while fib(a)*fib(b) < prod:
        a = b
        b += 1

    if fib(a)*fib(b) == prod:
        return [fib(a), fib(b), True]
    else:
        return [fib(a), fib(b), False]


print(productFib(714))
print(productFib(800))
print(productFib(4895))
print(productFib(104))
print(productFib(105))
print(productFib(5895))
