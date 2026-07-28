class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = {}
        for i in tasks:
            c[i] = 1 + c.get(i,0)
        res =1

        for i in c.values():
            res *= i

        return res

    