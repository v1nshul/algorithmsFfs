class Solution:
    def encode(self, strs: List[str]) -> str:
        for s in strs:
            s = s + ' '
            strs.pop(s)
    def decode(self, s: str) -> List[str]:
        tmp =''
        for i in s:
            if i != ' ':
                tmp += i
            else:    
                strs.append(tmp)
                tmp =''

            


