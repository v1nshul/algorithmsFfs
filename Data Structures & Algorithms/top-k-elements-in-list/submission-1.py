class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res =[]
        for i in nums:
            d[i] = 1 + d.get(i,0)
        
        c = []
        for i,j in d.items():
            c.append([i,j])
        c.sort()
        c = c[::-1]
        print(c)
        
        for i in range(k):
            res.append(c[i][0])

        return res

        