from functools import cache


def fact(n):
    if (n==0):
        return 1
    return n*fact(n-1)

#for i in range(30):
   # print(i, fact(i))

def fib(n):
    if(n<=2):
        return 1
    return fib(n-1) + fib(n-2)

def fibcached(n)
    if(n in cache):



        return 1
    return fib(n-1) + fib(n-2)

