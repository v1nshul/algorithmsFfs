class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        u = {'+','-','*','/'}

        res = int(tokens[0])
        stack = []

        for i in range(1,len(tokens)):
            if tokens[i] not in u:
                stack.append(tokens[i])
            else:
                if tokens[i] == '+':
                    while stack:
                        c = stack.pop()
                        res += int(c) 
                elif tokens[i] == '-':
                    while stack:
                        c = stack.pop()
                        res -= int(c)
                elif tokens[i] == '*':
                    while stack:
                        c = stack.pop()
                        res = res*int(c)
                else:
                    while stack:
                        c = stack.pop()
                        res = res//int(c)
        return res
                
                    
                        