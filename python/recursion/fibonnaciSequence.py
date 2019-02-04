def fib_iteration(n):
    a=0
    b=0

    for i in range(n):

        a,b = b,a+b

    return a


def fib_rec(n):
    # Base case
    if(n==0 or n==1):
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)



n =10
cache = [None]*(n+1)

def fib_dynamic(n):
    #Base case
    if(n==0 or n==1):
        return n

    #Check cache for fib calculate

    if cache[n] != None:
        return cache[n]
    
    #Keep setting cache
    cache[n] = fib_dynamic(n-1)+fib_dynamic(n-2)

    return cache[n]