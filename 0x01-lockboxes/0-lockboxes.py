#!/usr/bin/python3
''' lockbox module '''
def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track the locked/unlocked status of each box
    unlocked[0] = True  # The first box is initially unlocked

    # Iterate through each box and check its keys
    for box in range(n):
        if unlocked[box]:
            for key in boxes[box]:
                if key < n:  # Ignore keys that don't correspond to a box
                    unlocked[key] = True

    # Check if all boxes are unlocked
    return all(unlocked)

