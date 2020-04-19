#!/usr/bin/env python3
import re
import fileinput
import sys
from heuristics import *
from solvable import *
from a_star import a_star_impl

def parse():
    dict = {}
    with open(sys.argv[1]) as f:
        content = f.read()
    without_hash = re.sub('#.*', '', content).strip()
    puzzles = without_hash.split()
    print(without_hash)
    try:
        puzzle_size = int(puzzles[0])
    except:
        exit("Parsing Error int" + puzzles[0])

    puzzles = [ int(puzzle) for puzzle in puzzles[1:]]
    without_hash = without_hash.splitlines()[1:]

    for line in without_hash:
        line_length = len(line.split())
        if (line_length is not puzzle_size):
            exit("Parsing Error")
    print(puzzles)
    return puzzles, puzzle_size

def main():
    grid, size = parse()
    if not solvable(grid):
        print("Error: This N-puzzle isn't solvable.")
        return
    goal = [i + 1 for i in range(size * size)]
    goal[-1] = 0
    #check if input puzzle go from 0 to N - 1
    for tile in goal:
        if tile not in grid:
            exit("Parsing Error")
    a_star_impl(grid, goal, manhattan_distance_heuristic)

if __name__ == '__main__':
    main()

