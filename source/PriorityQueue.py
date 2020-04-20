#maybe set in in constructor later
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def insert(self, node):
        if len(self.queue) is 0:
            self.queue.append(node)
            return
        for i, elem in enumerate(self.queue):
            if elem.f > node.f:
                self.queue.insert(i, node)
                return
        self.queue.append(node)

    def pop(self):
        # elem = min(self.queue, key=lambda x:x.f)
        elem = self.queue[0]
        self.queue.remove(elem)
        return elem
