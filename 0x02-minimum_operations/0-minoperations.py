#!/usr/bin/python3
""" Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n
"""


def minOperations(n):
    """ Given a number n, write a method that calculates
        the fewest number of operations needed to result in exactly n
    """
    if n <= 1:
        return 0

    run = [0] * (n + 1)

    for i in range(2, n + 1):
        run[i] = i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                run[i] = min(run[i], run[j] + i // j)

    return run[n]
