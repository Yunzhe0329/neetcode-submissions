class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, spd] for pos, spd in zip(position, speed)]
        pair.sort(reverse = True)
        # stack
        carfleet = []
        for p, s in pair:
            # stack 代表抵達時間
            carfleet.append((target - p) / s)
            # 比較小代表會形成車隊，pop掉
            # stack[3, 3] -> 同時到達，代表在終點時會剛好形成一個車隊
            if len(carfleet) >= 2 and carfleet[-1] <= carfleet[-2]:
                carfleet.pop()
        return len(carfleet)
