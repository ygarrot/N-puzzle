import numpy as np
from math import sqrt

def chunks(l):
    n = int(sqrt(len(l)))
    return np.matrix([l[i:i+n] for i in range(0, len(l), n)])

def snail_to_ordered_by_ygarrot(snail, goal, size):
    '''
    snail_to_ordered and ordered_to_snail functions are
    historical curiosities left over from earlier days before
    the advent of N-puzzle solving.
    '''
    toto        = []
    ordered = [i + 1 for i in range(size * size)]
    ordered[-1] = 0

    for i in range(len(ordered)):
        toto.insert(i, snail[goal.index(ordered[i])])
    return toto


# def snail_to_ordered(grid):
# 	size = int(math.sqrt(len(grid)))
# 	grid_ret = grid.copy()
# 	for i in range(size // 2):
# 		for j in range(size - 1 - 2 * i):
# 			index = size + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1))) + 2
# 			grid_ret[index] = grid[size * (j + i + 2) - i - 1]
# 	for i in range((size - 1) // 2 + (1 - size % 2)):
# 		for j in range(size - 1 - 2 * i):
# 			index = size + (size - 1) + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1)))
# 			grid_ret[index] = grid[size * (size - i) - (2 + i) - j]
# 	for i in range((size - 1) // 2):
# 		for j in range(size - 2 - 2 * i):
# 			index = size + 2 * (size - 1) + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1))) - 2
# 			grid_ret[index] = grid[size * (size - (2 + i)) - size * j + i]
# 	for i in range((size - 2) // 2 + size % 2):
# 		for j in range(size - 2 - 2 * i):
# 			index = size + 2 * (size - 1) + (size - 2) + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1))) - 4
# 			grid_ret[index] = grid[size * (i + 1) + (i + 1) + j]
# 	return grid_ret

# def ordered_to_snail(grid):
# 	size = int(math.sqrt(len(grid)))
# 	grid_ret = grid.copy()
# 	for i in range(size // 2):
# 		for j in range(size - 1 - 2 * i):
# 			index = size + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1))) + 2
# 			grid_ret[size * (j + i + 2) - i - 1] = grid[index]
# 	for i in range((size - 1) // 2):
# 		for j in range(size - 1 - 2 * i):
# 			index = size + (size - 1) + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1)))
# 			grid_ret[size * (size - i) - (2 + i) - j] = grid[index]
# 	for i in range((size - 1) // 2):
# 		for j in range(size - 2 - 2 * i):
# 			index = size + 2 * (size - 1) + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1))) - 2
# 			grid_ret[size * (size - (2 + i)) - size * j + i] = grid[index]
# 	for i in range((size - 2) // 2):
# 		for j in range(size - 2 - 2 * i):
# 			index = size + 2 * (size - 1) + (size - 2) + j
# 			for k in range(i):
# 				index += (4 * (size - 2 * (k + 1))) - 4
# 			grid_ret[size * (i + 1) + (i + 1) + j] = grid[index]
# 	if size % 2:
# 		grid_ret[len(grid_ret) // 2] = 0
# 	else:
# 		grid_ret[len(grid_ret) // 2 + (size - 4) // 2 + 1] = 0
# 	return grid_ret
