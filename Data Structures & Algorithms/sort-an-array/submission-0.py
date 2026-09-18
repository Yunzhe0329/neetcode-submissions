class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def Merge(arr, L, M, R):
            left, right = arr[L:M + 1], arr[M + 1: R + 1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                i += 1
                j += 1
            while k < len(right):
                nums[i] = right[k]
                i += 1
                k += 1

        def MergeSort(arr, left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            MergeSort(arr, left, mid)
            MergeSort(arr, mid + 1, right)
            Merge(arr, left, mid ,right)
        
        MergeSort(nums, 0, len(nums) - 1)
        return nums