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
    a. Recursive implementation
    b. Non-recursive implementation
"""


def rht_root(r, n, p):
    if n > 1:
        low = 1
        up = n
    else:
        low = 0
        up = 1

    while low <= up:
        mid = (low + up) / 2
        target = mid ** r

        if n - p <= target <= n + p:
            return mid
        elif target < n - p:
            low = mid
        else:
            up = mid


# print(rht_root(10,0.5,0.001))
# print(0.93310546875**10)

def find_root(x, r, p):
    if x > 1:
        return find_rth_root(1, x, x, r, p)
    return find_rth_root(0, 1, x, r, p)


def find_rth_root(lb, rb, x, r, p):
    """
    lb: right boundary
    rb: right boundary
    x: the number
    r: the root
    p: the precision
    res: result

    """
    number = (lb + rb) / 2
    res = number ** r  # average of boundaries to power r

    if (res >= (x - p)) and (res <= (x + p)):
        return number

    if res < (x - p):
        return find_rth_root(number, rb, x, r, p)

    if res > (x + p):
        return find_rth_root(lb, number, x, r, p)


# print(find_root(0.3, 10, 0.01))

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
