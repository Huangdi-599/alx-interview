#!/usr/bin/python3
"""
Module for calculating the fewest number of operations to reach a specific number of characters
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to obtain n characters
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    if n > 1:
        operations += n

    return operations
