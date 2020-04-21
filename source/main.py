#!/usr/bin/env python3

import config
import re
import fileinput
import sys
from heuristics import *
from solvable import *
from snail import *
from a_star import a_star_impl

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


def parse():
    dict = {}
    with open(sys.argv[1]) as f:
        content = f.read()
    without_hash = re.sub('#.*', '', content).strip()
    puzzles = without_hash.split()
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
    return puzzles, puzzle_size

def main():
    grid, size = parse()
    if not solvable(snail_to_ordered(grid)):
        print("Error : N-puzzle not solvable !")
        quit()
    print("N-puzzle is solvable !")
    config.goal = make_goal(size)
    #check if input puzzle go from 0 to N - 1
    for tile in config.goal:
        if tile not in grid:
            exit("Parsing Error")
    a_star_impl(grid, config.goal, manhattan_distance_heuristic)

if __name__ == '__main__':
    main()

