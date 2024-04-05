class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 8
        # 0 1 2 3 4 5 6 7 8
        
        low = 0
        high = int(sqrt(c))
        
        if high**2 == c:
            return True
        
        while low<=high:
            val= low **2 + high **2
            if val == c:
                return True
            if val > c:
                high-=1
            else:
                low+=1
        return False
            