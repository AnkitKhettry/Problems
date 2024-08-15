# This is just for understanding the concept.
# Use python's heapq when actually solving problems.

class MinHeap:

    def __init__(self):
        self.heap = []

    def _get_parent_idx(self, idx):
        return int((idx-1)/2)

    def _get_children_idx(self, idx):
        return (idx*2) + 1, (idx*2) + 2

    def _swap(self, idx1, idx2):
        temp = self.heap[idx2]
        self.heap[idx2] = self.heap[idx1]
        self.heap[idx1] = temp

    def heappush(self, elem):
        self.heap.append(elem)
        curr_idx = len(self.heap) - 1
        parent_idx = self._get_parent_idx(curr_idx)
        while self.heap[parent_idx] > self.heap[curr_idx]:
            self._swap(parent_idx, curr_idx)
            curr_idx = parent_idx
            parent_idx = self._get_parent_idx(curr_idx)

    def heappop(self):
        # Swap root with last element and then remove it
        root = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        # Now bubble to new root downwards
        curr_idx = 0
        child1, child2 = self._get_children_idx(curr_idx)
        min_elem_idx = self._get_min_elem_idx(curr_idx, child1, child2)

        while min_elem_idx != curr_idx:
            self._swap(min_elem_idx, curr_idx)
            curr_idx = min_elem_idx
            child1, child2 = self._get_children_idx(curr_idx)
            min_elem_idx = self._get_min_elem_idx(curr_idx, child1, child2)

        return root

    def _get(self, idx):
        if idx < len(self.heap):
            return self.heap[idx]
        else:
            return float("inf")

    def _get_min_elem_idx(self, idx1, idx2, idx3):

        if self._get(idx1) <= self._get(idx2) and self._get(idx1) <= self._get(idx3):
            return idx1
        elif self._get(idx2) <= self._get(idx3):
            return idx2
        else:
            return idx3

    def heapify(self, arr=[]):
        for elem in arr:
            self.heappush(elem)


class MaxHeap:

    def __init__(self):
        self.heap = []

    def _get_parent_idx(self, idx):
        return int((idx-1)/2)

    def _get_children_idx(self, idx):
        return (idx*2) + 1, (idx*2) + 2

    def _swap(self, idx1, idx2):
        temp = self.heap[idx2]
        self.heap[idx2] = self.heap[idx1]
        self.heap[idx1] = temp

    def heappush(self, elem):
        self.heap.append(elem)
        curr_idx = len(self.heap) - 1
        parent_idx = self._get_parent_idx(curr_idx)
        while self.heap[parent_idx] < self.heap[curr_idx]:
            self._swap(parent_idx, curr_idx)
            curr_idx = parent_idx
            parent_idx = self._get_parent_idx(curr_idx)

    def heappop(self):
        # Swap root with last element and then remove it
        root = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        # Now bubble to new root downwards
        curr_idx = 0
        child1, child2 = self._get_children_idx(curr_idx)
        max_elem_idx = self._get_max_elem_idx(curr_idx, child1, child2)

        while max_elem_idx != curr_idx:
            self._swap(max_elem_idx, curr_idx)
            curr_idx = max_elem_idx
            child1, child2 = self._get_children_idx(curr_idx)
            max_elem_idx = self._get_max_elem_idx(curr_idx, child1, child2)

        return root

    def _get(self, idx):
        if idx < len(self.heap):
            return self.heap[idx]
        else:
            return float("-inf")

    def _get_max_elem_idx(self, idx1, idx2, idx3):

        if self._get(idx1) >= self._get(idx2) and self._get(idx1) >= self._get(idx3):
            return idx1
        elif self._get(idx2) >= self._get(idx3):
            return idx2
        else:
            return idx3

    def heapify(self, arr=[]):
        for elem in arr:
            self.heappush(elem)


if __name__ == "__main__":
    min_heap = MinHeap()

    min_heap.heappush(32)
    min_heap.heappush(31)
    min_heap.heappush(14)
    min_heap.heappush(39)
    min_heap.heappush(36)

    print(min_heap.heap)
    print(min_heap.heappop())
    print(min_heap.heap)

    min_heap_2 = MinHeap()
    min_heap_2.heapify([32, 31, 14, 39, 36])
    print(min_heap_2.heap)

    max_heap = MaxHeap()

    max_heap.heappush(32)
    max_heap.heappush(31)
    max_heap.heappush(14)
    max_heap.heappush(39)
    max_heap.heappush(36)

    print(max_heap.heap)
    print(max_heap.heappop())
    print(min_heap.heap)

    max_heap_2 = MinHeap()
    max_heap_2.heapify([32, 31, 14, 39, 36])
    print(max_heap_2.heap)
