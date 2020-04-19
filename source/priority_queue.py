#!/usr/bin/env python3

from heuristics import *
from math import sqrt
import numpy as np
import copy

heuristic_fn = manhattan_distance_heuristic

def is_valid_vertical_move(index, new_index, puzzle_size):
    return new_index >= 0 and new_index < puzzle_size

def is_valid_horizontal_move(index, new_index, puzzle_size):
    i = index - new_index
    if (new_index < 0 or new_index > puzzle_size):
        return False
    if (index is 0 and i is -1):
        return True
    if (index is 1):
        return True
    # print(((index + 1) % int(sqrt(puzzle_size))), new_index, i)
    if (((index + 1) % int(sqrt(puzzle_size))) is 0 and i is -1):
        return False
    if (((index + 1) % int(sqrt(puzzle_size))) is 1 and i is +1):
        return False
    return True

def tile_swap_2_index(new_lst, index, new_index, valid_move_fn):
    # print(index, new_index, index-new_index, "not valid" if not valid_move_fn(index, new_index, len(new_lst)) else "valid")
    if not valid_move_fn(index, new_index, len(new_lst)):
        return None

    lst = copy.deepcopy(new_lst)
    #swap
    lst[index], lst[new_index] = lst[new_index], lst[index]
    node = Node()
    node.grid = lst
    node.empty_case_index = new_index
    return node

def LEFT(i):
    return i - 1

def RIGHT(i):
    return i + 1

def UP(i, puzzle_size):
    return i - puzzle_size

def DOWN(i, puzzle_size):
    return i + puzzle_size

def swap_left(lst, index):
    return tile_swap_2_index(lst, index, LEFT(index), is_valid_horizontal_move)

def swap_right(lst, index):
    return tile_swap_2_index(lst, index, RIGHT(index), is_valid_horizontal_move)

def swap_down(lst, index):
    return tile_swap_2_index(lst, index, DOWN(index, int(sqrt(len(lst)))), is_valid_vertical_move)

def swap_up(lst, index):
    return tile_swap_2_index(lst, index, UP(index, int(sqrt(len(lst)))), is_valid_vertical_move)

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

class Node(object):
    def __init__(self, h = 0, g = 0, f = 0, empty_case_index = 0, grid = []):
        self.h = h
        self.g = g
        self.f = f
        self.empty_case_index = empty_case_index
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.parents = []
        self.grid = grid


    def __str__(self):
        lst = np.matrix(chunks(self.grid, int(sqrt(len(self.grid)))))
        return  str(lst)

    def set_parent(self):
        i = self.empty_case_index
        self.left = swap_left(self.grid, i)
        self.right = swap_right(self.grid, i)
        self.up = swap_up(self.grid, i)
        self.down = swap_down(self.grid, i)
        self.parents = [x for x in [self.right, self.left, self.up, self.down] if x is not None]
        for node in self.parents:
            node.h = heuristic_fn(node.grid)
            node.g = node.g + 1
            node.f = node.h + node.g
