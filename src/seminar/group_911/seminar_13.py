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


def get_lower_bound(number):
    if number >= 1:
        return 1
    else:
        return 0


def get_upper_bound(number):
    if number >= 1:
        return number
    else:
        return 1


def search_root(root_order, number, precision):
    return search_root_implementation(get_lower_bound(number), get_upper_bound(number), root_order, number, precision)


def search_root_implementation(lower, upper, root_order, number, precision):
    middle = lower + ((upper - lower) / 2)
    approximation = middle ** root_order
    if number - precision <= approximation <= number + precision:
        return middle

    if approximation < number - precision:
        return search_root_implementation(middle, upper, root_order, number, precision)
    else:
        return search_root_implementation(lower, middle, root_order, number, precision)


# Badea Dan
"""
r-th root of a number with precision p ( non recursive )
"""


def search_root_ab(r, n, p):
    a = 1
    b = 1

    while (a / b) ** r < n - p or (a / b) ** r > n + p:
        if (a / b) ** r > n + p:
            b = b + 1
        else:
            a = a + 1
    return a / b


import random


# Random testing
def test_search_root():
    for i in range(1000):
        n = random.randint(0, 10)
        r = random.randint(2, 20)
        p = 1 / (10 ** random.randint(1, 6))

        # x = search_root(r, n, p)
        x = search_root_ab(r, n, p)

        print(n, r, p, x)
        assert n - p <= x ** r <= n + p


# test_search_root()
# Cirstea Andrei (I think it's working)


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
