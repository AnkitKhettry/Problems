from builtins import Exception
from collections import deque


class Queue:

    def __init__(self, max_size):
        self.queue = deque()
        self.max_size = max_size

    def enqueue(self, val):
        if len(self.queue) < self.max_size:
            self.queue.append(val)
        else:
            raise Exception(f"Overflow Error. Breaching max size {self.max_size}")

    def dequeue(self):
        curr_size = len(self.queue)
        if curr_size == 0:
            raise Exception("Queue empty!!")
        return self.queue.popleft()

    def get_size(self):
        return len(self.queue)

    def print(self):
        print(self.queue)


if __name__ == "__main__":
    queue = Queue(max_size=5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.print()
    print(queue.dequeue())
    queue.print()
    print(queue.dequeue())
    queue.print()
    print(queue.dequeue())
    queue.print()
    print(queue.dequeue())
    queue.print()
    print(queue.dequeue())
    queue.print()
