#!/usr/bin/python3
"""UTF-8 Validation"""


def get_bits(num):
    """returns leading set bits number"""
    set_bits = 0
    bit = 1 << 7
    while bit & num:
        set_bits += 1
        bit = bit >> 1
    return set_bits


def validUTF8(data):
    """determines if data set is valid UTF-8 encoding"""
    count = 0
    for i in range(len(data)):
        if count == 0:
            count = get_bits(data[i])
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        count -= 1
    return count == 0
