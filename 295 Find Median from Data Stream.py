import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower_heap = list()  # negate input and output
        self.upper_heap = list()
        self.median = None

    def addNum(self, num: int) -> None:
        if not self.upper_heap or num > self.upper_heap[0]:
            heapq.heappush(self.upper_heap, num)
        else:
            heapq.heappush(self.lower_heap, -num)

        if len(self.upper_heap) > len(self.lower_heap) + 1:
            heapq.heappush(self.lower_heap, -heapq.heappop(self.upper_heap))
        elif len(self.upper_heap) < len(self.lower_heap):
            heapq.heappush(self.upper_heap, -heapq.heappop(self.lower_heap))

    def findMedian(self) -> float:
        if len(self.upper_heap) == len(self.lower_heap):
            return (self.upper_heap[0] - self.lower_heap[0]) / 2
        else:
            return float(self.upper_heap[0])

    # def addNum(self, num: int) -> None:
    #     if self.median is not None:
    #         self.add_odd(num)
    #     else:
    #         self.even_add(num)
    #
    # def even_add(self, num: int) -> None:
    #     if self.lower_heap:
    #         if num < -self.lower_heap[0]:
    #             self.median = -heapq.heappushpop(self.lower_heap, -num)
    #         elif num > self.upper_heap[0]:
    #             self.median = heapq.heappushpop(self.upper_heap, num)
    #         else:
    #             self.median = num
    #     else:
    #         self.median = num
    #
    # def add_odd(self, num: int) -> None:
    #     if self.lower_heap:
    #         for item in (num, self.median):
    #             if item < -self.lower_heap[0]:
    #                 heapq.heappush(self.lower_heap, -item)
    #             else:
    #                 heapq.heappush(self.upper_heap, item)
    #         if len(self.lower_heap) > len(self.upper_heap):
    #             item = -heapq.heappop(self.lower_heap)
    #             heapq.heappush(self.upper_heap, item)
    #         elif len(self.lower_heap) < len(self.upper_heap):
    #             item = heapq.heappop(self.upper_heap)
    #             heapq.heappush(self.lower_heap, -item)
    #     else:
    #         if num < self.median:
    #             self.lower_heap.append(-num)
    #             self.upper_heap.append(self.median)
    #         else:
    #             self.lower_heap.append(-self.median)
    #             self.upper_heap.append(num)
    #     self.median = None
    #
    # def findMedian(self) -> float:
    #     if self.median:
    #         return float(self.median)
    #     elif not self.lower_heap:
    #         return None
    #     else:
    #         return (-self.lower_heap[0] + self.upper_heap[0]) / 2


func_dict = {
    "MedianFinder": MedianFinder,
    "addNum": MedianFinder.addNum,
    "findMedian": MedianFinder.findMedian,
}
for funcs, args in (
    (
        ["addNum","addNum","findMedian","addNum","findMedian"],
        [[1],[2],[],[3],[]]
    ),
    (
        ["addNum","addNum","findMedian"],
        [[0],[0],[]]
    ),
    (
        ["addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
        [[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
        # [null,null,-1.00000,null,-1.50000,null,-2.00000,null,-2.50000,null,-3.00000]
    ),
):
    print("Begin!!")
    obj = MedianFinder()
    for func, arg in zip(funcs, args):
        print(func_dict[func](obj, *arg))


# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# obj.findMedian(*[])
#
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# heap = [10, 4, 8, 3, 24, 865, 4, 2, 9]
# heapq.heapify(heap)
# asnw = heapq.nlargest(5, heap)

[]

