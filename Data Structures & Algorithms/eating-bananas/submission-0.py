class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        while True:
            tt = 0
            for p in piles:
                tt += math.ceil(p/s)
            if tt <= h:
                return s
            s += 1
        return s