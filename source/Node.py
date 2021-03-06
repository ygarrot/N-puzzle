#!/usr/bin/env python3

import config
from heuristics import *
from math import sqrt
import numpy as np
import copy

def LEFT(i):
    return i - 1

def RIGHT(i):
    return i + 1

def UP(i, puzzle_size):
    return i - puzzle_size

def DOWN(i, puzzle_size):
    return i + puzzle_size

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

class Node(object):
    def __init__(self, h = 0, g = 0, f = 0, empty_case_index = 0, grid = []):
        self.h = h
        self.g = g
        self.f = f
        self.index = empty_case_index
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.size = len(grid)
        self.sqrt = int(sqrt(len(grid)))
        self.child = None
        self.parents = []
        self.grid = grid


    def __eq__(self, other):
        return self.f == other.f

    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
        lst = np.matrix(chunks(self.grid, int(sqrt(len(self.grid)))))
        return  str(lst)

    def set_parent(self):
        self.left    = self.swap_left()
        self.right   = self.swap_right()
        self.up      = self.swap_up()
        self.down    = self.swap_down()
        self.parents = [x for x in [self.right, self.left, self.up, self.down] if x is not None]

        for node in self.parents:
            node.h     = config.heuristic_fn(node.grid)
            node.size  = len(node.grid)
            node.sqrt  = int(sqrt(len(node.grid)))
            node.child = self
            node.g     = self.g + 1
            node.f     = config.calc_fScore(node.h, node.g)

    def swap_left(self):
        return self.tile_swap_2_index(LEFT(self.index), self.is_valid_horizontal_move)

    def swap_right(self):
        return self.tile_swap_2_index(RIGHT(self.index), self.is_valid_horizontal_move)

    def swap_down(self):
        return self.tile_swap_2_index(DOWN(self.index, self.sqrt), self.is_valid_vertical_move)

    def swap_up(self):
        return self.tile_swap_2_index(UP(self.index, self.sqrt), self.is_valid_vertical_move)

    def is_valid_vertical_move(self, new_index):
        return new_index >= 0 and new_index < self.size

    def is_valid_horizontal_move(self, new_index):
        index = self.index
        i = index - new_index
        if (new_index < 0 or new_index > self.size):
            return False
        if (index is 0 and i is -1):
            return True
        if (index is 1):
            return True
        if (((index + 1) % self.sqrt) is 0 and i is -1):
            return False
        if (((index + 1) % self.sqrt) is 1 and i is +1):
            return False
        return True

    def tile_swap_2_index(self, new_index, valid_move_fn):
        index = self.index
        if not valid_move_fn(new_index):
            return None
        lst = copy.deepcopy(self.grid)
        lst[index], lst[new_index] = lst[new_index], lst[index]
        node = Node()
        node.grid = lst
        node.index = new_index
        return node
