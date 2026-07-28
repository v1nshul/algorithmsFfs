class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = 0
        mn = nums[0]

        for n in range(1,len(nums)):
            if nums[n] > mn:
                r += 1
                mn = nums[n]
            elif nums[n] < mn:
                r += 1
                break
            else:
                1 +1 == 2
        newarr = nums[r:len(nums)] + nums[0:r]
        print(nums,newarr,r)
        return newarr[0]

