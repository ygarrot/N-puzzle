#!/usr/bin/env python3

#f score is the sum of the cost to reach that node and the heuristic value of that node.
import config
from Node import *
import numpy as np
from PriorityQueue import *

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def print_recc(f, elem):
    if (elem.child):
        print_recc(f, elem.child)
    print(np.matrix(chunks(elem.grid, elem.sqrt)))
    print()
    f.write(' '.join(['{: >2}'.format(x) for x in elem.grid]))
    f.write('\n')

def print_for_visu(process):
    f = open("test/visu.txt", "w")
    print_recc(f, process)
    f.close()

def a_star_impl(grid, goal, heuristic_ptr):
    heuristic_ptr= config.heuristic_fn
    start = Node(h = heuristic_ptr(grid), empty_case_index = grid.index(0), grid = grid)
    open_set = PriorityQueue()
    closed_set = PriorityQueue()
    open_set.insert(start)
    time_complexity = 0

    while open_set:
        process = open_set.pop()
        if process.h is 0 or process.grid is goal:
            print("Ordered Sequence:")
            print_for_visu(process)
            print("Time Complexity: {}\n"
                  "Number of moves: {}".format(time_complexity, process.g))
            return
        closed_set.insert(process)
        process.set_parent()
        for node in process.parents:
            in_close = node.grid in [x.grid for x in closed_set.queue]
            in_open = node.grid in [x.grid for x in open_set.queue]
            # in_close = node in closed_set.queue
            # in_open = node in open_set.queue
            if in_close:
                continue
            new_g = process.g + 1
            if not in_open:
                node.g = new_g
                open_set.insert(node)
                time_complexity += 1
            else:
                if (node.g > new_g):
                    node.g = new_g
            node.f = config.calc_fScore(node.h, node.g)
    raise ValueError('No Path Found')
