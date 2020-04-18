#!/usr/bin/env python3

def parse():
	with open("../test.txt") as f:
		content = f.read().splitlines()
	for line in content:
		line = line.split()
		for i, word in enumerate(line):
			if "#" in word:
				del line[i + 1:]
				del word[word.index('#'):]
		print(line)
	print(content)

def main():
	parse()

if __name__ == '__main__':
    main()

