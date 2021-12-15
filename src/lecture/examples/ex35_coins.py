"""
Created on Jan 10, 2017

@author: Arthur
"""


def compute_sum(b, sum):
    """
    Compute the paid amount with the current candidate
    """
    amount = 0
    for coin in b:
        nr_coins = (sum - amount) // coin
        # If this is a candidate solution,
        # we need to use at least 1 coin
        if nr_coins == 0:
            nr_coins = 1
        amount += nr_coins * coin
    return amount


def select_most_promising(c):
    """
    Select the largest coin from the remaining
    input:
        c - candidate coins
    Return the largest coin
    """
    return max(c)


def acceptable(b, sum):
    """
    Verify if a candidate solution is valid (we are not over amount)
    """
    amount = compute_sum(b, sum)
    return amount <= sum


def solution(b, sum):
    """
    Verify if a candidate solution is an actual solution
    (we are at the required amount)
    """
    amount = compute_sum(b, sum)
    return amount == sum


def build_solution_string(b, sum):
    """
    Pretty print the solution
    """
    sol_str = ''
    amount = 0
    for coin in b:
        nr_coins = (sum - amount) // coin
        sol_str += str(nr_coins) + '*' + str(coin)
        amount += nr_coins * coin
        if sum - amount > 0:
            sol_str += " + "
    return sol_str


def greedy(c, sum):
    """
    Main function
    """
    # The empty set is the candidate solution
    b = []
    while not solution(b, sum) and c != []:
        # Select best candidate (local optimum)
        candidate = select_most_promising(c)
        c.remove(candidate)
        # If the candidate is acceptable, add it
        if acceptable(b + [candidate], sum):
            b.append(candidate)
    if solution(b, sum):
        return build_solution_string(b, sum)


'''
    Let's see how it works
'''
for amount in range(1, 55):
    print('Amount ' + str(amount) + "=" + greedy([1, 5, 10], amount))
