import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item):
        heapq.heappush(self.elements, (item.f, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
