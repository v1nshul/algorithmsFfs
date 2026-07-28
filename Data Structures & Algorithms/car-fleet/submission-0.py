class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = 0
        
        seen = defaultdict(list)
        for i in range(len(position)):
            stack = []
            t = (target-position[i])//speed[i]
            stack.append([position[i],speed[i]])
            seen[t] = [position[i],speed[i]]
            j = i + 1
            while j < len(position):
                tj = (target-position[j])//speed[j]
                if t <= tj and [position[j],speed[j]] not in seen.values():
                    stack.append([position[j],speed[j]])
                    seen[tj] = position[j],speed[j]
                j += 1
            res += 1
        return res-1

            

        