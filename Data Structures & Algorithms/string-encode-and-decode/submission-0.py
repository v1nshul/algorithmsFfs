class Solution:
    s = ''
    def encode(self, strs: List[str]) -> str:
        for i in strs:
            s += i + ' '
            strs.pop(i)
    def decode(self, s: str) -> List[str]:
        tmp =''
        for i in s:
            if i != ' ':
                tmp += i
            else:    
                strs.append(tmp)
                tmp =''

            


