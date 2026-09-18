class MaxHeap:
    def __init__(self):
        self.heap = []

    def _sift_down(self, i):
        n = len(self.heap)
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self._sift_down(largest)
    
    def _sift_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._sift_up(parent)
    
    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root
    
    def peek(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = MaxHeap()
        for stone in stones:
            h.push(stone)

        while  len(h) > 1:
            first = h.pop()
            second = h.pop()

            if second != first:
                h.push(first - second)       
        return h.peek() if len(h) == 1 else 0