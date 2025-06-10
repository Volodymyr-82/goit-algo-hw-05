from typing import Callable, Dict
def caching_fibonacci():

    cache: Dict[int, int] = {}
    def fibonacci(n):
        nonlocal cache
        if n <=0:
            return 0
        if n==1:
            return 1
        if n in cache:
            return cache[n]
        else:    
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
               
            return cache[n]

    return fibonacci
fib = caching_fibonacci()
print(fib(15))