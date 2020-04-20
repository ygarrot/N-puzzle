all: visu

run:
	@./res_npuzzle-gen.py -s -i 36 5 > test/test.txt
	@head -1 test/test.txt
	@./source/main.py test/test.txt

visu:
	@./res_npuzzle-gen.py -s -i 36 5 > test/test.txt
	@head -1 test/test.txt
	@./source/main.py test/test.txt
	@python source/ogl.py
