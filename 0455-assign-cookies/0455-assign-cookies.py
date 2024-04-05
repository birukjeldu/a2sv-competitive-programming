class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = 0
        r = 0
        res = 0
        while r < len(s)  and l < len(g):
            if s[r] >= g[l]:
                res += 1
                l += 1
                r += 1
                
            elif s[r] < g[l]:
                r += 1
                
                
        return res
                