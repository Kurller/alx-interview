#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]
    for key in keys:
        if key < n and not opened[key]:
            opened[key] = True
            keys += boxes[key]
    return all(opened)

