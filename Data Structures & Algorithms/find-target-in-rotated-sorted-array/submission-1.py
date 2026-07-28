class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r= 0, n -1

        mi = 0
        narr = []
        if nums[l] < nums[r]:
            narr = nums
        else:
            while l <= r:
                m = (l+r)//2

                if m > r and nums[m] < nums[m+1]:
                    mi = m
                elif m < l and nums[m] > nums[m - 1]:
                    mi = m
                
                elif m > l and nums[m] >= nums[l]:
                    l = m +1
                else:
                    r = m - 1
            narr = nums[0:mi] + nums[mi:len(nums)]

        l,r = 0, n-1
        while l <= r:
            m = (l+r) //2
            if narr[m] > target:
                r -= 1
            elif narr[m] < target:
                l += 1
            else:
                return m
        return -1
