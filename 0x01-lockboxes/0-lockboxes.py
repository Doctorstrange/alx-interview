#!/usr/bin/python3
"""Returns the string representation of the given float `n`."""


def canUnlockAll(boxes):
    """
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 1:
        return True

    opened_boxes = set([0])

    keys_to_check = boxes[0]

    while keys_to_check:
        current_key = keys_to_check.pop()

        if current_key < len(boxes) and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys_to_check.extend(boxes[current_key])

    return len(opened_boxes) == len(boxes)
