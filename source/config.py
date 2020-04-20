import heuristics

is_greedy = False
goal = []
heuristic_fn = None 

def calc_fScore(h, g):
    print(g, h)
    return h if is_greedy else g + h
