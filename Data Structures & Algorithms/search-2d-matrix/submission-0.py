class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        l,r = 0, n-1
        while l < len(matrix):
            m = (l+r)//2

            if matrix[l][m] == target:
                return True
            elif matrix[l][r] < target:
                l+= 1
            else:
                r -= 1
                if r < 0:
                    r = n
                    l+=1
                
                
        return False