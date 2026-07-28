class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        mn = nums[0]
        i = 0
        while l < r:             
            m = (l+r)//2

            if nums[m] < nums[m-1]:
                i = m
                break
            elif nums[m] > nums[m-1]:
                l= m
        
        
        if i != len(nums):
            newarr = nums[i:len(nums)] + nums[0:i]
            print(nums,newarr,i)
            return newarr[0]
        else:
            return nums[0]

