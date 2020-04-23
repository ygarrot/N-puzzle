#!/usr/bin/env python3
import argparse
import config
import re
import heuristics
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


def parse_file(file_name):
    dict = {}
    with open(file_name) as f:
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

def parse_arg():
    parser = argparse.ArgumentParser(description='Faster N-Puzzle you have ever seen')
    parser.add_argument("-g", "--greedy", default=False, action="store_true",
                                       help="Are You a Greedy Bastard?")
    parser.add_argument("-a", "--algorithm", dest="heuristic",
            default="linear_conflict_manhattan_distance",
            choices=["hamming_distance", "manhattan_distance", "linear_conflict_manhattan_distance"],
            help="choose algorithm function")
    parser.add_argument("path", type=str, default="none", help="input file name")
    args = parser.parse_args()
    config.is_greedy = args.greedy
    config.heuristic_fn = getattr(heuristics, args.heuristic)
    return args.path

def main():
    grid, size = parse_file(parse_arg())
    config.goal = make_goal(size)
    if not solvable(grid):
        print("Error : N-puzzle not solvable !")
        return
    print("N-puzzle is solvable !")
    #check if input puzzle go from 0 to N - 1
    for tile in config.goal:
        if tile not in grid:
            exit("Parsing Error")
    a_star_impl(grid, config.goal, config.heuristic_fn)

if __name__ == '__main__':
    main()
