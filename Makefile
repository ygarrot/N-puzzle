all: gen

run:
	./res_npuzzle-gen.py -s -i 36 5 > test/test.txt
	head -1 test/test.txt
	./source/main.py test/test.txt

gen:
	./res_npuzzle-gen.py -s -i 36 5 > test/test.txt
	head -1 test/test.txt
	./source/main.py test/test.txt
	./source/ogl.py
