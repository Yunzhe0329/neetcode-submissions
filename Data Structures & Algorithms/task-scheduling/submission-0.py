class MaxHeap:
    def __init__(self):
        self.heap = []
    def sift_down(self, i):
        n = len(self.heap)
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and self.heap[l] > self.heap[largest]:
            largest = l
        if r < n and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.sift_down(largest)
    def sift_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.sift_up(parent)
    def push(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return root
    def peak(self):
        return self.heap[0] if self.heap else None
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        h = MaxHeap()

        for t in count.values():
            h.push(t)
        
        time = 0

        while h.heap:
            temp = []
            cycle = 0

            for _ in range(n + 1):
                if h.heap:
                    freq = h.pop()
                    cycle += 1
                    if freq - 1 > 0:
                        temp.append(freq - 1)
            for item in temp:
                h.push(item)
            if not h.heap:
                time += cycle
            else:
                time += (n + 1)
        return time


        