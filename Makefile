all: gen

run:
	./source/main.py 

gen:
	./res_npuzzle-gen.py -s -i 1 3 > test/test.txt
	head -1 test/test.txt
	./source/main.py test/test.txt
