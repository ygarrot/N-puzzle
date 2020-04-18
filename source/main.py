#!/usr/bin/env python3
import re
from priority_queue import PriorityQueue
import fileinput
import sys

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

    puzzles = puzzles[1:]
    without_hash = without_hash.splitlines()[1:]

    for line in without_hash:
        line_length = len(line.split())
        if (line_length is not puzzle_size):
            exit("Parsing Error")
    print(puzzles)

def main():
    parse()

if __name__ == '__main__':
    main()

