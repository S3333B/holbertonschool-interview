#!/usr/bin/python3
"""
Minimum Operations module.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters.

    Args:
        n (int): target number of H characters

    Returns:
        int: minimum number of operations, or 0 if impossible
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
