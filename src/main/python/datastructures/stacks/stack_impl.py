from builtins import Exception


class Stack:

    def __init__(self, max_size):
        self.arr = []
        self.max_size = max_size

    def push(self, val):
        if len(self.arr) < self.max_size:
            self.arr.append(val)
        else:
            raise Exception(f"Stack Overflow Error. Breaching max size {self.max_size}")

    def pop(self):
        curr_size = len(self.arr)
        if curr_size == 0:
            raise Exception("Stack empty!!")
        return self.arr.pop()

    def get_size(self):
        return len(self.arr)

    def print(self):
        print(self.arr)

if __name__ == "__main__":
    stack = Stack(max_size=5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print()
    print(stack.pop())
    stack.print()
    print(stack.pop())
    stack.print()
    print(stack.pop())
    stack.print()
    print(stack.pop())
    stack.print()
    print(stack.pop())
    stack.print()
