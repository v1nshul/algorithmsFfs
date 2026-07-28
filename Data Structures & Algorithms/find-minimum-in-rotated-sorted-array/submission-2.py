class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = 0
        mn = nums[0]

        for n in range(1,len(nums)):
            if nums[n] > mn:
                r += 1
                mn = nums[n]
            else:
                r += 1
                break
        newarr = nums[r:len(nums)] + nums[0:r]
        print(newarr,r)
        return newarr[0]

