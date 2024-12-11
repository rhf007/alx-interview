#!/usr/bin/python3
"""
Prime Game
"""


def primes(n):
    """Return list of prime numbers between 1 and n
       Args:
         n: Range
    """
    p = []
    s = [True] * (n + 1)
    for j in range(2, n + 1):
        if (s[j]):
            p.append(j)
            for i in range(j, n + 1, j):
                s[i] = False
    return p


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x: no. of rounds
        nums: Range for each round
    Return:
        Winner or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    M = B = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            B += 1
        else:
            M += 1
    if M > B:
        return 'Maria'
    elif B > M:
        return 'Ben'
    return None
