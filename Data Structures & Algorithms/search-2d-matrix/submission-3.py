class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)

        for i in range(rows):
            if target > matrix[i][-1] or target < matrix[i][0]:
                continue
            if self.BS(matrix[i], target):
                return True
        return False


    def BS(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False