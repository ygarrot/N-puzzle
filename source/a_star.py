#!/usr/bin/env python3

#f score is the sum of the cost to reach that node and the heuristic value of that node.
from priority_queue import *

def a_star_impl(grid, goal, heuristic_ptr):
    start = Node(h = heuristic_ptr(grid), empty_case_index = grid.index(0), grid = grid)
    start.set_parent()

    open_set = PriorityQueue()
    open_set.insert(start)

    closed_set = PriorityQueue()

    while open_set.queue:
        process = open_set.queue[-1]

        if process is goal:
            print("solved")
            #return path(process)

        open_set.queue.remove(process)
        closed_set.insert(process)

        for node in process.parents:

            if node in closed_set.queue:
                continue

            if node not in open_set.queue:
                open_set.insert(node)
            else:
                actual_node = node

                if node.g < actual_node.g:
                    actual_node.g = node.g
                    actual_node.f = node.f
                    actual_node.parents = node.parents

    exit("unsolvable")
