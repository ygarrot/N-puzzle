import heuristics

is_greedy = False
goal = []
heuristic_fn = None 

def calc_fScore(h, g):
    return h if is_greedy else g + h
