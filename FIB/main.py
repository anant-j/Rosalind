import time
n = 28
k = 2

def fib(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1, k) + k*fib(n-2, k)

def fib_with_memo(n, k, memo):
    if n == 1 or n == 2:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib_with_memo(n-1, k, memo) + k*fib_with_memo(n-2, k, memo)
            return memo[n]

start_time = time.time()
print(fib(n, k))
print((time.time() - start_time))

start_time = time.time()
print(fib_with_memo(n, k, {}))
print((time.time() - start_time))