class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pair = []
        for i in range(n):
            pair.append((position[i], speed[i]))
        pair.sort(reverse = True)
        carFleet = []
        for pos, spd in pair:
            carFleet.append((target - pos) / spd)
            while len(carFleet) >= 2 and carFleet[-1] <= carFleet[-2]:
                carFleet.pop()
        
        return len(carFleet)
            


