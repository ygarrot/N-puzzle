all: gen

run:
	./source/main.py

gen:
	./res_npuzzle-gen.py -s -i 36 3 > test/test.txt
	head -1 test/test.txt
	./source/main.py test/test.txt
	./source/ogl.py
