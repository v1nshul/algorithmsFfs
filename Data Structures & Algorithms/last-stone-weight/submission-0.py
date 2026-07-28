class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxh = heapq.heapify_max(stones)
        while len(maxh) > 1:
            x = heapq.heappop_max(maxh)
            y = heapq.heappop_max(maxh)
            if x == y:
                continue
            else:
                heapq.heappush_max(maxh, x-y)
        if maxh:
            return maxh[0]
        return 0