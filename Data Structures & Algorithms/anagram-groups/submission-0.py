class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]

        if len(strs) == 1:
            return [strs]

        def check(s1,s2):
            d1 = {}
            d2 = {}
            if len(s1) != len(s2):
                return False
            for i in range(len(s1)):
                d1[s1[i]] = 1 + d1.get(s1[i],0)
                d2[s2[i]] = 1 + d2.get(s2[i],0)
            return d1==d2

        seen = []
        for s in strs:
            temp = []
            if s not in seen:
                temp.append(s)
            seen.append(s)
            for j in strs:
                if j != s and j not in seen:
                    if check(j,s):
                        temp.append(j)
                        seen.append(j)
            if len(temp) > 0: res.append(temp)
        return res

