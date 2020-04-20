import math

def get_inversions(grid):
    inversions = 0
    for i, v in enumerate(grid):
        if grid[i] is 0:
            continue
        j = i + 1
        while j < len(grid):
            if grid[j] < v and grid[j]:
                inversions += 1
            j += 1
    return inversions

def odd(n):
    return (n % 2) != 0

def solvable(grid):
    """Return True if the puzzle is solvable or False if it's not."""
    size = int(math.sqrt(len(grid)))
    inversions = get_inversions(grid)
    if not odd(size):
        return not odd(inversions)
    else:
        if not odd(grid.index(0)):
            return not odd(inversions)
        return odd(inversions)
