def make_goal(s):
    ts = s*s
    puzzle = [-1 for i in range(ts)]
    cur = 1
    x = 0
    ix = 1
    y = 0
    iy = 0
    while True:
        puzzle[x + y*s] = cur
        if cur == 0:
            break
        cur += 1
        if x + ix == s or x + ix < 0 or (ix != 0 and puzzle[x + ix + y*s] != -1):
            iy = ix
            ix = 0
        elif y + iy == s or y + iy < 0 or (iy != 0 and puzzle[x + (y+iy)*s] != -1):
            ix = -iy
            iy = 0
        x += ix
        y += iy
        if cur == s*s:
            cur = 0
    return puzzle


if __name__ == "__main__":
    print(make_goal(4))
