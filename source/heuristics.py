#!/usr/bin/env python3

import math
import config

def hamming_distance(grid):
    h = 0
    for i, v in enumerate(grid):
        if i != config.goal.index(v):
            h += 1
    return h

def manhattan_distance(grid):
    h = 0
    size = int(math.sqrt(len(grid)))
    for i, v in enumerate(grid):
        if i != config.goal.index(v):
            curr_col = i % size
            curr_row = i // size
            target_col = (config.goal.index(v)) % size
            target_row = (config.goal.index(v)) // size
            h += abs(target_col - curr_col) + abs(target_row - curr_row)
    return h

def linear_conflict_manhattan_distance(grid):
    h = manhattan_distance(grid)
    size = int(math.sqrt(len(grid)))
    for i, v in enumerate(grid):
        if i != config.goal.index(v):
            curr_col = i % size
            curr_row = i // size
            target_col = (config.goal.index(v)) % size
            target_row = (config.goal.index(v)) // size
                        #move left
            if target_col - curr_col > 0:
                while (curr_col < target_col):
                    i += 1
                    curr_col = i % size
                    if (grid[v] - 1) // size == target_row:
                        h += 1
                        #move right
            elif target_col - curr_col < 0:
                while (curr_col > target_col):
                    i -= 1
                    curr_col = i % size
                    if (grid[v] - 1) // size == target_row:
                        h += 1
                        #move up
            if target_row - curr_row > 0:
                while (curr_row < target_row):
                    i += 3
                    curr_row = i // size
                    if (grid[i] - 1) % size == target_col:
                        h += 1
                        #move down
            elif target_row - curr_row < 0:
                while (curr_row > target_row):
                    i -= 3
                    curr_row = i // size
                    if (grid[i] - 1) % size == target_col:
                        h += 1
    return h
