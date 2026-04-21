from collections import deque


class ExecutionQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        return len(self.queue)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None
