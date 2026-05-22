#!/usr/bin/python3
"""
Module that contains the function canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): list of lists containing keys

    Returns:
        True if all boxes can be opened, otherwise False
    """

    opened = set([0])
    keys = [0]

    while keys:
        current = keys.pop()

        for key in boxes[current]:

            if key < len(boxes) and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
