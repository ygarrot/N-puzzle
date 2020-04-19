all: gen

run:
	./source/main.py 

gen:
	./res_npuzzle-gen.py -i 12 3 > test/test.txt
	head -1 test/test.txt
	./source/main.py test/test.txt
