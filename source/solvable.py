import math

def get_inversions(grid):
    inversions = 0
    for i in range(len(grid)):
        if grid[i] is 0:
            continue
        for j in range(i + 1, len(grid)):
            if grid[j] is not 0 and grid[i] > grid[j]:
                inversions += 1
    return inversions

def odd(n):
    return (n % 2) != 0

def solvable(grid):
    """Return True if the puzzle is solvable or False if it's not."""
    size = int(math.sqrt(len(grid)))
    inversions = get_inversions(grid)
    if odd(size):
        return not odd(inversions)
    else:
        if odd(grid.index(0)):
            return not odd(inversions)
        return odd(inversions)
