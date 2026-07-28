class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target== nums[0]:
            return 0
        l,r = 0, len(nums) -1

        while l < r:
            m = (l+r)//2
            if nums[m] > target:
                r -= 1
            elif nums[m] < target:
                l += 1
            else:
                return m
        return -1