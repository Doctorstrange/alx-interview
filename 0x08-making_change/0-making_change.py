#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    hold = 0
    temp = 0
    coins.sort(reverse=True)
    for x in coins:
        while hold < total:
            hold += x
            temp += 1
        if hold == total:
            return temp
        hold -= x
        temp -= 1
    return -1
