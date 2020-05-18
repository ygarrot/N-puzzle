all: visu

greedy:
	@./res_npuzzle-gen.py -s -i 36 5 > test/test.txt
	@head -1 test/test.txt
	@./source/main.py -g test/test.txt

run:
	@./res_npuzzle-gen.py -s -i 30 4 > test/test.txt
	@head -1 test/test.txt
	@./source/main.py test/test.txt

visu:
	@./res_npuzzle-gen.py -s -i 50000 3 > test/test.txt
	@head -1 test/test.txt
	@./source/main.py test/test.txt
	@g++ visu/main.cpp visu/ogldev_util.cpp -lglut -lOpenGL -lGLEW
	@./a.out
