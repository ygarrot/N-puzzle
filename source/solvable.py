import math

def get_inversions(grid):
    inversions = 0
    row = 0
    for i, v in enumerate(grid):
        if i % 2 is 0:
            row += 1
        if grid[i] is 0:
            blank_row = row
            continue
        j = i + 1
        while j < len(grid):
            if grid[j] < v and grid[j]:
                inversions += 1
            j += 1
    return inversions, row

def odd(n):
    return (n % 2) != 0

def solvable(grid):
    """Return True if the puzzle is solvable or False if it's not."""
    size = int(math.sqrt(len(grid)))
    inversions , b_row = get_inversions(grid)
    if not odd(size):
        return not odd(inversions)
    else:
        # print(size, b_row, (grid.index(0) // size)+2)
        if not odd(b_row):
            return not odd(inversions)
        return odd(inversions)
