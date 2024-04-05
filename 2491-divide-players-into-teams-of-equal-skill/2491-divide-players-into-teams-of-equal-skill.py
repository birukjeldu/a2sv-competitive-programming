class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        
        l = 0
        r = len(skill) - 1
        sk = 0
        res = 0
        
        while l < r:
            res += skill[l] * skill[r]
            sk = skill[l] + skill[r]
            l+=1
            r-= 1
            
            if sk != skill[l] + skill[r]:
                return -1
            
        return res