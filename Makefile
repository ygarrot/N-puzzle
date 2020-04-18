all: gen

run:
	./source/main.py 

gen:
	./res_npuzzle-gen.py -i 12 3 | ./source/main.py test/test.txt
