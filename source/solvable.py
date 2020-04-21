import math

def get_inversions(grid):
	inversions = 0
	for i, v in enumerate(grid):
		if (v != 0):
			j = i + 1
			while j < len(grid):
				if grid[j] < v and grid[j] != 0:
					inversions += 1
				j += 1
	return inversions

def odd(n):
	return n % 2

def solvable(grid):
	"""Return True if the puzzle is solvable or False if it's not."""
	size = int(math.sqrt(len(grid)))
	inversions = get_inversions(grid)
	if odd(size):
		if odd(inversions):
			return False
		else:
			return True
	else:
		if (odd(inversions) and odd(grid.index(0) // size + 1)) or (not odd(inversions) and not odd(grid.index(0) // size + 1)):
			return True
		else:
			return False
