all: gen

run:
	./source/main.py

gen:
	# ./res_npuzzle-gen.py -u -i 1 4 > test/test.txt
	head -1 test/test.txt
	./source/main.py test/test.txt
