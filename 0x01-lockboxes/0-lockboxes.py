#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize a list to keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True  # Mark the first box as visited

    # Initialize a list to keep track of keys we have
    keys = boxes[0]

    # Iterate through the keys list
    while keys:
        key = keys.pop(0)  # Get the first key from the list
        if not visited[key]:
            visited[key] = True  # Mark the box as visited
            keys += boxes[key]  # Add the keys from the box to the keys list

    # Check if all boxes have been visited
    return all(visited)

