"""
    Recursion

    1. A recursive step -> progress towards a base case
    2. A non-recursive step must exist
"""


def factorial(n):
    """
    Determine the factorial of given number
    :param n: Determine n!
    :return: n!
    """
    if n == 0:
        # Base case, without recursion
        return 1

    # Take the recursive step
    return n * factorial(n - 1)


# print(factorial(6))

# 0,1, 1, 2, 3, 5, 8, 11, ...
def fib(n):
    """
    Determine n-th term of Fibonacci
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)


# T(n) = T(n-2) + T(n-1) + 1, n > 1
# T(n) = 1, n <= 1
# T(n) = ( 2^(n-1) ) + 1

# Store precalculated values here
memory = {0: 1, 1: 1}


def fib_2(n):
    """
    Determine n-th term of Fibonacci
    :param n:
    :return:
    """
    if n not in memory:
        memory[n] = fib_2(n - 2) + fib_2(n - 1)
    return memory[n]


# T(n) = n


print(fib(40))
# print(fib_2(400))
