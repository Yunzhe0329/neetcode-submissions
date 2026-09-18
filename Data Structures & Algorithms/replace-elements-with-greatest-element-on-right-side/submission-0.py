class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        n = len(arr)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            res[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return res

