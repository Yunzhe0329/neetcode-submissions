class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] ==0:
                    j = n   
                    break
                # 透過res[j]暫存的結果跳到比T[j]溫度高的日子
                j += res[j]
            # 沒有越界，代表找到T[j]高的日子
            if j < n:
                res[i] = j - i
        return res

                    
