class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = heapq.heapify_max(nums)

        while k > 0:
            heapq.heappop_max(m)
            k -=1
        return m[0]