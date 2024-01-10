from builtins import Exception


class Queue:

    def __init__(self, max_size):
        self.arr = []
        self.max_size = max_size

    def enqueue(self, val):
        if len(self.arr) < self.max_size:
            self.arr.append(val)
        else:
            raise Exception(f"Overflow Error. Breaching max size {self.max_size}")

    def dequeue(self):
        curr_size = len(self.arr)
        if curr_size == 0:
            raise Exception("Queue empty!!")
        return self.arr.pop(0)

    def get_size(self):
        return len(self.arr)

    def print(self):
        print(self.arr)


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
