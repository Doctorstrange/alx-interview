#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding."""


def count_leading_ones(set):
    """Returns number of leading set"""
    count = 0
    cover = 1 << 7
    while set & cover:
        count += 1
        cover >>= 1
    return count


def validUTF8(data):
    """valid UTF-8 encoding representation"""
    for set in data:
        leading_ones = count_leading_ones(set)

        if leading_ones == 0:
            continue

        if leading_ones == 1 or leading_ones > 4:
            return False

        for i in range(1, leading_ones):
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False

    return True
