"""
    Divide & Conquer
"""

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive)
    a. Chip & conquer, recursive
    b. Divide in halves, non-recursive
    c. Divide in halves, recursive
"""

"""
2. Calculate the r-th root of a given number x with a given precision p
"""


# Non-recursive solution
def n_th_root(n, r, p):
    if n < 1:
        low = 0
        high = 1
    else:
        low = 1
        high = n
    mid = (low + high) / 2
    while not (mid ** r - p <= n <= mid ** r + p):
        if mid ** r < n:
            low = (high + low) / 2
        else:
            high = (high + low) / 2
        mid = (high + low) / 2
    return mid


# Recursive Solution #
def binary_search(start, end, a, b, r):
    mid = (start + end) / 2
    if a <= mid ** r <= b:
        return mid

    if mid ** r > b:
        return binary_search(start, mid - 1, a, b, r)
    elif mid ** r < a:
        return binary_search(mid + 1, end, a, b, r)


def recursive_solution(n, r, p):
    a = n - p
    b = n + p
    x = binary_search(0, n, a, b, r)
    return x


import random


# Random testing
def test_recursive_solution():
    for i in range(1000):
        n = random.randint(0, 10)
        r = random.randint(2, 20)
        p = 1 / 10 ** random.randint(1, 6)

        x = recursive_solution(n, r, p)
        # print(n, r, p, x)
        assert n - p <= x ** r <= n + p


# test_recursive_solution()

"""
3. Calculate the maximum subarray sum (subarray = elements having continuous indices)
    a. Naive implementation
    b. Divide & conquer implementation
    
    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    Backtracking
"""

"""
4. Recursive implementation for permutations
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


bkt_rec([], 4)

"""
5. Change the code for generating the permutation above to work for the n-Queen problem
"""

"""
A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column

6. Generate all the N x N Latin squares for a given number N. 

7. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the first 
row and column are sorted.
"""
