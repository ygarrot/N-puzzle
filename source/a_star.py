#!/usr/bin/env python3

#f score is the sum of the cost to reach that node and the heuristic value of that node.
import config
from Node import *

def print_recc(f, elem):
    if (elem.child):
        print_recc(f, elem.child)
    f.write(' '.join([str(x) for x in elem.grid]))
    f.write('\n')

def print_for_visu(process):
    f = open("test/visu.txt", "w")
    print_recc(f, process)
    f.close()

def a_star_impl(grid, goal, heuristic_ptr):
    heuristic_ptr= config.heuristic_fn
    start = Node(h = heuristic_ptr(grid), empty_case_index = grid.index(0), grid = grid)
    open_set = []
    closed_set = []
    open_set.append(start)

    while open_set:
        #calc fscore
        process = min(open_set, key=lambda x:x.h + x.g)
        if process.h is 0 or process.grid is goal:
            print_for_visu(process)
            return

        open_set.remove(process)
        closed_set.append(process)
        process.set_parent()
        for node in process.parents:
            # in_close = node.grid in [x.grid for x in closed_set]
            # in_open = node.grid in [x.grid for x in open_set]
            in_close = node in closed_set
            in_open = node in open_set
            if in_close:
                continue
            new_g = process.g + 1
            if not in_open:
                node.g = new_g
                # node.set_parent()
                open_set.append(node)
            else:
                if (node.g > new_g):
                    node.g = new_g
    raise ValueError('No Path Found')
