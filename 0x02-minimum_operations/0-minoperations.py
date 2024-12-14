#!/usr/bin/python3
"""
Minimum Operations
"""

import math


def factors(n):
    """factors of number"""
    lst = []
    while n % 2 == 0:
        lst.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            lst.append(i)
            n = n / i
    if n > 2:
        lst.append(n)
    return lst


def minOperations(n):
    """minimum operations"""
    if type(n) != int or n < 2:
        return 0
    else:
        numop = sum(factors(n))
        return int(numop)
