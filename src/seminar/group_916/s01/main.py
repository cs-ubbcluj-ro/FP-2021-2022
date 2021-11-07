"""

@author: radu
Problem 1
a) Compute the sum of the first n natural numbers.
b) Check if a given integer number n is prime.
c) Compute the greatest common divisor between two integers a and b.
d) Compute the first prime number greater than a given integer n.
e) Print the first k prime numbers greater than a given integer n.

 
"""
from math import sqrt


def sum_of_first_n_natural_numbers(n):
    """ Computes the sum of the first n natural numbers.

    Given n, a natural number, the function return the sum of the first n natural numbers.
    n: natural number
    Returns: the sum of the first n natural numbers
    """
    s = 0
    for i in range(n):
        s += i

    return s


def is_prime(n):
    # todo: docs
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a if a > 0 else -a


def next_prime(n):
    while True:
        n = n + 1
        if is_prime(n):
            return n


if __name__ == '__main__':
    print("hello")
    print(sum_of_first_n_natural_numbers(3))
    print(is_prime(49))
    print(gcd(12, -18))
    print(next_prime(17))
    print("bye")
