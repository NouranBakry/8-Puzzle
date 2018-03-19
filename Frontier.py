from collections import deque


class Frontier:

    def __init__(self):
        self.items = [()]
        # self.states = deque()

    def enqueue(self, item):
        self.items.append(item)

    def deque(self):
        return self.items.pop(0)