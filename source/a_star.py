#!/usr/bin/env python3

#f score is the sum of the cost to reach that node and the heuristic value of that node.
from priority_queue import *

def a_star_impl(grid, goal, heuristic_ptr):
    start = Node(h = heuristic_ptr(grid), empty_case_index = grid.index(0), grid = grid)
    open_set = PriorityQueue()
    start.set_parent()
    open_set.insert(start)

    closed_set = PriorityQueue()

    while open_set.queue:
        process = open_set.queue[0]
        # print(process.h)
        print(process.grid)

        # print(len(open_set.queue))
        if process is goal:
            print("solved")
            #return path(process)

        open_set.queue.remove(process)
        closed_set.insert(process)

        for node in process.parents:
            in_close = node.grid in [x.grid for x in closed_set.queue]
            in_open = node.grid in [x.grid for x in open_set.queue]
            # print(in_close)
            # print(in_open)

            if in_close:
                continue

            if not in_open:
                open_set.insert(node)
                node.set_parent()
            else:
                actual_node = node

                if node.g < actual_node.g:
                    actual_node.g = node.g
                    actual_node.h = node.h
                    actual_node.f = node.f
                    actual_node.parents = node.parents

    exit("unsolvable")
