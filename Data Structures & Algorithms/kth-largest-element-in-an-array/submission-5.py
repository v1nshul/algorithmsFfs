class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nl(k,nums)[-1]