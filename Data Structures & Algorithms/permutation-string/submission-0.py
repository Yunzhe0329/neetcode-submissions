class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)
        
        bound = len(countS1)

        for i in range(len(s2)):
            countS2, curr = {}, 0
            for j in range(i, len(s2)):
                countS2[s2[j]] = 1 + countS2.get(s2[j], 0)
                if countS1.get(s2[j],0) < countS2[s2[j]]:
                    break
                if countS1.get(s2[j],0) == countS2[s2[j]]:
                    curr += 1
                if curr == bound:
                    return True
        return False
