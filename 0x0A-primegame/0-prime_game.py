#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # initializes possible prime numbers
    ben = 0
    maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)
    # for each game round
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # to determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    carry out called function
    """
    # check through prime numbers
    for x in range(2, len(ls)):
        try:
            ls[x * x] = 0
        except (ValueError, IndexError):
            break
