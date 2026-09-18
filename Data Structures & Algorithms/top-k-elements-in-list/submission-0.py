class MinHeap:
    def __init__(self):
        self.heap = []
    def sift_down(self, i):
        n = len(self.heap)
        smallest = i
        l = 2  * i + 1
        r = 2  * i + 2
        
        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.sift_down(smallest)
    def sift_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
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
        root  = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return root
    def peak(self):
        if not self.heap:
            return None
        return self.heap[0]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count hash map
        count = {}
        for num in nums:
            count[num] = 1  + count.get(num, 0)
        
        # build MinHeap 
        h = MinHeap()
        for num, freq in count.items():
            h.push((freq, num))
            if len(h.heap) > k:
                h.pop()
        return [num for freq, num in h.heap]

        