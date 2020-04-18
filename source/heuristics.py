#!/usr/bin/env python3

import math

def hamming_distance_heuristic(grid):
	h = 0
	for i, v in enumerate(grid):
		if v - 1 != i and v != 0:
			h += 1
	return h

def manhattan_distance_heuristic(grid):
	h = 0
	size = int(math.sqrt(len(grid)))
	for i, v in enumerate(grid):
		if v - 1 != i and v != 0:
			curr_col = i % size
			curr_row = i // size
			target_col = (v - 1) % size
			target_row = (v - 1) // size
			h += abs(target_col - curr_col) + abs(target_row - curr_row)
	return h

def linear_conflict_manhattan_distance_heuristic(grid):
	h = manhattan_distance_heuristic(grid)
	size = int(math.sqrt(len(grid)))
	for i, v in enumerate(grid):
		if v - 1 != i and v != 0:
			curr_col = i % size
			curr_row = i // size
			target_col = (v - 1) % size
			target_row = (v - 1) // size
                        #move left
			if target_col - curr_col > 0:
				while (curr_col < target_col):
					curr_col += 1
					if (grid[curr_row * size + curr_col] - 1) // size == target_row:
						h += 1
                        #move right
			elif target_col - curr_col < 0:
				while (curr_col > target_col):
					curr_col -= 1
					if (grid[curr_row * size + curr_col] - 1) // size == target_row:
						h += 1
                        #move up
			if target_row - curr_row > 0:
				while (curr_row < target_row):
					curr_row += 1
					if (grid[curr_row * size + curr_col] - 1) % size == target_col:
						h += 1
                        #move down
			elif target_row - curr_row < 0:
				while (curr_row > target_row):
					curr_row -= 1
					if (grid[curr_row * size + curr_col] - 1) % size == target_col:
						h += 1
	return h
