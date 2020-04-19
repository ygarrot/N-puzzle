#!/usr/bin/env python3

from heuristics import *
import copy

heuristic_fn = manhattan_distance_heuristic
def is_valid_move(index, puzzle_size):
    return index >= 0 and index < puzzle_size

def tile_swap_2_index(new_lst, index, new_index):
    if not is_valid_move(LEFT(new_index), len(new_lst)):
        return None
    lst = copy.deepcopy(new_lst)
    #swap
    lst[index], lst[new_index] = lst[new_index], lst[index]
    node = Node()
    node.grid = lst
    node.empty_case_index = new_index
    node.h = heuristic_fn(lst)
    return node

def LEFT(i):
    return i + 1

def RIGHT(i):
    return i - 1

def UP(i, puzzle_size):
    return i + puzzle_size

def DOWN(i, puzzle_size):
    return i - puzzle_size

def swap_left(lst, index):
    return tile_swap_2_index(lst, index, LEFT(index))

def swap_right(lst, index):
    return tile_swap_2_index(lst, index, RIGHT(index))

def swap_down(lst, index):
    return tile_swap_2_index(lst, index, DOWN(index, int(sqrt(len(lst)))))

def swap_up(lst, index):
    return tile_swap_2_index(lst, index, UP(index, int(sqrt(len(lst)))))

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

from math import sqrt
import numpy as np
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
        return  str(lst) + ' '.join([str(i) for i in self.parents])

    def set_parent(self):
        i = self.empty_case_index
        puzzle_size = int(sqrt(len(self.grid)))

        self.left = swap_left(self.grid, i)
        self.right = swap_right(self.grid, i)
        self.up = swap_up(self.grid, i)
        self.down = swap_down(self.grid, i)

        self.parents = [x for x in [self.right, self.left, self.up, self.down] if x is not None]
        # for node in self.parents:
        #     print(node)


#maybe set in in constructor later
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def insert(self, node):
        node.set_parent()
        if len(self.queue) is 0:
            self.queue.append(node)
            return
        for i, elem in enumerate(self.queue):
            if (elem.h is 0):
                print(elem.grid)
                exit()
            if elem.h > node.h:
                self.queue.insert(i, node)
                return
        # print('\n'.join([str(x) for x in self.queue]))
        self.queue.append(node)

    def clean(self):
        for node in self.queue:
            del node

