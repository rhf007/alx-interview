#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    check if all boxes are unlocked

    Parameters:
    boxes (List[List[int]]): The list of boxes

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    seen = set([0])
    unseen = set(boxes[0]).difference(set([0]))
    while len(unseen) > 0:
        key = unseen.pop()
        if key == 0 or key >= n or key < 0:
            continue
        if key not in seen:
            unseen = unseen.union(boxes[key])
            seen.add(key)
    return n == len(seen)
