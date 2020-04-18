#!/usr/bin/env python3
from priority_queue import PriorityQueue
import fileinput

def parse():
	dict = {}
	with open("../test.txt") as f:
		content = f.read().splitlines()
	for j, line in enumerate(content):
		line = line.split()
		for i, word in enumerate(line):
			if "#" in word:
				del line[i + 1:]
				word = word[word.index('#') + 1:]
			dict[j * 3 + i] = word;
	print(dict)

def main():
	parse()

if __name__ == '__main__':
    main()

