"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
"""

import heapq


class MedianFinder(object):

    def __init__(self):
        self.max_heap = [float("inf")]
        heapq.heapify(self.max_heap)
        self.min_heap = [float("inf")]
        heapq.heapify(self.min_heap)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.min_heap) > len(self.max_heap):
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) > (len(self.min_heap) + 1):
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == (len(self.min_heap) + 1):
            return -self.max_heap[0]
        else:
            return (float(-self.max_heap[0] + self.min_heap[0])) / 2


if __name__ == "__main__":
    medianFinder = MedianFinder();
    medianFinder.addNum(1);
    medianFinder.addNum(2);
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3);
    assert medianFinder.findMedian() == 2.0
