import math

def snail_to_ordered(grid):
	size = int(math.sqrt(len(grid)))
	grid_ret = grid.copy()
	for i in range(size // 2):
		for j in range(size - 1 - 2 * i):
			index = size + j
			for k in range(i):
				index += (4 * (size - 2 * (k + 1))) + 2
			grid_ret[index] = grid[size * (j + i + 2) - i - 1]
	for i in range((size - 1) // 2):
		for j in range(size - 1 - 2 * i):
			index = size + (size - 1) + j
			for k in range(i):
				index += (4 * (size - 2 * (k + 1)))
			grid_ret[index] = grid[size * (size - i) - (2 + i) - j]
	for i in range((size - 1) // 2):
		for j in range(size - 2 - 2 * i):
			index = size + 2 * (size - 1) + j
			for k in range(i):
				index += (4 * (size - 2 * (k + 1))) - 2
			grid_ret[index] = grid[size * (size - (2 + i)) - size * j + i]
	for i in range((size - 2) // 2):
		for j in range(size - 2 - 2 * i):
			index = size + 2 * (size - 1) + (size - 2) + j
			for k in range(i):
				index += (4 * (size - 2 * (k + 1))) - 4
			grid_ret[index] = grid[size * (i + 1) + (i + 1) + j]
	grid_ret[len(grid_ret) - 1] = 0
	return grid_ret

def ordered_to_snail(grid):
	size = int(math.sqrt(len(grid)))

def main():
	grid = snail_to_ordered([1,2,3,8,0,4,7,6,5])
	print(grid[0:3])
	print(grid[3:6])
	print(grid[6:9])
	print()
	grid = snail_to_ordered([1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7])
	print(grid[0:4])
	print(grid[4:8])
	print(grid[8:12])
	print(grid[12:16])
	print()
	grid = snail_to_ordered([1,2,3,4,5,16,17,18,19,6,15,24,0,20,7,14,23,22,21,8,13,12,11,10,9])
	print(grid[0:5])
	print(grid[5:10])
	print(grid[10:15])
	print(grid[15:20])
	print(grid[20:25])
	print()
	grid = snail_to_ordered([1,2,3,4,5,6,20,21,22,23,24,7,19,32,33,34,25,8,18,31,0,35,26,9,17,30,29,28,27,10,16,15,14,13,12,11])
	print(grid[0:6])
	print(grid[6:12])
	print(grid[12:18])
	print(grid[18:24])
	print(grid[24:30])
	print(grid[30:36])
	print()
	grid = snail_to_ordered([1,2,3,4,5,6,7,24,25,26,27,28,29,8,23,40,41,42,43,30,9,22,39,48,0,44,31,10,21,38,47,46,45,32,11,20,37,36,35,34,33,12,19,18,17,16,15,14,13])
	print(grid[0:7])
	print(grid[7:14])
	print(grid[14:21])
	print(grid[21:28])
	print(grid[28:35])
	print(grid[35:42])
	print(grid[42:49])
	print()



if __name__ == '__main__':
	main()
