#!/usr/bin/env python3
from priority_queue import PriorityQueue
import fileinput

def main():

    print(fileinput.input().readline())
    for line in fileinput.input():
        print(type(line))
        if line:
            print("hello world")
            
        elem_per_line = len(line.split(" "))
        print(elem_per_line)
        print(line)

if __name__ == '__main__':
    main()

