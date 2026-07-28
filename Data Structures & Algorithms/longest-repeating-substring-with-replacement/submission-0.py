class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 1:
            return 0
        subs = 1

        l=0
        r = l + 1

        while l < len(s) and r < len(s):
            curs = 1
            count = 0
            while r < len(s) and count <= k:
                if s[l] != s[r]:
                    count += 1
                    if count > k:
                        break
                curs += 1
                r += 1
            subs = max(subs, curs)
            print(subs,curs)
            l += 1
            r = l +1
        
        return subs