#!/usr/bin/env python3

import math

def make_goal(s):
	ts = s*s
	puzzle = [-1 for i in range(ts)]
	cur = 1
	x = 0
	ix = 1
	y = 0
	iy = 0
	while True:
		puzzle[x + y*s] = cur
		if cur == 0:
			break
		cur += 1
		if x + ix == s or x + ix < 0 or (ix != 0 and puzzle[x + ix + y*s] != -1):
			iy = ix
			ix = 0
		elif y + iy == s or y + iy < 0 or (iy != 0 and puzzle[x + (y+iy)*s] != -1):
			ix = -iy
			iy = 0
		x += ix
		y += iy
		if cur == s*s:
			cur = 0

	return puzzle

def hamming_distance_heuristic(grid):
	h = 0
	for i, v in enumerate(grid):
		if v - 1 != i and v != 0:
			h += 1
	return h

def manhattan_distance_heuristic(grid):
	h = 0
	goal = make_goal(int(math.sqrt(len(grid))))
	size = int(math.sqrt(len(grid)))
	for i, v in enumerate(grid):
		if i != goal.index(v):
			curr_col = i % size
			curr_row = i // size
			target_col = (goal.index(v)) % size
			target_row = (goal.index(v)) // size
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
