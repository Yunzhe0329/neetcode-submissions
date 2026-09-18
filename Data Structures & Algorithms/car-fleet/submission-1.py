class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, spd] for pos, spd in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            # stack 代表抵達時間
            stack.append((target - p) / s)
            # 比較小代表會形成車隊，pop掉
            # stack[3, 3] -> 同時到達，代表在終點時會剛好形成一個車隊
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
